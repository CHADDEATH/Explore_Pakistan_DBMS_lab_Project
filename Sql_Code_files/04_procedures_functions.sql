/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 04_procedures_functions.sql
ORDER  : 4 of 8
PURPOSE: Business logic, Trip Budget Estimator, Admin authentication,
         Currency conversion, and controlled administrative DDL procedures.
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;

PROMPT =========================================================;
PROMPT CREATING PROCEDURES AND FUNCTIONS...;
PROMPT =========================================================;

-- 1. FUNCTION: verify_admin_login
-- Validates admin credentials using salted SHA-256 hashing.
CREATE OR REPLACE FUNCTION verify_admin_login (
    p_username IN VARCHAR2,
    p_password IN VARCHAR2
) RETURN NUMBER IS
    v_stored_hash VARCHAR2(128);
    v_salt        VARCHAR2(64);
    v_calc_hash   VARCHAR2(128);
BEGIN
    SELECT password_hash, salt
      INTO v_stored_hash, v_salt
      FROM users_admin
     WHERE username = LOWER(TRIM(p_username));

    -- Compute SHA-256 hash using Oracle's STANDARD_HASH
    SELECT STANDARD_HASH(p_password || v_salt, 'SHA256')
      INTO v_calc_hash
      FROM dual;

    IF LOWER(v_calc_hash) = LOWER(v_stored_hash) THEN
        RETURN 1; -- Login Successful
    ELSE
        RETURN 0; -- Authentication Failed
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0; -- Unknown username
    WHEN OTHERS THEN
        RETURN 0;
END verify_admin_login;
/

-- 2. PROCEDURE: calculate_trip_budget
-- Comprehensive Trip Budget Estimator taking days, star rating, people, and guide flag.
CREATE OR REPLACE PROCEDURE calculate_trip_budget (
    p_city_id        IN NUMBER,
    p_days           IN NUMBER,
    p_star_rating    IN NUMBER,
    p_num_people     IN NUMBER,
    p_include_guide  IN CHAR DEFAULT 'Y',
    o_total_cost     OUT NUMBER,
    o_hotel_cost     OUT NUMBER,
    o_food_cost      OUT NUMBER,
    o_transport_cost OUT NUMBER,
    o_guide_cost     OUT NUMBER,
    o_entry_cost     OUT NUMBER
) IS
    v_city_name       VARCHAR2(50);
    v_avg_room_rate   NUMBER := 0;
    v_rooms_needed    NUMBER := 1;
    v_daily_food_rate NUMBER := 2500; -- Daily food budget per person in PKR
    v_daily_local_tx  NUMBER := 1500; -- Daily urban transport allowance
    v_daily_guide_rt  NUMBER := 0;
    v_avg_entry_sum   NUMBER := 0;
BEGIN
    IF p_days <= 0 OR p_num_people <= 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Days and number of travelers must be greater than zero.');
    END IF;

    SELECT city_name INTO v_city_name FROM cities WHERE city_id = p_city_id;

    -- Calculate rooms needed (assume standard 2 persons per room)
    v_rooms_needed := CEIL(p_num_people / 2);

    -- 1. Hotel Cost Calculation
    SELECT NVL(AVG(r.price_per_night), 15000)
      INTO v_avg_room_rate
      FROM room_types r
      JOIN hotels h ON r.hotel_id = h.hotel_id
     WHERE h.city_id = p_city_id
       AND h.star_rating = p_star_rating;

    o_hotel_cost := v_avg_room_rate * v_rooms_needed * p_days;

    -- 2. Food Cost Calculation
    o_food_cost := v_daily_food_rate * p_num_people * p_days;

    -- 3. Transport Cost Calculation
    o_transport_cost := v_daily_local_tx * p_days;

    -- 4. Tour Guide Cost
    IF UPPER(p_include_guide) = 'Y' THEN
        SELECT NVL(AVG(daily_rate), 6500)
          INTO v_daily_guide_rt
          FROM tour_guides
         WHERE city_id = p_city_id;
        o_guide_cost := v_daily_guide_rt * p_days;
    ELSE
        o_guide_cost := 0;
    END IF;

    -- 5. Landmark Entry Fees (Aggregate of key city attractions per person)
    SELECT NVL(SUM(entry_fee), 300)
      INTO v_avg_entry_sum
      FROM landmarks
     WHERE city_id = p_city_id;
    o_entry_cost := v_avg_entry_sum * p_num_people;

    -- Total Budget
    o_total_cost := o_hotel_cost + o_food_cost + o_transport_cost + o_guide_cost + o_entry_cost;

    -- Display Formatted Summary to DBMS_OUTPUT
    DBMS_OUTPUT.PUT_LINE('=====================================================');
    DBMS_OUTPUT.PUT_LINE('TRIP BUDGET ESTIMATE: ' || v_city_name);
    DBMS_OUTPUT.PUT_LINE('Duration: ' || p_days || ' Days | Travelers: ' || p_num_people || ' | Hotel Tier: ' || p_star_rating || '-Star');
    DBMS_OUTPUT.PUT_LINE('=====================================================');
    DBMS_OUTPUT.PUT_LINE('1. Accommodation (' || v_rooms_needed || ' room(s) x ' || p_days || ' nights) : PKR ' || TO_CHAR(o_hotel_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('2. Food & Dining Allowance            : PKR ' || TO_CHAR(o_food_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('3. Local Urban Transport              : PKR ' || TO_CHAR(o_transport_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('4. Certified Tour Guide Service       : PKR ' || TO_CHAR(o_guide_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('5. Sightseeing & Landmark Entry Fees  : PKR ' || TO_CHAR(o_entry_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('-----------------------------------------------------');
    DBMS_OUTPUT.PUT_LINE('TOTAL ESTIMATED TRIP BUDGET           : PKR ' || TO_CHAR(o_total_cost, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('=====================================================');
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20002, 'Specified city ID ' || p_city_id || ' does not exist.');
END calculate_trip_budget;
/

-- 3. FUNCTION: convert_currency
-- Converts a PKR amount to target foreign currency based on exchange rates.
CREATE OR REPLACE FUNCTION convert_currency (
    p_amount_pkr        IN NUMBER,
    p_target_currency   IN VARCHAR2
) RETURN NUMBER IS
    v_rate NUMBER;
BEGIN
    SELECT exchange_rate_to_pkr
      INTO v_rate
      FROM currencies
     WHERE currency_code = UPPER(TRIM(p_target_currency));

    RETURN ROUND(p_amount_pkr / v_rate, 2);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20003, 'Currency code ' || p_target_currency || ' not supported.');
END convert_currency;
/

-- 4. PROCEDURE: sp_book_room
-- Safely inserts a booking after checking availability and calculating price.
CREATE OR REPLACE PROCEDURE sp_book_room (
    p_hotel_id      IN NUMBER,
    p_room_id       IN NUMBER,
    p_guest_name    IN VARCHAR2,
    p_guest_contact IN VARCHAR2,
    p_check_in      IN DATE,
    p_check_out     IN DATE,
    o_booking_id    OUT NUMBER,
    o_total_price   OUT NUMBER
) IS
    v_price_per_night NUMBER;
    v_nights          NUMBER;
    v_conflict_count  NUMBER := 0;
BEGIN
    IF p_check_out <= p_check_in THEN
        RAISE_APPLICATION_ERROR(-20004, 'Check-out date must be strictly after check-in date.');
    END IF;

    -- Verify room exists and belongs to hotel
    SELECT price_per_night
      INTO v_price_per_night
      FROM room_types
     WHERE room_id = p_room_id AND hotel_id = p_hotel_id;

    -- Conflict check: detect overlapping confirmed bookings for this room
    SELECT COUNT(*)
      INTO v_conflict_count
      FROM bookings
     WHERE room_id = p_room_id
       AND status = 'CONFIRMED'
       AND (p_check_in < check_out_date AND p_check_out > check_in_date);

    IF v_conflict_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20005, 'Room is already booked for the specified dates.');
    END IF;

    v_nights := TRUNC(p_check_out) - TRUNC(p_check_in);
    o_total_price := v_nights * v_price_per_night;

    INSERT INTO bookings (
        hotel_id, room_id, guest_name, guest_contact, check_in_date, check_out_date, total_price, status
    ) VALUES (
        p_hotel_id, p_room_id, p_guest_name, p_guest_contact, p_check_in, p_check_out, o_total_price, 'CONFIRMED'
    ) RETURNING booking_id INTO o_booking_id;

    DBMS_OUTPUT.PUT_LINE('Booking created successfully. ID: ' || o_booking_id || ' | Total: PKR ' || o_total_price);
END sp_book_room;
/

-- 5. ADMINISTRATIVE DDL PROCEDURE: admin_execute_ddl
-- Allows authorized admin to execute controlled DDL statements dynamically.
CREATE OR REPLACE PROCEDURE admin_execute_ddl (
    p_ddl_statement IN VARCHAR2
) IS
BEGIN
    EXECUTE IMMEDIATE p_ddl_statement;
    INSERT INTO audit_log (table_name, operation, record_id, new_values, admin_user)
    VALUES ('SYSTEM_DDL', 'DDL_EXEC', 'SCHEMA', SUBSTR(p_ddl_statement, 1, 4000), USER);
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Admin DDL executed successfully.');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Admin DDL execution failed: ' || SQLERRM);
        RAISE;
END admin_execute_ddl;
/

PROMPT 04_procedures_functions.sql executed successfully.
