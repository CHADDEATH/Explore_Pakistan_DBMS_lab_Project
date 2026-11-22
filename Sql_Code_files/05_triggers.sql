/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 05_triggers.sql
ORDER  : 5 of 8
PURPOSE: Implements Business Rule triggers (overlap check, price calculation,
         rating auto-aggregation, and full Audit Logging).
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;

PROMPT =========================================================;
PROMPT CREATING BUSINESS AND AUDIT TRIGGERS...;
PROMPT =========================================================;

-- 1. TRIGGER: trg_booking_price_and_overlap
-- Automatically calculates total_price and verifies zero booking date overlaps.
CREATE OR REPLACE TRIGGER trg_booking_price_and_overlap
BEFORE INSERT OR UPDATE ON bookings
FOR EACH ROW
DECLARE
    v_room_rate      NUMBER;
    v_nights         NUMBER;
    v_overlaps       NUMBER := 0;
BEGIN
    -- 1. Date sanity check
    IF :NEW.check_out_date <= :NEW.check_in_date THEN
        RAISE_APPLICATION_ERROR(-20010, 'Check-out date must be strictly greater than check-in date.');
    END IF;

    -- 2. Calculate nights and total price from room_types rate
    SELECT price_per_night
      INTO v_room_rate
      FROM room_types
     WHERE room_id = :NEW.room_id;

    v_nights := TRUNC(:NEW.check_out_date) - TRUNC(:NEW.check_in_date);
    :NEW.total_price := v_nights * v_room_rate;

    -- 3. Overlap check for confirmed reservations
    IF :NEW.status = 'CONFIRMED' THEN
        SELECT COUNT(*)
          INTO v_overlaps
          FROM bookings
         WHERE room_id = :NEW.room_id
           AND status = 'CONFIRMED'
           AND booking_id != NVL(:NEW.booking_id, -1)
           AND (:NEW.check_in_date < check_out_date AND :NEW.check_out_date > check_in_date);

        IF v_overlaps > 0 THEN
            RAISE_APPLICATION_ERROR(-20011, 'Booking Conflict: Room ' || :NEW.room_id || ' is already booked for this duration.');
        END IF;
    END IF;
END;
/

-- 2. TRIGGER: trg_update_hotel_rating
-- Recomputes hotels.rating_avg whenever a review is inserted, updated, or removed.
CREATE OR REPLACE TRIGGER trg_update_hotel_rating
AFTER INSERT OR UPDATE OR DELETE ON reviews
FOR EACH ROW
DECLARE
    v_target_hotel NUMBER;
    v_avg          NUMBER(3,2);
BEGIN
    v_target_hotel := NVL(:NEW.hotel_id, :OLD.hotel_id);

    IF v_target_hotel IS NOT NULL THEN
        SELECT NVL(ROUND(AVG(rating), 2), 0.0)
          INTO v_avg
          FROM reviews
         WHERE hotel_id = v_target_hotel;

        UPDATE hotels
           SET rating_avg = v_avg
         WHERE hotel_id = v_target_hotel;
    END IF;
END;
/

-- 3. AUDIT TRIGGER: trg_audit_hotels
-- Comprehensive audit logging for administrative DML on HOTELS.
CREATE OR REPLACE TRIGGER trg_audit_hotels
AFTER INSERT OR UPDATE OR DELETE ON hotels
FOR EACH ROW
DECLARE
    v_op  VARCHAR2(10);
    v_old CLOB;
    v_new CLOB;
    v_id  VARCHAR2(100);
BEGIN
    IF INSERTING THEN
        v_op := 'INSERT';
        v_id := TO_CHAR(:NEW.hotel_id);
        v_new := 'Name=' || :NEW.hotel_name || ', Stars=' || :NEW.star_rating || ', CityID=' || :NEW.city_id;
    ELSIF UPDATING THEN
        v_op := 'UPDATE';
        v_id := TO_CHAR(:NEW.hotel_id);
        v_old := 'Name=' || :OLD.hotel_name || ', Stars=' || :OLD.star_rating || ', Rating=' || :OLD.rating_avg;
        v_new := 'Name=' || :NEW.hotel_name || ', Stars=' || :NEW.star_rating || ', Rating=' || :NEW.rating_avg;
    ELSIF DELETING THEN
        v_op := 'DELETE';
        v_id := TO_CHAR(:OLD.hotel_id);
        v_old := 'Name=' || :OLD.hotel_name || ', CityID=' || :OLD.city_id;
    END IF;

    INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, admin_user, log_timestamp)
    VALUES ('HOTELS', v_op, v_id, v_old, v_new, USER, SYSTIMESTAMP);
END;
/

-- 4. AUDIT TRIGGER: trg_audit_landmarks
-- Audit logging for LANDMARKS table.
CREATE OR REPLACE TRIGGER trg_audit_landmarks
AFTER INSERT OR UPDATE OR DELETE ON landmarks
FOR EACH ROW
DECLARE
    v_op  VARCHAR2(10);
    v_old CLOB;
    v_new CLOB;
    v_id  VARCHAR2(100);
BEGIN
    IF INSERTING THEN
        v_op := 'INSERT';
        v_id := TO_CHAR(:NEW.landmark_id);
        v_new := 'Name=' || :NEW.landmark_name || ', Fee=' || :NEW.entry_fee || ', Cat=' || :NEW.category;
    ELSIF UPDATING THEN
        v_op := 'UPDATE';
        v_id := TO_CHAR(:NEW.landmark_id);
        v_old := 'Name=' || :OLD.landmark_name || ', Fee=' || :OLD.entry_fee;
        v_new := 'Name=' || :NEW.landmark_name || ', Fee=' || :NEW.entry_fee;
    ELSIF DELETING THEN
        v_op := 'DELETE';
        v_id := TO_CHAR(:OLD.landmark_id);
        v_old := 'Name=' || :OLD.landmark_name;
    END IF;

    INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, admin_user, log_timestamp)
    VALUES ('LANDMARKS', v_op, v_id, v_old, v_new, USER, SYSTIMESTAMP);
END;
/

-- 5. AUDIT TRIGGER: trg_audit_bookings
-- Audit logging for BOOKINGS table.
CREATE OR REPLACE TRIGGER trg_audit_bookings
AFTER INSERT OR UPDATE OR DELETE ON bookings
FOR EACH ROW
DECLARE
    v_op  VARCHAR2(10);
    v_old CLOB;
    v_new CLOB;
    v_id  VARCHAR2(100);
BEGIN
    IF INSERTING THEN
        v_op := 'INSERT';
        v_id := TO_CHAR(:NEW.booking_id);
        v_new := 'Guest=' || :NEW.guest_name || ', RoomID=' || :NEW.room_id || ', Total=' || :NEW.total_price;
    ELSIF UPDATING THEN
        v_op := 'UPDATE';
        v_id := TO_CHAR(:NEW.booking_id);
        v_old := 'Status=' || :OLD.status || ', Total=' || :OLD.total_price;
        v_new := 'Status=' || :NEW.status || ', Total=' || :NEW.total_price;
    ELSIF DELETING THEN
        v_op := 'DELETE';
        v_id := TO_CHAR(:OLD.booking_id);
        v_old := 'Guest=' || :OLD.guest_name || ', Total=' || :OLD.total_price;
    END IF;

    INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, admin_user, log_timestamp)
    VALUES ('BOOKINGS', v_op, v_id, v_old, v_new, USER, SYSTIMESTAMP);
END;
/

PROMPT 05_triggers.sql executed successfully.
