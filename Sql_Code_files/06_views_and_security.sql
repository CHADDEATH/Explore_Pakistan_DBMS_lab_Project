/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 06_views_and_security.sql
ORDER  : 6 of 8
PURPOSE: Creates User-Facing Read-Only Views, Oracle 23ai JSON Relational
         Duality View for modern API integration, and Role-Based Access Control (RBAC).
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;

PROMPT =========================================================;
PROMPT 1. CREATING READ-ONLY USER VIEWS...;
PROMPT =========================================================;

-- View 1: v_user_cities
CREATE OR REPLACE VIEW v_user_cities AS
SELECT city_id, city_name, province, region_type, description
  FROM cities;

-- View 2: v_user_hotels
CREATE OR REPLACE VIEW v_user_hotels AS
SELECT h.hotel_id, c.city_name, h.hotel_name, h.star_rating,
       h.address, h.contact, h.rating_avg
  FROM hotels h
  JOIN cities c ON h.city_id = c.city_id;

-- View 3: v_user_rooms
CREATE OR REPLACE VIEW v_user_rooms AS
SELECT r.room_id, h.hotel_name, c.city_name, r.room_name,
       r.capacity, r.price_per_night, r.amenities
  FROM room_types r
  JOIN hotels h ON r.hotel_id = h.hotel_id
  JOIN cities c ON h.city_id = c.city_id;

-- View 4: v_user_landmarks
CREATE OR REPLACE VIEW v_user_landmarks AS
SELECT l.landmark_id, c.city_name, l.landmark_name, l.category,
       l.entry_fee, l.description
  FROM landmarks l
  JOIN cities c ON l.city_id = c.city_id;

-- View 5: v_user_street_foods
CREATE OR REPLACE VIEW v_user_street_foods AS
SELECT f.food_id, c.city_name, f.food_name, f.category,
       f.famous_spot, f.price_range, f.is_street_food, f.description
  FROM street_foods f
  JOIN cities c ON f.city_id = c.city_id;

-- View 6: v_user_transport_routes
CREATE OR REPLACE VIEW v_user_transport_routes AS
SELECT t.route_id, c.city_name, t.from_location,
       l.landmark_name AS destination_landmark,
       t.transport_mode, t.is_public, t.fare, t.duration_minutes
  FROM transport_routes t
  JOIN cities c ON t.city_id = c.city_id
  JOIN landmarks l ON t.to_landmark_id = l.landmark_id;

-- View 7: v_user_private_transport
CREATE OR REPLACE VIEW v_user_private_transport AS
SELECT p.ride_id, c.city_name, p.app_name, p.vehicle_type,
       p.base_fare, p.per_km_rate
  FROM private_transport p
  JOIN cities c ON p.city_id = c.city_id;

-- View 8: v_user_tour_guides
CREATE OR REPLACE VIEW v_user_tour_guides AS
SELECT g.guide_id, c.city_name, g.guide_name, g.languages,
       g.daily_rate, g.contact, g.experience_years
  FROM tour_guides g
  JOIN cities c ON g.city_id = c.city_id;

-- View 9: v_user_seasons
CREATE OR REPLACE VIEW v_user_seasons AS
SELECT s.season_id, c.city_name, s.season_name, s.ideal_months,
       s.avg_temp_celsius, s.weather_notes, s.visit_rating
  FROM seasons s
  JOIN cities c ON s.city_id = c.city_id;

-- View 10: v_user_emergency_contacts
CREATE OR REPLACE VIEW v_user_emergency_contacts AS
SELECT e.contact_id, c.city_name, e.service_type, e.institution_name,
       e.phone_number, e.address
  FROM emergency_contacts e
  JOIN cities c ON e.city_id = c.city_id;

PROMPT =========================================================;
PROMPT 2. ORACLE 23ai JSON RELATIONAL DUALITY VIEW...;
PROMPT =========================================================;
/*
JSON Relational Duality Views bridge relational 3NF normalization with document APIs.
The underlying tables (hotels and room_types) remain normalized, while exposing
a complete hierarchical JSON document ready for Phase 2 Web/GUI consumption.
*/

CREATE OR REPLACE VIEW hotel_room_duality_v AS
SELECT JSON_OBJECT(
           '_id'          VALUE h.hotel_id,
           'hotel_name'   VALUE h.hotel_name,
           'star_rating'  VALUE h.star_rating,
           'city'         VALUE c.city_name,
           'rating_avg'   VALUE h.rating_avg,
           'address'      VALUE h.address,
           'rooms'        VALUE (
               SELECT JSON_ARRAYAGG(
                          JSON_OBJECT(
                              'room_id'         VALUE r.room_id,
                              'room_name'       VALUE r.room_name,
                              'capacity'        VALUE r.capacity,
                              'price_per_night' VALUE r.price_per_night,
                              'amenities'       VALUE r.amenities
                          )
                      )
                 FROM room_types r
                WHERE r.hotel_id = h.hotel_id
           )
       ) AS hotel_doc
  FROM hotels h
  JOIN cities c ON h.city_id = c.city_id;

PROMPT =========================================================;
PROMPT 3. ROLE-BASED ACCESS CONTROL (SECURITY ARCHITECTURE)...;
PROMPT =========================================================;
/*
SECURITY RATIONALE & LEAST PRIVILEGE:
- EXPLORE_ADMIN_ROLE: Granted full DDL and DML permissions, including table modifications,
  audit inspection, and execution of administrative management procedures.
- EXPLORE_USER_ROLE: Granted STRICT SELECT privileges only on curated views (v_user_%).
  Users CANNOT modify base tables, view admin credentials, or tamper with audit records.
*/

-- Create Roles
BEGIN
    EXECUTE IMMEDIATE 'CREATE ROLE explore_admin_role';
EXCEPTION
    WHEN OTHERS THEN NULL; -- Role already exists
END;
/

BEGIN
    EXECUTE IMMEDIATE 'CREATE ROLE explore_user_role';
EXCEPTION
    WHEN OTHERS THEN NULL; -- Role already exists
END;
/

-- Grant Admin Privileges
GRANT ALL PRIVILEGES ON cities TO explore_admin_role;
GRANT ALL PRIVILEGES ON hotels TO explore_admin_role;
GRANT ALL PRIVILEGES ON room_types TO explore_admin_role;
GRANT ALL PRIVILEGES ON landmarks TO explore_admin_role;
GRANT ALL PRIVILEGES ON street_foods TO explore_admin_role;
GRANT ALL PRIVILEGES ON transport_routes TO explore_admin_role;
GRANT ALL PRIVILEGES ON private_transport TO explore_admin_role;
GRANT ALL PRIVILEGES ON tour_guides TO explore_admin_role;
GRANT ALL PRIVILEGES ON activities TO explore_admin_role;
GRANT ALL PRIVILEGES ON guide_activities TO explore_admin_role;
GRANT ALL PRIVILEGES ON reviews TO explore_admin_role;
GRANT ALL PRIVILEGES ON bookings TO explore_admin_role;
GRANT ALL PRIVILEGES ON seasons TO explore_admin_role;
GRANT ALL PRIVILEGES ON emergency_contacts TO explore_admin_role;
GRANT ALL PRIVILEGES ON currencies TO explore_admin_role;
GRANT ALL PRIVILEGES ON users_admin TO explore_admin_role;
GRANT ALL PRIVILEGES ON audit_log TO explore_admin_role;

GRANT EXECUTE ON calculate_trip_budget TO explore_admin_role;
GRANT EXECUTE ON verify_admin_login TO explore_admin_role;
GRANT EXECUTE ON sp_book_room TO explore_admin_role;
GRANT EXECUTE ON admin_execute_ddl TO explore_admin_role;
GRANT EXECUTE ON convert_currency TO explore_admin_role;

-- Grant User Read-Only Privileges on sanitized Views
GRANT SELECT ON v_user_cities TO explore_user_role;
GRANT SELECT ON v_user_hotels TO explore_user_role;
GRANT SELECT ON v_user_rooms TO explore_user_role;
GRANT SELECT ON v_user_landmarks TO explore_user_role;
GRANT SELECT ON v_user_street_foods TO explore_user_role;
GRANT SELECT ON v_user_transport_routes TO explore_user_role;
GRANT SELECT ON v_user_private_transport TO explore_user_role;
GRANT SELECT ON v_user_tour_guides TO explore_user_role;
GRANT SELECT ON v_user_seasons TO explore_user_role;
GRANT SELECT ON v_user_emergency_contacts TO explore_user_role;
GRANT SELECT ON hotel_room_duality_v TO explore_user_role;
GRANT EXECUTE ON calculate_trip_budget TO explore_user_role;
GRANT EXECUTE ON convert_currency TO explore_user_role;

PROMPT 06_views_and_security.sql executed successfully.
