/*
================================================================================
PROJECT: Explore Pakistan - Phase 1 (DBMS Lab Project)
SCRIPT : 02_constraints.sql
ORDER  : 2 of 8
PURPOSE: Implements Foreign Keys, Unique Keys, and CHECK Constraints across all tables.
IDEMPOTENT: Uses alter statements that cleanly establish constraints.
================================================================================
*/

SET ECHO ON;
SET FEEDBACK ON;

PROMPT =========================================================;
PROMPT ADDING FOREIGN KEY CONSTRAINTS...;
PROMPT =========================================================;

-- HOTELS Foreign Key
ALTER TABLE hotels
    ADD CONSTRAINT fk_hotels_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- ROOM_TYPES Foreign Key
ALTER TABLE room_types
    ADD CONSTRAINT fk_rooms_hotel FOREIGN KEY (hotel_id)
    REFERENCES hotels (hotel_id) ON DELETE CASCADE;

-- LANDMARKS Foreign Key
ALTER TABLE landmarks
    ADD CONSTRAINT fk_landmarks_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- STREET_FOODS Foreign Key
ALTER TABLE street_foods
    ADD CONSTRAINT fk_foods_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- TRANSPORT_ROUTES Foreign Keys
ALTER TABLE transport_routes
    ADD CONSTRAINT fk_routes_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

ALTER TABLE transport_routes
    ADD CONSTRAINT fk_routes_landmark FOREIGN KEY (to_landmark_id)
    REFERENCES landmarks (landmark_id) ON DELETE CASCADE;

-- PRIVATE_TRANSPORT Foreign Key
ALTER TABLE private_transport
    ADD CONSTRAINT fk_priv_trans_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- TOUR_GUIDES Foreign Key
ALTER TABLE tour_guides
    ADD CONSTRAINT fk_guides_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- ACTIVITIES Foreign Key
ALTER TABLE activities
    ADD CONSTRAINT fk_activities_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- GUIDE_ACTIVITIES Junction Foreign Keys
ALTER TABLE guide_activities
    ADD CONSTRAINT fk_ga_guide FOREIGN KEY (guide_id)
    REFERENCES tour_guides (guide_id) ON DELETE CASCADE;

ALTER TABLE guide_activities
    ADD CONSTRAINT fk_ga_activity FOREIGN KEY (activity_id)
    REFERENCES activities (activity_id) ON DELETE CASCADE;

-- REVIEWS Foreign Keys
ALTER TABLE reviews
    ADD CONSTRAINT fk_reviews_hotel FOREIGN KEY (hotel_id)
    REFERENCES hotels (hotel_id) ON DELETE CASCADE;

ALTER TABLE reviews
    ADD CONSTRAINT fk_reviews_food FOREIGN KEY (food_id)
    REFERENCES street_foods (food_id) ON DELETE CASCADE;

ALTER TABLE reviews
    ADD CONSTRAINT fk_reviews_landmark FOREIGN KEY (landmark_id)
    REFERENCES landmarks (landmark_id) ON DELETE CASCADE;

-- BOOKINGS Foreign Keys
ALTER TABLE bookings
    ADD CONSTRAINT fk_bookings_hotel FOREIGN KEY (hotel_id)
    REFERENCES hotels (hotel_id) ON DELETE CASCADE;

ALTER TABLE bookings
    ADD CONSTRAINT fk_bookings_room FOREIGN KEY (room_id)
    REFERENCES room_types (room_id) ON DELETE CASCADE;

-- SEASONS Foreign Key
ALTER TABLE seasons
    ADD CONSTRAINT fk_seasons_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

-- EMERGENCY_CONTACTS Foreign Key
ALTER TABLE emergency_contacts
    ADD CONSTRAINT fk_contacts_city FOREIGN KEY (city_id)
    REFERENCES cities (city_id) ON DELETE CASCADE;

PROMPT =========================================================;
PROMPT ADDING DOMAIN AND INTEGRITY CHECK CONSTRAINTS...;
PROMPT =========================================================;

-- CITIES Constraints
ALTER TABLE cities
    ADD CONSTRAINT chk_cities_region
    CHECK (region_type IN ('Metropolitan', 'City', 'Northern Area', 'Coastal', 'Historical'));

-- HOTELS Constraints
ALTER TABLE hotels
    ADD CONSTRAINT chk_hotels_stars
    CHECK (star_rating BETWEEN 2 AND 5);

ALTER TABLE hotels
    ADD CONSTRAINT chk_hotels_rating_avg
    CHECK (rating_avg BETWEEN 0.0 AND 5.0);

-- ROOM_TYPES Constraints
ALTER TABLE room_types
    ADD CONSTRAINT chk_rooms_capacity
    CHECK (capacity > 0);

ALTER TABLE room_types
    ADD CONSTRAINT chk_rooms_price
    CHECK (price_per_night > 0);

-- LANDMARKS Constraints
ALTER TABLE landmarks
    ADD CONSTRAINT chk_landmarks_category
    CHECK (category IN ('Historical', 'Natural', 'Cultural', 'Religious', 'Monument', 'Park', 'Museum', 'Recreation'));

ALTER TABLE landmarks
    ADD CONSTRAINT chk_landmarks_entry_fee
    CHECK (entry_fee >= 0);

-- STREET_FOODS Constraints
ALTER TABLE street_foods
    ADD CONSTRAINT chk_foods_is_street
    CHECK (is_street_food IN ('Y', 'N'));

-- TRANSPORT_ROUTES Constraints
ALTER TABLE transport_routes
    ADD CONSTRAINT chk_routes_is_public
    CHECK (is_public IN ('Y', 'N'));

ALTER TABLE transport_routes
    ADD CONSTRAINT chk_routes_fare
    CHECK (fare >= 0);

ALTER TABLE transport_routes
    ADD CONSTRAINT chk_routes_duration
    CHECK (duration_minutes > 0);

-- PRIVATE_TRANSPORT Constraints
ALTER TABLE private_transport
    ADD CONSTRAINT chk_priv_trans_base_fare
    CHECK (base_fare >= 0);

ALTER TABLE private_transport
    ADD CONSTRAINT chk_priv_trans_km_rate
    CHECK (per_km_rate >= 0);

-- TOUR_GUIDES Constraints
ALTER TABLE tour_guides
    ADD CONSTRAINT chk_guides_rate
    CHECK (daily_rate > 0);

ALTER TABLE tour_guides
    ADD CONSTRAINT chk_guides_exp
    CHECK (experience_years >= 0);

-- REVIEWS Constraints:
-- Pure 3NF Relational Integrity: Enforces that exactly ONE foreign key target is populated per review.
ALTER TABLE reviews
    ADD CONSTRAINT chk_reviews_target_exclusivity
    CHECK (
        (CASE WHEN hotel_id IS NOT NULL THEN 1 ELSE 0 END +
         CASE WHEN food_id IS NOT NULL THEN 1 ELSE 0 END +
         CASE WHEN landmark_id IS NOT NULL THEN 1 ELSE 0 END) = 1
    );

ALTER TABLE reviews
    ADD CONSTRAINT chk_reviews_rating
    CHECK (rating BETWEEN 1 AND 5);

-- BOOKINGS Constraints
ALTER TABLE bookings
    ADD CONSTRAINT chk_bookings_dates
    CHECK (check_out_date > check_in_date);

ALTER TABLE bookings
    ADD CONSTRAINT chk_bookings_price
    CHECK (total_price >= 0);

ALTER TABLE bookings
    ADD CONSTRAINT chk_bookings_status
    CHECK (status IN ('CONFIRMED', 'CANCELLED', 'COMPLETED'));

-- SEASONS Constraints
ALTER TABLE seasons
    ADD CONSTRAINT chk_seasons_rating
    CHECK (visit_rating BETWEEN 1.0 AND 5.0);

-- EMERGENCY_CONTACTS Constraints
ALTER TABLE emergency_contacts
    ADD CONSTRAINT chk_contacts_type
    CHECK (service_type IN ('Police Helpline', 'Hospital / Emergency', 'Rescue / Ambulance', 'Tourist Police', 'Disaster Management', 'Foreign Consulate / Embassy'));

-- CURRENCIES Constraints
ALTER TABLE currencies
    ADD CONSTRAINT chk_curr_rate
    CHECK (exchange_rate_to_pkr > 0);

-- AUDIT_LOG Constraints
ALTER TABLE audit_log
    ADD CONSTRAINT chk_audit_operation
    CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE'));

PROMPT 02_constraints.sql executed successfully.
