# Entity Relationship (ER) Diagram: Explore Pakistan

The database schema is designed in strict **Third Normal Form (3NF)** with clear primary/foreign key cardinalities and integrity constraints.

```mermaid
erDiagram
    CITIES ||--o{ HOTELS : "has"
    CITIES ||--o{ LANDMARKS : "features"
    CITIES ||--o{ STREET_FOODS : "offers"
    CITIES ||--o{ TRANSPORT_ROUTES : "operates"
    CITIES ||--o{ PRIVATE_TRANSPORT : "provides"
    CITIES ||--o{ TOUR_GUIDES : "bases"
    CITIES ||--o{ ACTIVITIES : "hosts"
    CITIES ||--o{ SEASONS : "experiences"
    CITIES ||--o{ EMERGENCY_CONTACTS : "serviced_by"

    HOTELS ||--o{ ROOM_TYPES : "offers"
    HOTELS ||--o{ BOOKINGS : "receives"
    ROOM_TYPES ||--o{ BOOKINGS : "reserved_in"
    HOTELS ||--o{ REVIEWS : "evaluated_by"
    STREET_FOODS ||--o{ REVIEWS : "evaluated_by"
    LANDMARKS ||--o{ REVIEWS : "evaluated_by"

    LANDMARKS ||--o{ TRANSPORT_ROUTES : "destination_of"

    TOUR_GUIDES ||--o{ GUIDE_ACTIVITIES : "performs"
    ACTIVITIES ||--o{ GUIDE_ACTIVITIES : "guided_by"

    CITIES {
        NUMBER city_id PK
        VARCHAR2 city_name UK
        VARCHAR2 province
        VARCHAR2 region_type
        VARCHAR2 description
        VARCHAR2 source_url
        DATE date_retrieved
    }

    HOTELS {
        NUMBER hotel_id PK
        NUMBER city_id FK
        VARCHAR2 hotel_name
        NUMBER star_rating
        VARCHAR2 address
        VARCHAR2 contact
        NUMBER rating_avg
        VECTOR embedding
        VARCHAR2 source_url
        DATE date_retrieved
    }

    ROOM_TYPES {
        NUMBER room_id PK
        NUMBER hotel_id FK
        VARCHAR2 room_name
        NUMBER capacity
        NUMBER price_per_night
        VARCHAR2 amenities
        VARCHAR2 source_url
        DATE date_retrieved
    }

    LANDMARKS {
        NUMBER landmark_id PK
        NUMBER city_id FK
        VARCHAR2 landmark_name
        VARCHAR2 category
        NUMBER entry_fee
        VARCHAR2 description
        VECTOR embedding
        VARCHAR2 source_url
        DATE date_retrieved
    }

    STREET_FOODS {
        NUMBER food_id PK
        NUMBER city_id FK
        VARCHAR2 food_name
        VARCHAR2 category
        VARCHAR2 famous_spot
        VARCHAR2 price_range
        CHAR is_street_food
        VARCHAR2 description
        VARCHAR2 source_url
        DATE date_retrieved
    }

    TRANSPORT_ROUTES {
        NUMBER route_id PK
        NUMBER city_id FK
        VARCHAR2 from_location
        NUMBER to_landmark_id FK
        VARCHAR2 transport_mode
        CHAR is_public
        NUMBER fare
        NUMBER duration_minutes
        VARCHAR2 source_url
        DATE date_retrieved
    }

    PRIVATE_TRANSPORT {
        NUMBER ride_id PK
        NUMBER city_id FK
        VARCHAR2 app_name
        VARCHAR2 vehicle_type
        NUMBER base_fare
        NUMBER per_km_rate
        VARCHAR2 source_url
        DATE date_retrieved
    }

    TOUR_GUIDES {
        NUMBER guide_id PK
        NUMBER city_id FK
        VARCHAR2 guide_name
        VARCHAR2 languages
        NUMBER daily_rate
        VARCHAR2 contact
        NUMBER experience_years
        VARCHAR2 source_url
        DATE date_retrieved
    }

    ACTIVITIES {
        NUMBER activity_id PK
        NUMBER city_id FK
        VARCHAR2 activity_name
        VARCHAR2 activity_type
        NUMBER estimated_duration_hours
        VARCHAR2 description
        VARCHAR2 source_url
        DATE date_retrieved
    }

    GUIDE_ACTIVITIES {
        NUMBER guide_id PK, FK
        NUMBER activity_id PK, FK
    }

    REVIEWS {
        NUMBER review_id PK
        NUMBER hotel_id FK
        NUMBER food_id FK
        NUMBER landmark_id FK
        VARCHAR2 reviewer_name
        NUMBER rating
        VARCHAR2 review_text
        DATE review_date
    }

    BOOKINGS {
        NUMBER booking_id PK
        NUMBER hotel_id FK
        NUMBER room_id FK
        VARCHAR2 guest_name
        VARCHAR2 guest_contact
        DATE check_in_date
        DATE check_out_date
        NUMBER total_price
        VARCHAR2 status
        TIMESTAMP created_at
    }

    SEASONS {
        NUMBER season_id PK
        NUMBER city_id FK
        VARCHAR2 season_name
        VARCHAR2 ideal_months
        VARCHAR2 avg_temp_celsius
        VARCHAR2 weather_notes
        NUMBER visit_rating
        VARCHAR2 source_url
        DATE date_retrieved
    }

    EMERGENCY_CONTACTS {
        NUMBER contact_id PK
        NUMBER city_id FK
        VARCHAR2 service_type
        VARCHAR2 institution_name
        VARCHAR2 phone_number
        VARCHAR2 address
        VARCHAR2 source_url
        DATE date_retrieved
    }

    CURRENCIES {
        VARCHAR2 currency_code PK
        VARCHAR2 currency_name
        NUMBER exchange_rate_to_pkr
        DATE last_updated
        VARCHAR2 source_url
    }

    USERS_ADMIN {
        NUMBER admin_id PK
        VARCHAR2 username UK
        VARCHAR2 password_hash
        VARCHAR2 salt
        TIMESTAMP created_at
    }

    AUDIT_LOG {
        NUMBER log_id PK
        VARCHAR2 table_name
        VARCHAR2 operation
        VARCHAR2 record_id
        CLOB old_values
        CLOB new_values
        VARCHAR2 admin_user
        TIMESTAMP log_timestamp
    }
```

---

## Relational Characteristics

1. **Strict 3NF Compliance**: Non-key attributes are transitively independent of the primary keys.
2. **Referential Integrity**: Cascading deletes (`ON DELETE CASCADE`) maintain orphan-free children tables.
3. **Polymorphic Safety**: The `reviews` table utilizes dedicated nullable foreign key columns with a mutually exclusive `CHECK` constraint:
   $$	ext{CHECK }((	ext{hotel\_id IS NOT NULL}) + (	ext{food\_id IS NOT NULL}) + (	ext{landmark\_id IS NOT NULL}) = 1)$$
   This maintains native Oracle foreign key indexability and referential integrity without generic untyped ID pointers.
4. **Automated Auditability**: Every administrative mutation is tracked in `audit_log` through row-level triggers.
