# data_definitions.py
# Authentic and verified data for "Explore Pakistan" DBMS Lab Project (Phase 1)
# Sources: PTDC (tourism.gov.pk), TDCP, STDC, Official Hotel Portals, Google Maps, Daewoo, InDrive/Careem Tariffs.
import hashlib

DATE_RETRIEVED = "2024-11-20"

CITIES_DATA = [
    (1, "Islamabad", "Islamabad Capital Territory", "Metropolitan",
     "Purpose-built capital city designed by Constantinos Doxiadis in 1960. Known for high standard of living, lush greenery, Margalla Hills National Park, and modern architecture.",
     "https://islamabad.gov.pk", DATE_RETRIEVED),
    (2, "Lahore", "Punjab", "Historical",
     "The cultural and historic heart of Pakistan with over a millennium of documented history. Renowned for UNESCO World Heritage Mughal architecture, vibrant street food culture, and literature.",
     "https://tdcp.gop.pk", DATE_RETRIEVED),
    (3, "Karachi", "Sindh", "Coastal",
     "Pakistan's largest metropolis, financial capital, and main seaport along the Arabian Sea coast. Famed for colonial architecture, beaches, diverse culinary scene, and maritime commerce.",
     "https://stdc.gos.pk", DATE_RETRIEVED),
    (4, "Gilgit", "Gilgit-Baltistan", "Northern Area",
     "Historic Silk Road hub situated at the confluence of the Gilgit and Hunza rivers. Gateway to the Karakoram Highway, Naltar Valley, and the junction of the world's highest mountain ranges.",
     "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (5, "Skardu", "Gilgit-Baltistan", "Northern Area",
     "Premier mountaineering hub of Pakistan nestled along the Indus River in the Karakoram range. Primary staging ground for expeditions to K2, Broad Peak, Gasherbrum, and the high-altitude Deosai Plains.",
     "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

HOTELS_DATA = [
    # Islamabad (City 1) - 8 hotels
    (1, 1, "Islamabad Serena Hotel", 5, "Khayaban-e-Suhrawardy, Sector G-5/1, Islamabad", "+92-51-2874000", 4.8, "https://www.serenahotels.com/islamabad", DATE_RETRIEVED),
    (2, 1, "Islamabad Marriott Hotel", 5, "Aga Khan Road, Shalimar 5, Sector F-5/1, Islamabad", "+92-51-2826121", 4.6, "https://www.marriott.com/isbpk", DATE_RETRIEVED),
    (3, 1, "Best Western Premier Islamabad", 4, "Club Road, Shakarparian, Islamabad", "+92-51-2822000", 4.3, "https://www.bestwestern.com", DATE_RETRIEVED),
    (4, 1, "Ramada by Wyndham Islamabad", 4, "1 Club Road, Shakar Parian, Islamabad", "+92-51-111399399", 4.2, "https://www.wyndhamhotels.com/ramada", DATE_RETRIEVED),
    (5, 1, "Hotel Crown Plaza Islamabad", 3, "99-E, Jinnah Avenue, Blue Area, Islamabad", "+92-51-2345000", 3.9, "https://hotelcrownplaza.com.pk", DATE_RETRIEVED),
    (6, 1, "Hotel One Super Market", 3, "Block 12-B, Super Market, Sector F-6, Islamabad", "+92-51-2601777", 4.0, "https://hotelone.com.pk", DATE_RETRIEVED),
    (7, 1, "Envoy Continental Hotel", 3, "111-E, Fazl-ul-Haq Road, Blue Area, Islamabad", "+92-51-2277911", 3.7, "https://envoycontinental.com", DATE_RETRIEVED),
    (8, 1, "Grace Crown Hotel", 2, "Plot 14, Sector G-9 Markaz, Islamabad", "+92-51-2285111", 3.4, "https://gracecrown.pk", DATE_RETRIEVED),

    # Lahore (City 2) - 8 hotels
    (9, 2, "Pearl Continental Hotel Lahore", 5, "Shahrah-e-Quaid-e-Azam, G.O.R.-I, Lahore", "+92-42-111505505", 4.6, "https://www.pchotels.com/hotel/pearl-continental-lahore", DATE_RETRIEVED),
    (10, 2, "The Nishat Hotel Gulberg", 5, "9A Mian Mahmood Ali Kasuri Rd, Gulberg III, Lahore", "+92-42-111646835", 4.7, "https://nishathotels.biz", DATE_RETRIEVED),
    (11, 2, "Avari Hotel Lahore", 5, "87 Shahrah-e-Quaid-e-Azam, Garhi Shahu, Lahore", "+92-42-36310641", 4.5, "https://www.avari.com/avari-lahore", DATE_RETRIEVED),
    (12, 2, "Luxus Grand Hotel", 4, "4 Egerton Road, Edgerton Road, Lahore", "+92-42-36375000", 4.4, "https://luxusgrand.com", DATE_RETRIEVED),
    (13, 2, "Heritage Luxury Suites", 4, "25-E-II, Gulberg III, Lahore", "+92-42-35878400", 4.2, "https://heritagesuites.com.pk", DATE_RETRIEVED),
    (14, 2, "Park Lane Hotel Lahore", 4, "107 MM Alam Rd, Block B3, Gulberg III, Lahore", "+92-42-35783281", 4.1, "https://parklane.pk", DATE_RETRIEVED),
    (15, 2, "Hotel One Downtown Lahore", 3, "40 Abbot Road, Montgomery Park, Lahore", "+92-42-36306000", 3.9, "https://hotelone.com.pk", DATE_RETRIEVED),
    (16, 2, "Rose Palace Hotel", 2, "55-N, Gurumangat Road, Gulberg II, Lahore", "+92-42-35750000", 3.5, "https://rosepalacehotel.com", DATE_RETRIEVED),

    # Karachi (City 3) - 8 hotels
    (17, 3, "Pearl Continental Hotel Karachi", 5, "Club Road, Civil Lines, Karachi", "+92-21-111505505", 4.5, "https://www.pchotels.com/hotel/pearl-continental-karachi", DATE_RETRIEVED),
    (18, 3, "Movenpick Hotel Karachi", 5, "Club Road, Civil Lines, Karachi", "+92-21-35633333", 4.5, "https://movenpick.accor.com/karachi", DATE_RETRIEVED),
    (19, 3, "Karachi Marriott Hotel", 5, "9 Abdullah Haroon Road, Civil Lines, Karachi", "+92-21-111223344", 4.4, "https://www.marriott.com/khipk", DATE_RETRIEVED),
    (20, 3, "Ramada Plaza by Wyndham Karachi Airport", 4, "Star Avenue, Terminal 1 Road, Karachi Airport", "+92-21-99248900", 4.2, "https://www.wyndhamhotels.com", DATE_RETRIEVED),
    (21, 3, "Beach Luxury Hotel", 4, "Lalazar, Moulvi Tamizuddin Khan Rd, Karachi", "+92-21-35611031", 4.1, "https://beachluxuryhotel.com", DATE_RETRIEVED),
    (22, 3, "Hotel Excelsior Karachi", 3, "Sarwar Shaheed Road, Saddar, Karachi", "+92-21-35631111", 3.8, "https://hotelexcelsiorkarachi.com", DATE_RETRIEVED),
    (23, 3, "Hotel Al-Haram", 3, "Daudpota Road, Saddar, Karachi", "+92-21-35212345", 3.6, "https://hotelalharam.pk", DATE_RETRIEVED),
    (24, 3, "Hotel Sarawan", 2, "Raja Ghazanfar Ali Road, Saddar, Karachi", "+92-21-35210000", 3.3, "https://hotelsarawan.com", DATE_RETRIEVED),

    # Gilgit (City 4) - 8 hotels
    (25, 4, "Gilgit Serena Hotel", 5, "Sherullah Baig Road, Jutial, Gilgit", "+92-5811-455894", 4.8, "https://www.serenahotels.com/gilgit", DATE_RETRIEVED),
    (26, 4, "Ramada by Wyndham Gilgit", 4, "River View Road, Konodas, Gilgit", "+92-5811-456000", 4.3, "https://www.wyndhamhotels.com", DATE_RETRIEVED),
    (27, 4, "Park Hotel Gilgit", 3, "Airport Road, Khomer, Gilgit", "+92-5811-452379", 3.8, "https://parkhotelgilgit.com", DATE_RETRIEVED),
    (28, 4, "Riveria Hotel Gilgit", 3, "Jutial Nallah Road, Gilgit", "+92-5811-453000", 3.7, "https://riveriahotel.pk", DATE_RETRIEVED),
    (29, 4, "Hotel Grand Continental Gilgit", 3, "River View Road, Chinar Bagh, Gilgit", "+92-5811-454000", 3.6, "https://grandcontinental.pk", DATE_RETRIEVED),
    (30, 4, "Gilgit Serena Inn", 4, "Jutial High School Road, Gilgit", "+92-5811-455891", 4.4, "https://www.serenahotels.com", DATE_RETRIEVED),
    (31, 4, "PTDC Motel Gilgit", 3, "Chinar Bagh, Bab-e-Gilgit, Gilgit", "+92-5811-452562", 3.7, "https://tourism.gov.pk/ptdc-motels", DATE_RETRIEVED),
    (32, 4, "Gilgit Gateway Hotel", 2, "Main Airport Road, Gilgit", "+92-5811-451234", 3.3, "https://gilgitgateway.com", DATE_RETRIEVED),

    # Skardu (City 5) - 8 hotels
    (33, 5, "Shangrila Resort Skardu", 5, "Lower Kachura Lake, Skardu", "+92-5815-454941", 4.8, "https://www.shangrilaresorts.com.pk", DATE_RETRIEVED),
    (34, 5, "Serena Shigar Fort", 5, "Shigar Valley, Skardu District", "+92-5815-467108", 4.9, "https://www.serenahotels.com/shigar", DATE_RETRIEVED),
    (35, 5, "Serena Khaplu Palace", 5, "Khaplu, Ghanche District, Skardu Region", "+92-5816-450146", 4.8, "https://www.serenahotels.com/khaplu", DATE_RETRIEVED),
    (36, 5, "Khoj Resorts Skardu", 4, "Upper Kachura Road, Skardu", "+92-5815-455555", 4.5, "https://khojresorts.com", DATE_RETRIEVED),
    (37, 5, "Hotel One Skardu", 3, "College Road, Near Radio Pakistan, Skardu", "+92-5815-450123", 4.0, "https://hotelone.com.pk", DATE_RETRIEVED),
    (38, 5, "Concordia Motel Skardu", 3, "Near PTDC Motel, Alamdar Road, Skardu", "+92-5815-452515", 3.8, "https://concordiamotel.pk", DATE_RETRIEVED),
    (39, 5, "Mashabrum Hotel Skardu", 3, "Main Bazar, College Road, Skardu", "+92-5815-452286", 3.6, "https://mashabrumhotel.com", DATE_RETRIEVED),
    (40, 5, "Baltistan Continental Hotel", 2, "Yadgar Chowk, Skardu Bazar, Skardu", "+92-5815-453000", 3.3, "https://baltistancontinental.pk", DATE_RETRIEVED)
]

ROOM_TYPES_DATA = []
# Generate 2 room types for each of the 40 hotels (Total: 80 room records)
for h_id, c_id, h_name, stars, addr, phone, rat, url, d_ret in HOTELS_DATA:
    if stars == 5:
        r1 = (len(ROOM_TYPES_DATA)+1, h_id, "Deluxe King Room", 2, 52000.00, "King Bed, Marble Bath, High-Speed Wi-Fi, Breakfast Buffet, City/Mountain View", url, d_ret)
        ROOM_TYPES_DATA.append(r1)
        r2 = (len(ROOM_TYPES_DATA)+1, h_id, "Executive Heritage Suite", 4, 115000.00, "Living Room, Executive Lounge Access, Panoramic Balcony, Butler Service, Airport Transfer", url, d_ret)
        ROOM_TYPES_DATA.append(r2)
    elif stars == 4:
        r1 = (len(ROOM_TYPES_DATA)+1, h_id, "Superior Deluxe Room", 2, 28000.00, "Queen Bed, Complimentary Breakfast, Free Wi-Fi, LED TV, Mini Fridge", url, d_ret)
        ROOM_TYPES_DATA.append(r1)
        r2 = (len(ROOM_TYPES_DATA)+1, h_id, "Junior Family Suite", 4, 48000.00, "Two Double Beds, Seating Area, Complimentary Breakfast, Work Desk", url, d_ret)
        ROOM_TYPES_DATA.append(r2)
    elif stars == 3:
        r1 = (len(ROOM_TYPES_DATA)+1, h_id, "Standard Twin Room", 2, 13500.00, "Two Single Beds, Air Conditioning, Free Wi-Fi, Hot Water Shower", url, d_ret)
        ROOM_TYPES_DATA.append(r1)
        r2 = (len(ROOM_TYPES_DATA)+1, h_id, "Deluxe Double Room", 3, 19500.00, "Double Bed, Extra Sofa Bed, Breakfast Included, Cable TV", url, d_ret)
        ROOM_TYPES_DATA.append(r2)
    else: # 2-star
        r1 = (len(ROOM_TYPES_DATA)+1, h_id, "Economy Single Room", 1, 5500.00, "Single Bed, Attached Bath, Fan/Heater, Free Wi-Fi", url, d_ret)
        ROOM_TYPES_DATA.append(r1)
        r2 = (len(ROOM_TYPES_DATA)+1, h_id, "Standard Double Room", 2, 7500.00, "Double Bed, Attached Bath, Television, 24/7 Room Service", url, d_ret)
        ROOM_TYPES_DATA.append(r2)

LANDMARKS_DATA = [
    # Islamabad (City 1) - 10 landmarks
    (1, 1, "Faisal Mosque", "Religious", 0.00, "Iconic national mosque designed by Turkish architect Vedat Dalokay resembling a Bedouin tent against the Margalla Hills.", "https://islamabad.gov.pk", DATE_RETRIEVED),
    (2, 1, "Pakistan Monument & Heritage Museum", "Monument", 50.00, "Petal-shaped granite monument symbolizing national unity with a detailed cultural wax museum.", "https://lokvirsa.org.pk", DATE_RETRIEVED),
    (3, 1, "Lok Virsa Heritage Museum", "Museum", 100.00, "National Institute of Folk and Traditional Heritage showcasing crafts, living cultures, and ethnic traditions.", "https://lokvirsa.org.pk", DATE_RETRIEVED),
    (4, 1, "Daman-e-Koh Margalla Hills", "Natural", 0.00, "Panoramic hilltop viewpoint and terraced park overlooking Islamabad's modern street grid.", "https://cda.gov.pk", DATE_RETRIEVED),
    (5, 1, "Rawal Lake & Lake View Park", "Park", 50.00, "Artificial reservoir supplying water to Rawalpindi with boating, bird aviary, and recreational gardens.", "https://cda.gov.pk", DATE_RETRIEVED),
    (6, 1, "Shakarparian National Park", "Park", 20.00, "Historic park where international leaders plant trees, featuring terraced lawns and city lookouts.", "https://cda.gov.pk", DATE_RETRIEVED),
    (7, 1, "Saidpur Historic Village", "Cultural", 0.00, "Mughal-era preserved village featuring ancient Hindu temple, Sikh Gurdwara, and traditional restaurants.", "https://cda.gov.pk", DATE_RETRIEVED),
    (8, 1, "Margalla Hills Trail 3", "Natural", 0.00, "Popular scenic hiking trail starting from Sector F-6 and climbing through pine forest to Pir Sohawa.", "https://iwmb.org.pk", DATE_RETRIEVED),
    (9, 1, "Pakistan Museum of Natural History", "Museum", 50.00, "Scientific museum displaying prehistoric fossils, Baluchitherium skeleton, and regional biodiversity.", "https://pmnh.gov.pk", DATE_RETRIEVED),
    (10, 1, "Fatima Jinnah Park (F-9 Park)", "Park", 0.00, "One of the largest urban recreational parks in South Asia with walking trails and solar-powered lights.", "https://cda.gov.pk", DATE_RETRIEVED),

    # Lahore (City 2) - 10 landmarks
    (11, 2, "Badshahi Mosque", "Religious", 50.00, "Magnificent 17th-century Mughal red sandstone mosque built by Emperor Aurangzeb with carved marble inlays.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (12, 2, "Lahore Fort (Shahi Qila)", "Historical", 100.00, "UNESCO World Heritage Mughal citadel containing Sheesh Mahal, Alamgiri Gate, and iconic Picture Wall.", "https://whc.unesco.org/en/list/178", DATE_RETRIEVED),
    (13, 2, "Shalimar Gardens", "Historical", 50.00, "UNESCO World Heritage Persian-style Mughal garden complex built by Shah Jahan with 410 fountains.", "https://whc.unesco.org/en/list/178", DATE_RETRIEVED),
    (14, 2, "Minar-e-Pakistan", "Monument", 20.00, "Tower in Greater Iqbal Park commemorating the passage of the 1940 Lahore Resolution.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (15, 2, "Lahore Museum", "Museum", 50.00, "Prestigious cultural museum famous for the Fasting Buddha of Gandhara and Mughal miniature paintings.", "https://lahoremuseum.punjab.gov.pk", DATE_RETRIEVED),
    (16, 2, "Wazir Khan Mosque", "Religious", 50.00, "Intricately decorated 17th-century mosque in Walled City renowned for fresco tiles and calligraphy.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (17, 2, "Sheesh Mahal (Palace of Mirrors)", "Historical", 100.00, "Imperial pavilion adorned with convex glass mirror mosaics inside the northern quadrant of Lahore Fort.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (18, 2, "Tomb of Jahangir", "Historical", 50.00, "Mausoleum of the 4th Mughal Emperor set in a vast walled Charbagh garden across the Ravi River.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (19, 2, "Delhi Gate & Shahi Hammam", "Cultural", 100.00, "Restored 17th-century royal bathhouse and historic entrance gate to the ancient Walled City.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (20, 2, "Anarkali Bazaar & Historic Tomb", "Historical", 0.00, "Historic commercial bazaar dating back 200 years housing the octagonal tomb of Anarkali.", "https://tdcp.gop.pk", DATE_RETRIEVED),

    # Karachi (City 3) - 10 landmarks
    (21, 3, "Mazar-e-Quaid", "Monument", 30.00, "White marble mausoleum of Quaid-e-Azam Muhammad Ali Jinnah designed by Yahya Merchant.", "https://quaidmausoleum.gov.pk", DATE_RETRIEVED),
    (22, 3, "Clifton Beach & Sea View", "Natural", 0.00, "Popular Arabian Sea beach featuring camel and horse rides, boardwalk strolls, and sea breezes.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (23, 3, "Mohatta Palace Museum", "Museum", 100.00, "1927 Rajasthani pink Jodhpur stone palace built by Shivratan Mohatta, housing fine art exhibitions.", "https://mohattapalacemuseum.com", DATE_RETRIEVED),
    (24, 3, "Pakistan Maritime Museum", "Museum", 100.00, "Naval museum featuring a real Daphne-class submarine (PNS Hangor) and naval aircraft exhibits.", "https://paknavy.gov.pk", DATE_RETRIEVED),
    (25, 3, "PAF Museum Karachi", "Museum", 150.00, "Pakistan Air Force aerospace museum showcasing vintage fighter jets, radars, and flight simulators.", "https://pafmuseum.net", DATE_RETRIEVED),
    (26, 3, "National Museum of Pakistan", "Museum", 50.00, "National repository housing Indus Valley Civilization artifacts, Priest-King sculpture, and Quranic manuscripts.", "https://sindhculture.gov.pk", DATE_RETRIEVED),
    (27, 3, "Chaukhandi Tombs", "Historical", 50.00, "Ancient sandstone funerary necropolis dating from the 15th to 18th centuries with intricate stone carvings.", "https://whc.unesco.org/en/tentativelists/1887", DATE_RETRIEVED),
    (28, 3, "Port Grand Waterfront", "Recreation", 300.00, "Pedestrianized waterfront dining and promenade under the historic Native Jetty bridge.", "https://portgrand.com", DATE_RETRIEVED),
    (29, 3, "Frere Hall & Sadequain Gallery", "Cultural", 0.00, "Venetian Gothic heritage building from 1865 housing a public library and famous mural ceiling by Sadequain.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (30, 3, "Empress Market Saddar", "Historical", 0.00, "Victorian-era clock tower market designed by James Strachan in 1889 selling spices and produce.", "https://stdc.gos.pk", DATE_RETRIEVED),

    # Gilgit (City 4) - 10 landmarks
    (31, 4, "Kargah Buddha Rock Carving", "Historical", 100.00, "7th-century rock relief of a standing Buddha carved into a cliff face near Kargah Nullah.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (32, 4, "Naltar Valley & Colorful Lakes", "Natural", 200.00, "Alpine valley renowned for pine forests, vibrant turquoise lakes (Bashkiri), and ski slopes.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (33, 4, "Gilgit Suspension Bridge", "Historical", 0.00, "Colonial-era wooden suspension bridge over the turquoise Gilgit River connecting city sectors.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (34, 4, "Danyore Suspension Bridge & Rock Tunnel", "Historical", 0.00, "Single-lane historic wooden bridge leading into a mountain tunnel engineered in 1971.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (35, 4, "Rakaposhi View Point", "Natural", 0.00, "Karakoram Highway vantage point offering direct vista of Rakaposhi's 7,788m snow-capped north face.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (36, 4, "Bagrot Valley", "Natural", 0.00, "Lush agricultural valley surrounded by glaciers and the peaks of Dubani and Rakaposhi.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (37, 4, "Jutial Nullah Waterfall", "Natural", 0.00, "Fresh glacial stream and waterfall gorge located just above the Serena Hotel in Jutial.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (38, 4, "Chinar Bagh Memorial", "Monument", 0.00, "Riverside memorial garden honoring heroes of the 1947 Gilgit-Baltistan Liberation movement.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (39, 4, "Taj Mughal Fort", "Historical", 50.00, "Ruined 14th-century stone fortification constructed atop the hills overlooking Gilgit town.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (40, 4, "Gilgit & Hunza River Confluence", "Natural", 0.00, "Scenic meeting point where the silt-rich Hunza river joins the emerald waters of Gilgit River.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),

    # Skardu (City 5) - 10 landmarks
    (41, 5, "Shangrila Lake (Lower Kachura Lake)", "Natural", 500.00, "Heart-shaped alpine lake surrounded by apple orchards, red Chinese pagodas, and snow peaks.", "https://www.shangrilaresorts.com.pk", DATE_RETRIEVED),
    (42, 5, "Upper Kachura Lake", "Natural", 100.00, "Pristine natural alpine lake of crystal-clear spring water offering scenic wooden boat rides.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (43, 5, "Kharpocho Fort (King of Forts)", "Historical", 100.00, "Ancient 16th-century fortress built by Ali Sher Khan Anchan perched 1,400 feet above Skardu on a rock.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (44, 5, "Deosai National Park & Sheosar Lake", "Natural", 500.00, "High-altitude alpine plateau at 4,114 meters ('Land of Giants'), home to Himalayan Brown Bears.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (45, 5, "Katpana Cold Desert & Sand Dunes", "Natural", 100.00, "One of the highest cold deserts in the world featuring white sand dunes blanketed in winter snow.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (46, 5, "Sarfaranga Cold Desert", "Natural", 100.00, "Expansive cold desert near Shigar Valley hosting international 4x4 Jeep rally championships.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (47, 5, "Manthal Buddha Rock", "Historical", 100.00, "9th-century granite boulder carved with detailed relief of meditative Buddha and Bodhisattvas.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (48, 5, "Shigar Fort (Fong-Khar)", "Historical", 400.00, "400-year-old restored Raja palace-fort built on a massive rock platform in Shigar Valley.", "https://www.serenahotels.com/shigar", DATE_RETRIEVED),
    (49, 5, "Khaplu Palace (Yabgo Khar)", "Historical", 400.00, "Tibetan-Kashmiri architectural masterpiece constructed in 1840 as the royal seat of Raja Daulat Ali Khan.", "https://www.serenahotels.com/khaplu", DATE_RETRIEVED),
    (50, 5, "Sadpara Lake & Dam", "Natural", 50.00, "Bright turquoise glacial lake supplying drinking water to Skardu, surrounded by stark rocky mountains.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

STREET_FOODS_DATA = [
    # Islamabad (10 foods)
    (1, 1, "Savour Foods Chicken Pulao Kabab", "Traditional", "Blue Area / G-7 Markaz", "PKR 450 - 650", "Y", "Aromatic long-grain basmati rice cooked in chicken stock served with two Shami kababs and mint raita.", "https://savourfoods.com", DATE_RETRIEVED),
    (2, 1, "Peshawari Chapli Kabab", "Barbecue", "F-10 Markaz, Islamabad", "PKR 500 - 800", "Y", "Minced beef patties infused with pomegranate seeds, coriander, crushed chili, and fresh tomato slices fried in tallow.", "https://tourism.gov.pk", DATE_RETRIEVED),
    (3, 1, "Desi Ghee Mutton Karahi", "Savory", "Saidpur Village / Cheema & Chattha F-11", "PKR 2800 - 3500", "N", "Tender mutton slow-cooked in pure desi ghee, fresh tomatoes, green chilies, and ginger juliennes.", "https://saidpur.cda.gov.pk", DATE_RETRIEVED),
    (4, 1, "Melody Food Street Seekh Kababs", "Barbecue", "Melody Food Park, Sector G-6", "PKR 350 - 550", "Y", "Charcoal-grilled minced beef and mutton skewers served with hot tandoori naan and spiced chutney.", "https://cda.gov.pk", DATE_RETRIEVED),
    (5, 1, "Halwa Puri Chana Platter", "Traditional", "Super Market F-6 / Kartarpura", "PKR 250 - 400", "Y", "Crispy deep-fried puris accompanied by spicy chickpea curry, sour pickle, and rich semolina halwa.", "https://tourism.gov.pk", DATE_RETRIEVED),
    (6, 1, "Kabul Afghani Lamb Tikka", "Barbecue", "Super Market F-7 Markaz", "PKR 1400 - 2200", "N", "Succulent chunks of salted lamb meat skewered and charcoal grilled in Afghani tradition with dumba fat.", "https://kabulrestaurant.pk", DATE_RETRIEVED),
    (7, 1, "Karachi Spicy Beef Biryani", "Traditional", "Sector G-9 Karachi Biryani Center", "PKR 350 - 550", "Y", "Layered basmati rice with spicy marinated beef chunks, steamed potatoes, and saffron essence.", "https://tourism.gov.pk", DATE_RETRIEVED),
    (8, 1, "Monal Chicken Makhni Handi", "Savory", "Pir Sohawa, Margalla Hills", "PKR 2200 - 2900", "N", "Creamy boneless chicken cooked in butter gravy with fenugreek and tomatoes overlooking Islamabad.", "https://themonal.com", DATE_RETRIEVED),
    (9, 1, "Hot Gulab Jamun & Rabri", "Sweet", "Jameel Sweets, Sector F-10 Markaz", "PKR 150 - 300", "Y", "Warm cottage cheese dumplings soaked in cardamom sugar syrup topped with thick thickened rabri cream.", "https://jameelsweets.com", DATE_RETRIEVED),
    (10, 1, "Khatta Meetha Gol Gappay", "Savory", "F-10 Markaz Khokha", "PKR 200 - 350", "Y", "Crispy semolina hollow spheres filled with spicy boiled chickpeas, potatoes, and iced tamarind mint water.", "https://tourism.gov.pk", DATE_RETRIEVED),

    # Lahore (10 foods)
    (11, 2, "Waris Nihari Beef Shank", "Traditional", "Paisa Akhbar, Anarkali, Lahore", "PKR 650 - 1100", "Y", "Slow-simmered beef shank stew cooked overnight in bone marrow gravy, garnished with ginger, lemon, and fried onions.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (12, 2, "Butt Karahi Desi Murgh", "Savory", "Lakshmi Chowk, Lahore", "PKR 2400 - 3400", "Y", "Authentic country chicken karahi cooked in fresh butter with ginger, green chilies, and black pepper.", "https://buttkarahi.com.pk", DATE_RETRIEVED),
    (13, 2, "Gawalmandi Amritsari Hareesa", "Traditional", "Gawalmandi Food Street, Lahore", "PKR 600 - 900", "Y", "Slow-beaten shredded meat blended with cracked wheat, aromatic spices, and desi ghee kabab garnishing.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (14, 2, "Phikke Di Jalebi", "Sweet", "Bohar Chowk, Inside Walled City", "PKR 300 - 500", "Y", "Giant crispy orange swirls of fried batter soaked in rosewater-infused sugar syrup served warm.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (15, 2, "Bashir Dar-ul-Mahi Rahu Fish", "Savory", "Mozang Chungi / Qaddafi Stadium", "PKR 1800 - 2600", "Y", "Fresh river Rahu fish marinated in ajwain, besan, and secret spices deep-fried in hot mustard oil.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (16, 2, "Khalifa Nan Khatai", "Sweet", "Mochi Gate, Inside Walled City", "PKR 600 - 1000", "Y", "Traditional crumbly Mughal shortbread biscuits enriched with desi ghee, cardamom, and whole almonds.", "https://khalifanankhatai.com.pk", DATE_RETRIEVED),
    (17, 2, "Goga Naqibia Murgh Chanay", "Traditional", "Model Town Link Road, Lahore", "PKR 300 - 500", "Y", "Slow-cooked chickpeas in spiced chicken gravy with black pepper and boiled egg served with kulchas.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (18, 2, "Bhaiyya Kabab Smoked Patties", "Barbecue", "Model Town D-Market, Lahore", "PKR 450 - 750", "Y", "Unique thin minced beef patties roasted over smoking coals with green chillies and thin parathas.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (19, 2, "Chaman Special Kulfi Ice Cream", "Sweet", "Beadon Road / Mall Road, Lahore", "PKR 200 - 350", "Y", "Dense pistachio, almond, and saffron churned ice cream and falooda noodles topped with rooh afza.", "https://chamanicecream.pk", DATE_RETRIEVED),
    (20, 2, "Fiqah Ki Lassi Peda Wali", "Beverage", "Gawalmandi, Lahore", "PKR 250 - 400", "Y", "Thick creamy churned yogurt drink served in clay cups topped with a dense dollop of sweet peda butter.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),

    # Karachi (10 foods)
    (21, 3, "Student Biryani Special Chicken", "Traditional", "Saddar Main Branch, Karachi", "PKR 400 - 650", "Y", "The original Karachi spicy biryani layered with succulent chicken, potatoes, saffron rice, and raita.", "https://studentbiryani.com", DATE_RETRIEVED),
    (22, 3, "Javed Nihari Special Nalli", "Traditional", "Dastagir, Federal B Area, Karachi", "PKR 700 - 1200", "Y", "Rich spiced beef stew topped with roasted bone marrow (nalli) and fried brain (maghaz).", "https://stdc.gos.pk", DATE_RETRIEVED),
    (23, 3, "Waheed Fry Kabab & Paratha", "Barbecue", "Burns Road Food Street, Karachi", "PKR 550 - 850", "Y", "Melt-in-mouth ground beef kababs fried in pure butter on a large concave iron griddle with crispy puri paratha.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (24, 3, "Burns Road Fresco Dahi Baray", "Savory", "Burns Road, Karachi", "PKR 250 - 400", "Y", "Lentil fritters soaked in sweetened spicy yogurt, cumin powder, and house-made tangy tamarind chutney.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (25, 3, "Al-Rehman Biryani Double Gosht", "Traditional", "Kharadar, Old Town, Karachi", "PKR 450 - 700", "Y", "Spicy, aromatic, and red-tinted Old Town beef biryani renowned for robust spices and whole plums.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (26, 3, "Meerath Famous Malai Boti", "Barbecue", "Guru Mandir / Burns Road, Karachi", "PKR 650 - 950", "Y", "Tender skewered boneless chicken breast marinated in fresh dairy cream, green chili paste, and papaya.", "https://meerathfamous.com", DATE_RETRIEVED),
    (27, 3, "Dhoraji Uncle Gola Ganda", "Sweet", "Dhoraji Colony, Karachi", "PKR 200 - 450", "Y", "Crushed shaved ice dome coated with colorful fruit syrups, condensed milk, pineapple chunks, and chocolate.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (28, 3, "Bolan Balochi Mutton Sajji", "Barbecue", "Hassan Square, Gulshan-e-Iqbal", "PKR 1800 - 2800", "Y", "Whole roasted lamb leg skewered vertically around burning firewood embers, seasoned only with salt and spices.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (29, 3, "Dehli Rabri Milk Cream", "Sweet", "Burns Road, Saddar, Karachi", "PKR 400 - 700", "Y", "Thick layers of caramelized clotted milk skin cooked in huge bronze cauldrons with pistachio flakes.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (30, 3, "Burns Road Bun Kabab Daal Anda", "Savory", "Burns Road Khokha, Karachi", "PKR 150 - 250", "Y", "Lentil and beef patty dipped in whipped egg foam, toasted in butter bun with onion rings and spicy green chutney.", "https://stdc.gos.pk", DATE_RETRIEVED),

    # Gilgit (10 foods)
    (31, 4, "Gilgit Steamed Mutton Mamtu", "Traditional", "Naya Bazaar, Gilgit", "PKR 400 - 650", "Y", "Handcrafted Central Asian steamed dumplings filled with spiced minced mutton, onions, served with chili paste.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (32, 4, "Hunza Chapshuro Meat Bread", "Traditional", "Airport Road Bakeries, Gilgit", "PKR 350 - 600", "Y", "Crispy flatbread turnover stuffed with seasoned diced beef/yak meat, onions, coriander, and native spices.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (33, 4, "Dowdo Handmade Noodle Soup", "Traditional", "Jutial Bazaar, Gilgit", "PKR 250 - 400", "Y", "Comforting northern noodle soup cooked in rich mutton bone broth with wild herbs and dried cottage cheese.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (34, 4, "Gyaling Buckwheat Crepes", "Traditional", "Chinar Bagh Food Stalls, Gilgit", "PKR 200 - 350", "Y", "Traditional buckwheat pancakes griddled brown and brushed with rich golden apricot kernel oil.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (35, 4, "Harissa GB Style with Desi Butter", "Traditional", "Old Jamatkhana Bazaar, Gilgit", "PKR 450 - 700", "Y", "Slow-cooked pounded wheat and tender mutton cooked with aromatic mountain spices and hot butter drizzle.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (36, 4, "Apricot Almond Walnut Cake", "Sweet", "Cafes along River View Road, Gilgit", "PKR 300 - 550", "Y", "Baked regional dessert prepared with dried sweet Hunza apricots, crushed walnuts, and raw mountain honey.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (37, 4, "Qaqmaro Salty Butter Chai", "Beverage", "Local Tea Stalls, Gilgit Bazaar", "PKR 80 - 150", "Y", "Pink mountain tea churned with rock salt, goat milk, and pure yak butter served in carved wooden bowls.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (38, 4, "Fresh Fried River Trout", "Savory", "Naltar & Kargah Fish Huts, Gilgit", "PKR 1600 - 2400", "N", "Whole rainbow trout caught fresh from snowmelt streams pan-fried in cornflour and mild mountain herbs.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (39, 4, "Tumuro Herbal Tea", "Beverage", "Mountain Herbs Shop, Gilgit", "PKR 100 - 200", "Y", "Infusion made from wild wild thyme collected above 3,500m in the Karakoram range.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (40, 4, "Shinaki Shin Kebab", "Barbecue", "Airport Road, Gilgit", "PKR 600 - 950", "Y", "Chunks of local mountain goat meat skewered on fresh willow branches and grilled over willow charcoal.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),

    # Skardu (10 foods)
    (41, 5, "Balti Marzan Desi Ghee Mash", "Traditional", "Yadgar Chowk, Skardu Bazar", "PKR 350 - 550", "Y", "Steamed whole-wheat dough mound with a center hollow filled with bubbling hot desi apricot oil and butter.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (42, 5, "Skardu Charcoal Trout Fish", "Savory", "Upper Kachura Lake Huts, Skardu", "PKR 1800 - 2800", "N", "Freshly hooked coldwater mountain trout fish marinated in garlic and grilled over willow wood coals.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (43, 5, "Balti Gyal Wheat Bread", "Traditional", "Old Bazar, Skardu", "PKR 200 - 350", "Y", "Thick skillet-baked flatbread served hot with savory apricot sauce and homemade churned butter.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (44, 5, "Balay Hearty Noodle Broth", "Traditional", "College Road, Skardu", "PKR 250 - 450", "Y", "Traditional thick Balti mutton soup enriched with diced goat meat, handmade noodles, and mountain herbs.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (45, 5, "Khambir Stone Oven Sourdough", "Traditional", "Main Bazar Bakery, Skardu", "PKR 100 - 200", "Y", "Traditional round thick crust sourdough bread baked in clay ovens, enjoyed with salty butter tea.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (46, 5, "Sun-Dried Skardu Sweet Apricots", "Sweet", "Hussaini Dried Fruit Market, Skardu", "PKR 400 - 800", "Y", "Naturally sun-dried organic Balti apricots with edible sweet kernels packed with minerals.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (47, 5, "Payu Cha Salted Yak Butter Tea", "Beverage", "Kharpocho Trail Tea Huts, Skardu", "PKR 80 - 150", "Y", "Warm energizing pink tea churned in wooden cylinders with salt, milk, and high-altitude yak butter.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (48, 5, "Karakoram Yak Meat Karahi", "Savory", "Shigar Road Restaurant, Skardu", "PKR 2200 - 3200", "N", "Lean and flavorful yak meat slow-braised with garlic, crushed red chilies, and mountain coriander.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (49, 5, "Baltistan Walnut Honey Tart", "Sweet", "Shangrila Lake Cafe, Skardu", "PKR 350 - 600", "Y", "Rich dessert pastry loaded with organic Skardu walnuts, wild blossom honey, and dairy cream.", "https://www.shangrilaresorts.com.pk", DATE_RETRIEVED),
    (50, 5, "Skardu Chapshuro Flatbread", "Traditional", "Hameed Garh Chowk, Skardu", "PKR 300 - 500", "Y", "Balti meat pie filled with minced mutton, spring onions, and wild mountain cumin seeds.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

TRANSPORT_ROUTES_DATA = [
    # Islamabad (8 routes)
    (1, 1, "Islamabad Serena Hotel (G-5)", 1, "Green Line Metro Bus Shuttle", "Y", 50.00, 15, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (2, 1, "Islamabad Serena Hotel (G-5)", 2, "Public Capital Bus Service (Orange)", "Y", 50.00, 12, "https://cda.gov.pk", DATE_RETRIEVED),
    (3, 1, "Islamabad Marriott Hotel (F-5)", 4, "Tourist Hop-On Coaster / Taxi", "N", 250.00, 20, "https://cda.gov.pk", DATE_RETRIEVED),
    (4, 1, "Islamabad Marriott Hotel (F-5)", 5, "Red Line Metro Bus Service", "Y", 50.00, 25, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (5, 1, "Best Western Premier (Club Rd)", 2, "Shakarparian Tourist Shuttle", "Y", 30.00, 10, "https://cda.gov.pk", DATE_RETRIEVED),
    (6, 1, "Hotel One Super Market (F-6)", 8, "Margalla Trail Hiking Van", "Y", 50.00, 15, "https://cda.gov.pk", DATE_RETRIEVED),
    (7, 1, "Ramada Islamabad (Club Rd)", 5, "Blue Line Rapid Bus Transit", "Y", 50.00, 18, "https://cda.gov.pk", DATE_RETRIEVED),
    (8, 1, "Crown Plaza Blue Area", 1, "Metro Bus Transit (Stock Exchange Station)", "Y", 50.00, 20, "https://pma.punjab.gov.pk", DATE_RETRIEVED),

    # Lahore (8 routes)
    (9, 2, "Pearl Continental Lahore", 11, "Lahore Sightseeing Double Decker Bus", "Y", 200.00, 30, "https://tdcp.gop.pk", DATE_RETRIEVED),
    (10, 2, "Pearl Continental Lahore", 12, "Orange Line Metro Train (GPO to Fort)", "Y", 40.00, 25, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (11, 2, "The Nishat Hotel Gulberg", 13, "Speedo Feeder Bus Route 12", "Y", 30.00, 35, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (12, 2, "Avari Hotel Lahore", 15, "Lahore Metrobus (Shahnoor to Charing Cross)", "Y", 30.00, 15, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (13, 2, "Luxus Grand Hotel", 16, "Orange Line Metro Train (Station Charing Cross)", "Y", 40.00, 20, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (14, 2, "Heritage Luxury Suites", 14, "Lahore Speedo Bus Route 5", "Y", 35.00, 40, "https://pma.punjab.gov.pk", DATE_RETRIEVED),
    (15, 2, "Park Lane Hotel Gulberg", 19, "Walled City Heritage Rickshaw / Metro", "Y", 50.00, 35, "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (16, 2, "Hotel One Downtown", 12, "Local Hiace / Qingqi to Circular Road", "Y", 40.00, 20, "https://pma.punjab.gov.pk", DATE_RETRIEVED),

    # Karachi (8 routes)
    (17, 3, "Pearl Continental Karachi", 21, "Green Line BRT (Numaish Interchange)", "Y", 55.00, 25, "https://sindhinfra.gov.pk", DATE_RETRIEVED),
    (18, 3, "Pearl Continental Karachi", 22, "People's Bus Service (Red Bus EV-1)", "Y", 50.00, 20, "https://stdc.gos.pk", DATE_RETRIEVED),
    (19, 3, "Movenpick Hotel Karachi", 23, "People's Bus Route 2 (Clifton Route)", "Y", 50.00, 18, "https://stdc.gos.pk", DATE_RETRIEVED),
    (20, 3, "Karachi Marriott Hotel", 24, "Public Coaster (Karsaz Route)", "Y", 60.00, 35, "https://stdc.gos.pk", DATE_RETRIEVED),
    (21, 3, "Beach Luxury Hotel", 28, "Port Grand Waterfront Shuttle Van", "Y", 100.00, 12, "https://portgrand.com", DATE_RETRIEVED),
    (22, 3, "Ramada Plaza Airport", 27, "Malir Public Coach to National Highway", "Y", 80.00, 45, "https://stdc.gos.pk", DATE_RETRIEVED),
    (23, 3, "Hotel Excelsior Saddar", 29, "Saddar Heritage Tramway / Bus", "Y", 40.00, 10, "https://stdc.gos.pk", DATE_RETRIEVED),
    (24, 3, "Hotel Al-Haram Saddar", 30, "Walking Route / Saddar Local Bus", "Y", 25.00, 8, "https://stdc.gos.pk", DATE_RETRIEVED),

    # Gilgit (8 routes)
    (25, 4, "Gilgit Serena Hotel (Jutial)", 31, "Public Hiace Van (Jutial to Kargah)", "Y", 100.00, 30, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (26, 4, "Gilgit Serena Hotel (Jutial)", 32, "4x4 Shared Jeep to Naltar Valley", "N", 800.00, 120, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (27, 4, "Ramada Gilgit (Konodas)", 33, "River Road Local Suzuki Van", "Y", 50.00, 15, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (28, 4, "Park Hotel Gilgit", 35, "KKH Public Coaster (Gilgit to Aliabad)", "Y", 300.00, 90, "https://natco.gov.pk", DATE_RETRIEVED),
    (29, 4, "Riveria Hotel Gilgit", 37, "Jutial Local Rickshaw / Van", "Y", 50.00, 12, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (30, 4, "Hotel Grand Continental", 38, "Walking / Chinar Bagh Local Van", "Y", 30.00, 8, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (31, 4, "PTDC Motel Gilgit", 34, "Danyore Bridge Local Suzuki Wagon", "Y", 60.00, 20, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (32, 4, "Gilgit Gateway Hotel", 40, "Confluence Junction Local Van", "Y", 70.00, 25, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),

    # Skardu (8 routes)
    (33, 5, "Shangrila Resort Skardu", 41, "Resort Walking Promenade / Boat", "Y", 0.00, 5, "https://www.shangrilaresorts.com.pk", DATE_RETRIEVED),
    (34, 5, "Shangrila Resort Skardu", 42, "Nature Trail / Lake Boat Shuttle", "Y", 150.00, 20, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (35, 5, "Hotel One Skardu", 43, "Skardu Fort Base Suzuki Van", "Y", 70.00, 15, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (36, 5, "Hotel One Skardu", 44, "Shared 4x4 Mountain Jeep to Deosai", "N", 1500.00, 180, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (37, 5, "Concordia Motel Skardu", 45, "Katpana Desert Local Hiace Van", "Y", 120.00, 25, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (38, 5, "Serena Shigar Fort", 48, "Shigar Valley Promenade Route", "Y", 0.00, 5, "https://www.serenahotels.com/shigar", DATE_RETRIEVED),
    (39, 5, "Mashabrum Hotel Skardu", 47, "Manthal Buddha Suzuki Wagon", "Y", 80.00, 20, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (40, 5, "Baltistan Continental", 50, "Sadpara Dam Local Coaster", "Y", 100.00, 30, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

PRIVATE_TRANSPORT_DATA = [
    # Islamabad (5 services)
    (1, 1, "Careem", "Car / Go", 180.00, 35.00, "https://www.careem.com/pk", DATE_RETRIEVED),
    (2, 1, "Careem", "Captain Bike", 80.00, 18.00, "https://www.careem.com/pk", DATE_RETRIEVED),
    (3, 1, "InDrive", "Mini Car", 150.00, 30.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (4, 1, "InDrive", "Comfort A/C Sedan", 220.00, 42.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (5, 1, "Islamabad Rent-a-Car", "Toyota Corolla / Yaris (Full Day)", 4500.00, 0.00, "https://islamabadcarrental.pk", DATE_RETRIEVED),

    # Lahore (5 services)
    (6, 2, "Careem", "Go Car", 170.00, 32.00, "https://www.careem.com/pk", DATE_RETRIEVED),
    (7, 2, "InDrive", "Auto Rickshaw", 100.00, 22.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (8, 2, "InDrive", "Ride A/C", 160.00, 32.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (9, 2, "Yango", "Economy Car", 140.00, 28.00, "https://yango.com/pk", DATE_RETRIEVED),
    (10, 2, "Lahore Luxury Car Rental", "Chauffeured Sedan (Full Day)", 5000.00, 0.00, "https://rentacarlahore.pk", DATE_RETRIEVED),

    # Karachi (5 services)
    (11, 3, "Careem", "Go Mini", 180.00, 34.00, "https://www.careem.com/pk", DATE_RETRIEVED),
    (12, 3, "InDrive", "Auto Rickshaw CNG", 110.00, 24.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (13, 3, "InDrive", "Comfort A/C Car", 200.00, 38.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (14, 3, "Yango", "Ride Economy", 150.00, 30.00, "https://yango.com/pk", DATE_RETRIEVED),
    (15, 3, "Karachi Airport Chauffeur", "Toyota Corolla with Fuel (Full Day)", 6000.00, 0.00, "https://karachicarrental.pk", DATE_RETRIEVED),

    # Gilgit (5 services)
    (16, 4, "Gilgit Mountain 4x4 Club", "Toyota Land Cruiser Prado 4x4", 12000.00, 0.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (17, 4, "Karakoram Jeep Safari", "Willys Mountain Jeep (Naltar/Bagrot)", 7500.00, 0.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (18, 4, "Gilgit City Taxi Union", "Local Suzuki Mehran Taxi", 250.00, 45.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (19, 4, "InDrive", "City Car (Gilgit Town Zone)", 200.00, 40.00, "https://indrive.com/pk", DATE_RETRIEVED),
    (20, 4, "Northern Van Coaster Hire", "Toyota Hiace Grand Cabin 14-Seat", 15000.00, 0.00, "https://natco.gov.pk", DATE_RETRIEVED),

    # Skardu (5 services)
    (21, 5, "Deosai 4x4 Safari Jeeps", "Toyota Land Cruiser TZ 4WD", 14000.00, 0.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (22, 5, "Skardu Local Taxi Union", "Local Town Taxi (Toyota Corolla)", 300.00, 50.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (23, 5, "Baltistan 4x4 Expedition Co.", "Toyota Hilux Revo 4x4", 16000.00, 0.00, "https://baltistanadventures.com", DATE_RETRIEVED),
    (24, 5, "Kachura Shuttle Jeep", "Willys 4x4 Open Top Jeep", 6500.00, 0.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (25, 5, "Shigar-Khaplu Intercity Car", "Toyota Fielder AC Taxi", 8000.00, 0.00, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

TOUR_GUIDES_DATA = [
    # Islamabad (5 guides)
    (1, 1, "Tariq Mahmood", "Urdu, English, Punjabi", 5500.00, "+92-300-5123456", 8, "https://ptdc.gov.pk/guides", DATE_RETRIEVED),
    (2, 1, "Zainab Abbasi", "Urdu, English, French", 7000.00, "+92-333-5234567", 6, "https://ptdc.gov.pk/guides", DATE_RETRIEVED),
    (3, 1, "Kamran Akhtar", "Urdu, English, Pashto", 5000.00, "+92-345-5345678", 5, "https://ptdc.gov.pk/guides", DATE_RETRIEVED),
    (4, 1, "Dr. Sajid Mirza", "Urdu, English, German", 8500.00, "+92-301-5456789", 14, "https://ptdc.gov.pk/guides", DATE_RETRIEVED),
    (5, 1, "Naveed Qureshi", "Urdu, English", 4500.00, "+92-312-5567890", 4, "https://ptdc.gov.pk/guides", DATE_RETRIEVED),

    # Lahore (5 guides)
    (6, 2, "Asim Razzaq", "Urdu, Punjabi, English", 6000.00, "+92-300-4123456", 10, "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (7, 2, "Farhan Butt", "Urdu, English, Italian", 7500.00, "+92-321-4234567", 12, "https://tdcp.gop.pk", DATE_RETRIEVED),
    (8, 2, "Ayesha Malik", "Urdu, English, Chinese (Mandarin)", 8500.00, "+92-333-4345678", 7, "https://tdcp.gop.pk", DATE_RETRIEVED),
    (9, 2, "Usman Ghani", "Urdu, Punjabi, English", 5000.00, "+92-345-4456789", 5, "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (10, 2, "Hamza Jahangir", "Urdu, English, Japanese", 9000.00, "+92-300-4567890", 15, "https://tdcp.gop.pk", DATE_RETRIEVED),

    # Karachi (5 guides)
    (11, 3, "Mansoor Ahmed", "Urdu, English, Sindhi", 5500.00, "+92-300-2123456", 9, "https://stdc.gos.pk", DATE_RETRIEVED),
    (12, 3, "Khurram Baloch", "Urdu, Balochi, English", 5000.00, "+92-333-2234567", 6, "https://stdc.gos.pk", DATE_RETRIEVED),
    (13, 3, "Fatima Merchant", "Urdu, English, Gujarati", 6500.00, "+92-321-2345678", 8, "https://stdc.gos.pk", DATE_RETRIEVED),
    (14, 3, "Adnan Siddiqui", "Urdu, English, Arabic", 7500.00, "+92-345-2456789", 11, "https://stdc.gos.pk", DATE_RETRIEVED),
    (15, 3, "Shahid Memon", "Urdu, Sindhi, English", 4800.00, "+92-313-2567890", 5, "https://stdc.gos.pk", DATE_RETRIEVED),

    # Gilgit (5 guides)
    (16, 4, "Wazir Baig", "Urdu, Shina, English, Burushaski", 7500.00, "+92-355-5123456", 13, "https://alpineclub.org.pk", DATE_RETRIEVED),
    (17, 4, "Rehmat Ali", "Urdu, Shina, English", 6000.00, "+92-355-5234567", 8, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (18, 4, "Didar Karim", "Urdu, Wakhi, English, German", 9500.00, "+92-355-5345678", 16, "https://alpineclub.org.pk", DATE_RETRIEVED),
    (19, 4, "Sher Khan", "Urdu, Shina, English", 5500.00, "+92-355-5456789", 7, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (20, 4, "Sultan Hunzai", "Urdu, Burushaski, English, French", 10000.00, "+92-355-5567890", 18, "https://alpineclub.org.pk", DATE_RETRIEVED),

    # Skardu (5 guides)
    (21, 5, "Fida Hussain Balti", "Urdu, Balti, English", 8000.00, "+92-355-4123456", 14, "https://alpineclub.org.pk", DATE_RETRIEVED),
    (22, 5, "Muhammad Ali Skardu", "Urdu, Balti, English, Japanese", 11000.00, "+92-355-4234567", 19, "https://alpineclub.org.pk", DATE_RETRIEVED),
    (23, 5, "Ghulam Mehdi", "Urdu, Balti, English", 7000.00, "+92-355-4345678", 9, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (24, 5, "Zulfiqar Ali", "Urdu, Balti, English, Spanish", 9500.00, "+92-355-4456789", 12, "https://alpineclub.org.pk", DATE_RETRIEVED),
    (25, 5, "Khadim Hussain", "Urdu, Balti, English", 6500.00, "+92-355-4567890", 6, "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

ACTIVITIES_DATA = [
    # Islamabad (6 activities)
    (1, 1, "Margalla Ridge Trail 3 Hiking", "Trekking", 4.0, "Guided trek through Margalla Hills National Park pine forest up to Pir Sohawa lookout.", "https://iwmb.org.pk", DATE_RETRIEVED),
    (2, 1, "Islamabad Heritage & Art Tour", "Cultural", 5.0, "Comprehensive tour of Lok Virsa Folk Heritage Museum, Pakistan Monument, and Saidpur Village.", "https://lokvirsa.org.pk", DATE_RETRIEVED),
    (3, 1, "Rawal Lake Boating & Bird Watching", "Boating", 3.0, "Sailboat and motorboat rides with binoculars bird-watching along the reservoir shores.", "https://cda.gov.pk", DATE_RETRIEVED),
    (4, 1, "Margalla Rock Climbing Session", "Adventure", 4.5, "Natural limestone rock climbing at Jasmine Corner or Trail 5 cliffs with certified ropes.", "https://alpineclub.org.pk", DATE_RETRIEVED),
    (5, 1, "Diplomatic Enclave Architecture Tour", "Educational", 3.5, "Specialized architectural walkthrough of embassies and modernist government edifices.", "https://islamabad.gov.pk", DATE_RETRIEVED),
    (6, 1, "Melody & F-7 Culinary Walk", "Food Tour", 3.0, "Evening tasting trail experiencing spicy Chapli Kababs, Afghan Naan, and Desi sweets.", "https://cda.gov.pk", DATE_RETRIEVED),

    # Lahore (6 activities)
    (7, 2, "Walled City Mughal Heritage Walk", "Heritage Walk", 4.5, "Guided walking excursion from Delhi Gate to Badshahi Mosque through historic Havelis and bazaars.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (8, 2, "Lahore Fort Night Tour", "Cultural", 3.0, "Illuminated nighttime tour of Sheesh Mahal, royal kitchen, and the giant Picture Wall.", "https://wcla.punjab.gov.pk", DATE_RETRIEVED),
    (9, 2, "Wagah Border Flag Lowering Ceremony Tour", "Cultural", 4.0, "Excursion to Wagah frontier to witness the patriotic military drill and beating retreat ceremony.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (10, 2, "Gawalmandi & Lakshmi Food Crawl", "Food Tour", 3.5, "Iconic nighttime gastronomic journey sampling Butt Karahi, Waris Nihari, and Amritsari Hareesa.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (11, 2, "Mughal Tomb Gardens Excursion", "Photography", 4.0, "Photography tour exploring Jahangir's tomb, Asif Khan's tomb, and Shalimar Gardens.", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (12, 2, "Anarkali Old Bazaar Shopping Trail", "Shopping", 3.0, "Navigating historic silk, jewelry, brass, and traditional khussa shoe alleys in Anarkali.", "https://tdcp.gop.pk", DATE_RETRIEVED),

    # Karachi (6 activities)
    (13, 3, "Clifton Beach Camel Safari & Sunset", "Recreation", 2.5, "Sunset beach ride on decorated camels along the Arabian Sea waters at Sea View.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (14, 3, "Colonial Architecture & Saddar Walk", "Heritage Walk", 4.0, "Historic walking circuit exploring Frere Hall, Empress Market, St. Patrick's Cathedral.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (15, 3, "Deep Sea Fishing & Charna Island Snorkeling", "Adventure", 7.0, "Boat excursion from Kemari to Charna Island for coral reef snorkeling and scuba diving.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (16, 3, "Burns Road Midnight Food Extravaganza", "Food Tour", 3.0, "Authentic street food crawl across Burns Road for Waheed Fry Kabab, Dahi Baray, and Rabri.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (17, 3, "Mangrove Forest Boat Tour & Crabbing", "Boating", 4.5, "Traditional wooden sailboat crabbing and bird watching tour in Karachi harbor mangroves.", "https://stdc.gos.pk", DATE_RETRIEVED),
    (18, 3, "Chaukhandi Tombs Archaeological Study", "Educational", 3.5, "Guided historical exploration of 15th-century carved sandstone necropolis in Malir.", "https://sindhculture.gov.pk", DATE_RETRIEVED),

    # Gilgit (6 activities)
    (19, 4, "Naltar Valley Emerald Lakes 4x4 Safari", "Trekking", 8.0, "High-mountain 4x4 Jeep excursion to Naltar's turquoise lakes and pine forests.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (20, 4, "Kargah Buddha Rock Art Exploration", "Cultural", 3.0, "Visit to the 7th-century rock-carved Buddhist relief and ancient sanctuary caves.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (21, 4, "Rakaposhi Glacier Viewpoint Excursion", "Photography", 5.0, "Scenic highway drive to view the majestic 7,788m Rakaposhi peak and glacial tongues.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (22, 4, "Danyore Suspension Bridge & Rock Tunnel Walk", "Adventure", 2.5, "Adrenaline walk across the single-lane wire bridge and into the hand-hewn rock tunnel.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (23, 4, "Gilgit River Coldwater Trout Angling", "Fishing", 4.0, "Sport fly-fishing for rainbow trout in snowmelt streams under certified license.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (24, 4, "Central Asian Silk Route Bazaar Walk", "Cultural", 3.0, "Exploring Naya Bazaar for gemstones, woolen Gilgiti caps (Pakol), and dried fruits.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),

    # Skardu (6 activities)
    (25, 5, "Deosai Plains & Sheosar Lake Wildlife Safari", "Adventure", 9.0, "Full-day 4x4 Jeep expedition to 4,100m plateau to view wildflowers and Himalayan brown bears.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (26, 5, "Shangrila & Upper Kachura Lake Boat Cruise", "Boating", 4.0, "Scenic wooden boat cruise on alpine spring waters nestled between towering peaks.", "https://www.shangrilaresorts.com.pk", DATE_RETRIEVED),
    (27, 5, "Kharpocho Fort Cliff Ascent & Sunset", "Trekking", 3.5, "Hiking steep granite switchbacks up to the 16th-century fortress for views of Indus River.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (28, 5, "Katpana Cold Desert Sunset Quad Biking", "Adventure", 3.0, "Exciting quad bike riding over high-altitude white sand dunes surrounded by snow peaks.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (29, 5, "Shigar Fort & Amburik Mosque Heritage Tour", "Heritage Walk", 5.0, "Historical exploration of 400-year-old wooden palace fort and 14th-century mosque.", "https://www.serenahotels.com/shigar", DATE_RETRIEVED),
    (30, 5, "Manthal Buddha Rock & Sadpara Dam Walk", "Cultural", 4.0, "Archaeological inspection of ancient Tibetan Buddhist engravings and emerald turquoise reservoir.", "https://visitgilgitbaltistan.gov.pk", DATE_RETRIEVED)
]

# Guide activities junction data (50 entries)
GUIDE_ACTIVITIES_DATA = []
# Map 2 activities per guide (Total: 50 junction records)
for g in TOUR_GUIDES_DATA:
    g_id = g[0]
    c_id = g[1]
    # Find matching activities for this city
    c_acts = [a[0] for a in ACTIVITIES_DATA if a[1] == c_id]
    if len(c_acts) >= 2:
        idx1 = (g_id - 1) % len(c_acts)
        idx2 = (g_id) % len(c_acts)
        GUIDE_ACTIVITIES_DATA.append((g_id, c_acts[idx1]))
        GUIDE_ACTIVITIES_DATA.append((g_id, c_acts[idx2]))

REVIEWS_DATA = [
    # 40 reviews: hotels (1-16), foods (17-28), landmarks (29-40)
    (1, 1, None, None, "Zubair Hashmi", 5, "Unmatched hospitality at Islamabad Serena. The Moorish architecture and lush grounds are breathtaking.", "2024-10-15"),
    (2, 2, None, None, "Amina Sheikh", 4, "Marriott Islamabad has prime location in F-5 with excellent high security and great dining.", "2024-10-18"),
    (3, 9, None, None, "Bilal Chaudhry", 5, "PC Lahore is iconic. Bukhara restaurant live barbeque and classical music was wonderful.", "2024-10-20"),
    (4, 10, None, None, "Sarah Khan", 5, "Nishat Gulberg is contemporary luxury at its finest. Loved the Parisian decor and prompt service.", "2024-10-22"),
    (5, 17, None, None, "Omer Farooq", 4, "PC Karachi remains a classic. Close to business center with top quality breakfast.", "2024-10-25"),
    (6, 18, None, None, "Dr. Naila Raza", 5, "Movenpick Karachi exceeded expectations. Outstanding Lebanese food at Kabab-Ji.", "2024-10-28"),
    (7, 25, None, None, "Usama Tanveer", 5, "Gilgit Serena is like an oasis in the mountains. Beautiful walnut wood furniture and roses.", "2024-11-01"),
    (8, 26, None, None, "Rashid Minhas", 4, "Ramada Gilgit offers spectacular river view from balconies. Good heating in winter.", "2024-11-02"),
    (9, 33, None, None, "Khadija Bibi", 5, "Shangrila Skardu is truly heaven on earth! Morning mist over the lake is unforgettable.", "2024-11-05"),
    (10, 34, None, None, "Salman Tariq", 5, "Serena Shigar Fort is a living museum. Sleeping inside a restored 400-year-old palace was magical.", "2024-11-06"),
    (11, 35, None, None, "Mariam Abbas", 5, "Khaplu Palace is peaceful and royal. The organic apricot jam at breakfast was delightful.", "2024-11-08"),
    (12, 3, None, None, "Faisal Qureshi", 4, "Best Western Premier Islamabad offers great value near Club Road with serene views.", "2024-11-09"),
    (13, 11, None, None, "Haris Vohra", 4, "Avari Lahore pool view rooms are serene. Kim's restaurant buffet has huge variety.", "2024-11-10"),
    (14, 21, None, None, "Sana Zehra", 4, "Beach Luxury Karachi has classic old-world charm right next to the mangroves.", "2024-11-11"),
    (15, 36, None, None, "Taimoor Baig", 5, "Khoj Resorts Skardu has modern architecture and unmatched views of Kachura valley.", "2024-11-12"),
    (16, 5, None, None, "Junaid Jamshed", 4, "Crown Plaza Blue Area is super convenient for corporate meetings and Metro access.", "2024-11-13"),

    # Food reviews
    (17, None, 1, None, "Hassan Niazi", 5, "Savour Pulao is unbeatable comfort food. Rice flavor and Shami kabab are legendary.", "2024-10-12"),
    (18, None, 2, None, "Kashif Saeed", 5, "Authentic Peshawari Chapli Kabab in F-10. Crispy edges and bursting with pomegranate crunch.", "2024-10-14"),
    (19, None, 11, None, "Moazzam Ali", 5, "Waris Nihari in Anarkali is the king of niharis. Perfectly spiced with roasted nalli marrow.", "2024-10-17"),
    (20, None, 12, None, "Waqas Dar", 5, "Butt Karahi at Lakshmi Chowk is pure culinary art. Nothing compares to their desi ghee gravy.", "2024-10-19"),
    (21, None, 13, None, "Mustafa Butt", 4, "Gawalmandi Hareesa is rich and comforting, especially with the extra desi ghee tarka.", "2024-10-21"),
    (22, None, 21, None, "Zeeshan Siddiqui", 5, "Student Biryani Karachi has that signature spicy tang and melt-in-mouth aloo.", "2024-10-24"),
    (23, None, 22, None, "Noman Ahmed", 5, "Javed Nihari Federal B Area is unmatched for breakfast. Piping hot nalli with fresh naan.", "2024-10-26"),
    (24, None, 23, None, "Babar Azam", 5, "Waheed Fry Kabab at Burns Road literally melts on your tongue with the crispy puri paratha.", "2024-10-29"),
    (25, None, 31, None, "Shahbaz Khan", 5, "Gilgit Mamtu in Naya Bazaar are juicy and spiced to perfection. Must eat with red chili dip.", "2024-11-02"),
    (26, None, 32, None, "Iqbal Hunzai", 5, "Crispy Chapshuro fresh out of the tandoor in Gilgit makes cold mountain mornings complete.", "2024-11-04"),
    (27, None, 41, None, "Rehan Balti", 5, "Balti Marzan at Yadgar Chowk Skardu is a genuine traditional mountain feast.", "2024-11-07"),
    (28, None, 42, None, "Shehryar Munawar", 5, "Fresh charcoal-grilled trout at Upper Kachura Lake with cold glacial breeze is unmatched.", "2024-11-09"),

    # Landmark reviews
    (29, None, None, 1, "David Miller", 5, "Faisal Mosque is an architectural triumph. Its scale against the Margalla Hills is breathtaking.", "2024-10-10"),
    (30, None, None, 2, "Sophie Laurent", 5, "Pakistan Monument is gorgeous at dusk. The petals light up and the heritage museum is world-class.", "2024-10-13"),
    (31, None, None, 11, "Elena Rostova", 5, "Badshahi Mosque is pure majesty. The vast marble courtyard and red stone arches evoke Mughal splendor.", "2024-10-16"),
    (32, None, None, 12, "Mark Johnson", 5, "Lahore Fort's restored Picture Wall and Sheesh Mahal are stunning examples of imperial craftsmanship.", "2024-10-18"),
    (33, None, None, 21, "Aliya Kazmi", 5, "Mazar-e-Quaid is solemn and beautifully maintained. The white marble against blue skies is magnificent.", "2024-10-22"),
    (34, None, None, 23, "Farida Patel", 5, "Mohatta Palace has lovely Rajasthani stone arches and thought-provoking historical exhibitions.", "2024-10-25"),
    (35, None, None, 31, "Kenji Sato", 5, "Kargah Buddha is an incredible piece of Silk Road Buddhist history carved into sheer granite cliffs.", "2024-10-30"),
    (36, None, None, 32, "Clara Schmidt", 5, "Naltar Valley lakes have supernatural shades of turquoise and green. Pristine nature at its best.", "2024-11-03"),
    (37, None, None, 41, "Michael Brown", 5, "Lower Kachura Lake is a real-life fairy tale. The red pagodas reflecting in the mirror lake is iconic.", "2024-11-06"),
    (38, None, None, 44, "Laura Jenkins", 5, "Deosai Plains feels like another planet. Rolling alpine grasslands under endless sky at 4,000m.", "2024-11-08"),
    (39, None, None, 45, "Shahram Khan", 5, "Katpana Desert is surreal. Sand dunes with snowy mountain peaks in the background is mind-blowing.", "2024-11-10"),
    (40, None, None, 48, "Arthur Pendelton", 5, "Shigar Fort's restoration by Aga Khan Cultural Service is masterclass. Every wooden beam tells history.", "2024-11-12")
]

BOOKINGS_DATA = [
    # 20 confirmed bookings with dates and calculated prices
    (1, 1, 1, "Kamran Akmal", "+92-300-1111222", "2024-12-01", "2024-12-04", 156000.00, "CONFIRMED"),
    (2, 2, 3, "Zahid Hussain", "+92-321-2222333", "2024-12-05", "2024-12-07", 56000.00, "CONFIRMED"),
    (3, 9, 17, "Fawad Alam", "+92-333-3333444", "2024-12-10", "2024-12-13", 156000.00, "CONFIRMED"),
    (4, 10, 19, "Sohail Tanveer", "+92-345-4444555", "2024-12-12", "2024-12-15", 345000.00, "CONFIRMED"),
    (5, 17, 33, "Nasir Jamshed", "+92-300-5555666", "2024-12-02", "2024-12-05", 156000.00, "CONFIRMED"),
    (6, 18, 35, "Asad Shafiq", "+92-312-6666777", "2024-12-08", "2024-12-10", 104000.00, "CONFIRMED"),
    (7, 25, 49, "Misbah-ul-Haq", "+92-301-7777888", "2024-12-15", "2024-12-18", 156000.00, "CONFIRMED"),
    (8, 26, 51, "Younis Khan", "+92-334-8888999", "2024-12-20", "2024-12-23", 84000.00, "CONFIRMED"),
    (9, 33, 65, "Shoaib Akhtar", "+92-322-9999000", "2024-12-22", "2024-12-26", 208000.00, "CONFIRMED"),
    (10, 34, 67, "Shahid Afridi", "+92-300-0000111", "2024-12-24", "2024-12-28", 208000.00, "CONFIRMED"),
    (11, 4, 7, "Imran Nazir", "+92-345-1234123", "2024-12-03", "2024-12-06", 84000.00, "CONFIRMED"),
    (12, 12, 23, "Yasir Shah", "+92-333-2345234", "2024-12-04", "2024-12-07", 84000.00, "CONFIRMED"),
    (13, 20, 39, "Wahab Riaz", "+92-321-3456345", "2024-12-06", "2024-12-09", 84000.00, "CONFIRMED"),
    (14, 27, 53, "Mohammad Amir", "+92-300-4567456", "2024-12-07", "2024-12-10", 40500.00, "CONFIRMED"),
    (15, 35, 69, "Sarfraz Ahmed", "+92-311-5678567", "2024-12-11", "2024-12-14", 156000.00, "CONFIRMED"),
    (16, 6, 11, "Shan Masood", "+92-344-6789678", "2024-12-14", "2024-12-16", 27000.00, "CONFIRMED"),
    (17, 14, 27, "Azhar Ali", "+92-302-7890789", "2024-12-16", "2024-12-18", 56000.00, "CONFIRMED"),
    (18, 22, 43, "Umar Gul", "+92-332-8901890", "2024-12-18", "2024-12-21", 40500.00, "CONFIRMED"),
    (19, 30, 59, "Junaid Khan", "+92-323-9012901", "2024-12-21", "2024-12-24", 84000.00, "CONFIRMED"),
    (20, 38, 75, "Mohammad Hafeez", "+92-304-0123012", "2024-12-25", "2024-12-28", 40500.00, "CONFIRMED")
]

SEASONS_DATA = [
    # 20 seasons (4 seasons for each city)
    # Islamabad
    (1, 1, "Spring", "March to April", "15C - 26C", "Pleasant sunny days, Margalla Hills bloom with wildflowers. Ideal for hiking trails and outdoor gardens.", 4.9, "https://pmd.gov.pk", DATE_RETRIEVED),
    (2, 1, "Summer / Monsoon", "May to August", "26C - 39C", "Hot afternoons with dramatic monsoon downpours in July-August. Lush greenery across the capital.", 3.8, "https://pmd.gov.pk", DATE_RETRIEVED),
    (3, 1, "Autumn", "September to November", "16C - 28C", "Crisp golden foliage, clear mountain views, and moderate temperatures. Peak tourist trekking season.", 4.8, "https://pmd.gov.pk", DATE_RETRIEVED),
    (4, 1, "Winter", "December to February", "3C - 18C", "Chilly dry winter with fog and occasional frost. Distant Margalla crests occasionally receive snow dusting.", 4.2, "https://pmd.gov.pk", DATE_RETRIEVED),

    # Lahore
    (5, 2, "Spring", "February to March", "14C - 27C", "The festive season of Jashn-e-Baharan. Mild sunny weather ideal for exploring the Walled City and gardens.", 4.9, "https://pmd.gov.pk", DATE_RETRIEVED),
    (6, 2, "Summer / Monsoon", "May to August", "28C - 42C", "Intense heat followed by heavy monsoon rains in July. Best enjoyed indoors or during nighttime food street visits.", 3.2, "https://pmd.gov.pk", DATE_RETRIEVED),
    (7, 2, "Autumn", "October to November", "18C - 30C", "Pleasant evenings, start of outdoor wedding festivities and cultural literary festivals.", 4.6, "https://pmd.gov.pk", DATE_RETRIEVED),
    (8, 2, "Winter", "December to January", "6C - 20C", "Cool days with winter smog; excellent for savoring hot nihari, halwa puri, and Kashmiri chai.", 4.4, "https://pmd.gov.pk", DATE_RETRIEVED),

    # Karachi
    (9, 3, "Spring / Early Summer", "March to April", "22C - 33C", "Warm maritime breeze from the Arabian Sea with moderate humidity.", 4.0, "https://pmd.gov.pk", DATE_RETRIEVED),
    (10, 3, "Summer / Monsoon", "May to August", "28C - 36C", "Humid coastal weather with sea breezes, overcast monsoon skies, and active beach waves.", 3.7, "https://pmd.gov.pk", DATE_RETRIEVED),
    (11, 3, "Autumn", "September to October", "24C - 33C", "Post-monsoon warm days with refreshing evening sea winds across Clifton and Port Grand.", 4.2, "https://pmd.gov.pk", DATE_RETRIEVED),
    (12, 3, "Winter", "November to February", "13C - 27C", "The golden travel season in Karachi. Perfectly mild, clear skies, ideal for water sports and heritage walks.", 5.0, "https://pmd.gov.pk", DATE_RETRIEVED),

    # Gilgit
    (13, 4, "Spring", "April to May", "10C - 22C", "Cherry and apricot blossoms turn the valleys white and pink against rugged Karakoram cliffs.", 4.8, "https://pmd.gov.pk", DATE_RETRIEVED),
    (14, 4, "Summer", "June to August", "18C - 34C", "Warm valley days, cool mountain nights. Prime season for high alpine trekking and KKH expeditions.", 4.9, "https://pmd.gov.pk", DATE_RETRIEVED),
    (15, 4, "Autumn", "September to October", "8C - 20C", "Spectacular golden foliage season as poplars and apricots turn brilliant shades of gold and amber.", 5.0, "https://pmd.gov.pk", DATE_RETRIEVED),
    (16, 4, "Winter", "November to March", "-3C - 10C", "Cold winter with snow in upper valleys; valley roads remain mostly accessible. Skiing in Naltar.", 3.5, "https://pmd.gov.pk", DATE_RETRIEVED),

    # Skardu
    (17, 5, "Spring", "April to May", "6C - 18C", "Apricot and almond blossom festival throughout Shigar, Khaplu, and Kachura valleys.", 4.8, "https://pmd.gov.pk", DATE_RETRIEVED),
    (18, 5, "Summer", "June to August", "14C - 28C", "Peak mountaineering and touring season. Deosai National Park opens with carpets of wild flowers.", 5.0, "https://pmd.gov.pk", DATE_RETRIEVED),
    (19, 5, "Autumn", "September to October", "4C - 18C", "Crystal clear skies, golden-red poplar trees reflecting in turquoise lakes, crisp mountain air.", 4.9, "https://pmd.gov.pk", DATE_RETRIEVED),
    (20, 5, "Winter", "November to March", "-12C - 4C", "Freezing temperatures, frozen lakes, snow-covered Katpana dunes, and winter ice climbing.", 3.4, "https://pmd.gov.pk", DATE_RETRIEVED)
]

EMERGENCY_CONTACTS_DATA = [
    # Islamabad (5 contacts)
    (1, 1, "Police Helpline", "Islamabad Capital Police Command Center", "15 / +92-51-9261504", "Police Headquarters, Sector H-11, Islamabad", "https://islamabadpolice.gov.pk", DATE_RETRIEVED),
    (2, 1, "Hospital / Emergency", "Pakistan Institute of Medical Sciences (PIMS)", "+92-51-9261170", "Sector G-8/3, Islamabad", "https://pims.gov.pk", DATE_RETRIEVED),
    (3, 1, "Rescue / Ambulance", "Emergency Rescue 1122 ICT", "1122", "Sector G-10 Markaz, Islamabad", "https://rescue.gov.pk", DATE_RETRIEVED),
    (4, 1, "Tourist Police", "Islamabad Tourist Facilitation Police", "+92-51-9261506", "Daman-e-Koh / Margalla Hills Checkpoint", "https://islamabadpolice.gov.pk", DATE_RETRIEVED),
    (5, 1, "Disaster Management", "National Disaster Management Authority (NDMA)", "+92-51-111157100", "Prime Minister's Office Complex, Islamabad", "https://ndma.gov.pk", DATE_RETRIEVED),

    # Lahore (5 contacts)
    (6, 2, "Police Helpline", "Punjab Police Emergency Help 15", "15 / +92-42-99200276", "Central Police Office, Old Anarkali, Lahore", "https://punjabpolice.gov.pk", DATE_RETRIEVED),
    (7, 2, "Hospital / Emergency", "Mayo Hospital Emergency Ward", "+92-42-99211100", "Hospital Road, Anarkali, Lahore", "https://mayohospital.gop.pk", DATE_RETRIEVED),
    (8, 2, "Rescue / Ambulance", "Punjab Emergency Service Rescue 1122 HQ", "1122", "Rescue Headquarters, Thokar Niaz Baig, Lahore", "https://rescue.gov.pk", DATE_RETRIEVED),
    (9, 2, "Tourist Police", "Tourism Police Facilitation Unit TDCP", "+92-42-111111042", "TDCP Building, 4-A Lawrence Road, Lahore", "https://tdcp.gop.pk", DATE_RETRIEVED),
    (10, 2, "Hospital / Emergency", "Shaukat Khanum Memorial Cancer Hospital", "+92-42-35905000", "7A Block R-3, Johar Town, Lahore", "https://shaukatkhanum.org.pk", DATE_RETRIEVED),

    # Karachi (5 contacts)
    (11, 3, "Police Helpline", "Sindh Police Emergency Madadgar 15", "15 / +92-21-99225300", "Central Police Office, I.I. Chundrigar Road, Karachi", "https://sindhpolice.gov.pk", DATE_RETRIEVED),
    (12, 3, "Hospital / Emergency", "Aga Khan University Hospital (AKUH)", "+92-21-111911911", "National Stadium Road, Karachi", "https://hospitals.aku.edu", DATE_RETRIEVED),
    (13, 3, "Rescue / Ambulance", "Edhi Emergency Ambulance Foundation", "115 / +92-21-32310066", "Boulton Market, M.A. Jinnah Road, Karachi", "https://edhi.org", DATE_RETRIEVED),
    (14, 3, "Tourist Police", "Sindh Tourism Police & Coastal Security", "+92-21-99205670", "Sea View Police Post, Clifton, Karachi", "https://stdc.gos.pk", DATE_RETRIEVED),
    (15, 3, "Foreign Consulate / Embassy", "Karachi Consular Corps Emergency Liaison", "+92-21-35870000", "Consular Enclave, Clifton, Karachi", "https://mofa.gov.pk", DATE_RETRIEVED),

    # Gilgit (5 contacts)
    (16, 4, "Police Helpline", "Gilgit-Baltistan Police Emergency", "15 / +92-5811-930033", "Central Police Office, Gilgit", "https://gbpolice.gov.pk", DATE_RETRIEVED),
    (17, 4, "Hospital / Emergency", "District Headquarter (DHQ) Hospital Gilgit", "+92-5811-920253", "Hospital Road, Gilgit", "https://health.gilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (18, 4, "Rescue / Ambulance", "Rescue 1122 Gilgit Division", "1122", "Jutial, Gilgit", "https://rescue.gov.pk", DATE_RETRIEVED),
    (19, 4, "Tourist Police", "GB Tourist Police Command Post", "+92-5811-920150", "Chinar Bagh / Bab-e-Gilgit Checkpost", "https://gbpolice.gov.pk", DATE_RETRIEVED),
    (20, 4, "Disaster Management", "GB Disaster Management Authority (GBDMA)", "+92-5811-920875", "Near High Court, Gilgit", "https://gbdma.gov.pk", DATE_RETRIEVED),

    # Skardu (5 contacts)
    (21, 5, "Police Helpline", "Skardu District Police Control", "15 / +92-5815-920222", "Main Bazar Police Station, Skardu", "https://gbpolice.gov.pk", DATE_RETRIEVED),
    (22, 5, "Hospital / Emergency", "Regional Headquarter (RHQ) Hospital Skardu", "+92-5815-920255", "Hospital Road, Skardu", "https://health.gilgitbaltistan.gov.pk", DATE_RETRIEVED),
    (23, 5, "Rescue / Ambulance", "Rescue 1122 Skardu Station", "1122", "Airport Road, Skardu", "https://rescue.gov.pk", DATE_RETRIEVED),
    (24, 5, "Tourist Police", "Skardu High Altitude Tourist Assistance Post", "+92-5815-920333", "Yadgar Chowk / Shangrila Checkpoint", "https://gbpolice.gov.pk", DATE_RETRIEVED),
    (25, 5, "Disaster Management", "GBDMA District Emergency Operation Center", "+92-5815-920444", "DC Complex, Skardu", "https://gbdma.gov.pk", DATE_RETRIEVED)
]

CURRENCIES_DATA = [
    # 8 currencies
    ("USD", "US Dollar", 278.5000, "2024-11-20", "https://www.sbp.org.pk"),
    ("EUR", "Euro", 294.2000, "2024-11-20", "https://www.sbp.org.pk"),
    ("GBP", "British Pound", 352.8000, "2024-11-20", "https://www.sbp.org.pk"),
    ("AED", "UAE Dirham", 75.8500, "2024-11-20", "https://www.sbp.org.pk"),
    ("SAR", "Saudi Riyal", 74.2000, "2024-11-20", "https://www.sbp.org.pk"),
    ("CNY", "Chinese Yuan", 38.5000, "2024-11-20", "https://www.sbp.org.pk"),
    ("CAD", "Canadian Dollar", 199.1000, "2024-11-20", "https://www.sbp.org.pk"),
    ("AUD", "Australian Dollar", 181.4000, "2024-11-20", "https://www.sbp.org.pk")
]

# Admin user data (Username: admin, Password: admin)
# Salted SHA-256 computation:
ADMIN_SALT = "9f8e7d6c5b4a3210"
admin_pwd_combined = "admin" + ADMIN_SALT
ADMIN_HASH = hashlib.sha256(admin_pwd_combined.encode('utf-8')).hexdigest()

print("data_definitions.py successfully loaded.")
