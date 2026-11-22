/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 07_reports.sql
ORDER  : 7 of 8
PURPOSE: Advanced Admin Analytical Reports utilizing GROUP BY, HAVING, RANK(),
         DENSE_RANK(), ROW_NUMBER(), and Subqueries.
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;
SET LINESIZE 200;
SET PAGESIZE 100;

PROMPT =========================================================;
PROMPT REPORT 1: TOP-3 RATED HOTELS PER CITY (DENSE_RANK);
PROMPT =========================================================;
SELECT city_name, hotel_name, star_rating, rating_avg, city_rank
  FROM (
      SELECT c.city_name, h.hotel_name, h.star_rating, h.rating_avg,
             DENSE_RANK() OVER (PARTITION BY c.city_name ORDER BY h.rating_avg DESC, h.star_rating DESC) AS city_rank
        FROM hotels h
        JOIN cities c ON h.city_id = c.city_id
  )
 WHERE city_rank <= 3
 ORDER BY city_name, city_rank;

PROMPT =========================================================;
PROMPT REPORT 2: CHEAPEST ROOM OPTION PER STAR RATING (ROW_NUMBER);
PROMPT =========================================================;
SELECT star_rating, hotel_name, room_name, price_per_night, capacity
  FROM (
      SELECT h.star_rating, h.hotel_name, r.room_name, r.price_per_night, r.capacity,
             ROW_NUMBER() OVER (PARTITION BY h.star_rating ORDER BY r.price_per_night ASC) AS rn
        FROM room_types r
        JOIN hotels h ON r.hotel_id = h.hotel_id
  )
 WHERE rn = 1
 ORDER BY star_rating DESC;

PROMPT =========================================================;
PROMPT REPORT 3: CITY TOURISM PROFILE & AVERAGE ROOM RATES (GROUP BY);
PROMPT =========================================================;
SELECT c.city_name,
       c.region_type,
       COUNT(DISTINCT h.hotel_id) AS total_hotels,
       ROUND(AVG(r.price_per_night), 2) AS avg_room_rate_pkr,
       COUNT(DISTINCT l.landmark_id) AS total_landmarks,
       ROUND(AVG(l.entry_fee), 2) AS avg_landmark_fee_pkr
  FROM cities c
  LEFT JOIN hotels h ON c.city_id = h.city_id
  LEFT JOIN room_types r ON h.hotel_id = r.hotel_id
  LEFT JOIN landmarks l ON c.city_id = l.city_id
 GROUP BY c.city_name, c.region_type
 ORDER BY avg_room_rate_pkr DESC;

PROMPT =========================================================;
PROMPT REPORT 4: LANDMARK DENSITY BY CATEGORY (HAVING > 3);
PROMPT =========================================================;
SELECT category,
       COUNT(*) AS landmark_count,
       MIN(entry_fee) AS min_fee_pkr,
       MAX(entry_fee) AS max_fee_pkr,
       ROUND(AVG(entry_fee), 2) AS avg_fee_pkr
  FROM landmarks
 GROUP BY category
HAVING COUNT(*) > 3
 ORDER BY landmark_count DESC;

PROMPT =========================================================;
PROMPT REPORT 5: PUBLIC VS PRIVATE TRANSIT ECONOMIC COMPARISON;
PROMPT =========================================================;
SELECT c.city_name,
       ROUND(AVG(t.fare), 2) AS avg_public_route_fare_pkr,
       ROUND(AVG(t.duration_minutes), 1) AS avg_public_duration_mins,
       ROUND(AVG(p.base_fare), 2) AS avg_private_base_fare_pkr,
       ROUND(AVG(p.per_km_rate), 2) AS avg_private_per_km_pkr
  FROM cities c
  LEFT JOIN transport_routes t ON c.city_id = t.city_id AND t.is_public = 'Y'
  LEFT JOIN private_transport p ON c.city_id = p.city_id
 GROUP BY c.city_name
 ORDER BY c.city_name;

PROMPT =========================================================;
PROMPT REPORT 6: TOUR GUIDE VERSATILITY & DAILY RATES;
PROMPT =========================================================;
SELECT c.city_name,
       COUNT(g.guide_id) AS total_guides,
       ROUND(AVG(g.daily_rate), 2) AS avg_daily_rate_pkr,
       ROUND(AVG(g.experience_years), 1) AS avg_experience_years,
       MAX(g.daily_rate) AS peak_guide_rate_pkr
  FROM tour_guides g
  JOIN cities c ON g.city_id = c.city_id
 GROUP BY c.city_name
 ORDER BY avg_daily_rate_pkr DESC;

PROMPT =========================================================;
PROMPT REPORT 7: STREET FOOD DIVERSITY BY REGION (GROUP BY);
PROMPT =========================================================;
SELECT c.city_name,
       f.category,
       COUNT(*) AS item_count,
       LISTAGG(f.food_name, ', ') WITHIN GROUP (ORDER BY f.food_name) AS sample_dishes
  FROM street_foods f
  JOIN cities c ON f.city_id = c.city_id
 GROUP BY c.city_name, f.category
 ORDER BY c.city_name, item_count DESC;

PROMPT =========================================================;
PROMPT REPORT 8: HOTEL BOOKING REVENUE RANKING (WINDOW FUNCTION);
PROMPT =========================================================;
SELECT h.hotel_name,
       c.city_name,
       COUNT(b.booking_id) AS confirmed_bookings,
       SUM(b.total_price) AS total_revenue_pkr,
       RANK() OVER (ORDER BY SUM(b.total_price) DESC) AS revenue_rank
  FROM bookings b
  JOIN hotels h ON b.hotel_id = h.hotel_id
  JOIN cities c ON h.city_id = c.city_id
 WHERE b.status = 'CONFIRMED'
 GROUP BY h.hotel_name, c.city_name
 ORDER BY revenue_rank;

PROMPT =========================================================;
PROMPT REPORT 9: ADMINISTRATIVE AUDIT ACTIVITY LOG SUMMARY;
PROMPT =========================================================;
SELECT table_name,
       operation,
       COUNT(*) AS operation_count,
       MIN(log_timestamp) AS first_logged,
       MAX(log_timestamp) AS last_logged
  FROM audit_log
 GROUP BY table_name, operation
 ORDER BY operation_count DESC;

PROMPT =========================================================;
PROMPT REPORT 10: INTERNATIONAL CURRENCY CONVERSION TARIFF;
PROMPT =========================================================;
SELECT h.hotel_name,
       r.room_name,
       r.price_per_night AS rate_pkr,
       ROUND(r.price_per_night / (SELECT exchange_rate_to_pkr FROM currencies WHERE currency_code = 'USD'), 2) AS rate_usd,
       ROUND(r.price_per_night / (SELECT exchange_rate_to_pkr FROM currencies WHERE currency_code = 'EUR'), 2) AS rate_eur,
       ROUND(r.price_per_night / (SELECT exchange_rate_to_pkr FROM currencies WHERE currency_code = 'GBP'), 2) AS rate_gbp,
       ROUND(r.price_per_night / (SELECT exchange_rate_to_pkr FROM currencies WHERE currency_code = 'AED'), 2) AS rate_aed
  FROM room_types r
  JOIN hotels h ON r.hotel_id = h.hotel_id
 WHERE h.star_rating = 5 AND r.room_name LIKE '%Suite%'
 ORDER BY r.price_per_night DESC;

PROMPT 07_reports.sql executed successfully.
