/*
================================================================================
PROJECT: Explore Pakistan - Dedicated Admin Panel
SCRIPT : 10_admin_panel_interactive.sql
RUN IN : Oracle SQL Developer / SQL*Plus (F5)
================================================================================
*/

SET SERVEROUTPUT ON SIZE 1000000;
SET LINESIZE 200;
SET PAGESIZE 100;
SET VERIFY OFF;
SET FEEDBACK OFF;

PROMPT ================================================================================;
PROMPT                  EXPLORE PAKISTAN - ADMIN MANAGEMENT PANEL
PROMPT ================================================================================;
PROMPT  AUTHENTICATION REQUIRED. DEFAULT CREDENTIALS: admin / admin
PROMPT ================================================================================;

ACCEPT enter_admin_username DEFAULT 'admin' PROMPT 'Enter Admin Username [Default admin]: ';
ACCEPT enter_admin_password DEFAULT 'admin' PROMPT 'Enter Admin Password [Default admin]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  SELECT ADMINISTRATIVE ACTION:
PROMPT    [1] View Top Rated Hotels Report (RANK & Ratings)
PROMPT    [2] View Hotel Booking Revenue Ranking
PROMPT    [3] View Recent Audit Trail Log (audit_log)
PROMPT    [4] View Currency Exchange Rates Tariff
PROMPT    [5] Test Room Booking Conflict Prevention Engine
PROMPT    [6] Test Oracle 23ai AI Semantic Vector Search
PROMPT --------------------------------------------------------------------------------;

ACCEPT select_admin_action_1_to_6 DEFAULT '1' PROMPT 'Choose Admin Action (1 to 6) [Default 1]: ';

DECLARE
    v_user   VARCHAR2(50) := TRIM('&enter_admin_username');
    v_pass   VARCHAR2(50) := TRIM('&enter_admin_password');
    v_action NUMBER       := TO_NUMBER(NVL(TRIM('&select_admin_action_1_to_6'), '1'));
    v_auth   NUMBER       := 0;
    v_bid    NUMBER;
    v_cost   NUMBER;
BEGIN
    v_auth := verify_admin_login(v_user, v_pass);

    IF v_auth = 0 THEN
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('>>> ACCESS DENIED: Invalid administrator username or password.');
        RETURN;
    END IF;

    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('>>> LOGIN SUCCESSFUL! Welcome Administrator (' || v_user || ')');
    DBMS_OUTPUT.PUT_LINE('================================================================================');

    IF v_action = 1 THEN
        DBMS_OUTPUT.PUT_LINE('REPORT: TOP 3 RATED HOTELS PER CITY (DENSE_RANK)');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR r IN (
            SELECT city_name, hotel_name, star_rating, rating_avg, city_rank
              FROM (
                  SELECT c.city_name, h.hotel_name, h.star_rating, h.rating_avg,
                         DENSE_RANK() OVER (PARTITION BY c.city_name ORDER BY h.rating_avg DESC, h.star_rating DESC) AS city_rank
                    FROM hotels h JOIN cities c ON h.city_id = c.city_id
              )
             WHERE city_rank <= 3
             ORDER BY city_name, city_rank
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  [' || RPAD(r.city_name, 10) || '] Rank #' || r.city_rank || ' : ' || RPAD(r.hotel_name, 35) || ' (' || r.star_rating || '-Star) | Rating: ' || r.rating_avg);
        END LOOP;

    ELSIF v_action = 2 THEN
        DBMS_OUTPUT.PUT_LINE('REPORT: HOTEL BOOKING REVENUE RANKING');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR b IN (
            SELECT h.hotel_name, c.city_name, COUNT(b.booking_id) AS cnt, SUM(b.total_price) AS rev,
                   RANK() OVER (ORDER BY SUM(b.total_price) DESC) AS rnk
              FROM bookings b JOIN hotels h ON b.hotel_id = h.hotel_id JOIN cities c ON h.city_id = c.city_id
             WHERE b.status = 'CONFIRMED'
             GROUP BY h.hotel_name, c.city_name
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  Rank #' || b.rnk || ' : ' || RPAD(b.hotel_name, 35) || ' (' || RPAD(b.city_name, 10) || ') | Bookings: ' || b.cnt || ' | Revenue: PKR ' || TO_CHAR(b.rev, '999,999,990.00'));
        END LOOP;

    ELSIF v_action = 3 THEN
        DBMS_OUTPUT.PUT_LINE('REPORT: RECENT AUDIT TRAIL LOG ENTRIES');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR a IN (
            SELECT log_id, table_name, operation, record_id, admin_user, TO_CHAR(log_timestamp, 'YYYY-MM-DD HH24:MI:SS') as tstamp
              FROM audit_log
             ORDER BY log_id DESC
             FETCH FIRST 10 ROWS ONLY
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  Log #' || LPAD(a.log_id, 3) || ' | ' || RPAD(a.table_name, 12) || ' | ' || RPAD(a.operation, 8) || ' | Rec ID: ' || RPAD(a.record_id, 10) || ' | User: ' || a.admin_user || ' | ' || a.tstamp);
        END LOOP;

    ELSIF v_action = 4 THEN
        DBMS_OUTPUT.PUT_LINE('REPORT: LIVE CURRENCY CONVERSION TARIFF (VS PKR)');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR cu IN (SELECT currency_code, currency_name, exchange_rate_to_pkr, TO_CHAR(last_updated, 'YYYY-MM-DD') as lu FROM currencies ORDER BY exchange_rate_to_pkr DESC) LOOP
            DBMS_OUTPUT.PUT_LINE('  1 ' || cu.currency_code || ' (' || RPAD(cu.currency_name, 20) || ') = PKR ' || TO_CHAR(cu.exchange_rate_to_pkr, '990.0000') || ' [Updated: ' || cu.lu || ']');
        END LOOP;

    ELSIF v_action = 5 THEN
        DBMS_OUTPUT.PUT_LINE('TEST: ROOM RESERVATION & CONFLICT OVERLAP PREVENTION ENGINE');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        BEGIN
            sp_book_room(
                p_hotel_id      => 1,
                p_room_id       => 1,
                p_guest_name    => 'Audit Admin Test',
                p_guest_contact => '+92-300-1234567',
                p_check_in      => TO_DATE('2025-06-01', 'YYYY-MM-DD'),
                p_check_out     => TO_DATE('2025-06-05', 'YYYY-MM-DD'),
                o_booking_id    => v_bid,
                o_total_price   => v_cost
            );
            DBMS_OUTPUT.PUT_LINE('Step 1: Placed initial booking ID ' || v_bid || ' for June 1 to June 5. Total: PKR ' || v_cost);

            -- Attempt conflicting overlap
            sp_book_room(
                p_hotel_id      => 1,
                p_room_id       => 1,
                p_guest_name    => 'Conflicting Guest',
                p_guest_contact => '+92-300-7654321',
                p_check_in      => TO_DATE('2025-06-03', 'YYYY-MM-DD'),
                p_check_out     => TO_DATE('2025-06-07', 'YYYY-MM-DD'),
                o_booking_id    => v_bid,
                o_total_price   => v_cost
            );
            DBMS_OUTPUT.PUT_LINE('FAIL: Overlap check did not trigger.');
        EXCEPTION
            WHEN OTHERS THEN
                DBMS_OUTPUT.PUT_LINE('Step 2: SUCCESS! Overlapping reservation was blocked by trigger.');
                DBMS_OUTPUT.PUT_LINE('Trigger rejection message: ' || SQLERRM);
        END;

    ELSIF v_action = 6 THEN
        DBMS_OUTPUT.PUT_LINE('TEST: ORACLE 23ai AI SEMANTIC VECTOR SEARCH');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('Query: Searching for top landmarks nearest to historic mountain fortress (Skardu Kharpocho embedding):');
        FOR s IN (
            SELECT landmark_name, category, entry_fee,
                   ROUND(VECTOR_DISTANCE(embedding, (SELECT embedding FROM landmarks WHERE landmark_id = 43), COSINE), 4) AS sim
              FROM landmarks
             ORDER BY sim ASC
             FETCH FIRST 5 ROWS ONLY
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(s.landmark_name, 35) || ' (' || RPAD(s.category, 12) || ') | Similarity Distance: ' || s.sim || ' | Fee: PKR ' || s.entry_fee);
        END LOOP;

    ELSE
        DBMS_OUTPUT.PUT_LINE('Invalid action selected. Enter a number between 1 and 6.');
    END IF;
    DBMS_OUTPUT.PUT_LINE('================================================================================');
END;
/
