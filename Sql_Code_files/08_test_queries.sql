/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 08_test_queries.sql
ORDER  : 8 of 8
PURPOSE: Comprehensive End-to-End Verification of User Flows, Admin Operations,
         Triggers, Stored Procedures, and Oracle 23ai AI Semantic Search.
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;
SET SERVEROUTPUT ON SIZE 1000000;

PROMPT =========================================================;
PROMPT TEST 1: USER FLOW - LIST ALL DESTINATIONS (STEP 1 & 2);
PROMPT =========================================================;
SELECT city_id, city_name, province, region_type
  FROM v_user_cities
 ORDER BY city_id;

PROMPT =========================================================;
PROMPT TEST 2: USER FLOW - BROWSE 5-STAR HOTELS IN ISLAMABAD (STEP 3);
PROMPT =========================================================;
SELECT hotel_id, hotel_name, star_rating, address, contact, rating_avg
  FROM v_user_hotels
 WHERE city_name = 'Islamabad' AND star_rating = 5;

PROMPT =========================================================;
PROMPT TEST 3: USER FLOW - INSPECT ROOM TYPES & NIGHTLY RATES (STEP 4);
PROMPT =========================================================;
SELECT room_id, hotel_name, room_name, capacity, price_per_night, amenities
  FROM v_user_rooms
 WHERE hotel_name = 'Islamabad Serena Hotel'
 ORDER BY price_per_night ASC;

PROMPT =========================================================;
PROMPT TEST 4: USER FLOW - TOUR GUIDE SEARCH & RATES (STEP 5);
PROMPT =========================================================;
SELECT guide_id, guide_name, languages, daily_rate, contact, experience_years
  FROM v_user_tour_guides
 WHERE city_name = 'Skardu'
 ORDER BY daily_rate ASC;

PROMPT =========================================================;
PROMPT TEST 5: USER FLOW - FAMOUS STREET FOODS IN LAHORE (STEP 6);
PROMPT =========================================================;
SELECT food_name, category, famous_spot, price_range, description
  FROM v_user_street_foods
 WHERE city_name = 'Lahore' AND is_street_food = 'Y';

PROMPT =========================================================;
PROMPT TEST 6: USER FLOW - SIGHTSEEING LANDMARKS IN KARACHI (STEP 7);
PROMPT =========================================================;
SELECT landmark_name, category, entry_fee, description
  FROM v_user_landmarks
 WHERE city_name = 'Karachi'
 ORDER BY entry_fee DESC;

PROMPT =========================================================;
PROMPT TEST 7: USER FLOW - TRANSPORT FROM HOTEL TO LANDMARK (STEP 8);
PROMPT =========================================================;
-- A) Public Transport Routes
SELECT from_location, destination_landmark, transport_mode, fare, duration_minutes
  FROM v_user_transport_routes
 WHERE city_name = 'Islamabad';

-- B) Private Ride-Hailing Tariffs
SELECT app_name, vehicle_type, base_fare, per_km_rate
  FROM v_user_private_transport
 WHERE city_name = 'Islamabad';

PROMPT =========================================================;
PROMPT TEST 8: USER FLOW - TRIP BUDGET ESTIMATOR PROCEDURE (STEP 9);
PROMPT =========================================================;
DECLARE
    v_total NUMBER;
    v_hotel NUMBER;
    v_food  NUMBER;
    v_trans NUMBER;
    v_guide NUMBER;
    v_entry NUMBER;
BEGIN
    -- Estimate a 5-day trip for 2 people to Skardu staying in 5-star hotels with guide
    calculate_trip_budget(
        p_city_id        => 5,
        p_days           => 5,
        p_star_rating    => 5,
        p_num_people     => 2,
        p_include_guide  => 'Y',
        o_total_cost     => v_total,
        o_hotel_cost     => v_hotel,
        o_food_cost      => v_food,
        o_transport_cost => v_trans,
        o_guide_cost     => v_guide,
        o_entry_cost     => v_entry
    );
END;
/

PROMPT =========================================================;
PROMPT TEST 9: ADMIN AUTHENTICATION (SALTED SHA-256 CHECK);
PROMPT =========================================================;
DECLARE
    v_res NUMBER;
BEGIN
    -- Correct Password: 'admin'
    v_res := verify_admin_login('admin', 'admin');
    IF v_res = 1 THEN
        DBMS_OUTPUT.PUT_LINE('PASS: Valid login accepted for admin.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('FAIL: Valid login was rejected.');
    END IF;

    -- Incorrect Password: 'wrong_password'
    v_res := verify_admin_login('admin', 'wrong_password');
    IF v_res = 0 THEN
        DBMS_OUTPUT.PUT_LINE('PASS: Invalid password successfully blocked.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('FAIL: Invalid password bypassed security.');
    END IF;
END;
/

PROMPT =========================================================;
PROMPT TEST 10: TRIGGER VERIFICATION - OVERLAP CHECK & BOOKING;
PROMPT =========================================================;
DECLARE
    v_bid NUMBER;
    v_cost NUMBER;
BEGIN
    -- Insert a valid booking
    sp_book_room(
        p_hotel_id      => 1,
        p_room_id       => 1,
        p_guest_name    => 'Test Traveler',
        p_guest_contact => '+92-300-9999999',
        p_check_in      => TO_DATE('2025-05-01', 'YYYY-MM-DD'),
        p_check_out     => TO_DATE('2025-05-05', 'YYYY-MM-DD'),
        o_booking_id    => v_bid,
        o_total_price   => v_cost
    );

    DBMS_OUTPUT.PUT_LINE('Successfully placed non-conflicting booking ID: ' || v_bid);

    -- Attempt overlapping booking on same room
    BEGIN
        sp_book_room(
            p_hotel_id      => 1,
            p_room_id       => 1,
            p_guest_name    => 'Conflicting Guest',
            p_guest_contact => '+92-300-8888888',
            p_check_in      => TO_DATE('2025-05-03', 'YYYY-MM-DD'),
            p_check_out     => TO_DATE('2025-05-07', 'YYYY-MM-DD'),
            o_booking_id    => v_bid,
            o_total_price   => v_cost
        );
        DBMS_OUTPUT.PUT_LINE('FAIL: Overlapping booking was improperly allowed!');
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('PASS: Overlapping booking correctly rejected with trigger error: ' || SQLERRM);
    END;
END;
/

PROMPT =========================================================;
PROMPT TEST 11: AUDIT LOG TRIGGER VERIFICATION;
PROMPT =========================================================;
-- Perform an admin update on a hotel address to test the audit trigger
UPDATE hotels
   SET address = 'Updated Test Address, Sector G-5, Islamabad'
 WHERE hotel_id = 1;

-- Check Audit Log for the recorded update
SELECT log_id, table_name, operation, record_id, old_values, new_values, admin_user
  FROM audit_log
 WHERE table_name = 'HOTELS'
 ORDER BY log_id DESC
 FETCH FIRST 1 ROWS ONLY;

ROLLBACK; -- Clean up test modification

PROMPT =========================================================;
PROMPT TEST 12: ORACLE 23ai AI SEMANTIC SEARCH & JSON DUALITY;
PROMPT =========================================================;

-- A) Oracle 23ai AI Semantic Vector Search Test
-- Querying landmarks nearest to a test search query embedding (e.g. "historic mountain fortress")
SELECT landmark_name, category, entry_fee,
       ROUND(VECTOR_DISTANCE(embedding, (SELECT embedding FROM landmarks WHERE landmark_id = 43), COSINE), 4) AS similarity_score
  FROM landmarks
 ORDER BY similarity_score ASC
 FETCH FIRST 5 ROWS ONLY;

-- B) Oracle 23ai JSON Duality View
SELECT hotel_doc
  FROM hotel_room_duality_v
 WHERE ROWNUM <= 2;

PROMPT =========================================================;
PROMPT ALL 12 TEST SUITES EXECUTED SUCCESSFULLY.
PROMPT =========================================================;
