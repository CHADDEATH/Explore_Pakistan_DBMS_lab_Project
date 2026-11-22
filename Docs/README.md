# Explore Pakistan – Phase 1: Database Architecture & Backend Logic

**Explore Pakistan** is an advanced relational database management lab project engineered for **Oracle Database 23ai**. It models the tourism and travel infrastructure of Pakistan across five key destinations: **Islamabad, Lahore, Karachi, Gilgit, and Skardu**.

This project encompasses a strictly normalized **Third Normal Form (3NF)** schema, business integrity triggers, automated trip budget estimation, salted SHA-256 authentication, role-based access control (RBAC), analytical administrative reporting, and modern Oracle 23ai features (**VECTOR embeddings** for semantic search and **JSON Relational Duality Views**).

---

## 1. Directory Structure

```text
Explore_Pakistan_Project/
├── sql/
│   ├── 01_schema.sql                # DDL physical schema with 17 normalized tables
│   ├── 02_constraints.sql           # PK, FK (CASCADE), and domain CHECK constraints
│   ├── 03_seed_data.sql             # 508 authentic verified records + 23ai vectors
│   ├── 04_procedures_functions.sql  # Trip budget estimator, login, booking logic, DDL
│   ├── 05_triggers.sql              # Booking overlap prevention, ratings, audit log
│   ├── 06_views_and_security.sql    # Read-only user views, JSON Duality, RBAC roles
│   ├── 07_reports.sql               # 10 advanced analytical reports (RANK, GROUP BY)
│   ├── 08_test_queries.sql          # 12 comprehensive test suites for user/admin flows
│   └── explore_pakistan_app.sql     # Interactive PL/SQL console menu application
├── Excel_Data/
│   ├── cities.xlsx                  # 5 authentic destinations
│   ├── hotels.xlsx                  # 40 hotels (2-star to 5-star)
│   ├── room_types.xlsx              # 80 room configurations with nightly rates in PKR
│   ├── landmarks.xlsx               # 50 historical, natural, cultural, religious sites
│   ├── street_foods.xlsx            # 50 iconic culinary spots and dishes
│   ├── transport_routes.xlsx        # 40 urban and public transit routes
│   ├── private_transport.xlsx       # 25 ride-hailing and 4x4 rental tariffs
│   ├── tour_guides.xlsx             # 25 certified tour guides with languages and rates
│   ├── activities.xlsx              # 30 guided tours and outdoor excursions
│   ├── guide_activities.xlsx        # 50 guide-activity junction records (M:N)
│   ├── reviews.xlsx                 # 40 traveler ratings and reviews
│   ├── bookings.xlsx                # 20 confirmed hotel bookings
│   ├── seasons.xlsx                 # 20 seasonal travel profiles and ratings
│   ├── emergency_contacts.xlsx      # 25 essential emergency services and helplines
│   └── currencies.xlsx              # 8 international currencies pegged to PKR
└── docs/
    ├── README.md                    # Project documentation & execution guide
    ├── ER_diagram.md                # Entity Relationship diagram and cardinalities
    ├── entry_count_summary.txt      # Total record breakdown (508 entries)
    └── unverified_data_report.xlsx  # Verified NULL field justifications
```

---

## 2. Authentication & Security Credentials

- **Admin Username**: `admin`
- **Admin Password**: `admin` (lowercase)
- **Security Implementation**:
  - Passwords are **NEVER** stored in plaintext.
  - Handled via `users_admin` table using a persistent salt (`9f8e7d6c5b4a3210`) combined with **SHA-256 hashing**.
  - Verified securely through the stored function `verify_admin_login(p_username, p_password)`.

---

## 3. Order of Script Execution (Oracle SQL Developer)

Execute the scripts in Oracle SQL Developer or SQL*Plus in the following strict sequential order:

1. **`01_schema.sql`**
   - Drops existing objects cleanly (`DROP TABLE ... CASCADE CONSTRAINTS PURGE`).
   - Creates 17 core and extended 3NF tables with `IDENTITY` columns, `VECTOR(384, FLOAT32)`, and `CLOB` audit fields.
2. **`02_constraints.sql`**
   - Establishes Foreign Keys (`ON DELETE CASCADE`), primary keys, and comprehensive `CHECK` constraints.
   - Enforces referential exclusivity on `reviews` ensuring exact 1-to-1 association with either a hotel, food, or landmark.
3. **`03_seed_data.sql`**
   - Inserts **508 authentic verified records** matching the Excel workbooks exactly.
   - Populates normalized 384-dimension vector embeddings for AI similarity search.
   - Commits all transactions.
4. **`04_procedures_functions.sql`**
   - Compiles stored PL/SQL logic:
     - `calculate_trip_budget(...)`: Automated budget breakdown.
     - `verify_admin_login(...)`: Salted cryptographic login check.
     - `sp_book_room(...)`: Booking validation and reservation engine.
     - `convert_currency(...)`: Multi-currency converter.
     - `admin_execute_ddl(...)`: Dynamic controlled DDL executor.
5. **`05_triggers.sql`**
   - `trg_booking_price_and_overlap`: Prevents conflicting dates for room reservations and recalculates prices.
   - `trg_update_hotel_rating`: Automatically updates `hotels.rating_avg` upon review changes.
   - `trg_audit_hotels`, `trg_audit_landmarks`, `trg_audit_bookings`: Automatically captures full audit logs (`audit_log`) on DML.
6. **`06_views_and_security.sql`**
   - Compiles sanitized user views (`v_user_%`).
   - Compiles Oracle 23ai **JSON Relational Duality View** (`hotel_room_duality_v`).
   - Configures `explore_admin_role` (full administrative rights) and `explore_user_role` (SELECT-only on views).
7. **`07_reports.sql`**
   - Runs 10 analytical administrative queries utilizing `DENSE_RANK()`, `ROW_NUMBER()`, `GROUP BY`, `HAVING`, and window functions.
8. **`08_test_queries.sql`**
   - Runs 12 automated test cases verifying both User Panel flows (Steps 1 through 9) and Admin operations (Triggers, Vectors, Duality).

---

## 4. Running the Interactive Console Menu

To launch the text-based console interface in SQL Developer / SQL*Plus:
```sql
SET SERVEROUTPUT ON SIZE 1000000;
@explore_pakistan_app.sql
```
- **Option 1 (User Panel)**: Direct access, read-only exploration of cities, hotels, street foods, transit, and trip budget estimates.
- **Option 2 (Admin Panel)**: Guides administrator through authentication and privileged database control.

---

## 5. Oracle 23ai Innovations Highlighted

1. **AI Semantic Vector Search**:
   - `hotels.embedding` and `landmarks.embedding` are defined as `VECTOR(384, FLOAT32)`.
   - Test Case 12 demonstrates similarity search via `VECTOR_DISTANCE(..., COSINE)`.
2. **JSON Relational Duality Views**:
   - `hotel_room_duality_v` aggregates normalized tables into JSON documents for modern web/API consumption while maintaining 3NF relational integrity underneath.
