"""
================================================================================
PROJECT: Explore Pakistan - Interactive Console Application
================================================================================
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datetime
from data_definitions import (
    CITIES_DATA, HOTELS_DATA, ROOM_TYPES_DATA, LANDMARKS_DATA,
    STREET_FOODS_DATA, TRANSPORT_ROUTES_DATA, PRIVATE_TRANSPORT_DATA,
    TOUR_GUIDES_DATA, ACTIVITIES_DATA, GUIDE_ACTIVITIES_DATA,
    REVIEWS_DATA, BOOKINGS_DATA, SEASONS_DATA,
    EMERGENCY_CONTACTS_DATA, CURRENCIES_DATA,
    ADMIN_SALT, ADMIN_HASH
)

# Authentic Coordinates (Latitude & Longitude) for all Landmarks
LANDMARK_COORDS = {
    1: ("33.7297° N", "73.0372° E"),   # Faisal Mosque
    2: ("33.6934° N", "73.0683° E"),   # Pakistan Monument
    3: ("33.6917° N", "73.0694° E"),   # Lok Virsa
    4: ("33.7428° N", "73.0583° E"),   # Daman-e-Koh
    5: ("33.6989° N", "73.1258° E"),   # Rawal Lake
    6: ("33.6900° N", "73.0700° E"),   # Shakarparian
    7: ("33.7408° N", "73.0678° E"),   # Saidpur Village
    8: ("33.7380° N", "73.0560° E"),   # Margalla Trail 3
    9: ("33.6925° N", "73.0708° E"),   # Museum of Natural History
    10: ("33.7000° N", "73.0180° E"),  # Fatima Jinnah Park F-9
    11: ("31.5882° N", "74.3096° E"),  # Badshahi Mosque
    12: ("31.5896° N", "74.3155° E"),  # Lahore Fort
    13: ("31.5861° N", "74.3817° E"),  # Shalimar Gardens
    14: ("31.5925° N", "74.3094° E"),  # Minar-e-Pakistan
    15: ("31.5683° N", "74.3083° E"),  # Lahore Museum
    16: ("31.5833° N", "74.3219° E"),  # Wazir Khan Mosque
    17: ("31.5898° N", "74.3142° E"),  # Sheesh Mahal
    18: ("31.6225° N", "74.3031° E"),  # Tomb of Jahangir
    19: ("31.5822° N", "74.3236° E"),  # Delhi Gate & Shahi Hammam
    20: ("31.5678° N", "74.3139° E"),  # Anarkali Bazaar
    21: ("24.8745° N", "67.0398° E"),  # Mazar-e-Quaid
    22: ("24.7937° N", "67.0281° E"),  # Clifton Beach
    23: ("24.8142° N", "67.0328° E"),  # Mohatta Palace
    24: ("24.8872° N", "67.0864° E"),  # Maritime Museum
    25: ("24.8692° N", "67.0944° E"),  # PAF Museum
    26: ("24.8547° N", "67.0194° E"),  # National Museum
    27: ("24.8647° N", "67.2711° E"),  # Chaukhandi Tombs
    28: ("24.8467° N", "66.9936° E"),  # Port Grand
    29: ("24.8475° N", "67.0331° E"),  # Frere Hall
    30: ("24.8600° N", "67.0278° E"),  # Empress Market
    31: ("35.9189° N", "74.2494° E"),  # Kargah Buddha
    32: ("36.1311° N", "74.1867° E"),  # Naltar Valley
    33: ("35.9228° N", "74.3089° E"),  # Gilgit Bridge
    34: ("35.9297° N", "74.3725° E"),  # Danyore Bridge
    35: ("36.1969° N", "74.2981° E"),  # Rakaposhi Viewpoint
    36: ("35.9833° N", "74.5500° E"),  # Bagrot Valley
    37: ("35.9000° N", "74.3500° E"),  # Jutial Waterfall
    38: ("35.9208° N", "74.3125° E"),  # Chinar Bagh
    39: ("35.9272° N", "74.3167° E"),  # Taj Mughal Fort
    40: ("35.9389° N", "74.3644° E"),  # Confluence
    41: ("35.4225° N", "75.4497° E"),  # Shangrila Lake
    42: ("35.4456° N", "75.4428° E"),  # Upper Kachura Lake
    43: ("35.3056° N", "75.6333° E"),  # Kharpocho Fort
    44: ("35.0303° N", "75.4419° E"),  # Deosai National Park
    45: ("35.3400° N", "75.5900° E"),  # Katpana Desert
    46: ("35.3622° N", "75.7533° E"),  # Sarfaranga Desert
    47: ("35.2806° N", "75.6417° E"),  # Manthal Buddha Rock
    48: ("35.4283° N", "75.7289° E"),  # Shigar Fort
    49: ("35.1558° N", "76.3353° E"),  # Khaplu Palace
    50: ("35.2333° N", "75.6333° E")   # Sadpara Dam
}

ACTIVE_BOOKINGS = [list(b) for b in BOOKINGS_DATA]

def sep(char="=", length=80):
    print(char * length)

def prompt_input(text):
    try:
        return input(f"{text} ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        sys.exit(0)

# ==============================================================================
# SUB-PANEL FUNCTIONS
# ==============================================================================

def show_hotels(city_id, city_name):
    sep("=")
    print(f"  HOTELS AND ROOMS IN {city_name.upper()}")
    sep("-")
    hotels = [h for h in HOTELS_DATA if h[1] == city_id]
    for h in hotels:
        print(f"  * [Hotel ID: {h[0]}] {h[2]} ({h[3]}-Star) | Rating: {h[6]:.1f}/5.0")
        print(f"    Address : {h[4]}")
        print(f"    Contact : {h[5] or 'N/A'}")
        rooms = [r for r in ROOM_TYPES_DATA if r[1] == h[0]]
        for r in rooms:
            print(f"      -> Room [ID: {r[0]}]: {r[2]} | Max {r[3]} Guests | PKR {r[4]:,.2f} / night")
            print(f"         Amenities: {r[5]}")
        print()
    sep("-")
    prompt_input(f"Press Enter to return to {city_name} Menu...")

def book_room_with_estimated_price(city_id, city_name):
    sep("=")
    print(f"  BOOK A HOTEL ROOM IN {city_name.upper()}")
    sep("-")
    hotels = [h for h in HOTELS_DATA if h[1] == city_id]
    for h in hotels:
        print(f"  [ID: {h[0]}] {h[2]} ({h[3]}-Star)")

    sep("-")
    h_in = prompt_input("Enter Hotel ID to Book (0 to Cancel):")
    if h_in in ("0", ""):
        return

    try:
        hotel_id = int(h_in)
        hotel = next((h for h in hotels if h[0] == hotel_id), None)
        if not hotel:
            print("[!] Hotel not found.")
            return

        rooms = [r for r in ROOM_TYPES_DATA if r[1] == hotel_id]
        print(f"\nAvailable Rooms in {hotel[2]}:")
        for r in rooms:
            print(f"  [ID: {r[0]}] {r[2]} | Max {r[3]} Guests | PKR {r[4]:,.2f} / night")

        r_in = prompt_input("Enter Room ID to Book (0 to Cancel):")
        if r_in in ("0", ""):
            return
        room_id = int(r_in)
        room = next((r for r in rooms if r[0] == room_id), None)
        if not room:
            print("[!] Room not found.")
            return

        guest_name = prompt_input("Enter Guest Name:")
        guest_phone = prompt_input("Enter Phone Number:")

        nights_in = prompt_input("Enter Number of Nights to Stay (e.g. 3):")
        nights = int(nights_in)
        if nights <= 0:
            print("[!] Number of nights must be greater than 0.")
            return

        today = datetime.date.today()
        cin = today + datetime.timedelta(days=1)
        cout = cin + datetime.timedelta(days=nights)

        total_est_price = nights * room[4]

        new_id = len(ACTIVE_BOOKINGS) + 1
        ACTIVE_BOOKINGS.append([new_id, hotel_id, room_id, guest_name, guest_phone, str(cin), str(cout), total_est_price, "CONFIRMED"])

        sep("=")
        print("  >>> BOOKING CONFIRMED & ESTIMATED PRICE SUMMARY <<<")
        sep("-")
        print(f"  Booking Reference     : #{new_id}")
        print(f"  Guest Name            : {guest_name} ({guest_phone})")
        print(f"  Hotel                 : {hotel[2]}")
        print(f"  Room Category         : {room[2]}")
        print(f"  Check-in Date         : {cin}")
        print(f"  Check-out Date        : {cout}")
        print(f"  Duration of Stay      : {nights} Night(s)")
        print(f"  Nightly Room Rate     : PKR {room[4]:,.2f} per night")
        sep("-")
        print(f"  TOTAL ESTIMATED PRICE : PKR {total_est_price:,.2f}")
        sep("=")
        prompt_input(f"Press Enter to return to {city_name} Menu...")
    except ValueError:
        print("[!] Invalid number entered.")

def show_landmarks(city_id, city_name):
    sep("=")
    print(f"  LANDMARKS AND SIGHTSEEING IN {city_name.upper()}")
    sep("-")
    landmarks = [l for l in LANDMARKS_DATA if l[1] == city_id]
    for idx, l in enumerate(landmarks, start=1):
        coords = LANDMARK_COORDS.get(l[0], ("33.7000° N", "73.0500° E"))
        fee_str = "FREE (PKR 0.00)" if l[4] == 0 else f"PKR {l[4]:,.2f}"
        print(f"[{idx}] {l[2].upper()} ({l[3]})")
        print(f"    - Coordinates : Latitude {coords[0]}, Longitude {coords[1]}")
        print(f"    - Entry Fee   : {fee_str}")
        print(f"    - Description : {l[5]}")
        print()
    sep("-")
    prompt_input(f"Press Enter to return to {city_name} Menu...")

def show_street_foods(city_id, city_name):
    sep("=")
    print(f"  AUTHENTIC STREET FOODS AND FAMOUS SPOTS IN {city_name.upper()}")
    sep("-")
    foods = [f for f in STREET_FOODS_DATA if f[1] == city_id]
    for idx, f in enumerate(foods, start=1):
        print(f"[{idx}] {f[2]} ({f[3]}) | {f[5]}")
        print(f"    - Famous Spot : {f[4]}")
        print(f"    - Description : {f[7]}")
        print()
    sep("-")
    prompt_input(f"Press Enter to return to {city_name} Menu...")

def show_taxi_planner(city_id, city_name):
    sep("=")
    print(f"  TAXI AND TRANSPORT PLANNER FOR {city_name.upper()}")
    sep("-")
    print("A) PUBLIC TRANSIT CORRIDORS (METRO / BUS / SHUTTLE):")
    routes = [t for t in TRANSPORT_ROUTES_DATA if t[1] == city_id and t[5] == "Y"]
    for r in routes:
        dest_landmark = next((l[2] for l in LANDMARKS_DATA if l[0] == r[3]), "City Landmark")
        print(f"  * From: {r[2]} -> To: {dest_landmark}")
        print(f"    Mode: {r[4]} | Fare: PKR {r[6]:,.2f} | Duration: {r[7]} mins")
    print()

    print("B) PRIVATE RIDE-HAILING TARIFFS (CAREEM / INDRIVE / YANGO / CABS):")
    rides = [p for p in PRIVATE_TRANSPORT_DATA if p[1] == city_id]
    for p in rides:
        km = f"PKR {p[5]:,.2f}/km" if p[5] > 0 else "Flat Daily Rate"
        print(f"  * {p[2]} ({p[3]}) -> Base Fare: PKR {p[4]:,.2f} | Per KM Rate: {km}")
    sep("-")
    prompt_input(f"Press Enter to return to {city_name} Menu...")

def show_full_panel(city_id, city_name, province, region, desc):
    sep("=")
    print(f"  FULL EXPLORATION PANEL: {city_name.upper()} ({province} - {region})")
    sep("=")
    print(f"  \"{desc}\"\n")

    print("1. TOP HOTELS & ROOMS:")
    for h in [h for h in HOTELS_DATA if h[1] == city_id][:3]:
        print(f"  * {h[2]} ({h[3]}-Star) | Rating: {h[6]:.1f}/5.0 | Tel: {h[5] or 'N/A'}")
        for r in [r for r in ROOM_TYPES_DATA if r[1] == h[0]]:
            print(f"     -> {r[2]} (Max {r[3]} Guests): PKR {r[4]:,.2f}/night")
    print()

    print("2. TOP LANDMARKS (WITH COORDINATES & FEES):")
    for l in [l for l in LANDMARKS_DATA if l[1] == city_id][:4]:
        c = LANDMARK_COORDS.get(l[0], ("33.7000° N", "73.0500° E"))
        fee = "FREE" if l[4] == 0 else f"PKR {l[4]:,.2f}"
        print(f"  * {l[2]} ({l[3]}) | Fee: {fee} | Coords: Lat {c[0]}, Lon {c[1]}")
    print()

    print("3. FAMOUS STREET FOODS:")
    for f in [f for f in STREET_FOODS_DATA if f[1] == city_id][:4]:
        print(f"  * {f[2]} ({f[4]}) - {f[5]}")
    print()

    print("4. TAXI & TRANSIT PLANNER:")
    for t in [t for t in TRANSPORT_ROUTES_DATA if t[1] == city_id][:2]:
        dest = next((l[2] for l in LANDMARKS_DATA if l[0] == t[3]), "Landmark")
        print(f"  * {t[4]}: {t[2]} -> {dest} (PKR {t[6]:,.2f}, {t[7]} mins)")
    for p in [p for p in PRIVATE_TRANSPORT_DATA if p[1] == city_id][:2]:
        print(f"  * {p[2]} ({p[3]}): Base PKR {p[4]:,.2f}")
    sep("=")
    prompt_input(f"Press Enter to return to {city_name} Menu...")

# ==============================================================================
# CITY SUB-MENU
# ==============================================================================

def city_sub_menu(city_tuple):
    city_id, city_name, province, region, desc, _, _ = city_tuple

    while True:
        sep("=")
        print(f"  {city_name.upper()} ({province})")
        sep("=")
        print("  [1] Hotels and Rooms")
        print("  [2] Book a Hotel Room (with Estimated Price)")
        print("  [3] Landmarks (with Latitude and Longitude)")
        print("  [4] Street Foods")
        print("  [5] Taxi and Transport Planner")
        print(f"  [6] Full {city_name} Panel (Show Everything)")
        print("  [0] Back to Cities Menu")
        sep("-")

        choice = prompt_input("Please select your option (0 to 6):")

        if choice == "1":
            show_hotels(city_id, city_name)
        elif choice == "2":
            book_room_with_estimated_price(city_id, city_name)
        elif choice == "3":
            show_landmarks(city_id, city_name)
        elif choice == "4":
            show_street_foods(city_id, city_name)
        elif choice == "5":
            show_taxi_planner(city_id, city_name)
        elif choice == "6":
            show_full_panel(city_id, city_name, province, region, desc)
        elif choice == "0":
            break
        else:
            print("[!] Invalid option. Please select 0 to 6.")

# ==============================================================================
# CITIES MENU
# ==============================================================================

def user_panel():
    while True:
        sep("=")
        print("  CITIES")
        sep("=")
        for c in CITIES_DATA:
            tag = " (Federal Capital)" if c[0] == 1 else f" ({c[2]})"
            print(f"  [{c[0]}] {c[1]}{tag}")
        print("  [0] Exit")
        sep("-")

        choice = prompt_input("Select one of the cities (1 to 5, or 0 to Exit):")

        if choice == "0":
            break

        try:
            cid = int(choice)
            chosen_city = next((c for c in CITIES_DATA if c[0] == cid), None)
            if chosen_city:
                city_sub_menu(chosen_city)
            else:
                print("[!] Invalid city number.")
        except ValueError:
            print("[!] Please enter a number between 1 and 5, or 0 to Exit.")

# ==============================================================================
# ADMIN PANEL
# ==============================================================================

def admin_panel():
    sep("=")
    print("  ADMIN PANEL")
    sep("=")
    pwd = prompt_input("Enter Admin Password (default: admin):")
    if pwd != "admin":
        print("[!] Incorrect password.")
        return

    while True:
        sep("=")
        print("  ADMIN MANAGEMENT")
        sep("=")
        print("  [1] View All Confirmed Bookings")
        print("  [2] View Top Rated Hotels Report")
        print("  [3] Live Currency Conversion Rates")
        print("  [0] Back to Main Menu")
        sep("-")

        act = prompt_input("Please select your option (0 to 3):")
        if act == "1":
            sep("-")
            print(f"{'ID':<4} | {'Guest':<18} | {'Dates':<24} | {'Price'}")
            sep("-")
            for b in ACTIVE_BOOKINGS:
                print(f"{b[0]:<4} | {b[3]:<18} | {b[5]} to {b[6]} | PKR {b[7]:,.2f}")
            prompt_input("Press Enter to continue...")
        elif act == "2":
            sep("-")
            for c in CITIES_DATA:
                print(f"City: {c[1]}")
                for h in [h for h in HOTELS_DATA if h[1] == c[0] and h[3] == 5]:
                    print(f"  * {h[2]}: {h[6]:.1f}/5.0")
            prompt_input("Press Enter to continue...")
        elif act == "3":
            sep("-")
            for cu in CURRENCIES_DATA:
                print(f"  1 {cu[0]} = PKR {cu[2]:.4f}")
            prompt_input("Press Enter to continue...")
        elif act == "0":
            break
        else:
            print("[!] Invalid option.")

# ==============================================================================
# MAIN MENU
# ==============================================================================

def main():
    while True:
        print()
        sep("=")
        print("  MAIN MENU")
        sep("=")
        print("  [1] Login as Admin")
        print("  [2] Login as User")
        print("  [0] Exit")
        sep("-")

        choice = prompt_input("Select your choice (1, 2, or 0 to Exit):")

        if choice == "1":
            admin_panel()
        elif choice == "2":
            user_panel()
        elif choice == "0":
            print("\nThank you for exploring Pakistan! Goodbye.\n")
            break
        else:
            print("[!] Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
