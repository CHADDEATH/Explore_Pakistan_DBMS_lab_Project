/*
================================================================================
PROJECT: Explore Pakistan - Dedicated User Panel Interactive Exploration
SCRIPT : 09_user_panel_interactive.sql
RUN IN : Oracle SQL Developer / SQL*Plus (F5)
================================================================================
*/

SET SERVEROUTPUT ON SIZE 1000000;
SET LINESIZE 200;
SET PAGESIZE 100;
SET VERIFY OFF;
SET FEEDBACK OFF;

PROMPT ================================================================================;
PROMPT                  EXPLORE PAKISTAN - INTERACTIVE USER PANEL
PROMPT ================================================================================;
PROMPT  NO LOGIN OR REGISTRATION REQUIRED. SELECT YOUR DESTINATION:
PROMPT    [1] Islamabad (Federal Capital)
PROMPT    [2] Lahore    (Cultural & Historical)
PROMPT    [3] Karachi   (Coastal & Financial Hub)
PROMPT    [4] Gilgit    (Silk Road & Karakoram Mountains)
PROMPT    [5] Skardu    (Gateway to K2, Deosai & Lakes)
PROMPT ================================================================================;

ACCEPT select_destination_1_to_5 DEFAULT '1' PROMPT 'Choose City Number (1 to 5) [Default 1]: ';
ACCEPT filter_star_rating_2_to_5_or_0 DEFAULT '5' PROMPT 'Filter Hotels by Stars (2, 3, 4, 5, or 0 for All) [Default 5]: ';
ACCEPT tour_guide_1_for_yes_2_for_no DEFAULT '1' PROMPT 'Do you want a Tour Guide? (1 for Yes, 2 for No) [Default 1]: ';
ACCEPT trip_days DEFAULT '3' PROMPT 'Trip Duration in Days [Default 3]: ';
ACCEPT traveler_count DEFAULT '2' PROMPT 'Number of Travelers [Default 2]: ';

DECLARE
    v_city_sel  NUMBER := TO_NUMBER(NVL(TRIM('&select_destination_1_to_5'), '1'));
    v_star_sel  NUMBER := TO_NUMBER(NVL(TRIM('&filter_star_rating_2_to_5_or_0'), '5'));
    v_guide_sel VARCHAR2(10) := TRIM('&tour_guide_1_for_yes_2_for_no');
    v_days      NUMBER := TO_NUMBER(NVL(TRIM('&trip_days'), '3'));
    v_people    NUMBER := TO_NUMBER(NVL(TRIM('&traveler_count'), '2'));

    v_cname VARCHAR2(50); v_prov VARCHAR2(50); v_reg VARCHAR2(30); v_desc VARCHAR2(1000);
    v_total NUMBER; v_hotel NUMBER; v_food NUMBER; v_trans NUMBER; v_guide NUMBER; v_entry NUMBER;
BEGIN
    IF v_city_sel NOT BETWEEN 1 AND 5 THEN v_city_sel := 1; END IF;
    SELECT city_name, province, region_type, description INTO v_cname, v_prov, v_reg, v_desc FROM cities WHERE city_id = v_city_sel;

    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('================================================================================');
    DBMS_OUTPUT.PUT_LINE('DESTINATION: ' || UPPER(v_cname) || ' (' || v_prov || ' - ' || v_reg || ')');
    DBMS_OUTPUT.PUT_LINE(v_desc);
    DBMS_OUTPUT.PUT_LINE('================================================================================');

    DBMS_OUTPUT.PUT_LINE('HOTELS & ROOM TIERS:');
    FOR h IN (SELECT hotel_id, hotel_name, star_rating, address, contact, rating_avg FROM hotels WHERE city_id = v_city_sel AND (v_star_sel = 0 OR star_rating = v_star_sel)) LOOP
        DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(h.hotel_name, 35) || ' [' || h.star_rating || '-Star] Avg Rating: ' || h.rating_avg || '/5.0 | Tel: ' || h.contact);
        FOR r IN (SELECT room_name, capacity, price_per_night FROM room_types WHERE hotel_id = h.hotel_id) LOOP
            DBMS_OUTPUT.PUT_LINE('     - ' || RPAD(r.room_name, 25) || ' | Max ' || r.capacity || ' Guests | PKR ' || TO_CHAR(r.price_per_night, '999,990.00') || '/night');
        END LOOP;
    END LOOP;

    IF v_guide_sel = '1' THEN
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('CERTIFIED TOUR GUIDES:');
        FOR g IN (SELECT guide_name, languages, daily_rate, contact FROM tour_guides WHERE city_id = v_city_sel) LOOP
            DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(g.guide_name, 20) || ' | Languages: ' || RPAD(g.languages, 30) || ' | PKR ' || TO_CHAR(g.daily_rate, '999,990.00') || '/day | ' || g.contact);
        END LOOP;
    END IF;

    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('STREET FOOD DELICACIES:');
    FOR f IN (SELECT food_name, famous_spot, price_range FROM street_foods WHERE city_id = v_city_sel) LOOP
        DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(f.food_name, 34) || ' | Spot: ' || RPAD(f.famous_spot, 28) || ' | ' || f.price_range);
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('FAMOUS LANDMARKS:');
    FOR l IN (SELECT landmark_name, category, entry_fee FROM landmarks WHERE city_id = v_city_sel) LOOP
        DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(l.landmark_name, 35) || ' | ' || RPAD(l.category, 12) || ' | Entry: PKR ' || l.entry_fee);
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('PUBLIC TRANSPORT CORRIDORS:');
    FOR t IN (SELECT t.from_location, l.landmark_name, t.transport_mode, t.fare FROM transport_routes t JOIN landmarks l ON t.to_landmark_id = l.landmark_id WHERE t.city_id = v_city_sel AND t.is_public = 'Y') LOOP
        DBMS_OUTPUT.PUT_LINE('  * ' || RPAD(t.from_location, 30) || ' -> ' || RPAD(l.landmark_name, 25) || ' | ' || RPAD(t.transport_mode, 25) || ' | PKR ' || t.fare);
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('');
    calculate_trip_budget(
        p_city_id        => v_city_sel,
        p_days           => v_days,
        p_star_rating    => CASE WHEN v_star_sel BETWEEN 2 AND 5 THEN v_star_sel ELSE 4 END,
        p_num_people     => v_people,
        p_include_guide  => CASE WHEN v_guide_sel = '1' THEN 'Y' ELSE 'N' END,
        o_total_cost     => v_total,
        o_hotel_cost     => v_hotel,
        o_food_cost      => v_food,
        o_transport_cost => v_trans,
        o_guide_cost     => v_guide,
        o_entry_cost     => v_entry
    );
END;
/
