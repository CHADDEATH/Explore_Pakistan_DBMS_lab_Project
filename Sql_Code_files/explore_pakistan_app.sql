/*
================================================================================
PROJECT: Explore Pakistan - Interactive PL/SQL Console Application
SCRIPT : explore_pakistan_app.sql
RUN IN : Oracle SQL Developer / SQL*Plus
USAGE  : Run Script (F5) in SQL Developer
================================================================================
*/

SET SERVEROUTPUT ON SIZE 1000000;
SET LINESIZE 200;
SET PAGESIZE 100;
SET VERIFY OFF;
SET FEEDBACK OFF;

PROMPT ================================================================================;
PROMPT                  WELCOME TO EXPLORE PAKISTAN (PHASE 1)
PROMPT ================================================================================;
PROMPT  CHOOSE YOUR PANEL:
PROMPT    [1] User Panel  - Direct Access (Read, Search, Explore, and Budget Estimator)
PROMPT    [2] Admin Panel - Requires Password Authentication (admin / admin)
PROMPT ================================================================================;

-- Prompt 1: Panel Selection
-- Dialog Box in SQL Developer will show: "Enter value for enter_1_for_user_panel_or_2_for_admin"
ACCEPT enter_1_for_user_panel_or_2_for_admin DEFAULT '1' PROMPT 'Select Panel (1 for User, 2 for Admin) [Default 1]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  DESTINATIONS AVAILABLE:
PROMPT    [1] Islamabad (Federal Capital)
PROMPT    [2] Lahore    (Cultural & Historical)
PROMPT    [3] Karachi   (Coastal & Financial Hub)
PROMPT    [4] Gilgit    (Silk Road & Karakoram Mountains)
PROMPT    [5] Skardu    (Gateway to K2, Deosai & Lakes)
PROMPT --------------------------------------------------------------------------------;

-- Prompt 2: Destination Selection
ACCEPT choose_city_1_Islamabad_2_Lahore_3_Karachi_4_Gilgit_5_Skardu DEFAULT '1' PROMPT 'Select City (1 to 5) [Default 1]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  HOTEL STAR RATING FILTER:
PROMPT    Enter: 5 (5-Star), 4 (4-Star), 3 (3-Star), 2 (2-Star), or 0 (Show All)
PROMPT --------------------------------------------------------------------------------;

-- Prompt 3: Star Rating Filter
ACCEPT filter_hotel_stars_2_to_5_or_0_for_all DEFAULT '5' PROMPT 'Filter Hotels by Stars (5, 4, 3, 2, or 0) [Default 5]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  TOUR GUIDE PREFERENCE:
PROMPT    [1] Yes - Show certified tour guides with languages, rates, and contact info
PROMPT    [2] No  - Skip tour guide
PROMPT --------------------------------------------------------------------------------;

-- Prompt 4: Guide Preference
ACCEPT need_tour_guide_enter_1_for_yes_or_2_for_no DEFAULT '1' PROMPT 'Need Tour Guide? (1 for Yes, 2 for No) [Default 1]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  TRIP BUDGET ESTIMATOR PARAMETERS:
PROMPT --------------------------------------------------------------------------------;

-- Prompt 5: Duration
ACCEPT trip_duration_in_days DEFAULT '3' PROMPT 'Enter Trip Duration in Days (e.g. 3, 5, 7) [Default 3]: ';

-- Prompt 6: Number of Travelers
ACCEPT number_of_travelers DEFAULT '2' PROMPT 'Enter Number of Travelers (e.g. 1, 2, 4) [Default 2]: ';

PROMPT ;
PROMPT --------------------------------------------------------------------------------;
PROMPT  ADMIN CREDENTIALS (If you selected Admin Panel):
PROMPT    Default Username: admin
PROMPT    Default Password: admin
PROMPT --------------------------------------------------------------------------------;

-- Prompt 7: Admin Username
ACCEPT admin_username_default_admin DEFAULT 'admin' PROMPT 'Admin Username (default: admin): ';

-- Prompt 8: Admin Password
ACCEPT admin_password_default_admin DEFAULT 'admin' PROMPT 'Admin Password (default: admin): ';

PROMPT ================================================================================;
PROMPT                       PROCESSING YOUR REQUEST...
PROMPT ================================================================================;

DECLARE
    v_panel_sel    VARCHAR2(10) := TRIM('&enter_1_for_user_panel_or_2_for_admin');
    v_city_sel     NUMBER       := TO_NUMBER(NVL(TRIM('&choose_city_1_Islamabad_2_Lahore_3_Karachi_4_Gilgit_5_Skardu'), '1'));
    v_star_sel     NUMBER       := TO_NUMBER(NVL(TRIM('&filter_hotel_stars_2_to_5_or_0_for_all'), '5'));
    v_guide_sel    VARCHAR2(10) := TRIM('&need_tour_guide_enter_1_for_yes_or_2_for_no');
    v_days         NUMBER       := TO_NUMBER(NVL(TRIM('&trip_duration_in_days'), '3'));
    v_people       NUMBER       := TO_NUMBER(NVL(TRIM('&number_of_travelers'), '2'));
    v_admin_user   VARCHAR2(50) := TRIM('&admin_username_default_admin');
    v_admin_pass   VARCHAR2(50) := TRIM('&admin_password_default_admin');

    v_city_name    VARCHAR2(50);
    v_province     VARCHAR2(50);
    v_region       VARCHAR2(30);
    v_city_desc    VARCHAR2(1000);

    v_total_cost   NUMBER;
    v_hotel_cost   NUMBER;
    v_food_cost    NUMBER;
    v_trans_cost   NUMBER;
    v_guide_cost   NUMBER;
    v_entry_cost   NUMBER;
    v_auth_result  NUMBER;
    v_hotel_count  NUMBER := 0;
BEGIN
    -- Fallback for city_sel range
    IF v_city_sel NOT BETWEEN 1 AND 5 THEN
        v_city_sel := 1;
    END IF;

    -- =========================================================================
    -- PANEL 1: USER PANEL FLOW (Steps 1 through 9)
    -- =========================================================================
    IF v_panel_sel = '1' THEN
        SELECT city_name, province, region_type, description
          INTO v_city_name, v_province, v_region, v_city_desc
          FROM cities
         WHERE city_id = v_city_sel;

        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('                         EXPLORE PAKISTAN - USER PANEL                          ');
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 1 & 2: SELECTED DESTINATION');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('City       : ' || UPPER(v_city_name) || ' (' || v_province || ')');
        DBMS_OUTPUT.PUT_LINE('Region     : ' || v_region);
        DBMS_OUTPUT.PUT_LINE('Description: ' || v_city_desc);
        DBMS_OUTPUT.PUT_LINE('');

        -- STEP 3 & 4: HOTELS & ROOM TYPES
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 3 & 4: HOTELS AND ROOM RATES');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR h IN (
            SELECT hotel_id, hotel_name, star_rating, address, contact, rating_avg
              FROM hotels
             WHERE city_id = v_city_sel
               AND (v_star_sel = 0 OR star_rating = v_star_sel)
             ORDER BY star_rating DESC, rating_avg DESC
        ) LOOP
            v_hotel_count := v_hotel_count + 1;
            DBMS_OUTPUT.PUT_LINE('  * [' || h.hotel_id || '] ' || RPAD(h.hotel_name, 35) || ' | ' || h.star_rating || '-Star | Rating: ' || TO_CHAR(h.rating_avg, '0.0') || '/5.0');
            DBMS_OUTPUT.PUT_LINE('    Address: ' || h.address || ' | Phone: ' || NVL(h.contact, 'N/A'));
            -- Show room types for this hotel
            FOR r IN (
                SELECT room_name, capacity, price_per_night, amenities
                  FROM room_types
                 WHERE hotel_id = h.hotel_id
                 ORDER BY price_per_night ASC
            ) LOOP
                DBMS_OUTPUT.PUT_LINE('      -> Room: ' || RPAD(r.room_name, 25) || ' | Guests: ' || r.capacity || ' | Rate: PKR ' || TO_CHAR(r.price_per_night, '999,990.00') || '/night');
                DBMS_OUTPUT.PUT_LINE('         Amenities: ' || r.amenities);
            END LOOP;
            DBMS_OUTPUT.PUT_LINE('');
        END LOOP;

        IF v_hotel_count = 0 THEN
            DBMS_OUTPUT.PUT_LINE('  No hotels found matching the specified star rating. Showing all hotels:');
            FOR h IN (SELECT hotel_id, hotel_name, star_rating FROM hotels WHERE city_id = v_city_sel) LOOP
                DBMS_OUTPUT.PUT_LINE('  * [' || h.hotel_id || '] ' || h.hotel_name || ' (' || h.star_rating || '-Star)');
            END LOOP;
        END IF;

        -- STEP 5: TOUR GUIDES
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 5: CERTIFIED TOUR GUIDES');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        IF v_guide_sel = '1' THEN
            FOR g IN (
                SELECT guide_name, languages, daily_rate, contact, experience_years
                  FROM tour_guides
                 WHERE city_id = v_city_sel
                 ORDER BY daily_rate ASC
            ) LOOP
                DBMS_OUTPUT.PUT_LINE('  * Guide: ' || RPAD(g.guide_name, 22) || ' | Experience: ' || g.experience_years || ' yrs | Rate: PKR ' || TO_CHAR(g.daily_rate, '999,990.00') || '/day');
                DBMS_OUTPUT.PUT_LINE('    Languages: ' || RPAD(g.languages, 35) || ' | Contact: ' || g.contact);
            END LOOP;
        ELSE
            DBMS_OUTPUT.PUT_LINE('  You selected: No Tour Guide required.');
        END IF;
        DBMS_OUTPUT.PUT_LINE('');

        -- STEP 6: STREET FOODS & FAMOUS DELICACIES
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 6: ICONIC STREET FOODS AND CULINARY SPOTS');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR f IN (
            SELECT food_name, category, famous_spot, price_range, description
              FROM street_foods
             WHERE city_id = v_city_sel
             ORDER BY food_id ASC
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(f.food_name, 35) || ' (' || f.category || ') - ' || f.price_range);
            DBMS_OUTPUT.PUT_LINE('    Famous Spot: ' || f.famous_spot);
            DBMS_OUTPUT.PUT_LINE('    Description: ' || f.description);
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('');

        -- STEP 7: SIGHTSEEING LANDMARKS
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 7: TOP SIGHTSEEING LANDMARKS');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        FOR l IN (
            SELECT landmark_id, landmark_name, category, entry_fee, description
              FROM landmarks
             WHERE city_id = v_city_sel
             ORDER BY entry_fee DESC
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('  * [' || l.landmark_id || '] ' || RPAD(l.landmark_name, 36) || ' | ' || RPAD(l.category, 12) || ' | Fee: PKR ' || TO_CHAR(l.entry_fee, '990.00'));
            DBMS_OUTPUT.PUT_LINE('    Info: ' || l.description);
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('');

        -- STEP 8: TRANSPORTATION (PUBLIC VS PRIVATE)
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 8: TRANSPORT ROUTES & RIDE-HAILING SERVICES');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('A) Public Urban Corridors:');
        FOR t IN (
            SELECT t.from_location, l.landmark_name, t.transport_mode, t.fare, t.duration_minutes
              FROM transport_routes t
              JOIN landmarks l ON t.to_landmark_id = l.landmark_id
             WHERE t.city_id = v_city_sel AND t.is_public = 'Y'
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('   -> From: ' || RPAD(t.from_location, 30) || ' To: ' || RPAD(t.landmark_name, 28) || ' | ' || RPAD(t.transport_mode, 25) || ' | PKR ' || t.fare || ' (' || t.duration_minutes || ' mins)');
        END LOOP;

        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('B) Private Ride-Hailing Tariffs (Careem, InDrive, Yango, Rentals):');
        FOR p IN (
            SELECT app_name, vehicle_type, base_fare, per_km_rate
              FROM private_transport
             WHERE city_id = v_city_sel
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('   -> ' || RPAD(p.app_name, 15) || ' | ' || RPAD(p.vehicle_type, 30) || ' | Base: PKR ' || p.base_fare || ' | Rate: PKR ' || p.per_km_rate || '/km');
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('');

        -- STEP 9: TRIP BUDGET ESTIMATE
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('STEP 9: ITEMIZED TRIP BUDGET ESTIMATE');
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        calculate_trip_budget(
            p_city_id        => v_city_sel,
            p_days           => v_days,
            p_star_rating    => CASE WHEN v_star_sel BETWEEN 2 AND 5 THEN v_star_sel ELSE 4 END,
            p_num_people     => v_people,
            p_include_guide  => CASE WHEN v_guide_sel = '1' THEN 'Y' ELSE 'N' END,
            o_total_cost     => v_total_cost,
            o_hotel_cost     => v_hotel_cost,
            o_food_cost      => v_food_cost,
            o_transport_cost => v_trans_cost,
            o_guide_cost     => v_guide_cost,
            o_entry_cost     => v_entry_cost
        );

        -- Emergency Contacts and Seasons quick footer
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('EMERGENCY CONTACTS IN ' || UPPER(v_city_name) || ':');
        FOR e IN (SELECT service_type, institution_name, phone_number FROM emergency_contacts WHERE city_id = v_city_sel) LOOP
            DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(e.service_type, 22) || ' : ' || RPAD(e.institution_name, 40) || ' | Tel: ' || e.phone_number);
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('                 END OF USER EXPLORATION REPORT (PHASE 1)                       ');
        DBMS_OUTPUT.PUT_LINE('================================================================================');

    -- =========================================================================
    -- PANEL 2: ADMIN PANEL FLOW (Requires Authentication)
    -- =========================================================================
    ELSIF v_panel_sel = '2' THEN
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('                        ADMIN PANEL - AUTHENTICATION                            ');
        DBMS_OUTPUT.PUT_LINE('================================================================================');
        DBMS_OUTPUT.PUT_LINE('Verifying credentials for username: ' || v_admin_user || '...');

        v_auth_result := verify_admin_login(v_admin_user, v_admin_pass);

        IF v_auth_result = 1 THEN
            DBMS_OUTPUT.PUT_LINE('>>> AUTHENTICATION SUCCESSFUL! Logged in as: ' || v_admin_user);
            DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
            DBMS_OUTPUT.PUT_LINE('ADMINISTRATIVE POWERS ACTIVE:');
            DBMS_OUTPUT.PUT_LINE('  * Full DDL and DML on all 17 tables (HOTELS, BOOKINGS, LANDMARKS, etc.)');
            DBMS_OUTPUT.PUT_LINE('  * Audit trail inspection (AUDIT_LOG table)');
            DBMS_OUTPUT.PUT_LINE('  * Controlled administrative DDL procedure: admin_execute_ddl(...)');
            DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
            DBMS_OUTPUT.PUT_LINE('CURRENT SYSTEM HEALTH SUMMARY:');
            FOR t IN (
                SELECT 'CITIES' as tbl, count(*) as cnt FROM cities
                UNION ALL SELECT 'HOTELS', count(*) FROM hotels
                UNION ALL SELECT 'ROOM_TYPES', count(*) FROM room_types
                UNION ALL SELECT 'LANDMARKS', count(*) FROM landmarks
                UNION ALL SELECT 'STREET_FOODS', count(*) FROM street_foods
                UNION ALL SELECT 'BOOKINGS', count(*) FROM bookings
                UNION ALL SELECT 'REVIEWS', count(*) FROM reviews
                UNION ALL SELECT 'AUDIT_LOG', count(*) FROM audit_log
            ) LOOP
                DBMS_OUTPUT.PUT_LINE('  Table ' || RPAD(t.tbl, 15) || ' : ' || LPAD(t.cnt, 4) || ' active records');
            END LOOP;
            DBMS_OUTPUT.PUT_LINE('--------------------------------------------------------------------------------');
            DBMS_OUTPUT.PUT_LINE('To view advanced analytical reports, execute:');
            DBMS_OUTPUT.PUT_LINE('  @07_reports.sql');
            DBMS_OUTPUT.PUT_LINE('To run the automated verification test suite, execute:');
            DBMS_OUTPUT.PUT_LINE('  @08_test_queries.sql');
            DBMS_OUTPUT.PUT_LINE('================================================================================');
        ELSE
            DBMS_OUTPUT.PUT_LINE('>>> AUTHENTICATION FAILED! Invalid username or password.');
            DBMS_OUTPUT.PUT_LINE('Note: The default credentials are username: admin, password: admin');
            DBMS_OUTPUT.PUT_LINE('================================================================================');
        END IF;

    ELSE
        DBMS_OUTPUT.PUT_LINE('Invalid panel choice. Please enter 1 for User Panel or 2 for Admin Panel.');
    END IF;
END;
/
