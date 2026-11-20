import os, json

TEMPLATES_DIR = r"c:\\Users\\URVASHI BHARTI\\OneDrive\\Desktop\\zoop\\templates"
ASSETS_DIR = r"c:\\Users\\URVASHI BHARTI\\OneDrive\\Desktop\\zoop\\assets"
os.makedirs(TEMPLATES_DIR, exist_ok=True)

templates_data = [
    # 1-12: Royal & Heritage Weddings
    {
        "id": 1, "slug": "01-royal-rajputana", "name": "Royal Rajputana Palace",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Emerald & Antique Gold",
        "wine": "#064E3B", "wine_d": "#022C22", "rose": "#047857", "rose_d": "#065F46",
        "gold": "#D4AF37", "gold_l": "#FDE68A", "blush": "#F6F3EB", "blush2": "#EFEAD8", "ivory": "#FCFBF7", "ink": "#132A13",
        "title": "Royal Wedding of Aarav & Ananya", "celebrants": "Aarav & Ananya", "subtitle": "Under the Royal Arches of Rajasthan",
        "c1_name": "Aarav Malhotra", "c1_par": "Son of Mr. Rajiv & Mrs. Neelam Malhotra",
        "c2_name": "Ananya Kapoor", "c2_par": "Daughter of Mr. Vikram & Mrs. Shalini Kapoor",
        "eyebrow": "॥ Shree Ganeshaya Namah ॥ Together with their families",
        "quote": "Two souls, one sacred vow — bound by eternal love and tradition.",
        "closing": "In every lifetime, I would find you and choose you again.",
        "date_str": "Sunday, 14th February 2027", "date_iso": "2027-02-14T19:30", "time_str": "7:30 PM",
        "venue": "The Leela Palace, Udaipur", "venue_addr": "Lake Pichola, Udaipur, Rajasthan 313001",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#AaravWedsAnanya",
        "events": [
            {"name": "Haldi Ceremony", "date": "12 Feb 2027, 10:00 AM", "venue": "Lakeside Courtyard", "dress": "Shades of Yellow", "note": "Turmeric, marigolds & laughter"},
            {"name": "Mehendi & Sangeet", "date": "13 Feb 2027, 6:00 PM", "venue": "Durbar Hall", "dress": "Indo-Western Glam", "note": "Henna, folk melodies & dance"},
            {"name": "The Royal Wedding", "date": "14 Feb 2027, 7:30 PM", "venue": "Jag Mandir Island", "dress": "Royal Traditional", "note": "Pheras under floral mandap"},
            {"name": "Grand Reception", "date": "15 Feb 2027, 8:00 PM", "venue": "Grand Ballroom", "dress": "Black Tie / Ethnic", "note": "Banquet dinner & toasts"}
        ]
    },
    {
        "id": 2, "slug": "02-udaivilas-splendor", "name": "Udaivilas Velvet Splendor",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Burgundy Velvet & Gold",
        "wine": "#6B1D2F", "wine_d": "#420F1B", "rose": "#9E3850", "rose_d": "#731E33",
        "gold": "#D4AF37", "gold_l": "#FDE68A", "blush": "#FFF5F5", "blush2": "#FCE8E8", "ivory": "#FFFCFC", "ink": "#2D0C13",
        "title": "Royal Wedding of Dev & Ishita", "celebrants": "Dev & Ishita", "subtitle": "A Majestic Affair on the Waters of Pichola",
        "c1_name": "Devendra Rathore", "c1_par": "Son of Maharaj Mahendra & Maharani Padmini Rathore",
        "c2_name": "Ishita Singhania", "c2_par": "Daughter of Mr. Alok & Mrs. Sunita Singhania",
        "eyebrow": "With the Divine Blessings of Lord Krishna",
        "quote": "Love is not gazing at each other, but looking together in the same direction.",
        "closing": "Forever begins the moment our hands meet.",
        "date_str": "Saturday, 27th November 2027", "date_iso": "2027-11-27T19:00", "time_str": "7:00 PM",
        "venue": "The Oberoi Udaivilas, Udaipur", "venue_addr": "Haridas Ji Ki Magri, Udaipur 313001",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "lanterns", "music": "sitar", "hashtag": "#DevkiIshita",
        "events": [
            {"name": "Mayun & Welcome", "date": "26 Nov 2027, 11:00 AM", "venue": "Kohinoor Lawn", "dress": "Festive Pastel", "note": "Traditional blessings and high tea"},
            {"name": "Sangeet Extravaganza", "date": "26 Nov 2027, 7:00 PM", "venue": "Chandra Mahal", "dress": "Regal Velvet & Silk", "note": "Sufi & Bollywood performances"},
            {"name": "Varmala & Pheras", "date": "27 Nov 2027, 7:00 PM", "venue": "Floating Mandap", "dress": "Traditional Marwari", "note": "Auspicious wedding ceremony"}
        ]
    },
    {
        "id": 3, "slug": "03-jaipur-regal-pink", "name": "Jaipur Regal Pink",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Terracotta Rose & Peacock Teal",
        "wine": "#832A3E", "wine_d": "#571625", "rose": "#0E7490", "rose_d": "#155E75",
        "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFA", "ink": "#3B0D16",
        "title": "Royal Wedding of Rohan & Meera", "celebrants": "Rohan & Meera", "subtitle": "Celebrate Love Amidst the Grandeur of the Pink City",
        "c1_name": "Rohan Shekhawat", "c1_par": "Son of Thakur Jagat & Mrs. Pratibha Shekhawat",
        "c2_name": "Meera Chauhan", "c2_par": "Daughter of Brig. Yashwant & Mrs. Gayatri Chauhan",
        "eyebrow": "॥ Mangalam Bhagwan Vishnu ॥",
        "quote": "Two lives, two hearts, joined together in friendship, united forever in love.",
        "closing": "You are my today and all of my tomorrows.",
        "date_str": "Friday, 10th December 2027", "date_iso": "2027-12-10T18:30", "time_str": "6:30 PM",
        "venue": "Rambagh Palace, Jaipur", "venue_addr": "Bhawani Singh Rd, Jaipur, Rajasthan 302005",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#RohanMeeraVows",
        "events": [
            {"name": "Ganesh Sthapana & Haldi", "date": "09 Dec 2027, 10:00 AM", "venue": "Kesar Bagh", "dress": "Yellow & Marigold", "note": "Auspicious commencement"},
            {"name": "Royal Sangeet Night", "date": "09 Dec 2027, 7:00 PM", "venue": "Jaigarh Hall", "dress": "Royal Pink & Gold", "note": "Celebratory dance & music"},
            {"name": "The Royal Vivah", "date": "10 Dec 2027, 6:30 PM", "venue": "Naksha Garden", "dress": "Traditional Royal", "note": "Sacred pheras"}
        ]
    },
    {
        "id": 4, "slug": "04-mughal-gardens", "name": "Mughal Gardens Trellis",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Sage Green & Champagne Gold",
        "wine": "#2D5A43", "wine_d": "#1A3728", "rose": "#4E7B62", "rose_d": "#365945",
        "gold": "#C5A059", "gold_l": "#F3E3B6", "blush": "#F3F7F4", "blush2": "#E4EDE6", "ivory": "#FAFDFB", "ink": "#14251C",
        "title": "Wedding of Zaid & Alizeh", "celebrants": "Zaid & Alizeh", "subtitle": "A Sacred Union Blessed by Eternity",
        "c1_name": "Zaid Farooqui", "c1_par": "Son of Dr. Tariq & Mrs. Rehana Farooqui",
        "c2_name": "Alizeh Qureshi", "c2_par": "Daughter of Mr. Mansoor & Mrs. Parveen Qureshi",
        "eyebrow": "Bismillah ar-Rahman ar-Rahim",
        "quote": "And We created you in pairs. — Surah An-Naba [78:8]",
        "closing": "May our love blossom through every season of life.",
        "date_str": "Saturday, 16th January 2027", "date_iso": "2027-01-16T19:00", "time_str": "7:00 PM",
        "venue": "Shalimar Bagh Pavilions, Srinagar", "venue_addr": "Dal Lake Shore, Srinagar, J&K 190025",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "stars", "music": "sitar", "hashtag": "#ZaidWedsAlizeh",
        "events": [
            {"name": "Manjha (Haldi)", "date": "15 Jan 2027, 11:00 AM", "venue": "Pine Terrace", "dress": "Sage & Mustard", "note": "Traditional flower blessing"},
            {"name": "Mehndi Ki Raat", "date": "15 Jan 2027, 6:30 PM", "venue": "Chinar Hall", "dress": "Emerald Elegance", "note": "Henna & ghazal night"},
            {"name": "Nikah & Walima", "date": "16 Jan 2027, 7:00 PM", "venue": "Grand Pavilion", "dress": "Formal Attire", "note": "Sacred vows & feast"}
        ]
    },
    {
        "id": 5, "slug": "05-jodhpur-sun-city", "name": "Jodhpur Sun City Blue",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Royal Cobalt & Sand Gold",
        "wine": "#1E3A8A", "wine_d": "#172554", "rose": "#2563EB", "rose_d": "#1D4ED8",
        "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#EFF6FF", "blush2": "#DBEAFE", "ivory": "#F8FAFC", "ink": "#0F172A",
        "title": "Royal Wedding of Ranveer & Kiara", "celebrants": "Ranveer & Kiara", "subtitle": "Golden Rays over the Blue Oasis of Marwar",
        "c1_name": "Ranveer Rathore", "c1_par": "Son of Sh. Gajendra & Smt. Kamla Rathore",
        "c2_name": "Kiara Advani", "c2_par": "Daughter of Sh. Jagdish & Smt. Genevieve Advani",
        "eyebrow": "॥ Jai Chamunda Maa ॥ Cordially Invite You",
        "quote": "Beneath the golden sun and silver moon, our two souls become one.",
        "closing": "Walking hand in hand through the fortress of forever.",
        "date_str": "Thursday, 18th March 2027", "date_iso": "2027-03-18T19:00", "time_str": "7:00 PM",
        "venue": "Umaid Bhawan Palace, Jodhpur", "venue_addr": "Circuit House Rd, Cantt Area, Jodhpur 342006",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "lanterns", "music": "piano", "hashtag": "#RanveerKiKiara",
        "events": [
            {"name": "Welcome High Tea", "date": "17 Mar 2027, 4:00 PM", "venue": "Palace Courtyard", "dress": "Casual Chic", "note": "Marwari hospitality"},
            {"name": "Desert Sangeet", "date": "17 Mar 2027, 7:30 PM", "venue": "Baradari Lawn", "dress": "Cobalt & Gold", "note": "Folk dancers and fireworks"},
            {"name": "The Royal Vivah", "date": "18 Mar 2027, 7:00 PM", "venue": "Lancer's Lawn", "dress": "Royal Traditional", "note": "Toran & Seven Vows"}
        ]
    },
    {
        "id": 6, "slug": "06-south-temple-kanjeevaram", "name": "South Temple Kanjeevaram",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Turmeric Yellow & Temple Ruby",
        "wine": "#991B1B", "wine_d": "#7F1D1D", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEF5", "ink": "#450A0A",
        "title": "Kalyanam of Karthik & Deepa", "celebrants": "Karthik & Deepa", "subtitle": "Auspicious Muhurtham with Nadhaswaram & Vedic Chants",
        "c1_name": "Karthik Subramanian", "c1_par": "Son of Sri K. Subramanian & Smt. Lakshmi",
        "c2_name": "Deepa Natarajan", "c2_par": "Daughter of Sri R. Natarajan & Smt. Meenakshi",
        "eyebrow": "॥ Om Sri Maha Ganapataye Namaha ॥",
        "quote": "Thali tying under the divine grace of Meenakshi Sundareswarar.",
        "closing": "May the blessings of elders light our path for seven lifetimes.",
        "date_str": "Friday, 21st May 2027", "date_iso": "2027-05-21T07:30", "time_str": "7:30 AM",
        "venue": "Raja Muthiah Mandram, Madurai", "venue_addr": "Melur Road, Madurai, Tamil Nadu 625020",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#DeepaWedsKarthik",
        "events": [
            {"name": "Vratham & Sumangali Prarthana", "date": "20 May 2027, 9:00 AM", "venue": "Gokulam Hall", "dress": "Madisar & Veshti", "note": "Ancestral blessings"},
            {"name": "Janavasam & Sangeet", "date": "20 May 2027, 6:00 PM", "venue": "Temple Courtyard", "dress": "Silk & Brocade", "note": "Grand floral procession"},
            {"name": "Auspicious Muhurtham", "date": "21 May 2027, 7:30 AM", "venue": "Main Mandapam", "dress": "Kanjeevaram Silk", "note": "Mangalya Dharanam"}
        ]
    },
    {
        "id": 7, "slug": "07-kerala-backwaters", "name": "Kerala Backwaters Serenade",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Kasavu Gold & Coconut Green",
        "wine": "#14532D", "wine_d": "#052E16", "rose": "#15803D", "rose_d": "#166534",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDF4", "blush2": "#DCFCE7", "ivory": "#FAFFFA", "ink": "#022C22",
        "title": "Wedding of Siddharth & Malavika", "celebrants": "Siddharth & Malavika", "subtitle": "A Sacred Union on the Tranquil Shores of Kumarakom",
        "c1_name": "Siddharth Menon", "c1_par": "Son of Sri K.P. Menon & Smt. Girija",
        "c2_name": "Malavika Nair", "c2_par": "Daughter of Sri Madhavan Nair & Smt. Sujatha",
        "eyebrow": "Hari Sri Ganapataye Namah",
        "quote": "Like water in the backwaters flowing toward the ocean, our lives unite.",
        "closing": "Light of the Nilavilakku guiding our eternal journey.",
        "date_str": "Sunday, 12th September 2027", "date_iso": "2027-09-12T10:15", "time_str": "10:15 AM",
        "venue": "Kumarakom Lake Resort, Kottayam", "venue_addr": "Vembanad Lake, Kumarakom, Kerala 686566",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "sitar", "hashtag": "#SidMaluUnion",
        "events": [
            {"name": "Ayyanar Puja & Welcome", "date": "11 Sep 2027, 4:00 PM", "venue": "Ayurveda Lawn", "dress": "Traditional Kerala", "note": "Jasmine garlands & tender coconut"},
            {"name": "Sunset Houseboat Soiree", "date": "11 Sep 2027, 6:00 PM", "venue": "Vembanad Cruise", "dress": "Resort Casual", "note": "Acoustic music and local delicacies"},
            {"name": "Thalikettu & Sadhya", "date": "12 Sep 2027, 10:15 AM", "venue": "Lakeside Mandap", "dress": "Kasavu Mundu & Saree", "note": "Traditional 24-dish feast"}
        ]
    },
    {
        "id": 8, "slug": "08-maratha-peshwa", "name": "Maratha Peshwa Heritage",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Peshwai Crimson & Saffron",
        "wine": "#831843", "wine_d": "#500724", "rose": "#C2410C", "rose_d": "#9A3412",
        "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFA", "ink": "#380619",
        "title": "Vivah of Aditya & Shruti", "celebrants": "Aditya & Shruti", "subtitle": "Honoring the Brave Traditions of Swarajya",
        "c1_name": "Aditya Deshmukh", "c1_par": "Son of Sh. Vijayrao & Smt. Sunandatai Deshmukh",
        "c2_name": "Shruti Kulkarni", "c2_par": "Daughter of Sh. Chandrakant & Smt. Anuradhatai Kulkarni",
        "eyebrow": "॥ Jai Bhavani, Jai Shivaji ॥",
        "quote": "With the sacred Antarpat dropping, two souls unite for eternity.",
        "closing": "May our love stand as mighty as the Sahyadri mountains.",
        "date_str": "Monday, 8th November 2027", "date_iso": "2027-11-08T11:45", "time_str": "11:45 AM",
        "venue": "Shaniwar Wada Heritage Grounds, Pune", "venue_addr": "Shaniwar Peth, Pune, Maharashtra 411030",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "sitar", "hashtag": "#AdityaWedsShruti",
        "events": [
            {"name": "Gauri Har Puja & Halad", "date": "07 Nov 2027, 10:00 AM", "venue": "Courtyard Hall", "dress": "Yellow Paithani", "note": "Auspicious turmeric ceremony"},
            {"name": "Peshwai Sangeet", "date": "07 Nov 2027, 7:00 PM", "venue": "Rajdarbar Hall", "dress": "Traditional Maharashtrian", "note": "Dhol tasha & classical fusion"},
            {"name": "Subha Vivah (Lagna)", "date": "08 Nov 2027, 11:45 AM", "venue": "Main Pandal", "dress": "Nauvari Saree & Dhoti", "note": "Saptapadi & Kanyadaan"}
        ]
    },
    {
        "id": 9, "slug": "09-bengali-zamindar", "name": "Bengali Zamindar Rajbari",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Crimson Alta & Terracotta",
        "wine": "#7F1D1D", "wine_d": "#450A0A", "rose": "#B91C1C", "rose_d": "#991B1B",
        "gold": "#D97706", "gold_l": "#FEF08A", "blush": "#FEF2F2", "blush2": "#FEE2E2", "ivory": "#FFFDFD", "ink": "#350808",
        "title": "Biye of Subhash & Debolina", "celebrants": "Subhash & Debolina", "subtitle": "The Sweet Echo of Shonkho & Ululu at the Rajbari",
        "c1_name": "Subhash Mukhopadhyay", "c1_par": "Son of Sri Debabrata & Smt. Jharna Mukhopadhyay",
        "c2_name": "Debolina Banerjee", "c2_par": "Daughter of Sri Alok & Smt. Madhabilata Banerjee",
        "eyebrow": "॥ Shubho Bibaho ॥",
        "quote": "Seven circles around the sacred fire, bound in crimson silk and betel leaves.",
        "closing": "Bhalobashar shuru ekhane — the beginning of endless love.",
        "date_str": "Wednesday, 1st December 2027", "date_iso": "2027-12-01T19:30", "time_str": "7:30 PM",
        "venue": "The Rajbari Bawali, Kolkata", "venue_addr": "Bawali, 24 Parganas South, West Bengal 700137",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#SubhashDebolinaBibaho",
        "events": [
            {"name": "Gaye Holud & Aiburobhat", "date": "30 Nov 2027, 10:00 AM", "venue": "Thakur Dalan", "dress": "Yellow Cotton Silk", "note": "Turmeric blessings and sweets"},
            {"name": "Shubho Drishti & Mala Badal", "date": "01 Dec 2027, 7:30 PM", "venue": "Central Courtyard", "dress": "Banarasi Silk & Topor", "note": "Betel leaf reveal and garlands"},
            {"name": "Bou Bhaat & Reception", "date": "03 Dec 2027, 7:30 PM", "venue": "Grand Hall", "dress": "Formal Ethnic", "note": "New bride welcome feast"}
        ]
    },
    {
        "id": 10, "slug": "10-punjabi-anand-karaj", "name": "Punjabi Anand Karaj",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Golden Mustard & Phulkari Red",
        "wine": "#831843", "wine_d": "#500724", "rose": "#E11D48", "rose_d": "#BE123C",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFFF7", "ink": "#380619",
        "title": "Anand Karaj of Harpreet & Simran", "celebrants": "Harpreet & Simran", "subtitle": "Blissful Union Under the Blessings of the Guru Granth Sahib",
        "c1_name": "Harpreet Singh Dhillon", "c1_par": "Son of S. Balwinder & Sd. Paramjit Kaur Dhillon",
        "c2_name": "Simran Kaur Sandhu", "c2_par": "Daughter of S. Gurmukh & Sd. Jaswinder Kaur Sandhu",
        "eyebrow": "॥ Ek Onkar Satnam ॥",
        "quote": "They are not said to be husband and wife who merely sit together. Rather, they alone are called husband and wife who have one soul in two bodies.",
        "closing": "Rab Rakha — May the Divine bless our voyage together.",
        "date_str": "Sunday, 5th December 2027", "date_iso": "2027-12-05T10:00", "time_str": "10:00 AM",
        "venue": "Heritage Haveli, Amritsar", "venue_addr": "GT Road, Amritsar, Punjab 143001",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "sitar", "hashtag": "#SimranDiHarpreet",
        "events": [
            {"name": "Maiyan & Jaggo", "date": "04 Dec 2027, 5:00 PM", "venue": "Haveli Lawns", "dress": "Bright Phulkari", "note": "Bhangra, gidda and brass lamps"},
            {"name": "Anand Karaj Ceremony", "date": "05 Dec 2027, 10:00 AM", "venue": "Gurdwara Sahib", "dress": "Pastel Pink & Turban", "note": "Four sacred Laavan"},
            {"name": "Grand Royal Reception", "date": "05 Dec 2027, 7:30 PM", "venue": "Grand Ballroom", "dress": "Glamorous Black Tie", "note": "DJ, live Dhol and feast"}
        ]
    },
    {
        "id": 11, "slug": "11-gujarati-lagan", "name": "Gujarati Lagan & Dandiya",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Bandhani Scarlet & Patola Gold",
        "wine": "#9A3412", "wine_d": "#7C2D12", "rose": "#EA580C", "rose_d": "#C2410C",
        "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEF7", "ink": "#431407",
        "title": "Lagan of Parth & Nidhi", "celebrants": "Parth & Nidhi", "subtitle": "A Celebration of Garba, Cheerful Joy and Seven Sacred Pheras",
        "c1_name": "Parth Shah", "c1_par": "Son of Sh. Kamleshbhai & Smt. Hansaben Shah",
        "c2_name": "Nidhi Patel", "c2_par": "Daughter of Sh. Chandrakantbhai & Smt. Minakshiben Patel",
        "eyebrow": "॥ Shree Ganeshay Namah ॥",
        "quote": "Hastamelap — where two hands unite to weave a destiny of happiness.",
        "closing": "Jeevan saathi, sukh-dukh na saathi.",
        "date_str": "Saturday, 23rd January 2027", "date_iso": "2027-01-23T18:00", "time_str": "6:00 PM",
        "venue": "Madhubhan Resort, Anand", "venue_addr": "Anand-Sojitra Rd, Vallabh Vidyanagar 388120",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "sitar", "hashtag": "#ParthKiNidhi",
        "events": [
            {"name": "Pithi & Mandap Muhurat", "date": "22 Jan 2027, 9:30 AM", "venue": "Resort Lawn", "dress": "Yellow Bandhej", "note": "Auspicious blessings"},
            {"name": "Raas-Garba Night", "date": "22 Jan 2027, 7:00 PM", "venue": "Amphitheatre", "dress": "Chaniya Choli & Kedia", "note": "Dandiya beats all night"},
            {"name": "Jaan Aagman & Lagan", "date": "23 Jan 2027, 6:00 PM", "venue": "Main Pavilion", "dress": "Panetar & Gharchola", "note": "Kanya Daan & Mangal Fera"}
        ]
    },
    {
        "id": 12, "slug": "12-kashmiri-chinar", "name": "Kashmiri Chinar Mist",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Autumn Chinar Gold & Saffron",
        "wine": "#7C2D12", "wine_d": "#431407", "rose": "#C2410C", "rose_d": "#9A3412",
        "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#FFF7ED", "blush2": "#FFEDD5", "ivory": "#FFFAF5", "ink": "#270B04",
        "title": "Nikah of Farhan & Zoya", "celebrants": "Farhan & Zoya", "subtitle": "Romance Mirrored in the Still Waters of Dal Lake",
        "c1_name": "Farhan Mir", "c1_par": "Son of Mr. Altaf & Mrs. Nighat Mir",
        "c2_name": "Zoya Bakshi", "c2_par": "Daughter of Mr. Zahoor & Mrs. Rukhsana Bakshi",
        "eyebrow": "Gar Firdaus bar roo-e zameen ast",
        "quote": "If there is a paradise on earth, it is here, it is here, it is here.",
        "closing": "Two hearts wrapped in the warm pashmina of love.",
        "date_str": "Friday, 15th October 2027", "date_iso": "2027-10-15T18:00", "time_str": "6:00 PM",
        "venue": "Vivanta Dal View, Srinagar", "venue_addr": "Kralsangri, Gopkar Rd, Srinagar 190001",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "lanterns", "music": "sitar", "hashtag": "#FarhanFoundZoya",
        "events": [
            {"name": "Livun & Haldi", "date": "14 Oct 2027, 11:00 AM", "venue": "Lake Terrace", "dress": "Chinar Embroidered", "note": "Kashmiri folk songs & kehwa"},
            {"name": "Mehndi & Wanwun", "date": "14 Oct 2027, 6:00 PM", "venue": "Pine Hall", "dress": "Saffron & Teal", "note": "Rabab melodies and henna"},
            {"name": "Nikah & Wazwan", "date": "15 Oct 2027, 6:00 PM", "venue": "Main Lawn", "dress": "Traditional Tilla", "note": "36-course royal banquet"}
        ]
    },

    # 13-22: Destination & Modern Luxury Weddings
    {
        "id": 13, "slug": "13-tuscan-vineyard", "name": "Tuscan Vineyard Romance",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Chianti Wine & Sunlit Olive",
        "wine": "#581C87", "wine_d": "#3B0764", "rose": "#4D7C0F", "rose_d": "#3F6212",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCF9FF", "ink": "#1E1B4B",
        "title": "Wedding of Liam & Olivia", "celebrants": "Liam & Olivia", "subtitle": "Under the Cypress Trees & Olive Groves of Florence",
        "c1_name": "Liam Montgomery", "c1_par": "Son of Charles & Victoria Montgomery",
        "c2_name": "Olivia De Luca", "c2_par": "Daughter of Matteo & Elena De Luca",
        "eyebrow": "Under the Tuscan Sun, Two Hearts Become One",
        "quote": "I love you not only for what you are, but for what I am when I am with you.",
        "closing": "A toast to a lifetime of sunset dinners and Italian wine.",
        "date_str": "Saturday, 18th September 2027", "date_iso": "2027-09-18T17:00", "time_str": "5:00 PM",
        "venue": "Villa Medicea di Lilliano, Florence", "venue_addr": "Via Lilliano e Meoli, 82, 50012 Bagno a Ripoli FI, Italy",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#LiamOliviaInTuscany",
        "events": [
            {"name": "Sunset Aperitivo & Pizza", "date": "17 Sep 2027, 6:00 PM", "venue": "The Olive Grove", "dress": "Smart Resort Chic", "note": "Wood-fired pizza & Prosecco"},
            {"name": "The Vows Ceremony", "date": "18 Sep 2027, 5:00 PM", "venue": "Courtyard Terrace", "dress": "Black Tie / Summer Formal", "note": "Exchange of vows overlooking Florence"},
            {"name": "Gala Dinner & Dancing", "date": "18 Sep 2027, 7:30 PM", "venue": "Limonaia Hall", "dress": "Evening Elegance", "note": "Chianti tasting & live jazz"}
        ]
    },
    {
        "id": 14, "slug": "14-santorini-sunset", "name": "Santorini Sunset Horizon",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Aegean Cobalt & Bougainvillea",
        "wine": "#1D4ED8", "wine_d": "#1E3A8A", "rose": "#DB2777", "rose_d": "#BE185D",
        "gold": "#F59E0B", "gold_l": "#FDE68A", "blush": "#EFF6FF", "blush2": "#DBEAFE", "ivory": "#F8FAFC", "ink": "#0F172A",
        "title": "Wedding of Lucas & Chloe", "celebrants": "Lucas & Chloe", "subtitle": "Overlooking the Caldera at Golden Sunset",
        "c1_name": "Lucas Vance", "c1_par": "Son of Peter & Diana Vance",
        "c2_name": "Chloe Theodorakis", "c2_par": "Daughter of Nikos & Sophia Theodorakis",
        "eyebrow": "From Greece with Love",
        "quote": "You are the finest, loveliest, tenderest, and most beautiful person I have ever known.",
        "closing": "Our love is as deep as the Aegean Sea.",
        "date_str": "Thursday, 24th June 2027", "date_iso": "2027-06-24T18:30", "time_str": "6:30 PM",
        "venue": "Canaves Oia Suites, Santorini", "venue_addr": "Oia 847 02, Cyclades, Greece",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#LucasAndChloeOia",
        "events": [
            {"name": "Welcome Catamaran Cruise", "date": "23 Jun 2027, 3:00 PM", "venue": "Amoudi Bay", "dress": "All White Resort", "note": "Swimming & Mediterranean tapas"},
            {"name": "Caldera Vows Ceremony", "date": "24 Jun 2027, 6:30 PM", "venue": "Infinity Terrace", "dress": "Island Formal", "note": "Sunset exchange of rings"},
            {"name": "Midnight Cliffside Party", "date": "24 Jun 2027, 8:30 PM", "venue": "Panorama Bar", "dress": "Cocktail Glam", "note": "Greek feast, dancing & sparklers"}
        ]
    },
    {
        "id": 15, "slug": "15-bali-tropical-paradise", "name": "Bali Tropical Paradise",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Frangipani Gold & Jungle Teal",
        "wine": "#0F766E", "wine_d": "#115E59", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDFA", "blush2": "#CCFBF1", "ivory": "#FAFFFE", "ink": "#042F2E",
        "title": "Wedding of Ethan & Sophia", "celebrants": "Ethan & Sophia", "subtitle": "A Sacred Blessing on the Cliffs of Uluwatu",
        "c1_name": "Ethan Brooks", "c1_par": "Son of David & Laura Brooks",
        "c2_name": "Sophia Zhang", "c2_par": "Daughter of Henry & Lin Zhang",
        "eyebrow": "Where the Rainforest Meets the Ocean",
        "quote": "In your arms, I have found my home, my peace, and my greatest adventure.",
        "closing": "Forever swimming in the tides of your love.",
        "date_str": "Saturday, 14th August 2027", "date_iso": "2027-08-14T16:30", "time_str": "4:30 PM",
        "venue": "AYANA Resort and Spa, Bali", "venue_addr": "Jimbaran, South Kuta, Badung Regency, Bali 80364",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "lanterns", "music": "piano", "hashtag": "#EthanSophiaBali",
        "events": [
            {"name": "Balinese Blessing & Sunset", "date": "13 Aug 2027, 5:00 PM", "venue": "Rock Bar Deck", "dress": "Tropical Linen", "note": "Canang sari flower offering"},
            {"name": "Cliffside Wedding Vows", "date": "14 Aug 2027, 4:30 PM", "venue": "Tresna Chapel", "dress": "Formal Island Elegance", "note": "Exchange of vows"},
            {"name": "Jungle Glow Reception", "date": "14 Aug 2027, 7:00 PM", "venue": "Champa Garden", "dress": "Cocktail Glam", "note": "Fire dancers and banquet"}
        ]
    },
    {
        "id": 16, "slug": "16-french-chateau", "name": "French Château Baroque",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Baroque Gold & Powder Rose",
        "wine": "#831843", "wine_d": "#500724", "rose": "#BE185D", "rose_d": "#9D174D",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FDF2F8", "blush2": "#FCE7F3", "ivory": "#FFFAFC", "ink": "#380619",
        "title": "Wedding of Alexander & Camille", "celebrants": "Alexander & Camille", "subtitle": "A Timeless Fairytale at Château de Chantilly",
        "c1_name": "Alexander Sterling", "c1_par": "Son of Lord Edward & Lady Margaret Sterling",
        "c2_name": "Camille De Montmirail", "c2_par": "Daughter of Count Henri & Countess Brigitte",
        "eyebrow": "L'Amour Toujours — Love Forever",
        "quote": "To love and be loved is to feel the sun from both sides.",
        "closing": "Vive les mariés — Long live our love.",
        "date_str": "Saturday, 11th September 2027", "date_iso": "2027-09-11T16:00", "time_str": "4:00 PM",
        "venue": "Château de Chantilly, France", "venue_addr": "60500 Chantilly, France",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#SterlingMontmirail",
        "events": [
            {"name": "Champagne Garden Welcome", "date": "10 Sep 2027, 5:30 PM", "venue": "Orangerie Lawn", "dress": "Cocktail Attire", "note": "Vintage Dom Pérignon & macarons"},
            {"name": "The Chapel Vows", "date": "11 Sep 2027, 4:00 PM", "venue": "Château Chapel", "dress": "Black Tie / Haute Couture", "note": "Choral symphony and vows"},
            {"name": "Gala Dinner & Waltz", "date": "11 Sep 2027, 7:30 PM", "venue": "Galerie des Peintures", "dress": "Grand Evening Gown", "note": "Classical waltz and feast"}
        ]
    },
    {
        "id": 17, "slug": "17-amalfi-coast-lemon", "name": "Amalfi Coast Limoncello",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Amalfi Lemon & Mediterranean Navy",
        "wine": "#1E3A8A", "wine_d": "#172554", "rose": "#EAB308", "rose_d": "#CA8A04",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FEFCE8", "blush2": "#FEF9C3", "ivory": "#FFFFFA", "ink": "#1E293B",
        "title": "Wedding of Mateo & Isabella", "celebrants": "Mateo & Isabella", "subtitle": "Scent of Lemon Blossoms over Positano Cliffs",
        "c1_name": "Mateo Rossi", "c1_par": "Son of Antonio & Francesca Rossi",
        "c2_name": "Isabella Moretti", "c2_par": "Daughter of Carlo & Giulia Moretti",
        "eyebrow": "Sotto il Cielo di Amalfi — Under the Amalfi Sky",
        "quote": "You are my sunshine, my sea breeze, and my true northern star.",
        "closing": "Salute a noi — Cheers to our eternal love.",
        "date_str": "Friday, 9th July 2027", "date_iso": "2027-07-09T18:00", "time_str": "6:00 PM",
        "venue": "Hotel Villa Cimbrone, Ravello", "venue_addr": "Via Santa Chiara, 26, 84010 Ravello SA, Italy",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#MateoIsabellaAmalfi",
        "events": [
            {"name": "Welcome Limoncello Soiree", "date": "08 Jul 2027, 6:00 PM", "venue": "Belvedere Terrace", "dress": "Mediterranean Chic", "note": "Artisanal limoncello & antipasti"},
            {"name": "Terrace of Infinity Ceremony", "date": "09 Jul 2027, 6:00 PM", "venue": "Terrazza dell'Infinito", "dress": "Summer Black Tie", "note": "Vows suspended between sea and sky"},
            {"name": "Romantic Italian Feast", "date": "09 Jul 2027, 8:00 PM", "venue": "Crypt Gardens", "dress": "Evening Elegance", "note": "Handmade pasta and fireworks"}
        ]
    },
    {
        "id": 18, "slug": "18-dubai-desert-glamour", "name": "Dubai Desert Oasis Glamour",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Dune Amber & Arabian Night",
        "wine": "#451A03", "wine_d": "#270B04", "rose": "#9A3412", "rose_d": "#7C2D12",
        "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#1E0D03",
        "title": "Wedding of Hamdan & Sarah", "celebrants": "Hamdan & Sarah", "subtitle": "A Thousand and One Nights of Golden Splendor",
        "c1_name": "Hamdan Al Maktoum", "c1_par": "Son of Sheikh Rashid & Sheikha Latifa",
        "c2_name": "Sarah Al Hashimi", "c2_par": "Daughter of Dr. Tariq & Mrs. Mona Al Hashimi",
        "eyebrow": "Under the Starlit Dunes of Arabia",
        "quote": "Love is the bridge between two souls across infinite sands.",
        "closing": "May the stars bless our golden voyage forever.",
        "date_str": "Saturday, 20th November 2027", "date_iso": "2027-11-20T19:00", "time_str": "7:00 PM",
        "venue": "Bab Al Shams Desert Resort, Dubai", "venue_addr": "Al Qudra Road, Dubai, United Arab Emirates",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "lanterns", "music": "sitar", "hashtag": "#HamdanSarahDubai",
        "events": [
            {"name": "Desert Sunset Welcome", "date": "19 Nov 2027, 5:00 PM", "venue": "Dune Lounge", "dress": "Arabian Chic", "note": "Falconry & oud melodies"},
            {"name": "The Royal Zafeh & Vows", "date": "20 Nov 2027, 7:00 PM", "venue": "Falcon Arena", "dress": "Formal Glamour", "note": "Traditional zafeh procession"},
            {"name": "Grand Royal Banquet", "date": "20 Nov 2027, 9:00 PM", "venue": "Al Forsan Ballroom", "dress": "Black Tie / Kandura & Abaya", "note": "Banquet under firelit skies"}
        ]
    },
    {
        "id": 19, "slug": "19-swiss-alps-winter", "name": "Swiss Alps Winter Wonderland",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Frosted Pine & Ice Silver",
        "wine": "#1E293B", "wine_d": "#0F172A", "rose": "#475569", "rose_d": "#334155",
        "gold": "#94A3B8", "gold_l": "#E2E8F0", "blush": "#F8FAFC", "blush2": "#F1F5F9", "ivory": "#FFFFFF", "ink": "#0F172A",
        "title": "Winter Wedding of Noah & Emma", "celebrants": "Noah & Emma", "subtitle": "A Sacred Vow Surrounded by Snowy Alpine Peaks",
        "c1_name": "Noah Lindqvist", "c1_par": "Son of Henrik & Astrid Lindqvist",
        "c2_name": "Emma Von Bern", "c2_par": "Daughter of Markus & Claudia Von Bern",
        "eyebrow": "Snowflakes Falling Like Gentle Blessings",
        "quote": "You are my warmest fire on the coldest winter day.",
        "closing": "Together in the snow, together for all seasons.",
        "date_str": "Saturday, 18th December 2027", "date_iso": "2027-12-18T16:00", "time_str": "4:00 PM",
        "venue": "Badrutt's Palace Hotel, St. Moritz", "venue_addr": "Via Serlas 27, 7500 St. Moritz, Switzerland",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#NoahEmmaAlpine",
        "events": [
            {"name": "Glühwein & Sleigh Welcome", "date": "17 Dec 2027, 5:00 PM", "venue": "Palace Terrace", "dress": "Winter Cashmere", "note": "Horse-drawn sleigh and hot cider"},
            {"name": "Snow Crystal Vows", "date": "18 Dec 2027, 4:00 PM", "venue": "Embassy Ballroom", "dress": "Black Tie / Faux Fur", "note": "Vows with Alpine panoramic view"},
            {"name": "Fondue & Fireplace Gala", "date": "18 Dec 2027, 7:00 PM", "venue": "Le Restaurant", "dress": "Evening Elegance", "note": "Swiss gastronomy & live harp"}
        ]
    },
    {
        "id": 20, "slug": "20-maldives-ocean-breeze", "name": "Maldives Ocean Breeze",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Lagoon Turquoise & Coral Pearl",
        "wine": "#0E7490", "wine_d": "#155E75", "rose": "#F43F5E", "rose_d": "#E11D48",
        "gold": "#F59E0B", "gold_l": "#FEF08A", "blush": "#ECFEFF", "blush2": "#CFFAFE", "ivory": "#FAFFFF", "ink": "#083344",
        "title": "Island Wedding of Kai & Mia", "celebrants": "Kai & Mia", "subtitle": "Barefoot Vows on Sparkling Turquoise Atolls",
        "c1_name": "Kai Montgomery", "c1_par": "Son of William & Jennifer Montgomery",
        "c2_name": "Mia Thorne", "c2_par": "Daughter of Gregory & Sandra Thorne",
        "eyebrow": "Written in Sand, Sealed by the Tide",
        "quote": "You are my compass, my anchor, and my ocean.",
        "closing": "Forever riding the waves of love with you.",
        "date_str": "Tuesday, 6th April 2027", "date_iso": "2027-04-06T17:30", "time_str": "5:30 PM",
        "venue": "Soneva Jani, Noonu Atoll, Maldives", "venue_addr": "Medhufaru Island, Noonu Atoll, Maldives",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#KaiMiaMaldives",
        "events": [
            {"name": "Dolphin Cruise Sunset", "date": "05 Apr 2027, 4:30 PM", "venue": "Lagoon Deck", "dress": "Resort Linen", "note": "Champagne & wild dolphin watching"},
            {"name": "Barefoot Sandbank Vows", "date": "06 Apr 2027, 5:30 PM", "venue": "Private Sandbank", "dress": "Island White", "note": "Barefoot ceremony at low tide"},
            {"name": "Overwater Cinema Dinner", "date": "06 Apr 2027, 8:00 PM", "venue": "Cinema Paradiso", "dress": "Smart Island Casual", "note": "Private dinner over the water"}
        ]
    },
    {
        "id": 21, "slug": "21-boho-chic-pampas", "name": "Boho Chic Pampas Sanctuary",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Warm Sienna Clay & Pampas Grass",
        "wine": "#9A3412", "wine_d": "#7C2D12", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#431407",
        "title": "Boho Wedding of Julian & Harper", "celebrants": "Julian & Harper", "subtitle": "Earthy Vibes, Macrame Arches & Eternal Promises",
        "c1_name": "Julian Miller", "c1_par": "Son of Anthony & Claire Miller",
        "c2_name": "Harper Wilde", "c2_par": "Daughter of Jonathan & Penelope Wilde",
        "eyebrow": "Wild Hearts Found Their Forever",
        "quote": "You are my wild soulmate and my greatest adventure.",
        "closing": "Rooted in love, blooming in joy.",
        "date_str": "Saturday, 22nd May 2027", "date_iso": "2027-05-22T17:00", "time_str": "5:00 PM",
        "venue": "Papaya Playa Project, Tulum", "venue_addr": "Km 4.5 Carretera Tulum-Boca Paila, 77780 Tulum, Mexico",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#JulianHarperTulum",
        "events": [
            {"name": "Copal Cleansing & Cocktails", "date": "21 May 2027, 6:00 PM", "venue": "Jungle Pavilion", "dress": "Boho Chic", "note": "Mezcal tasting & live acoustic guitar"},
            {"name": "Pampas Arch Vows", "date": "22 May 2027, 5:00 PM", "venue": "Beachfront Dunes", "dress": "Neutral Tones / Linen", "note": "Sunset exchange of rings"},
            {"name": "Moonlit Jungle Feast", "date": "22 May 2027, 7:30 PM", "venue": "Palapa Deck", "dress": "Barefoot Elegance", "note": "Organic dining & dancing by torches"}
        ]
    },
    {
        "id": 22, "slug": "22-art-deco-gatsby", "name": "Art Deco Gatsby Glamour",
        "category": "Wedding", "category_key": "wedding", "palette_name": "Onyx Black & Gilded Filigree",
        "wine": "#18181B", "wine_d": "#09090B", "rose": "#CA8A04", "rose_d": "#A16207",
        "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FAFAFA", "blush2": "#F4F4F5", "ivory": "#FFFFFF", "ink": "#18181B",
        "title": "Gatsby Wedding of Vincent & Genevieve", "celebrants": "Vincent & Genevieve", "subtitle": "Roaring 1920s Gilded Glamour at The Plaza",
        "c1_name": "Vincent De Luca", "c1_par": "Son of Francis & Evelyn De Luca",
        "c2_name": "Genevieve Fontaine", "c2_par": "Daughter of Jean-Luc & Vivienne Fontaine",
        "eyebrow": "A Little Party Never Killed Nobody",
        "quote": "He looked at her the way all women want to be looked at by a man.",
        "closing": "To the green light, to golden nights, to forever.",
        "date_str": "Saturday, 30th October 2027", "date_iso": "2027-10-30T19:30", "time_str": "7:30 PM",
        "venue": "The Plaza Hotel Grand Ballroom, NYC", "venue_addr": "768 5th Ave, New York, NY 10019",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#TheGreatDeLucaWedding",
        "events": [
            {"name": "Prohibition Speakeasy Welcome", "date": "29 Oct 2027, 8:00 PM", "venue": "The Rose Club", "dress": "1920s Flapper & Tuxedo", "note": "Martinis & live trumpet quartet"},
            {"name": "Gilded Arch Vows", "date": "30 Oct 2027, 7:30 PM", "venue": "Grand Ballroom", "dress": "Strictly Black Tie", "note": "Exchange of vows"},
            {"name": "Midnight Champagne Tower", "date": "30 Oct 2027, 9:30 PM", "venue": "Terrace Room", "dress": "Glamour Gowns", "note": "7-tier champagne tower & swing band"}
        ]
    },

    # 23-32: Engagement & Ring Ceremonies
    {
        "id": 23, "slug": "23-starlight-promise", "name": "Starlight Promise Engagement",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Midnight Navy & Constellation Gold",
        "wine": "#0F172A", "wine_d": "#020617", "rose": "#38BDF8", "rose_d": "#0284C7",
        "gold": "#F59E0B", "gold_l": "#FDE68A", "blush": "#F8FAFC", "blush2": "#E2E8F0", "ivory": "#0B132B", "ink": "#F8FAFC",
        "title": "Engagement of Kabir & Tara", "celebrants": "Kabir & Tara", "subtitle": "A Diamond Spark That Began an Eternity",
        "c1_name": "Kabir Singhania", "c1_par": "Son of Mr. Devendra & Mrs. Sunita Singhania",
        "c2_name": "Tara Raichand", "c2_par": "Daughter of Mr. Harsh & Mrs. Gayatri Raichand",
        "eyebrow": "Written in the Stars Above",
        "quote": "It was always you — from this moment until forever.",
        "closing": "Under a billion stars, she said yes.",
        "date_str": "Friday, 18th December 2026", "date_iso": "2026-12-18T19:30", "time_str": "7:30 PM",
        "venue": "Taj Lake Palace, Udaipur", "venue_addr": "Pichola, Udaipur, Rajasthan 313001",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "stars", "music": "piano", "hashtag": "#TaraFoundHerKabir",
        "events": [
            {"name": "Sunset Champagne Toast", "date": "18 Dec 2026, 6:00 PM", "venue": "Lakeside Deck", "dress": "Cocktail Glam", "note": "Welcome drinks & violin quartet"},
            {"name": "The Ring Exchange Ceremony", "date": "18 Dec 2026, 7:30 PM", "venue": "Crystal Pavilion", "dress": "Black Tie / Evening Gown", "note": "Auspicious exchange of rings"},
            {"name": "Gala Dinner & DJ", "date": "18 Dec 2026, 9:00 PM", "venue": "Durbar Courtyard", "dress": "Celebration Wear", "note": "Banquet dinner & dancing"}
        ]
    },
    {
        "id": 24, "slug": "24-champagne-toast", "name": "Champagne Toast Ring Ceremony",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Effervescent Champagne & Silk",
        "wine": "#581C87", "wine_d": "#3B0764", "rose": "#A855F7", "rose_d": "#9333EA",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCF9FF", "ink": "#2E1065",
        "title": "Engagement of Neil & Riya", "celebrants": "Neil & Riya", "subtitle": "Pour the Champagne, We're Getting Married!",
        "c1_name": "Neil Kapoor", "c1_par": "Son of Mr. Anil & Mrs. Sunita Kapoor",
        "c2_name": "Riya Mehra", "c2_par": "Daughter of Mr. Sanjay & Mrs. Neeta Mehra",
        "eyebrow": "Join Us to Raise a Glass of Joy",
        "quote": "Two hearts, one toast, and a lifetime of shared dreams.",
        "closing": "Cheers to love, laughter and happily ever after.",
        "date_str": "Saturday, 9th January 2027", "date_iso": "2027-01-09T20:00", "time_str": "8:00 PM",
        "venue": "The St. Regis Grand Ballroom, Mumbai", "venue_addr": "462 Senapati Bapat Marg, Lower Parel, Mumbai 400013",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#NeilRiyaToast",
        "events": [
            {"name": "Red Carpet Welcome", "date": "09 Jan 2027, 8:00 PM", "venue": "Astor Foyer", "dress": "Gala Glamour", "note": "Signature cocktails & saxophone"},
            {"name": "Ring Ceremony & Cake Toast", "date": "09 Jan 2027, 9:15 PM", "venue": "Imperial Ballroom", "dress": "Evening Best", "note": "Ring exchange & champagne pop"},
            {"name": "Dance Floor & Dinner", "date": "09 Jan 2027, 10:15 PM", "venue": "Grand Hall", "dress": "Party Chic", "note": "DJ set & gourmet dining"}
        ]
    },
    {
        "id": 25, "slug": "25-rose-gold-elegance", "name": "Rose Gold Geometric Sparkle",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Rose Gold & Dusty Blush",
        "wine": "#9D174D", "wine_d": "#700A34", "rose": "#F43F5E", "rose_d": "#E11D48",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFB", "ink": "#4C0519",
        "title": "Engagement of Aryan & Shanaya", "celebrants": "Aryan & Shanaya", "subtitle": "A Modern Symphony of Rose Gold & Diamonds",
        "c1_name": "Aryan Khanna", "c1_par": "Son of Mr. Rajesh & Mrs. Poonam Khanna",
        "c2_name": "Shanaya Oberoi", "c2_par": "Daughter of Mr. Vivek & Mrs. Simi Oberoi",
        "eyebrow": "The Journey of Forever Commences",
        "quote": "Every love story is beautiful, but ours is my favorite.",
        "closing": "Sparkling brighter together than we ever could alone.",
        "date_str": "Sunday, 14th February 2027", "date_iso": "2027-02-14T19:00", "time_str": "7:00 PM",
        "venue": "Fairmont Palace, Jaipur", "venue_addr": "2, RIICO Kukas, Jaipur, Rajasthan 302028",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#AryanShanayaEngaged",
        "events": [
            {"name": "Sunset Cocktail Hour", "date": "14 Feb 2027, 6:00 PM", "venue": "Aravalli Terrace", "dress": "Rose Gold / Black Tie", "note": "Harpist and signature canapés"},
            {"name": "Ring Exchange & Vows", "date": "14 Feb 2027, 7:30 PM", "venue": "Royal Pavilion", "dress": "Evening Gown & Tuxedo", "note": "Sparkler walkway & ring reveal"},
            {"name": "Gala Dinner Celebration", "date": "14 Feb 2027, 9:00 PM", "venue": "Grand Ballroom", "dress": "Formal Glam", "note": "Live fusion band and dining"}
        ]
    },
    {
        "id": 26, "slug": "26-twilight-garden", "name": "Twilight Garden Fairy Lights",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Twilight Lavender & Fairy Gold",
        "wine": "#6B21A8", "wine_d": "#4C1D95", "rose": "#A855F7", "rose_d": "#9333EA",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCFAFF", "ink": "#2E1065",
        "title": "Engagement of Daniel & Maya", "celebrants": "Daniel & Maya", "subtitle": "Love Blooming Under Fairy Lights & Purple Dusk",
        "c1_name": "Daniel D'Souza", "c1_par": "Son of Francis & Maria D'Souza",
        "c2_name": "Maya Saxena", "c2_par": "Daughter of Pradeep & Vandana Saxena",
        "eyebrow": "Come Celebrate Under the Stars",
        "quote": "You have bewitched me, body and soul, and I love, I love, I love you.",
        "closing": "A fairy-tale romance written in real life.",
        "date_str": "Friday, 26th March 2027", "date_iso": "2027-03-26T18:30", "time_str": "6:30 PM",
        "venue": "Lodhi Gardens Pavilion, New Delhi", "venue_addr": "Lodhi Rd, New Delhi 110003",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#DanMayaTwilight",
        "events": [
            {"name": "Garden Welcome", "date": "26 Mar 2027, 6:30 PM", "venue": "Bonsai Courtyard", "dress": "Garden Party Chic", "note": "Acoustic strings & mocktails"},
            {"name": "Ring Ceremony", "date": "26 Mar 2027, 7:45 PM", "venue": "Rose Arbor", "dress": "Lavender & Pastels", "note": "Exchange of rings"},
            {"name": "Candlelight Dinner", "date": "26 Mar 2027, 9:00 PM", "venue": "Main Lawn", "dress": "Elegant Evening", "note": "Buffet under the stars"}
        ]
    },
    {
        "id": 27, "slug": "27-solitaire-sparkle", "name": "Solitaire Sparkle Ring Box",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Obsidian Mirror & Platinum Sparkle",
        "wine": "#09090B", "wine_d": "#000000", "rose": "#64748B", "rose_d": "#475569",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F8FAFC", "blush2": "#E2E8F0", "ivory": "#FFFFFF", "ink": "#09090B",
        "title": "Engagement of Yash & Natasha", "celebrants": "Yash & Natasha", "subtitle": "A Timeless Diamond for an Eternal Bond",
        "c1_name": "Yash Vardhan", "c1_par": "Son of Mr. Alok & Mrs. Madhuri Vardhan",
        "c2_name": "Natasha Poonawalla", "c2_par": "Daughter of Mr. Cyrus & Mrs. Natasha Poonawalla",
        "eyebrow": "She Said Yes! Join Us to Celebrate",
        "quote": "Diamonds are eternal, but our love will outshine them all.",
        "closing": "Forever locked in the sparkle of your eyes.",
        "date_str": "Saturday, 17th April 2027", "date_iso": "2027-04-17T19:30", "time_str": "7:30 PM",
        "venue": "Alila Diwa Resort, Goa", "venue_addr": "48/10 Adao Waddo, Majorda, Goa 403713",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#YashGotTash",
        "events": [
            {"name": "Sunset Deck Party", "date": "16 Apr 2027, 5:30 PM", "venue": "Edge Bar Lawn", "dress": "Resort Glam", "note": "Cocktails with Goan breeze"},
            {"name": "Ring Ceremony & Cake", "date": "17 Apr 2027, 7:30 PM", "venue": "Banyan Courtyard", "dress": "Black Tie / Sparkles", "note": "Unveiling the solitaire"},
            {"name": "Beachside Afterparty", "date": "17 Apr 2027, 9:30 PM", "venue": "Majorda Beachfront", "dress": "Party Wear", "note": "DJ by the ocean"}
        ]
    },
    {
        "id": 28, "slug": "28-eternal-knot", "name": "Eternal Infinity Knot",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Vedic Gold & Sage Pearl",
        "wine": "#166534", "wine_d": "#14532D", "rose": "#15803D", "rose_d": "#166534",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDF4", "blush2": "#DCFCE7", "ivory": "#FAFFFA", "ink": "#052E16",
        "title": "Engagement of Vivaan & Ananya", "celebrants": "Vivaan & Ananya", "subtitle": "Two Destinies Tied with Sacred Infinity Threads",
        "c1_name": "Vivaan Reddy", "c1_par": "Son of Dr. K.S. & Mrs. Sunita Reddy",
        "c2_name": "Ananya Rao", "c2_par": "Daughter of Justice V. & Mrs. Lalitha Rao",
        "eyebrow": "The Sacred Promise of Lifetime Companionship",
        "quote": "The soul recognizes its counterpoint in a single heartbeat.",
        "closing": "Bound by the eternal knot of trust and affection.",
        "date_str": "Sunday, 2nd May 2027", "date_iso": "2027-05-02T11:00", "time_str": "11:00 AM",
        "venue": "ITC Grand Chola, Chennai", "venue_addr": "63 Anna Salai, Guindy, Chennai 600032",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#VivaanAnanyaKnot",
        "events": [
            {"name": "Nischithartham (Puja)", "date": "02 May 2027, 10:00 AM", "venue": "Rajendra Hall", "dress": "Traditional Silk", "note": "Lagna Patrika reading & blessings"},
            {"name": "Ring Exchange Ceremony", "date": "02 May 2027, 11:30 AM", "venue": "Mandapam", "dress": "Festive Attire", "note": "Exchange of engagement rings"},
            {"name": "Grand Royal Lunch", "date": "02 May 2027, 12:45 PM", "venue": "Madras Pavilion", "dress": "Traditional Wear", "note": "Traditional South Indian feast"}
        ]
    },
    {
        "id": 29, "slug": "29-golden-hour-rooftop", "name": "Golden Hour Rooftop Engagement",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Amber Skyline & Warm Candlelight",
        "wine": "#7C2D12", "wine_d": "#431407", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#270B04",
        "title": "Engagement of Sameer & Tanya", "celebrants": "Sameer & Tanya", "subtitle": "As the City Lights Turn On, Forever Begins",
        "c1_name": "Sameer Mathur", "c1_par": "Son of Mr. Rajesh & Mrs. Saroj Mathur",
        "c2_name": "Tanya Bhatia", "c2_par": "Daughter of Mr. Alok & Mrs. Preeti Bhatia",
        "eyebrow": "Come Celebrate Our Golden Hour",
        "quote": "I want to be your favorite sunset and your sweetest sunrise.",
        "closing": "High above the world, our adventure takes flight.",
        "date_str": "Saturday, 20th February 2027", "date_iso": "2027-02-20T18:00", "time_str": "6:00 PM",
        "venue": "AER Lounge Rooftop, Four Seasons Mumbai", "venue_addr": "1/136, Dr E Moses Rd, Worli, Mumbai 400018",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#SameerTanyaGolden",
        "events": [
            {"name": "Sunset Skyline Cocktails", "date": "20 Feb 2027, 6:00 PM", "venue": "Rooftop Sky Bar", "dress": "Chic Cocktail", "note": "Skyline view & acoustic saxophone"},
            {"name": "Ring Ceremony at Twilight", "date": "20 Feb 2027, 7:15 PM", "venue": "Central Vista", "dress": "Glamorous Evening", "note": "Exchange of rings & sparklers"},
            {"name": "Rooftop Party & Dinner", "date": "20 Feb 2027, 8:30 PM", "venue": "Main Lounge", "dress": "Party Glam", "note": "DJ beats & pan-Asian feast"}
        ]
    },
    {
        "id": 30, "slug": "30-vintage-love-letters", "name": "Vintage Love Letters & Wax Seal",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Aged Parchment & Crimson Wax",
        "wine": "#7F1D1D", "wine_d": "#450A0A", "rose": "#991B1B", "rose_d": "#7F1D1D",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FEF2F2", "blush2": "#FEE2E2", "ivory": "#FFFDFD", "ink": "#350808",
        "title": "Engagement of Armaan & Zoya", "celebrants": "Armaan & Zoya", "subtitle": "A Love Written in Quill and Sealed by Fate",
        "c1_name": "Armaan Siddiqui", "c1_par": "Son of Nawabzada Tariq & Begum Yasmeen",
        "c2_name": "Zoya Mirza", "c2_par": "Daughter of Mr. Waseem & Mrs. Shabnam Mirza",
        "eyebrow": "From the Pages of Our Shared Diary",
        "quote": "Whatever our souls are made of, his and mine are the same.",
        "closing": "Sealed with a vow, delivered with love.",
        "date_str": "Saturday, 6th March 2027", "date_iso": "2027-03-06T18:00", "time_str": "6:00 PM",
        "venue": "Glenburn Tea Estate, Darjeeling", "venue_addr": "Near Singritan, Darjeeling, West Bengal 734101",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#ArmaanZoyaStory",
        "events": [
            {"name": "High Tea on the Lawn", "date": "06 Mar 2027, 4:00 PM", "venue": "Glenburn Veranda", "dress": "Vintage Pastels", "note": "First flush tea & scones"},
            {"name": "Ring Ceremony & Poetry", "date": "06 Mar 2027, 6:00 PM", "venue": "Kanchenjunga Lawn", "dress": "Classic Evening", "note": "Reading vows & exchanging rings"},
            {"name": "Bonfire Dinner & Ghazals", "date": "06 Mar 2027, 8:00 PM", "venue": "Garden Pavilions", "dress": "Warm Elegance", "note": "Live sitar, bonfire and dining"}
        ]
    },
    {
        "id": 31, "slug": "31-velvet-romance", "name": "Velvet Romance & Candlelight",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Mulberry Velvet & Antique Bronze",
        "wine": "#581C87", "wine_d": "#3B0764", "rose": "#831843", "rose_d": "#500724",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCF9FF", "ink": "#2E1065",
        "title": "Engagement of Raghav & Radhika", "celebrants": "Raghav & Radhika", "subtitle": "A Candlelit Royal Evening at Taj Falaknuma",
        "c1_name": "Raghav Reddy", "c1_par": "Son of Mr. Pratap & Mrs. Shailaja Reddy",
        "c2_name": "Radhika Rao", "c2_par": "Daughter of Dr. Arvind & Mrs. Nalini Rao",
        "eyebrow": "A Regal Engagement in the City of Pearls",
        "quote": "Two souls intertwined like fine velvet, warm and everlasting.",
        "closing": "Tonight we promise forever.",
        "date_str": "Saturday, 27th February 2027", "date_iso": "2027-02-27T19:30", "time_str": "7:30 PM",
        "venue": "Taj Falaknuma Palace, Hyderabad", "venue_addr": "Engine Bowli, Fatima Nagar, Falaknuma, Hyderabad 500053",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "lanterns", "music": "sitar", "hashtag": "#RaghavRadhikaPalace",
        "events": [
            {"name": "Royal Horse Carriage Entry", "date": "27 Feb 2027, 7:00 PM", "venue": "Grand Palace Gates", "dress": "Nizami Elegance", "note": "Floral welcome & rose water"},
            {"name": "Ring Ceremony & Toast", "date": "27 Feb 2027, 8:15 PM", "venue": "101 Dining Hall", "dress": "Black Tie / Royal Ethnic", "note": "Ring exchange & champagne toast"},
            {"name": "Sufi Symphony & Feast", "date": "27 Feb 2027, 9:30 PM", "venue": "Gol Bungalow Terrace", "dress": "Regal Glamour", "note": "Sufi live band & Biryani banquet"}
        ]
    },
    {
        "id": 32, "slug": "32-cocktail-symphony", "name": "Cocktail Symphony & Jazz",
        "category": "Engagement", "category_key": "engagement", "palette_name": "Smoky Plum & Brass Accents",
        "wine": "#4C1D95", "wine_d": "#2E1065", "rose": "#7C3AED", "rose_d": "#6D28D9",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F5F3FF", "blush2": "#EDE9FE", "ivory": "#FAF8FF", "ink": "#1E1B4B",
        "title": "Engagement of Dhruv & Alisha", "celebrants": "Dhruv & Alisha", "subtitle": "Smooth Jazz, Signature Cocktails & Sweet Promises",
        "c1_name": "Dhruv Mehra", "c1_par": "Son of Mr. Vikram & Mrs. Meenakshi Mehra",
        "c2_name": "Alisha Vohra", "c2_par": "Daughter of Mr. Rohit & Mrs. Tina Vohra",
        "eyebrow": "Let's Get This Party Started!",
        "quote": "Love is the rhythm that makes our two hearts dance in harmony.",
        "closing": "To the rhythm of love and good times ahead.",
        "date_str": "Friday, 12th March 2027", "date_iso": "2027-03-12T20:00", "time_str": "8:00 PM",
        "venue": "Soho House Juhu, Mumbai", "venue_addr": "16 Juhu Tara Rd, Santa Cruz West, Mumbai 400049",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#DhruvAlishaGroove",
        "events": [
            {"name": "Speakeasy Welcome", "date": "12 Mar 2027, 8:00 PM", "venue": "Eva Bar", "dress": "Chic Cocktail", "note": "Craft cocktails & jazz trio"},
            {"name": "Ring Reveal & Speeches", "date": "12 Mar 2027, 9:15 PM", "venue": "Cinema Hall", "dress": "Glam Nightwear", "note": "Ring exchange & family roast"},
            {"name": "Rooftop Poolside Dance", "date": "12 Mar 2027, 10:30 PM", "venue": "Rooftop Pool", "dress": "Party Wear", "note": "DJ by the pool overlooking the sea"}
        ]
    },

    # 33-42: Baby Shower & Godh Bharai
    {
        "id": 33, "slug": "33-pastel-clouds-dream", "name": "Pastel Clouds & Starry Dream",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Cloud Pink & Sky Blue",
        "wine": "#DB2777", "wine_d": "#9D174D", "rose": "#0284C7", "rose_d": "#0369A1",
        "gold": "#F59E0B", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#E0F2FE", "ivory": "#FFFFFF", "ink": "#1E293B",
        "title": "Baby Shower for Maya & Arjun", "celebrants": "Welcoming Baby Sharma", "subtitle": "A Little Miracle is On The Way!",
        "c1_name": "Arjun Sharma", "c1_par": "Father-to-be (Son of Mr. R.K. & Mrs. Sarita Sharma)",
        "c2_name": "Maya Sharma", "c2_par": "Mother-to-be (Daughter of Mr. Ashok & Mrs. Rekha Verma)",
        "eyebrow": "Overflowing with Love & Anticipation",
        "quote": "Ten little fingers, ten little toes — with love and grace our family grows.",
        "closing": "A baby fills a place in your heart that you never knew was empty.",
        "date_str": "Sunday, 24th January 2027", "date_iso": "2027-01-24T15:30", "time_str": "3:30 PM",
        "venue": "The Oberoi Udaivilas, Udaipur", "venue_addr": "Haridas Ji Ki Magri, Udaipur 313001",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#BabySharmaOnTheWay",
        "events": [
            {"name": "Godh Bharai Blessings", "date": "24 Jan 2027, 3:30 PM", "venue": "Lawn Courtyard", "dress": "Pastel Pink or Blue", "note": "Flower shower & auspicious mantras"},
            {"name": "Fun Baby Games & Trivia", "date": "24 Jan 2027, 5:00 PM", "venue": "Lotus Lounge", "dress": "Pastel Chic", "note": "Guess the baby arrival date & prizes!"},
            {"name": "Cake Cutting & Feast", "date": "24 Jan 2027, 6:30 PM", "venue": "Grand Hall", "dress": "Comfortable Semi-Formal", "note": "High tea & sweet delights"}
        ]
    },
    {
        "id": 34, "slug": "34-teddy-bear-picnic", "name": "Teddy Bear Honey Picnic",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Honey Gold & Gingham Brown",
        "wine": "#78350F", "wine_d": "#451A03", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#451A03",
        "title": "Baby Shower for Priyanshu & Anjali", "celebrants": "We Can Bearly Wait!", "subtitle": "A Sweet Celebration for Our Upcoming Honey Bun",
        "c1_name": "Priyanshu Roy", "c1_par": "Proud Dad-to-be",
        "c2_name": "Anjali Roy", "c2_par": "Glowing Mom-to-be",
        "eyebrow": "A New Adventure Begins",
        "quote": "Sometimes the smallest things take up the most room in your heart. — Winnie the Pooh",
        "closing": "Warm cuddles and honey smiles await.",
        "date_str": "Saturday, 13th February 2027", "date_iso": "2027-02-13T16:00", "time_str": "4:00 PM",
        "venue": "Rosewood Manor Gardens, Bengaluru", "venue_addr": "Whitefield Main Rd, Bengaluru 560066",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#BearlyWaitRoy",
        "events": [
            {"name": "Honey Tea & Welcome", "date": "13 Feb 2027, 4:00 PM", "venue": "Manor Veranda", "dress": "Brown & Cream Gingham", "note": "Honey scones and fruit tea"},
            {"name": "Teddy Bear Baby Games", "date": "13 Feb 2027, 5:15 PM", "venue": "Picnic Lawn", "dress": "Warm Neutrals", "note": "Baby bingo and diaper toss"},
            {"name": "Celebration Dinner", "date": "13 Feb 2027, 7:00 PM", "venue": "Garden Pavilion", "dress": "Smart Casual", "note": "Artisanal dinner & dessert table"}
        ]
    },
    {
        "id": 35, "slug": "35-safari-little-cub", "name": "Safari Little Lion Cub",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Jungle Mint & Sunlit Ochre",
        "wine": "#14532D", "wine_d": "#052E16", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDF4", "blush2": "#DCFCE7", "ivory": "#FAFFFA", "ink": "#022C22",
        "title": "Baby Shower for Vikram & Sneha", "celebrants": "Welcome Our Little Cub!", "subtitle": "Born to Be Wild and Loved Beyond Measure",
        "c1_name": "Vikram Saxena", "c1_par": "Future Papa Bear",
        "c2_name": "Sneha Saxena", "c2_par": "Radiant Mama Lion",
        "eyebrow": "A Wild Blessing is on the Way",
        "quote": "You are our greatest adventure, little cub.",
        "closing": "May courage and kindness follow you wherever you roar.",
        "date_str": "Sunday, 7th March 2027", "date_iso": "2027-03-07T15:00", "time_str": "3:00 PM",
        "venue": "Emerald Park Pavilion, Pune", "venue_addr": "Koregaon Park Annexe, Pune 411036",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#LittleCubSaxena",
        "events": [
            {"name": "Jungle Welcome & Mocktails", "date": "07 Mar 2027, 3:00 PM", "venue": "Safari Gazebo", "dress": "Sage Green & Khaki", "note": "Tropical smoothies & treats"},
            {"name": "Safari Games & Wishing Tree", "date": "07 Mar 2027, 4:15 PM", "venue": "Main Lawn", "dress": "Safari Chic", "note": "Write advice for the little cub"},
            {"name": "Cake Cutting Celebration", "date": "07 Mar 2027, 6:00 PM", "venue": "Pavilion Hall", "dress": "Casual Festive", "note": "Lion cub themed cake & dinner"}
        ]
    },
    {
        "id": 36, "slug": "36-woodland-whimsy", "name": "Woodland Whimsical Forest",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Forest Moss & Golden Acorns",
        "wine": "#1E3A1E", "wine_d": "#0F200F", "rose": "#4D7C0F", "rose_d": "#365314",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F7FEE7", "blush2": "#ECFCCB", "ivory": "#FCFFF7", "ink": "#142514",
        "title": "Baby Shower for Ryan & Emily", "celebrants": "A Woodland Fairy Miracle", "subtitle": "Gentle Fawns, Whispering Pines & Baby Smiles",
        "c1_name": "Ryan Miller", "c1_par": "Father-to-be",
        "c2_name": "Emily Miller", "c2_par": "Mother-to-be",
        "eyebrow": "From Tiny Acorns Mighty Oaks Do Grow",
        "quote": "Such a big miracle in such a tiny little soul.",
        "closing": "May your life be filled with wonder and forest magic.",
        "date_str": "Saturday, 20th March 2027", "date_iso": "2027-03-20T14:30", "time_str": "2:30 PM",
        "venue": "Pinecrest Lodge, Manali", "venue_addr": "Club House Rd, Old Manali, HP 175131",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#WoodlandBabyMiller",
        "events": [
            {"name": "Forest Berry Punch & Treats", "date": "20 Mar 2027, 2:30 PM", "venue": "Woodland Porch", "dress": "Earthy Tones", "note": "Fresh berries & warm cider"},
            {"name": "Fawn Games & Diaper Raffle", "date": "20 Mar 2027, 3:45 PM", "venue": "Pine Courtyard", "dress": "Woodland Casual", "note": "Woodland crafts and trivia"},
            {"name": "Hearty Mountain High Tea", "date": "20 Mar 2027, 5:30 PM", "venue": "Fireplace Hall", "dress": "Warm Festive", "note": "Artisanal cheeses and pastries"}
        ]
    },
    {
        "id": 37, "slug": "37-celestial-stork", "name": "Celestial Stork Delivery",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Night Sky Blue & Stork Gold",
        "wine": "#1E3A8A", "wine_d": "#172554", "rose": "#38BDF8", "rose_d": "#0284C7",
        "gold": "#F59E0B", "gold_l": "#FDE68A", "blush": "#EFF6FF", "blush2": "#DBEAFE", "ivory": "#F8FAFC", "ink": "#0F172A",
        "title": "Baby Shower for Varun & Kirti", "celebrants": "Special Delivery from the Stars", "subtitle": "A Precious Bundle of Joy Floating Down from Heaven",
        "c1_name": "Varun Grover", "c1_par": "Father-to-be",
        "c2_name": "Kirti Grover", "c2_par": "Mother-to-be",
        "eyebrow": "Delivered with Love & Infinite Wonder",
        "quote": "When we wished upon a star, our dream came true in you.",
        "closing": "Your tiny wings have already touched our hearts.",
        "date_str": "Sunday, 11th April 2027", "date_iso": "2027-04-11T16:00", "time_str": "4:00 PM",
        "venue": "Grand Hyatt Courtyard, New Delhi", "venue_addr": "Vasant Kunj Phase II, Nelson Mandela Marg, New Delhi 110070",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "call", "ambient": "stars", "music": "piano", "hashtag": "#StorkBringsGroverBaby",
        "events": [
            {"name": "Welcome Clouds & Cocktails", "date": "11 Apr 2027, 4:00 PM", "venue": "Skyline Garden", "dress": "White & Gold / Blue", "note": "Cotton candy drinks and macarons"},
            {"name": "Stork Delivery Games", "date": "11 Apr 2027, 5:15 PM", "venue": "Crystal Lounge", "dress": "Semi-Formal", "note": "Guess the baby arrival weight!"},
            {"name": "Evening Starlight Banquet", "date": "11 Apr 2027, 7:00 PM", "venue": "Grand Dining Lawn", "dress": "Evening Chic", "note": "Multi-course celebration dinner"}
        ]
    },
    {
        "id": 38, "slug": "38-traditional-godh-bharai", "name": "Traditional Godh Bharai Blessing",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Green Glass Bangles & Marigold",
        "wine": "#166534", "wine_d": "#14532D", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#052E16",
        "title": "Godh Bharai of Pooja & Abhishek", "celebrants": "Auspicious Godh Bharai Sanskar", "subtitle": "Showering the Expectant Mother with Elders' Blessings",
        "c1_name": "Abhishek Joshi", "c1_par": "Son of Sh. Harish & Smt. Urmila Joshi",
        "c2_name": "Pooja Joshi", "c2_par": "Daughter of Sh. Kailash & Smt. Sharda Sharma",
        "eyebrow": "॥ Shubh Garbhadhan Blessings ॥",
        "quote": "A mother's lap is filled with sacred fruits, coins, and eternal love.",
        "closing": "May the newborn bring health, wisdom, and joy to the family.",
        "date_str": "Saturday, 24th April 2027", "date_iso": "2027-04-24T11:00", "time_str": "11:00 AM",
        "venue": "Heritage Haveli Courtyard, Jaipur", "venue_addr": "Amer Road, Jaipur 302002",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#PoojaKiGodhBharai",
        "events": [
            {"name": "Vedic Garbha Puja", "date": "24 Apr 2027, 10:30 AM", "venue": "Puja Sthal", "dress": "Traditional Saree", "note": "Maha Lakshmi and Gauri prayers"},
            {"name": "Godh Bharai & Choodi Rasam", "date": "24 Apr 2027, 11:30 AM", "venue": "Main Courtyard", "dress": "Green & Yellow Attire", "note": "Filling the lap with dry fruits & bangles"},
            {"name": "Sattvik Mahaprasad Feast", "date": "24 Apr 2027, 1:00 PM", "venue": "Bhojan Shala", "dress": "Comfortable Festive", "note": "Traditional 56 bhog sweets"}
        ]
    },
    {
        "id": 39, "slug": "39-sweet-lullaby-cradle", "name": "Sweet Lullaby Golden Cradle",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Lavender Mist & Gold Ribbon",
        "wine": "#6B21A8", "wine_d": "#4C1D95", "rose": "#A855F7", "rose_d": "#9333EA",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCFAFF", "ink": "#2E1065",
        "title": "Baby Shower for Kunal & Divya", "celebrants": "Rocking the Cradle of Love", "subtitle": "Sweet Dreams, Gentle Lullabies & Tender Kisses",
        "c1_name": "Kunal Bansal", "c1_par": "Excited Dad",
        "c2_name": "Divya Bansal", "c2_par": "Beautiful Mom-to-be",
        "eyebrow": "Hush Little Baby, You are So Loved",
        "quote": "Sleep tight, little dream; wake up to our open arms.",
        "closing": "Your cradle is ready, and our hearts are yours forever.",
        "date_str": "Sunday, 9th May 2027", "date_iso": "2027-05-09T16:00", "time_str": "4:00 PM",
        "venue": "Magnolia Gardens, Chandigarh", "venue_addr": "Sector 10, Chandigarh 160011",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#DivyaKunalBabyShower",
        "events": [
            {"name": "Lullaby High Tea", "date": "09 May 2027, 4:00 PM", "venue": "The Rose Gazebo", "dress": "Pastel Lavender & White", "note": "Lavender iced tea and macarons"},
            {"name": "Cradle Blessing & Games", "date": "09 May 2027, 5:15 PM", "venue": "Lawn Pavilion", "dress": "Garden Casual", "note": "Decorate the golden cradle"},
            {"name": "Sunset Feast & Sweets", "date": "09 May 2027, 6:45 PM", "venue": "Main Veranda", "dress": "Semi-Formal", "note": "Artisanal desserts and gourmet buffet"}
        ]
    },
    {
        "id": 40, "slug": "40-boho-baby-sunflower", "name": "Boho Baby Sunflower Sunshine",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Sunflower Ochre & Linen Cream",
        "wine": "#9A3412", "wine_d": "#7C2D12", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#431407",
        "title": "Baby Shower for Nikhil & Tanya", "celebrants": "Here Comes Our Sunshine!", "subtitle": "Bright Blooms, Warm Laughter & Golden Days",
        "c1_name": "Nikhil Kapoor", "c1_par": "Dad-to-be",
        "c2_name": "Tanya Kapoor", "c2_par": "Mom-to-be",
        "eyebrow": "You are My Sunshine, My Only Sunshine",
        "quote": "Keep your face always toward the sunshine, and shadows will fall behind you.",
        "closing": "Brightening our world in every possible way.",
        "date_str": "Saturday, 22nd May 2027", "date_iso": "2027-05-22T15:30", "time_str": "3:30 PM",
        "venue": "Sunburst Meadows, Gurugram", "venue_addr": "Sohna Road, Gurugram 122103",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#SunshineKapoorBaby",
        "events": [
            {"name": "Lemonade & Sunflower Bar", "date": "22 May 2027, 3:30 PM", "venue": "Meadow Deck", "dress": "Yellow & White Linen", "note": "Fresh lemonades and berry tartlets"},
            {"name": "Sunflower Wreath & Trivia", "date": "22 May 2027, 4:45 PM", "venue": "Open Lawn", "dress": "Boho Chic", "note": "DIY floral crown & baby name suggestions"},
            {"name": "Barbecue & Evening Feast", "date": "22 May 2027, 6:30 PM", "venue": "Barn House", "dress": "Casual", "note": "Farm-to-table dining under string lights"}
        ]
    },
    {
        "id": 41, "slug": "41-ocean-baby-whale", "name": "Ocean Whale Splash",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Seafoam Teal & Bubbly Blue",
        "wine": "#0E7490", "wine_d": "#155E75", "rose": "#0284C7", "rose_d": "#0369A1",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#ECFEFF", "blush2": "#CFFAFE", "ivory": "#FAFFFF", "ink": "#083344",
        "title": "Baby Shower for Aakash & Rhea", "celebrants": "A Whale of a Time Awaits!", "subtitle": "Splashing Into Parenthood with Hearts Full of Joy",
        "c1_name": "Aakash Mehta", "c1_par": "Captain Dad",
        "c2_name": "Rhea Mehta", "c2_par": "Mermaid Mom",
        "eyebrow": "Our Little Sailor is Dropping Anchor Soon",
        "quote": "May your dreams be as vast as the ocean and your laughter as bubbly as the sea.",
        "closing": "Anchored forever in unconditional love.",
        "date_str": "Sunday, 6th June 2027", "date_iso": "2027-06-06T16:00", "time_str": "4:00 PM",
        "venue": "Marine Terrace, Alibaug", "venue_addr": "Varsoli Beach Rd, Alibaug, Maharashtra 402201",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#WhaleWelcomeMehta",
        "events": [
            {"name": "Sea Breeze Welcome", "date": "06 Jun 2027, 4:00 PM", "venue": "Seaside Deck", "dress": "Nautical Navy & Sky Blue", "note": "Coconut water and coastal snacks"},
            {"name": "Oceanic Games & Quizzes", "date": "06 Jun 2027, 5:15 PM", "venue": "Beach Pavilion", "dress": "Beach Casual", "note": "Message in a bottle wishes"},
            {"name": "Seafood & Sundowner Dinner", "date": "06 Jun 2027, 7:00 PM", "venue": "Terrace Grill", "dress": "Resort Casual", "note": "Buffet dinner overlooking waves"}
        ]
    },
    {
        "id": 42, "slug": "42-hot-air-balloon-adventure", "name": "Hot Air Balloon Up & Away",
        "category": "Baby Shower", "category_key": "babyshower", "palette_name": "Pastel Cloud Balloon & Gold",
        "wine": "#0284C7", "wine_d": "#0369A1", "rose": "#DB2777", "rose_d": "#BE185D",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0F9FF", "blush2": "#E0F2FE", "ivory": "#FBFEFF", "ink": "#0C4A6E",
        "title": "Baby Shower for Manav & Shruti", "celebrants": "Up, Up & Away, Baby!", "subtitle": "Floating on Clouds of Wonder & Sweet Anticipation",
        "c1_name": "Manav Singhal", "c1_par": "Co-Pilot Dad",
        "c2_name": "Shruti Singhal", "c2_par": "Navigator Mom",
        "eyebrow": "Oh, The Places You'll Go!",
        "quote": "Soar high, dream big, and never lose your wonder.",
        "closing": "Your great adventure starts in our loving arms.",
        "date_str": "Saturday, 19th June 2027", "date_iso": "2027-06-19T15:00", "time_str": "3:00 PM",
        "venue": "Skyline Garden Pavilion, Hyderabad", "venue_addr": "Jubilee Hills, Road No. 36, Hyderabad 500033",
        "hero_img": "../assets/img/baby_hero.svg", "cover_img": "../assets/img/baby_cover.svg",
        "c1_img": "../assets/img/baby_hero.svg", "c2_img": "../assets/img/baby_cover.svg",
        "opening_style": "envelope", "ambient": "lanterns", "music": "piano", "hashtag": "#UpAndAwaySinghal",
        "events": [
            {"name": "Cloud Nine Punch & Desserts", "date": "19 Jun 2027, 3:00 PM", "venue": "Sky Gazebo", "dress": "Pastel Striped", "note": "Cupcakes and cloud smoothies"},
            {"name": "Balloon Wishes & Baby Bingo", "date": "19 Jun 2027, 4:15 PM", "venue": "Lawn Stage", "dress": "Comfortable Chic", "note": "Tie your wishes to mini balloons"},
            {"name": "Gourmet High Tea Feast", "date": "19 Jun 2027, 6:00 PM", "venue": "Grand Hall", "dress": "Semi-Formal", "note": "High tea dining and gifts"}
        ]
    },

    # 43-50: Birthday Celebrations & Milestones
    {
        "id": 43, "slug": "43-golden-jubilee-glam", "name": "Golden Jubilee 50th Birthday Glam",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Black Tie 24K Gold Foil",
        "wine": "#18181B", "wine_d": "#09090B", "rose": "#CA8A04", "rose_d": "#A16207",
        "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FAFAFA", "blush2": "#F4F4F5", "ivory": "#FFFFFF", "ink": "#18181B",
        "title": "50th Birthday Gala of Vikram Singhania", "celebrants": "Vikram Singhania", "subtitle": "Celebrating 50 Magnificent Years of Wisdom & Success",
        "c1_name": "Vikram Singhania", "c1_par": "Hosted with adoration by Sunita, Rohan & Ananya",
        "c2_name": "Golden 50th Milestone", "c2_par": "An evening of memories, champagne, and music",
        "eyebrow": "A Half-Century of Greatness & Elegance",
        "quote": "Count your life by smiles, not tears. Count your age by friends, not years.",
        "closing": "Cheers to 50 fabulous years and the brilliant journey ahead!",
        "date_str": "Saturday, 27th March 2027", "date_iso": "2027-03-27T20:00", "time_str": "8:00 PM",
        "venue": "The Taj Mahal Palace, Mumbai", "venue_addr": "Apollo Bunder, Colaba, Mumbai 400001",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#VikramTurns50",
        "events": [
            {"name": "Red Carpet Welcome & Cocktails", "date": "27 Mar 2027, 8:00 PM", "venue": "Gateway Foyer", "dress": "Black Tie / Gold Gala", "note": "Vintage champagne & live harp"},
            {"name": "Milestone Tribute & Toast", "date": "27 Mar 2027, 9:15 PM", "venue": "Ballroom", "dress": "Formal Evening", "note": "Video documentary & cake cutting"},
            {"name": "Gala Dinner & Jazz Swing", "date": "27 Mar 2027, 10:15 PM", "venue": "Crystal Room", "dress": "Evening Best", "note": "Multi-course feast and dancing"}
        ]
    },
    {
        "id": 44, "slug": "44-neon-midnight-bash", "name": "Cyber Neon Midnight Birthday",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Neon Violet & Electric Cyan",
        "wine": "#581C87", "wine_d": "#3B0764", "rose": "#06B6D4", "rose_d": "#0891B2",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#09090B", "blush2": "#18181B", "ivory": "#000000", "ink": "#FAF5FF",
        "title": "21st Birthday Bash of Aryan Kapoor", "celebrants": "Aryan Kapoor", "subtitle": "Turning 21 in Cyber Neon Glow!",
        "c1_name": "Aryan Kapoor", "c1_par": "Hosted by The Kapoor Squad",
        "c2_name": "21st Birthday Riot", "c2_par": "Non-stop DJ beats, laser shows & cocktails",
        "eyebrow": "Level 21 Unlocked — Game On!",
        "quote": "Youth has no age, but 21 means the party just officially began.",
        "closing": "Dance like nobody's watching, glow until the sun rises.",
        "date_str": "Friday, 16th April 2027", "date_iso": "2027-04-16T22:00", "time_str": "10:00 PM",
        "venue": "Dragonfly Club, Aerocity, New Delhi", "venue_addr": "Worldmark 1, Aerocity, New Delhi 110037",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#Aryan21Glow",
        "events": [
            {"name": "Glow Bar Pre-Drinks", "date": "16 Apr 2027, 10:00 PM", "venue": "VIP Mezzanine", "dress": "Neon & Cyber Black", "note": "Neon face paint & glow sticks"},
            {"name": "Midnight Cake & Confetti Cannons", "date": "16 Apr 2027, 11:59 PM", "venue": "Main Dance Floor", "dress": "Club Chic", "note": "Giant LED cake drop"},
            {"name": "Till Sunrise DJ Set", "date": "17 Apr 2027, 1:00 AM", "venue": "Club Arena", "dress": "Rave Wear", "note": "Top electronic DJ sets"}
        ]
    },
    {
        "id": 45, "slug": "45-vintage-retro-disco", "name": "Retro Disco Ball 30th Birthday",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Mirror Disco & Sunset Flare",
        "wine": "#9D174D", "wine_d": "#700A34", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFB", "ink": "#4C0519",
        "title": "30th Birthday Soiree of Alia Merchant", "celebrants": "Alia Merchant", "subtitle": "Flirty, Thriving & Grooving Into the 30s!",
        "c1_name": "Alia Merchant", "c1_par": "Hosted by Kabir, Rhea & Besties",
        "c2_name": "Studio 54 Disco Vibe", "c2_par": "Sequins, bell-bottoms & disco hits",
        "eyebrow": "Saying Goodbye to My 20s in High Heels",
        "quote": "30 and fabulous — the best chapter begins right now.",
        "closing": "Keep on dancing under the disco light.",
        "date_str": "Saturday, 8th May 2027", "date_iso": "2027-05-08T20:30", "time_str": "8:30 PM",
        "venue": "Soho Sky Bar, Mumbai", "venue_addr": "Juhu Tara Rd, Mumbai 400049",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#AliaDirtyThirty",
        "events": [
            {"name": "Sparkling Prosecco Hour", "date": "08 May 2027, 8:30 PM", "venue": "Rooftop Deck", "dress": "Sequins, Silks & 70s Glam", "note": "Disco cocktails & glitter bar"},
            {"name": "Cake Cutting & Cheers", "date": "08 May 2027, 10:00 PM", "venue": "Disco Dome", "dress": "Glitter Best", "note": "Disco ball drop & cake"},
            {"name": "ABBA & Funk Dance Party", "date": "08 May 2027, 11:00 PM", "venue": "Mirror Floor", "dress": "Dance Party", "note": "Retro playlist and late-night tacos"}
        ]
    },
    {
        "id": 46, "slug": "46-sweet-sixteen-blush", "name": "Sweet Sixteen Princess Tiara",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Blush Pink & Crystal Tiara",
        "wine": "#9D174D", "wine_d": "#700A34", "rose": "#F43F5E", "rose_d": "#E11D48",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFB", "ink": "#4C0519",
        "title": "Sweet 16 of Ananya Verma", "celebrants": "Ananya Verma", "subtitle": "Crowning a Year of Sparkling Dreams & Radiance",
        "c1_name": "Ananya Verma", "c1_par": "Hosted with pride by Rajesh & Shalini Verma",
        "c2_name": "Sweet Sixteen Gala", "c2_par": "Tiaras, ballroom dancing and friends",
        "eyebrow": "A Princess Milestone Celebration",
        "quote": "Behind you, all your memories. Before you, all your dreams.",
        "closing": "May your 16th year shine as bright as your smile.",
        "date_str": "Sunday, 12th September 2027", "date_iso": "2027-09-12T18:00", "time_str": "6:00 PM",
        "venue": "The Imperial Ballroom, New Delhi", "venue_addr": "Janpath, Connaught Place, New Delhi 110001",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#AnanyaSweet16",
        "events": [
            {"name": "Princess Red Carpet", "date": "12 Sep 2027, 6:00 PM", "venue": "Grand Foyer", "dress": "Princess Pink & Suits", "note": "Photo booth & tiara station"},
            {"name": "Candle Lighting & 16 Vows", "date": "12 Sep 2027, 7:15 PM", "venue": "Royal Pavilion", "dress": "Ballroom Gowns", "note": "Traditional 16 candles ceremony"},
            {"name": "Dinner & Teen Dance Floor", "date": "12 Sep 2027, 8:30 PM", "venue": "Ballroom", "dress": "Party Glam", "note": "Mocktail bar and DJ hits"}
        ]
    },
    {
        "id": 47, "slug": "47-dirty-thirty-bourbon", "name": "Bourbon & Cigar 30th Birthday",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Whiskey Amber & Rich Leather",
        "wine": "#451A03", "wine_d": "#270B04", "rose": "#78350F", "rose_d": "#451A03",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#1E0D03",
        "title": "30th Birthday of Karan Mehra", "celebrants": "Karan Mehra", "subtitle": "Aged to Perfection — Welcome to the 30s Club",
        "c1_name": "Karan Mehra", "c1_par": "Hosted by The Boyz & Family",
        "c2_name": "Bourbon & Steaks Night", "c2_par": "Aged malts, prime cuts and hearty laughs",
        "eyebrow": "Fine Malts & Finer Friends",
        "quote": "Age is merely the number of years the world has been enjoying you.",
        "closing": "To 30 years of brotherhood, grit, and good times.",
        "date_str": "Saturday, 2nd October 2027", "date_iso": "2027-10-02T20:00", "time_str": "8:00 PM",
        "venue": "The Malt & Cigar Club, Bengaluru", "venue_addr": "UB City, Vittal Mallya Rd, Bengaluru 560001",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "envelope", "ambient": "confetti", "music": "piano", "hashtag": "#KaranTurns30",
        "events": [
            {"name": "Single Malt Tasting", "date": "02 Oct 2027, 8:00 PM", "venue": "Cask Room", "dress": "Smart Blazer & Loafers", "note": "Guided scotch tasting by master sommelier"},
            {"name": "Birthday Toast & Steak Dinner", "date": "02 Oct 2027, 9:30 PM", "venue": "Dining Veranda", "dress": "Smart Casual", "note": "Prime steaks, burgers and laughs"},
            {"name": "Poker & Cigar Lounge", "date": "02 Oct 2027, 11:00 PM", "venue": "Private Den", "dress": "Casual", "note": "Friendly poker tables & cuban cigars"}
        ]
    },
    {
        "id": 48, "slug": "48-first-birthday-wild-one", "name": "First Birthday Wild One Adventure",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Jungle Mint & Sun Gold",
        "wine": "#15803D", "wine_d": "#14532D", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDF4", "blush2": "#DCFCE7", "ivory": "#FAFFFA", "ink": "#052E16",
        "title": "1st Birthday of Little Yuvaan", "celebrants": "Yuvaan is ONE!", "subtitle": "365 Days of Sweet Smiles, First Steps & Joy",
        "c1_name": "Yuvaan Singhal", "c1_par": "Beloved Son of Aman & Riddhi Singhal",
        "c2_name": "The Wild One Safari", "c2_par": "Balloons, cake smashes and baby laughter",
        "eyebrow": "Our Little Prince Turns One!",
        "quote": "One year of you has changed our whole world forever.",
        "closing": "Little hands, big dreams, endless love.",
        "date_str": "Sunday, 15th August 2027", "date_iso": "2027-08-15T16:00", "time_str": "4:00 PM",
        "venue": "Sunshine Meadow Lawns, Pune", "venue_addr": "Baner Hills Rd, Pune 411045",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#YuvaanTurnsOne",
        "events": [
            {"name": "Animal Kingdom Play Zone", "date": "15 Aug 2027, 4:00 PM", "venue": "Inflatable Park", "dress": "Safari / Colorful Casual", "note": "Bouncy castle and baby ball pit"},
            {"name": "The Big Cake Smash", "date": "15 Aug 2027, 5:15 PM", "venue": "Central Canopy", "dress": "Cute & Festive", "note": "Yuvaan's epic first cake smash!"},
            {"name": "Family Feast & Magic Show", "date": "15 Aug 2027, 6:30 PM", "venue": "Main Lawn", "dress": "Casual", "note": "Live magician, cotton candy and dinner"}
        ]
    },
    {
        "id": 49, "slug": "49-fabulous-forty-rose", "name": "Fabulous Forty Rose Gold Gala",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Rose Gold & Champagne Shimmer",
        "wine": "#831843", "wine_d": "#500724", "rose": "#BE185D", "rose_d": "#9D174D",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FDF2F8", "blush2": "#FCE7F3", "ivory": "#FFFAFC", "ink": "#380619",
        "title": "40th Birthday of Shalini Gupta", "celebrants": "Shalini Gupta", "subtitle": "40 Never Looked So Fabulous & Radiant",
        "c1_name": "Shalini Gupta", "c1_par": "Celebrated with love by Rajiv, Aryan & Friends",
        "c2_name": "Fabulous 40th Soiree", "c2_par": "Champagne toasts, laughter and glamorous dancing",
        "eyebrow": "Life Begins at Forty",
        "quote": "Forty is the old age of youth and the youth of old age — live it fiercely!",
        "closing": "Stepping into 40 with grace, fire, and champagne.",
        "date_str": "Saturday, 11th September 2027", "date_iso": "2027-09-11T20:00", "time_str": "8:00 PM",
        "venue": "Four Seasons Rooftop Terrace, Bengaluru", "venue_addr": "8 Bellary Rd, Ganganagar, Bengaluru 560032",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#ShaliniAt40",
        "events": [
            {"name": "Sparkling Cocktail Welcome", "date": "11 Sep 2027, 8:00 PM", "venue": "Copitas Bar", "dress": "Rose Gold / Black Tie", "note": "Signature cocktails & harp melodies"},
            {"name": "Birthday Toast & Cake Reveal", "date": "11 Sep 2027, 9:30 PM", "venue": "Rooftop Garden", "dress": "Glamour Gowns", "note": "Sparkler cake & toasts"},
            {"name": "Live Band & Gala Dinner", "date": "11 Sep 2027, 10:30 PM", "venue": "Grand Hall", "dress": "Party Chic", "note": "Live retro pop band & gourmet feast"}
        ]
    },
    {
        "id": 50, "slug": "50-circus-carnival-carnival", "name": "Circus Carnival Extravaganza",
        "category": "Birthday", "category_key": "birthday", "palette_name": "Carnival Red & Carousel Gold",
        "wine": "#991B1B", "wine_d": "#7F1D1D", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FEF2F2", "blush2": "#FEE2E2", "ivory": "#FFFDFD", "ink": "#450A0A",
        "title": "5th Birthday of Advik & Myra", "celebrants": "Advik & Myra's Carnival", "subtitle": "Step Right Up to the Greatest Show on Earth!",
        "c1_name": "Advik & Myra Kapoor", "c1_par": "Loving Parents: Rohit & Natasha Kapoor",
        "c2_name": "Carnival Circus Extravaganza", "c2_par": "Juggling, popcorn, merry-go-round & prizes",
        "eyebrow": "The Circus is Coming to Town!",
        "quote": "Laughter is timeless, imagination has no age, and dreams are forever.",
        "closing": "Thank you for joining our circus of joy!",
        "date_str": "Saturday, 23rd October 2027", "date_iso": "2027-10-23T15:30", "time_str": "3:30 PM",
        "venue": "Wonder Carnival Lawns, Noida", "venue_addr": "Sector 38A, Noida, UP 201301",
        "hero_img": "../assets/img/bday_hero.svg", "cover_img": "../assets/img/bday_cover.svg",
        "c1_img": "../assets/img/bday_cover.svg", "c2_img": "../assets/img/bday_hero.svg",
        "opening_style": "envelope", "ambient": "confetti", "music": "piano", "hashtag": "#KapoorTwinsCarnival",
        "events": [
            {"name": "Circus Games & Ticket Booths", "date": "23 Oct 2027, 3:30 PM", "venue": "Big Top Lawn", "dress": "Bright & Playful", "note": "Ring toss, popcorn & candy floss"},
            {"name": "Acrobatics & Puppet Show", "date": "23 Oct 2027, 4:45 PM", "venue": "Circus Tent", "dress": "Casual", "note": "Juggling clown and puppet theatre"},
            {"name": "Giant Carousel Cake & Dinner", "date": "23 Oct 2027, 6:00 PM", "venue": "Dining Canopy", "dress": "Party Wear", "note": "Carousel cake cutting & pizza banquet"}
        ]
    },

    # 51-55: Housewarming & Griha Pravesh
    {
        "id": 51, "slug": "51-sacred-kalash-auspicious", "name": "Sacred Kalash Griha Pravesh",
        "category": "Housewarming", "category_key": "housewarming", "palette_name": "Auspicious Terracotta & Marigold",
        "wine": "#9A3412", "wine_d": "#7C2D12", "rose": "#EA580C", "rose_d": "#C2410C",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#431407",
        "title": "Griha Pravesh of The Sharma Family", "celebrants": "'Anandam' — The Sharma Abode", "subtitle": "Entering Our New Sanctuary with Vedic Chants & Blessings",
        "c1_name": "Rajesh & Sunita Sharma", "c1_par": "With the Divine Blessings of Late Pt. Hari Prasad Sharma",
        "c2_name": "'Anandam' Residence", "c2_par": "A home built with dreams, prayers and elder blessings",
        "eyebrow": "॥ Shree Ganeshaya Namah ॥ Griha Pravesh",
        "quote": "A house is made of walls and beams; a home is built with love and dreams.",
        "closing": "May this home always echo with laughter, peace and prosperity.",
        "date_str": "Monday, 18th January 2027", "date_iso": "2027-01-18T09:30", "time_str": "9:30 AM",
        "venue": "'Anandam', Villa 42, Palm Greens, Gurugram", "venue_addr": "Sector 54, Golf Course Road, Gurugram 122002",
        "hero_img": "../assets/img/house_hero.svg", "cover_img": "../assets/img/house_cover.svg",
        "c1_img": "../assets/img/house_family.svg", "c2_img": "../assets/img/house_residence.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#SharmaGrihaPravesh",
        "events": [
            {"name": "Vastu Shanti & Ganpati Puja", "date": "18 Jan 2027, 9:30 AM", "venue": "Main Courtyard", "dress": "Traditional Indian Attire", "note": "Havan & chanting for positive energy"},
            {"name": "Auspicious Kalash Entry", "date": "18 Jan 2027, 11:30 AM", "venue": "Main Threshold", "dress": "Festive Wear", "note": "Boiling milk & threshold crossing"},
            {"name": "Anandam Mahaprasad Lunch", "date": "18 Jan 2027, 12:45 PM", "venue": "Garden & Dining Hall", "dress": "Comfortable Ethnic", "note": "Traditional satvik feast"}
        ]
    },
    {
        "id": 52, "slug": "52-diya-blessings", "name": "Diya Blessings & Marigold Toran",
        "category": "Housewarming", "category_key": "housewarming", "palette_name": "Brass Diya & Marigold Gold",
        "wine": "#7C2D12", "wine_d": "#431407", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFEFA", "ink": "#270B04",
        "title": "Housewarming of The Agarwal Family", "celebrants": "'Shanti Villa' — The Agarwals", "subtitle": "Lighting the First Lamp of Prosperity in Our New Abode",
        "c1_name": "Manoj & Renu Agarwal", "c1_par": "Sons: Rishabh & Aniket Agarwal",
        "c2_name": "'Shanti Villa'", "c2_par": "Plot 18, Emerald Enclave",
        "eyebrow": "॥ Shubha Griha Pravesham ॥",
        "quote": "May the light of diyas banish all darkness and welcome eternal peace.",
        "closing": "Our doors are open, our hearts are full.",
        "date_str": "Sunday, 7th February 2027", "date_iso": "2027-02-07T10:00", "time_str": "10:00 AM",
        "venue": "'Shanti Villa', Plot 18, Emerald Enclave, Jaipur", "venue_addr": "Sirsi Road, Jaipur, Rajasthan 302012",
        "hero_img": "../assets/img/house_hero.svg", "cover_img": "../assets/img/house_cover.svg",
        "c1_img": "../assets/img/house_family.svg", "c2_img": "../assets/img/house_residence.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#AgarwalShantiVilla",
        "events": [
            {"name": "Navagraha Havan", "date": "07 Feb 2027, 10:00 AM", "venue": "Rooftop Veranda", "dress": "Yellow / Orange Traditional", "note": "Vedic invocation and blessings"},
            {"name": "Toran Tying & Gruhapravesh", "date": "07 Feb 2027, 11:45 AM", "venue": "Main Teak Door", "dress": "Festive Attire", "note": "Marigold toran ceremony"},
            {"name": "Aashirwad & Rajasthani Lunch", "date": "07 Feb 2027, 1:00 PM", "venue": "Lawn Dining Area", "dress": "Comfortable Festive", "note": "Dal baati churma and sweets"}
        ]
    },
    {
        "id": 53, "slug": "53-modern-minimalist-home", "name": "Modern Minimalist Penthouse Housewarming",
        "category": "Housewarming", "category_key": "housewarming", "palette_name": "Warm Oak & Architectural Slate",
        "wine": "#1E293B", "wine_d": "#0F172A", "rose": "#475569", "rose_d": "#334155",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F8FAFC", "blush2": "#F1F5F9", "ivory": "#FFFFFF", "ink": "#0F172A",
        "title": "Housewarming of Rohit & Neha", "celebrants": "Skyline Penthouse 42", "subtitle": "A New Chapter in Our Sunlit Modern Sanctuary",
        "c1_name": "Rohit Verma", "c1_par": "Architect & Host",
        "c2_name": "Neha Verma", "c2_par": "Designer & Host",
        "eyebrow": "New Keys, New Address, Same Good Friends",
        "quote": "Home is a story of who we are, and a collection of all things we love.",
        "closing": "Come break in our floors and drink our wine!",
        "date_str": "Saturday, 27th February 2027", "date_iso": "2027-02-27T18:00", "time_str": "6:00 PM",
        "venue": "Penthouse 42, The Grand Residences, Bengaluru", "venue_addr": "Outer Ring Road, Bellandur, Bengaluru 560103",
        "hero_img": "../assets/img/house_hero.svg", "cover_img": "../assets/img/house_cover.svg",
        "c1_img": "../assets/img/house_family.svg", "c2_img": "../assets/img/house_residence.svg",
        "opening_style": "call", "ambient": "confetti", "music": "piano", "hashtag": "#VermaPenthouse42",
        "events": [
            {"name": "Skyline Sunset Wine & Cheese", "date": "27 Feb 2027, 6:00 PM", "venue": "Balcony Deck", "dress": "Smart Casual", "note": "Sunset view, cheese board & wines"},
            {"name": "Home Tour & Ribbon Cutting", "date": "27 Feb 2027, 7:15 PM", "venue": "Living Pavilion", "dress": "Contemporary Chic", "note": "Ribbon cutting & house tour"},
            {"name": "Dinner & Rooftop Stargazing", "date": "27 Feb 2027, 8:30 PM", "venue": "Dining Room & Terrace", "dress": "Casual", "note": "Woodfired pizzas & cocktails"}
        ]
    },
    {
        "id": 54, "slug": "54-lotus-sanctuary", "name": "Lotus Sanctuary Traditional Puja",
        "category": "Housewarming", "category_key": "housewarming", "palette_name": "Lotus Pink & Sandalwood Gold",
        "wine": "#9D174D", "wine_d": "#700A34", "rose": "#D97706", "rose_d": "#B45309",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFB", "ink": "#4C0519",
        "title": "Griha Pravesham of The Iyer Family", "celebrants": "'Gokulam' Residence", "subtitle": "Welcoming Goddess Lakshmi Into Our Lotus Abode",
        "c1_name": "S. Venkatraman & Uma Iyer", "c1_par": "Loving Parents of Divya & Vignesh",
        "c2_name": "'Gokulam' Villa", "c2_par": "No. 7, Temple View Enclave",
        "eyebrow": "॥ Om Namo Narayanaya ॥",
        "quote": "May peace dwell within our walls and prosperity within our doors.",
        "closing": "Your presence is our supreme blessing.",
        "date_str": "Friday, 12th March 2027", "date_iso": "2027-03-12T07:00", "time_str": "7:00 AM",
        "venue": "'Gokulam', Temple View Enclave, Chennai", "venue_addr": "ECR, Injambakkam, Chennai 600115",
        "hero_img": "../assets/img/house_hero.svg", "cover_img": "../assets/img/house_cover.svg",
        "c1_img": "../assets/img/house_family.svg", "c2_img": "../assets/img/house_residence.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#IyerGokulamHouse",
        "events": [
            {"name": "Ganapathi & Lakshmi Homam", "date": "12 Mar 2027, 6:30 AM", "venue": "Central Hall", "dress": "Veshti & Kanjeevaram", "note": "Auspicious Brahma Muhurtham homam"},
            {"name": "Go Puja & Milk Boiling", "date": "12 Mar 2027, 8:00 AM", "venue": "Front Portico", "dress": "Traditional Attire", "note": "Sacred cow puja and auspicious milk overflow"},
            {"name": "Traditional South Indian Breakfast", "date": "12 Mar 2027, 9:00 AM", "venue": "Dining Pavilion", "dress": "Comfortable Silk", "note": "Filter coffee, idlis and sweets"}
        ]
    },
    {
        "id": 55, "slug": "55-golden-key-unlocked", "name": "Golden Key Unlocked Celebration",
        "category": "Housewarming", "category_key": "housewarming", "palette_name": "Gilded Key Gold & Emerald Velvet",
        "wine": "#064E3B", "wine_d": "#022C22", "rose": "#047857", "rose_d": "#065F46",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F6F3EB", "blush2": "#EFEAD8", "ivory": "#FCFBF7", "ink": "#132A13",
        "title": "Housewarming of The Mehta Family", "celebrants": "'Aashiyana' — The Mehtas", "subtitle": "Unlocking a Lifetime of Warmth, Hospitality & Joy",
        "c1_name": "Deepak & Neeta Mehta", "c1_par": "Together with Yash & Pooja",
        "c2_name": "'Aashiyana' Villa", "c2_par": "Lane 14, Royal Palms",
        "eyebrow": "We've Got The Keys! Come Celebrate",
        "quote": "May love be the foundation of this house, and joy its crown.",
        "closing": "A house made beautiful by the people who visit it.",
        "date_str": "Sunday, 18th April 2027", "date_iso": "2027-04-18T17:00", "time_str": "5:00 PM",
        "venue": "'Aashiyana', Royal Palms, Ahmedabad", "venue_addr": "SG Highway, Bodakdev, Ahmedabad 380054",
        "hero_img": "../assets/img/house_hero.svg", "cover_img": "../assets/img/house_cover.svg",
        "c1_img": "../assets/img/house_family.svg", "c2_img": "../assets/img/house_residence.svg",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#MehtaAashiyana",
        "events": [
            {"name": "House Blessing Ceremony", "date": "18 Apr 2027, 5:00 PM", "venue": "Main Hall", "dress": "Festive Ethnic", "note": "Family puja and auspicious blessing"},
            {"name": "Golden Key Unveiling", "date": "18 Apr 2027, 6:15 PM", "venue": "Lawn Entrance", "dress": "Smart Indian", "note": "Unlocking the doors for our guests"},
            {"name": "Dinner & Garden Soiree", "date": "18 Apr 2027, 7:30 PM", "venue": "Private Garden", "dress": "Semi-Formal", "note": "Gujarati delicacies & live music"}
        ]
    },

    # 56-60: Anniversaries & Vow Renewals
    {
        "id": 56, "slug": "56-silver-jubilee-25th", "name": "Silver Jubilee 25th Anniversary",
        "category": "Anniversary", "category_key": "anniversary", "palette_name": "Sterling Silver & Crystal White",
        "wine": "#1E293B", "wine_d": "#0F172A", "rose": "#475569", "rose_d": "#334155",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F8FAFC", "blush2": "#E2E8F0", "ivory": "#FFFFFF", "ink": "#0F172A",
        "title": "25th Anniversary of Vikram & Sunita", "celebrants": "Vikram & Sunita", "subtitle": "A Quarter-Century of Enduring Love & Companionship",
        "c1_name": "Vikram Chopra", "c1_par": "Loving Husband & Soulmate",
        "c2_name": "Sunita Chopra", "c2_par": "Loving Wife & Guiding Light",
        "eyebrow": "25 Years Together — Our Silver Love Story",
        "quote": "Love doesn't just sit there like a stone; it had to be made, like bread; remade all the time, made new.",
        "closing": "The best thing to hold onto in life is each other.",
        "date_str": "Saturday, 10th April 2027", "date_iso": "2027-04-10T19:00", "time_str": "7:00 PM",
        "venue": "ITC Grand Bharat, Gurugram", "venue_addr": "Hasanpur Tauru, Mewat District, Gurugram 122105",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "stars", "music": "piano", "hashtag": "#ChoprasSilverLove",
        "events": [
            {"name": "Sunset Memory Exhibit", "date": "10 Apr 2027, 7:00 PM", "venue": "Aravalli Pavilion", "dress": "Cocktail Silver & Black", "note": "Walk through 25 years of memories"},
            {"name": "Silver Vow Renewal", "date": "10 Apr 2027, 8:15 PM", "venue": "Royal Amphitheatre", "dress": "Formal Evening", "note": "Exchange of silver rings & garland"},
            {"name": "Silver Jubilee Gala Dinner", "date": "10 Apr 2027, 9:30 PM", "venue": "Peacock Ballroom", "dress": "Black Tie / Royal Indian", "note": "Royal feast & couple waltz"}
        ]
    },
    {
        "id": 57, "slug": "57-golden-anniversary-50th", "name": "Golden Jubilee 50th Anniversary",
        "category": "Anniversary", "category_key": "anniversary", "palette_name": "Polished 24K Gold & Crimson Royal",
        "wine": "#831843", "wine_d": "#500724", "rose": "#BE185D", "rose_d": "#9D174D",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FDF2F8", "blush2": "#FCE7F3", "ivory": "#FFFAFC", "ink": "#380619",
        "title": "50th Golden Jubilee of Pt. Ram & Shanti Devi", "celebrants": "Pt. Ram & Shanti Devi", "subtitle": "Fifty Golden Years of Devotion, Family & Blessings",
        "c1_name": "Pt. Ram Narain Sharma", "c1_par": "Patriarch & Loving Husband",
        "c2_name": "Shmt. Shanti Devi Sharma", "c2_par": "Matriarch & Heart of the Family",
        "eyebrow": "50 Years of Golden Vows — 1977 to 2027",
        "quote": "Grow old along with me! The best is yet to be.",
        "closing": "Three generations standing tall under their umbrella of love.",
        "date_str": "Sunday, 21st November 2027", "date_iso": "2027-11-21T18:00", "time_str": "6:00 PM",
        "venue": "Jai Mahal Palace, Jaipur", "venue_addr": "Jacob Rd, Civil Lines, Jaipur 302006",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "sitar", "hashtag": "#SharmaGolden50",
        "events": [
            {"name": "Ganga Aarti & Swasti Vachan", "date": "21 Nov 2027, 6:00 PM", "venue": "Lotus Pond", "dress": "Golden Traditional", "note": "Vedic blessing for long health"},
            {"name": "50th Vow Renewal & Garland", "date": "21 Nov 2027, 7:15 PM", "venue": "Durbar Lawns", "dress": "Gold & Crimson Royal", "note": "Garlands from children & grandchildren"},
            {"name": "Royal Mahabhoj Feast", "date": "21 Nov 2027, 8:30 PM", "venue": "Palace Grounds", "dress": "Royal Indian", "note": "Traditional Rajasthani 32-course dinner"}
        ]
    },
    {
        "id": 58, "slug": "58-pearl-anniversary-30th", "name": "Pearl Anniversary 30th Romance",
        "category": "Anniversary", "category_key": "anniversary", "palette_name": "Iridescent Pearl & Sea Spray",
        "wine": "#0E7490", "wine_d": "#155E75", "rose": "#0284C7", "rose_d": "#0369A1",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#ECFEFF", "blush2": "#CFFAFE", "ivory": "#FAFFFF", "ink": "#083344",
        "title": "30th Pearl Anniversary of Sanjeev & Renu", "celebrants": "Sanjeev & Renu", "subtitle": "Three Decades of Rare & Precious Love",
        "c1_name": "Sanjeev Bajaj", "c1_par": "Loving Husband",
        "c2_name": "Renu Bajaj", "c2_par": "Loving Wife",
        "eyebrow": "Like Pearls Formed by Time and Patience",
        "quote": "A successful marriage requires falling in love many times, always with the same person.",
        "closing": "Cherishing 30 years of shared sunrise moments.",
        "date_str": "Saturday, 11th December 2027", "date_iso": "2027-12-11T18:30", "time_str": "6:30 PM",
        "venue": "Taj Fort Aguada Resort, Goa", "venue_addr": "Sinquerim, Candolim, Goa 403515",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "call", "ambient": "petals", "music": "piano", "hashtag": "#BajajPearl30",
        "events": [
            {"name": "Sunset Clifftop Cocktails", "date": "11 Dec 2027, 6:00 PM", "venue": "Sea Rock Lawn", "dress": "Pearl White & Pastel", "note": "Champagne overlooking the Arabian Sea"},
            {"name": "Pearl Ring Renewal Vows", "date": "11 Dec 2027, 7:30 PM", "venue": "Fort View Terrace", "dress": "Cocktail Elegance", "note": "Exchange of pearl anniversary rings"},
            {"name": "Beachside Banquet & Dance", "date": "11 Dec 2027, 9:00 PM", "venue": "Morisco Lawn", "dress": "Resort Glam", "note": "Fresh seafood and retro slow dance"}
        ]
    },
    {
        "id": 59, "slug": "59-ruby-romance-40th", "name": "Ruby Romance 40th Anniversary",
        "category": "Anniversary", "category_key": "anniversary", "palette_name": "Ruby Crimson & Champagne",
        "wine": "#991B1B", "wine_d": "#7F1D1D", "rose": "#E11D48", "rose_d": "#BE123C",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFAFB", "ink": "#450A0A",
        "title": "40th Ruby Anniversary of Deepak & Manju", "celebrants": "Deepak & Manju", "subtitle": "A Deep, Passionate Flame That Has Burned for 40 Years",
        "c1_name": "Deepak Malhotra", "c1_par": "Husband, Father & Patriarch",
        "c2_name": "Manju Malhotra", "c2_par": "Wife, Mother & Queen of the Home",
        "eyebrow": "40 Years of Devotion & Joy — Ruby Jubilee",
        "quote": "Love is not about how many days, months, or years you have been together. It is about how much you love each other every single day.",
        "closing": "Our hearts beat as one, ruby-bright and true.",
        "date_str": "Saturday, 16th October 2027", "date_iso": "2027-10-16T19:00", "time_str": "7:00 PM",
        "venue": "Umaid Bhawan Palace Gardens, Jodhpur", "venue_addr": "Cantt Area, Jodhpur 342006",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "petals", "music": "piano", "hashtag": "#DeepakManjuRuby40",
        "events": [
            {"name": "Royal Chariot Welcome", "date": "16 Oct 2027, 7:00 PM", "venue": "Palace Entrance", "dress": "Ruby Crimson & Silk", "note": "Traditional Rajasthani welcome"},
            {"name": "Ruby Ring Renewal & Toasts", "date": "16 Oct 2027, 8:15 PM", "venue": "Baradari Pavilion", "dress": "Royal Formal", "note": "Renewing marital vows"},
            {"name": "Grand Jubilee Banquet", "date": "16 Oct 2027, 9:30 PM", "venue": "Lancer's Lawn", "dress": "Black Tie / Royal Indian", "note": "Live sitar recital & royal dinner"}
        ]
    },
    {
        "id": 60, "slug": "60-diamond-forever-60th", "name": "Diamond Forever 60th Anniversary",
        "category": "Anniversary", "category_key": "anniversary", "palette_name": "Platinum Diamond & Regal Ivory",
        "wine": "#1E293B", "wine_d": "#0F172A", "rose": "#475569", "rose_d": "#334155",
        "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F8FAFC", "blush2": "#E2E8F0", "ivory": "#FFFFFF", "ink": "#0F172A",
        "title": "60th Diamond Jubilee of Harish & Kamla", "celebrants": "Harish & Kamla", "subtitle": "Six Decades of Unbreakable Devotion & Family Legacy",
        "c1_name": "Shri Harish Chand Singhal", "c1_par": "Patriarch, married 1967",
        "c2_name": "Smt. Kamla Singhal", "c2_par": "Matriarch, married 1967",
        "eyebrow": "60 Years of Sacred Marriage — Diamond Jubilee",
        "quote": "A diamond is forever, but the bond we created with our lives is eternal.",
        "closing": "Celebrating an inspiration to our entire lineage.",
        "date_str": "Sunday, 5th December 2027", "date_iso": "2027-12-05T17:30", "time_str": "5:30 PM",
        "venue": "The Oberoi Rajvilas, Jaipur", "venue_addr": "Goner Rd, Jagatpura, Jaipur 302031",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp",
        "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp",
        "opening_style": "envelope", "ambient": "stars", "music": "piano", "hashtag": "#SinghalDiamond60",
        "events": [
            {"name": "Sacred Veda Swasti Chants", "date": "05 Dec 2027, 5:30 PM", "venue": "Temple Courtyard", "dress": "Ivory & Gold Traditional", "note": "Puja of gratitude by 4 generations"},
            {"name": "Diamond Garland Ceremony", "date": "05 Dec 2027, 6:45 PM", "venue": "Sunken Lawn", "dress": "Regal Formal", "note": "Children and grandchildren paying homage"},
            {"name": "Diamond Jubilee Banquet", "date": "05 Dec 2027, 8:00 PM", "venue": "Grand Hall", "dress": "Formal Indian", "note": "Grand royal vegetarian feast"}
        ]
    }
]

# Write assets/templates-data.js so index.html can render the full interactive gallery
js_content = "window.GOLDENVOWS_TEMPLATES = " + json.dumps(templates_data, indent=2) + ";\n"
with open(os.path.join(ASSETS_DIR, "templates-data.js"), "w", encoding="utf-8") as f:
    f.write(js_content)
print("Generated assets/templates-data.js")



# Write assets/templates-data.js so index.html can render the full interactive gallery
js_content = "window.GOLDENVOWS_TEMPLATES = " + json.dumps(templates_data, indent=2) + ";\n"
with open(os.path.join(ASSETS_DIR, "templates-data.js"), "w", encoding="utf-8") as f:
    f.write(js_content)
print("Generated assets/templates-data.js")

for t in templates_data:
    filename = f"{t['slug']}.html"
    filepath = os.path.join(TEMPLATES_DIR, filename)
    cat_key = t.get("category_key", "wedding")

    if cat_key == "housewarming":
        header_banner = """
        <div class="hw-toran-banner">
          <div class="hw-toran-leaves">🍃 🌺 🍃 🌼 🍃 🌺 🍃 🌼 🍃</div>
          <p class="hw-vedic-sloka">॥ ॐ नमो भगवते वास्तुपुरुषाय नमः ॥</p>
          <div class="hw-kalash-badge">🪔 🏡 🪔</div>
          <h2 class="hw-main-title">GRIHA PRAVESH</h2>
          <p class="hw-sub-title">Auspicious Housewarming Ceremony</p>
        </div>"""
        
        events_html = ""
        for ev in t['events']:
            events_html += f"""
            <div class="hw-time-item">
              <div class="hw-time-icon">🪔</div>
              <div class="hw-time-info">
                <b>{ev['name']}</b>
                <span>{ev['date']}</span>
                <small>Venue: {ev['venue']} · Dress: {ev['dress']}</small>
                <em>{ev['note']}</em>
              </div>
            </div>"""

        stage_content = f"""
        <div class="hw-stage-card">
          <div class="hw-hero-frame">
            <img src="{t['hero_img']}" alt="Sanctuary Entrance" class="hw-hero-art">
            <div class="hw-hero-tag">Auspicious Abode</div>
          </div>
          <h1 class="hw-abode-title">{t['celebrants']}</h1>
          <p class="hw-date-line">✦ {t['date_str']} · {t['time_str']} ✦</p>
          <p class="hw-venue-line"><b>{t['venue']}</b><br><small>{t['venue_addr']}</small></p>

          <div class="hw-hosts-row">
            <div class="hw-host-box">
              <img src="{t['c1_img']}" alt="{t['c1_name']}">
              <b>{t['c1_name']}</b>
              <small>{t['c1_par']}</small>
            </div>
            <div class="hw-host-divider">✦</div>
            <div class="hw-host-box">
              <img src="{t['c2_img']}" alt="{t['c2_name']}">
              <b>{t['c2_name']}</b>
              <small>{t['c2_par']}</small>
            </div>
          </div>

          <blockquote class="hw-quote">“{t['quote']}”</blockquote>

          <div class="hw-timeline">
            <h3 class="hw-sec-head">Auspicious Puja &amp; Rituals Schedule</h3>
            {events_html}
          </div>

          <div class="hw-location-card">
            <h4>📍 Google Maps Route to {t['celebrants']}</h4>
            <p>{t['venue_addr']}</p>
            <a href="https://maps.google.com/?q={t['venue']}" target="_blank" rel="noopener" class="btn-hw-map">➤ Open Live Navigation Map</a>
          </div>

          <p class="hw-closing">“{t['closing']}”</p>
        </div>"""

    elif cat_key == "babyshower":
        header_banner = """
        <div class="baby-cloud-banner">
          <div class="baby-floating-icons">🍼 ☁️ 🧸 🌟 🍼</div>
          <p class="baby-eyebrow">A Sweet Little Miracle is on the Way!</p>
          <h2 class="baby-main-title">BABY SHOWER</h2>
          <p class="baby-sub-title">Godh Bharai &amp; Baby Blessings</p>
        </div>"""
        
        events_html = ""
        for ev in t['events']:
            events_html += f"""
            <div class="baby-event-item">
              <span class="baby-bullet">🧸</span>
              <div>
                <b>{ev['name']}</b>
                <p>{ev['date']} · {ev['venue']}</p>
                <small>{ev['note']} · Dress: {ev['dress']}</small>
              </div>
            </div>"""

        stage_content = f"""
        <div class="baby-stage-card">
          <div class="baby-cradle-box">
            <img src="{t['hero_img']}" alt="Baby Miracle" class="baby-hero-img">
          </div>
          <h1 class="baby-title">{t['celebrants']}</h1>
          <p class="baby-date">✦ {t['date_str']} · {t['time_str']} ✦</p>
          <p class="baby-venue">{t['venue']}</p>

          <div class="baby-parents-row">
            <div class="baby-parent-box">
              <div class="baby-avatar">👶</div>
              <b>{t['c1_name']}</b>
              <small>{t['c1_par']}</small>
            </div>
            <div class="baby-parent-divider">🍼</div>
            <div class="baby-parent-box">
              <div class="baby-avatar">🤱</div>
              <b>{t['c2_name']}</b>
              <small>{t['c2_par']}</small>
            </div>
          </div>

          <p class="baby-msg">“{t['quote']}”</p>

          <div class="baby-games-box">
            <h3 class="baby-sec-head">Baby Shower Schedule &amp; Games</h3>
            {events_html}
          </div>

          <p class="baby-closing">“{t['closing']}”</p>
        </div>"""

    elif cat_key == "birthday":
        header_banner = f"""
        <div class="bday-vip-banner">
          <div class="bday-barcode">||| | |||| | ||||| | ||</div>
          <p class="bday-pass-label">★ VIP CELEBRATION BASH ★</p>
          <h2 class="bday-title">{t['celebrants']}</h2>
          <p class="bday-sub">BIRTHDAY GALA &amp; PARTY NIGHT</p>
        </div>"""
        
        events_html = ""
        for ev in t['events']:
            date_label = ev['date'].split(',')[1].strip() if ',' in ev['date'] else 'Night'
            events_html += f"""
            <div class="bday-schedule-item">
              <span class="bday-badge-pill">{date_label}</span>
              <div>
                <b>{ev['name']}</b>
                <p>{ev['note']}</p>
                <small>Dress code: {ev['dress']}</small>
              </div>
            </div>"""

        stage_content = f"""
        <div class="bday-ticket-card">
          <div class="bday-ticket-top">
            <div class="bday-badge-circ">★ VIP CELEBRANT ★</div>
            <h1 class="bday-star-name">{t['celebrants']}</h1>
            <p class="bday-meta-tag">{t['eyebrow']}</p>
            <p class="bday-date-badge">✦ {t['date_str']} · {t['time_str']} ✦</p>
            <p class="bday-venue-badge">📍 {t['venue']}</p>
          </div>
          
          <div class="bday-perforated-line">
            <span class="notch notch-l"></span>
            <span class="dash-line"></span>
            <span class="notch notch-r"></span>
          </div>

          <div class="bday-ticket-bottom">
            <div class="bday-hero-box">
              <img src="{t['hero_img']}" alt="Party Stage" style="width:100%;height:190px;object-fit:cover;border-radius:14px;border:1.5px solid var(--gold);">
            </div>

            <div class="bday-host-badge">
              <b>{t['c1_name']}</b>
              <small>{t['c1_par']}</small>
            </div>
            <p class="bday-quote">“{t['quote']}”</p>

            <h3 class="bday-sec-head">🎉 Party Highlights &amp; DJ Timeline</h3>
            {events_html}

            <div class="bday-btn-wrap">
              <a href="https://maps.google.com/?q={t['venue']}" target="_blank" rel="noopener" class="btn-bday-map">Get Party Directions</a>
            </div>

            <p class="bday-closing">“{t['closing']}”</p>
          </div>
        </div>"""

    elif cat_key == "engagement":
        header_banner = f"""
        <div class="eng-star-banner">
          <div class="eng-ring-glow">💍</div>
          <p class="eng-eyebrow">Under a Sky of Infinite Stars</p>
          <h2 class="eng-title">{t['celebrants']}</h2>
          <p class="eng-sub">Engagement &amp; Ring Ceremony</p>
        </div>"""
        
        events_html = ""
        for ev in t['events']:
            events_html += f"""
            <div class="eng-time-card">
              <b>{ev['name']}</b>
              <p>✦ {ev['date']} · {ev['venue']}</p>
              <small>{ev['note']} · {ev['dress']}</small>
            </div>"""

        stage_content = f"""
        <div class="eng-stage-card">
          <div class="eng-solitaire-halo">
            <span class="eng-sparkle">✦</span>
            <h2>{t['celebrants']}</h2>
            <p>{t['date_str']} · {t['time_str']}</p>
            <p class="eng-place">{t['venue']}</p>
          </div>

          <div class="eng-couple-row">
            <div class="eng-person">
              <img src="{t['c1_img']}" alt="{t['c1_name']}">
              <b>{t['c1_name']}</b>
              <small>{t['c1_par']}</small>
            </div>
            <div class="eng-heart">💍</div>
            <div class="eng-person">
              <img src="{t['c2_img']}" alt="{t['c2_name']}">
              <b>{t['c2_name']}</b>
              <small>{t['c2_par']}</small>
            </div>
          </div>

          <p class="eng-vow">“{t['quote']}”</p>

          <div class="eng-timeline">
            <h3 class="eng-sec-head">Celebration Timings</h3>
            {events_html}
          </div>

          <p class="eng-closing">“{t['closing']}”</p>
        </div>"""

    else:
        header_banner = f"""
        <div class="wed-royal-banner">
          <p class="wed-sloka">{t['eyebrow']}</p>
          <div class="wed-symbol">✦ ❦ ✦</div>
          <h2 class="wed-title">{t['celebrants']}</h2>
          <p class="wed-sub">{t['subtitle']}</p>
        </div>"""
        
        events_html = ""
        for ev in t['events']:
            events_html += f"""
            <div class="wed-ceremony-item">
              <div class="wed-c-icon">✦</div>
              <div>
                <b>{ev['name']}</b>
                <p>{ev['date']} · {ev['venue']}</p>
                <small>Dress code: {ev['dress']} · {ev['note']}</small>
              </div>
            </div>"""

        stage_content = f"""
        <div class="wed-stage-card">
          <div class="wed-hero-arch">
            <img src="{t['hero_img']}" alt="Palace Mandap">
          </div>
          <h1 class="wed-couple-names">{t['celebrants']}</h1>
          <p class="wed-date-ribbon">✦ {t['date_str']} · {t['time_str']} ✦</p>
          <p class="wed-venue-tag">{t['venue']}</p>

          <div class="wed-couple-portraits">
            <div class="wed-person-card">
              <img src="{t['c1_img']}" alt="{t['c1_name']}">
              <b>{t['c1_name']}</b>
              <small>{t['c1_par']}</small>
            </div>
            <div class="wed-mandap-knot">❦</div>
            <div class="wed-person-card">
              <img src="{t['c2_img']}" alt="{t['c2_name']}">
              <b>{t['c2_name']}</b>
              <small>{t['c2_par']}</small>
            </div>
          </div>

          <blockquote class="wed-sacred-quote">“{t['quote']}”</blockquote>

          <div class="wed-functions-box">
            <h3 class="wed-sec-title">Sacred Functions &amp; Ceremonies</h3>
            {events_html}
          </div>

          <p class="wed-footer-quote">“{t['closing']}”</p>
        </div>"""

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{t['title']} — GoldenVows #{t['id']:02d}</title>
<meta name="description" content="{t['subtitle']} - {t['celebrants']}">
<link rel="stylesheet" href="../assets/fonts/fonts.css">
<link rel="stylesheet" href="../styles.css">
<style>
:root {{
  --wine: {t['wine']};
  --wine-d: {t['wine_d']};
  --rose: {t['rose']};
  --rose-d: {t['rose_d']};
  --gold: {t['gold']};
  --gold-l: {t['gold_l']};
  --blush: {t['blush']};
  --blush2: {t['blush2']};
  --ivory: {t['ivory']};
  --ink: {t['ink']};
}}

*, *::before, *::after, html, body {{
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}}
::-webkit-scrollbar {{
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  background: transparent !important;
}}
::-webkit-scrollbar-thumb, ::-webkit-scrollbar-track {{
  display: none !important;
  background: transparent !important;
}}

body {{
  background: {t['blush2']};
  margin: 0;
  padding: 0;
  color: var(--ink);
  font-family: var(--sans);
  overflow-x: hidden;
}}

.top-template-badge {{
  position: fixed;
  top: 10px;
  right: 14px;
  z-index: 1000;
  background: var(--wine);
  color: var(--gold-l);
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  border: 1px solid var(--gold);
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}}

.inv-main-wrap {{
  min-height: 100vh;
  padding: 60px 14px 90px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}}

/* Housewarming Specific */
.hw-toran-banner {{ text-align: center; margin-bottom: 14px; }}
.hw-toran-leaves {{ font-size: 20px; letter-spacing: 6px; margin-bottom: 6px; }}
.hw-vedic-sloka {{ font-family: var(--serif); font-size: 14px; color: var(--wine); font-weight: 700; letter-spacing: 1px; margin: 4px 0; }}
.hw-kalash-badge {{ font-size: 24px; margin: 6px 0; }}
.hw-main-title {{ font-family: var(--serif); font-size: 32px; color: var(--wine-d); letter-spacing: 3px; margin: 4px 0; }}
.hw-sub-title {{ font-family: var(--cap); font-size: 13px; color: var(--rose-d); text-transform: uppercase; letter-spacing: 2px; }}
.hw-stage-card {{ background: #FFFDF9; border: 2px solid var(--gold); border-radius: 24px; box-shadow: 0 20px 50px rgba(124, 45, 18, 0.15); max-width: 440px; width: 100%; padding: 24px 20px; text-align: center; box-sizing: border-box; }}
.hw-hero-frame {{ position: relative; border-radius: 18px; overflow: hidden; border: 1.5px solid var(--gold); margin-bottom: 16px; }}
.hw-hero-art {{ width: 100%; height: 200px; object-fit: cover; display: block; }}
.hw-hero-tag {{ position: absolute; bottom: 8px; right: 8px; background: rgba(124, 45, 18, 0.85); color: #FEF08A; font-size: 10px; font-weight: 700; padding: 3px 10px; border-radius: 999px; letter-spacing: 1px; }}
.hw-abode-title {{ font-family: var(--serif); font-size: 26px; color: var(--wine); margin: 8px 0 4px; }}
.hw-date-line {{ font-family: var(--cap); font-size: 13.5px; color: var(--rose-d); font-weight: 700; margin: 4px 0; }}
.hw-venue-line {{ font-size: 13px; color: #4B5563; margin: 4px 0 16px; }}
.hw-hosts-row {{ display: flex; align-items: center; justify-content: center; gap: 12px; background: rgba(212, 175, 55, 0.08); border: 1px solid rgba(212, 175, 55, 0.35); border-radius: 16px; padding: 14px 10px; margin: 14px 0; }}
.hw-host-box {{ flex: 1; text-align: center; }}
.hw-host-box img {{ width: 80px; height: 90px; border-radius: 12px; border: 1.5px solid var(--gold); object-fit: cover; margin: 0 auto 6px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
.hw-host-box b {{ display: block; font-size: 12.5px; color: var(--wine); }}
.hw-host-box small {{ font-size: 10.5px; color: #6B7280; display: block; }}
.hw-host-divider {{ color: var(--gold); font-size: 16px; }}
.hw-quote {{ font-family: var(--serif); font-style: italic; font-size: 14px; color: var(--wine-d); line-height: 1.5; margin: 14px 0; }}
.hw-timeline {{ text-align: left; margin: 18px 0; }}
.hw-sec-head {{ font-family: var(--serif); font-size: 18px; color: var(--wine); text-align: center; margin-bottom: 12px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 6px; }}
.hw-time-item {{ display: flex; gap: 10px; margin-bottom: 12px; background: #FFF; border: 1px solid #E5E7EB; border-radius: 12px; padding: 10px; }}
.hw-time-icon {{ font-size: 20px; line-height: 1; }}
.hw-time-info b {{ display: block; font-size: 13.5px; color: var(--wine); }}
.hw-time-info span {{ display: block; font-size: 11.5px; color: var(--rose-d); font-weight: 600; }}
.hw-time-info small {{ display: block; font-size: 11px; color: #6B7280; }}
.hw-time-info em {{ display: block; font-size: 10.5px; color: #9CA3AF; font-style: normal; margin-top: 2px; }}
.hw-location-card {{ background: rgba(212, 175, 55, 0.1); border: 1px dashed var(--gold); border-radius: 14px; padding: 14px; margin: 14px 0; }}
.hw-location-card h4 {{ margin: 0 0 4px; font-size: 13px; color: var(--wine); }}
.hw-location-card p {{ font-size: 12px; color: #4B5563; margin: 0 0 10px; }}
.btn-hw-map {{ display: inline-block; background: var(--wine); color: var(--gold-l); font-size: 12px; font-weight: 700; padding: 8px 18px; border-radius: 999px; text-decoration: none; }}
.hw-closing {{ font-family: var(--script); font-size: 22px; color: var(--wine); margin-top: 14px; }}

/* Baby Shower Specific */
.baby-cloud-banner {{ text-align: center; margin-bottom: 14px; }}
.baby-floating-icons {{ font-size: 22px; letter-spacing: 8px; }}
.baby-eyebrow {{ font-size: 13px; color: var(--rose-d); font-weight: 600; margin: 4px 0; }}
.baby-main-title {{ font-family: var(--serif); font-size: 32px; color: var(--wine); letter-spacing: 2px; margin: 2px 0; }}
.baby-sub-title {{ font-size: 13px; color: #9D174D; text-transform: uppercase; letter-spacing: 1.5px; }}
.baby-stage-card {{ background: #FFF; border-radius: 32px; box-shadow: 0 20px 45px rgba(244, 114, 182, 0.2); border: 2px solid #FBCFE8; max-width: 440px; width: 100%; padding: 24px 20px; text-align: center; box-sizing: border-box; }}
.baby-cradle-box {{ width: 100%; height: 180px; border-radius: 24px; overflow: hidden; background: #FFF1F2; margin-bottom: 14px; }}
.baby-hero-img {{ width: 100%; height: 100%; object-fit: cover; }}
.baby-title {{ font-family: var(--serif); font-size: 26px; color: var(--wine); margin: 6px 0; }}
.baby-date {{ font-size: 13.5px; color: #BE185D; font-weight: 700; }}
.baby-venue {{ font-size: 12.5px; color: #6B7280; margin: 2px 0 14px; }}
.baby-parents-row {{ display: flex; align-items: center; justify-content: center; gap: 12px; background: #FDF2F8; border: 1px dashed #F472B6; border-radius: 20px; padding: 12px; margin: 12px 0; }}
.baby-parent-box {{ flex: 1; text-align: center; }}
.baby-avatar {{ font-size: 28px; }}
.baby-parent-box b {{ display: block; font-size: 13px; color: var(--wine); }}
.baby-parent-box small {{ font-size: 11px; color: #6B7280; }}
.baby-parent-divider {{ font-size: 20px; }}
.baby-msg {{ font-family: var(--serif); font-style: italic; font-size: 14px; color: #831843; margin: 12px 0; }}
.baby-games-box {{ text-align: left; background: #F8FAFC; border-radius: 16px; padding: 14px; margin: 14px 0; }}
.baby-sec-head {{ text-align: center; font-size: 16px; color: var(--wine); margin: 0 0 10px; }}
.baby-event-item {{ display: flex; gap: 8px; margin-bottom: 10px; }}
.baby-bullet {{ font-size: 18px; }}
.baby-event-item b {{ font-size: 13px; color: var(--wine); }}
.baby-event-item p {{ font-size: 11.5px; color: #BE185D; margin: 1px 0; }}
.baby-event-item small {{ font-size: 10.5px; color: #6B7280; }}
.baby-closing {{ font-family: var(--script); font-size: 22px; color: var(--wine); margin-top: 10px; }}

/* Birthday VIP Pass Specific */
.bday-vip-banner {{ text-align: center; margin-bottom: 12px; }}
.bday-barcode {{ font-family: monospace; font-size: 18px; letter-spacing: 4px; color: var(--gold); }}
.bday-pass-label {{ font-size: 11px; letter-spacing: 3px; color: var(--gold); font-weight: 700; margin: 3px 0; }}
.bday-title {{ font-family: var(--serif); font-size: 30px; color: #FFF; margin: 2px 0; }}
.bday-sub {{ font-size: 12px; letter-spacing: 2px; color: #CA8A04; }}
.bday-ticket-card {{ background: #18181B; color: #FAFAFA; border-radius: 24px; box-shadow: 0 25px 60px rgba(0,0,0,0.5); border: 2px solid var(--gold); max-width: 440px; width: 100%; box-sizing: border-box; overflow: hidden; }}
.bday-ticket-top {{ padding: 24px 20px 16px; text-align: center; }}
.bday-badge-circ {{ display: inline-block; background: var(--gold); color: #18181B; font-size: 11px; font-weight: 800; letter-spacing: 2px; padding: 4px 14px; border-radius: 999px; margin-bottom: 8px; }}
.bday-star-name {{ font-family: var(--serif); font-size: 28px; color: #FFF; margin: 0 0 4px; }}
.bday-meta-tag {{ font-size: 11.5px; color: #A1A1AA; letter-spacing: 1px; text-transform: uppercase; margin: 0 0 10px; }}
.bday-date-badge {{ font-size: 13.5px; color: var(--gold-l); font-weight: 700; margin: 4px 0; }}
.bday-venue-badge {{ font-size: 12.5px; color: #E4E4E7; margin: 0; }}
.bday-perforated-line {{ position: relative; height: 20px; display: flex; align-items: center; margin: 4px 0; }}
.notch {{ position: absolute; width: 20px; height: 20px; border-radius: 50%; background: {t['blush2']}; top: 0; }}
.notch-l {{ left: -10px; }}
.notch-r {{ right: -10px; }}
.dash-line {{ width: 100%; height: 1px; border-top: 2px dashed rgba(212,175,55,0.4); margin: 0 14px; }}
.bday-ticket-bottom {{ padding: 16px 20px 24px; text-align: center; }}
.bday-hero-box {{ margin-bottom: 14px; }}
.bday-host-badge {{ background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 10px; margin-bottom: 14px; }}
.bday-host-badge b {{ display: block; font-size: 13.5px; color: var(--gold-l); }}
.bday-host-badge small {{ font-size: 11.5px; color: #A1A1AA; }}
.bday-quote {{ font-family: var(--serif); font-style: italic; font-size: 14px; color: #D4D4D8; margin: 12px 0 16px; line-height: 1.5; }}
.bday-sec-head {{ font-size: 15px; color: var(--gold-l); text-align: center; letter-spacing: 1px; margin: 0 0 12px; }}
.bday-schedule-item {{ display: flex; align-items: flex-start; gap: 10px; text-align: left; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 10px; margin-bottom: 8px; }}
.bday-badge-pill {{ background: var(--gold); color: #18181B; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 999px; white-space: nowrap; }}
.bday-schedule-item b {{ display: block; font-size: 13px; color: #FFF; }}
.bday-schedule-item p {{ font-size: 11.5px; color: #A1A1AA; margin: 2px 0 0; }}
.bday-schedule-item small {{ font-size: 10.5px; color: #71717A; display: block; }}
.bday-btn-wrap {{ margin: 18px 0 12px; }}
.btn-bday-map {{ display: inline-block; background: var(--gold); color: #18181B; font-size: 12px; font-weight: 800; padding: 8px 18px; border-radius: 999px; text-decoration: none; }}
.bday-closing {{ font-family: var(--script); font-size: 22px; color: var(--gold-l); margin-top: 14px; }}

/* Engagement Starlight Specific */
.eng-star-banner {{ text-align: center; margin-bottom: 14px; }}
.eng-ring-glow {{ font-size: 28px; filter: drop-shadow(0 0 10px rgba(255,215,0,0.6)); }}
.eng-eyebrow {{ font-size: 12.5px; letter-spacing: 2px; color: var(--gold-l); text-transform: uppercase; margin: 4px 0; }}
.eng-title {{ font-family: var(--serif); font-size: 30px; color: var(--gold-l); margin: 2px 0; }}
.eng-sub {{ font-size: 12px; color: #94A3B8; letter-spacing: 1px; }}
.eng-stage-card {{ background: rgba(15,23,42,0.85); backdrop-filter: blur(14px); border: 1.5px solid var(--gold); border-radius: 28px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); max-width: 440px; width: 100%; padding: 26px 20px; text-align: center; color: #F8FAFC; box-sizing: border-box; }}
.eng-solitaire-halo {{ background: radial-gradient(circle at center, rgba(56,189,248,0.15), transparent 70%); border: 1px solid rgba(212,175,55,0.4); border-radius: 20px; padding: 18px; margin-bottom: 16px; }}
.eng-sparkle {{ font-size: 20px; color: var(--gold); display: block; margin-bottom: 4px; }}
.eng-solitaire-halo h2 {{ font-family: var(--serif); font-size: 26px; color: var(--gold-l); margin: 0; }}
.eng-solitaire-halo p {{ font-size: 12.5px; color: #94A3B8; margin: 4px 0 0; }}
.eng-place {{ font-size: 12px; color: #CBD5E1; }}
.eng-couple-row {{ display: flex; align-items: center; justify-content: center; gap: 14px; margin: 16px 0; }}
.eng-person {{ text-align: center; }}
.eng-person img {{ width: 85px; height: 110px; border-radius: 14px; border: 1.5px solid var(--gold); object-fit: cover; box-shadow: 0 4px 14px rgba(0,0,0,0.3); }}
.eng-person b {{ display: block; font-size: 13px; color: var(--gold-l); margin-top: 4px; }}
.eng-person small {{ font-size: 10.5px; color: #94A3B8; display: block; }}
.eng-heart {{ font-size: 22px; color: var(--gold); }}
.eng-vow {{ font-family: var(--serif); font-style: italic; font-size: 13.5px; color: #E2E8F0; line-height: 1.5; margin: 14px 0; }}
.eng-timeline {{ text-align: left; margin: 16px 0; }}
.eng-sec-head {{ font-size: 15px; color: var(--gold-l); text-align: center; border-bottom: 1px solid rgba(212,175,55,0.25); padding-bottom: 6px; margin-bottom: 12px; }}
.eng-time-card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 10px 12px; margin-bottom: 8px; }}
.eng-time-card b {{ font-size: 13px; color: var(--gold-l); display: block; }}
.eng-time-card p {{ font-size: 11.5px; color: #CBD5E1; margin: 2px 0; }}
.eng-time-card small {{ font-size: 10.5px; color: #94A3B8; }}
.eng-closing {{ font-family: var(--script); font-size: 22px; color: var(--gold-l); margin-top: 14px; }}

/* Wedding Royal Rajputana Mandap Specific */
.wed-royal-banner {{ text-align: center; margin-bottom: 14px; }}
.wed-sloka {{ font-family: var(--serif); font-size: 13.5px; color: var(--wine); font-weight: 700; margin-bottom: 4px; }}
.wed-symbol {{ font-size: 14px; color: var(--gold); }}
.wed-title {{ font-family: var(--serif); font-size: 32px; color: var(--wine-d); margin: 2px 0; }}
.wed-sub {{ font-family: var(--cap); font-size: 13px; color: var(--rose-d); text-transform: uppercase; letter-spacing: 2px; }}
.wed-stage-card {{ background: #FFFDF8; border: 2px solid var(--gold); border-radius: 26px; box-shadow: 0 20px 50px rgba(6,78,59,0.15); max-width: 440px; width: 100%; padding: 24px 20px; text-align: center; box-sizing: border-box; }}
.wed-hero-arch {{ width: 100%; height: 210px; border-radius: 20px; overflow: hidden; border: 2px solid var(--gold); margin-bottom: 16px; }}
.wed-hero-arch img {{ width: 100%; height: 100%; object-fit: cover; }}
.wed-couple-names {{ font-family: var(--serif); font-size: 28px; color: var(--wine); margin: 6px 0; }}
.wed-date-ribbon {{ font-family: var(--cap); font-size: 13.5px; color: var(--rose-d); font-weight: 700; margin: 4px 0; }}
.wed-venue-tag {{ font-size: 13px; color: #4B5563; margin: 2px 0 16px; }}
.wed-couple-portraits {{ display: flex; align-items: center; justify-content: center; gap: 14px; background: rgba(212,175,55,0.08); border: 1px solid rgba(212,175,55,0.35); border-radius: 18px; padding: 14px; margin: 14px 0; }}
.wed-person-card {{ text-align: center; }}
.wed-person-card img {{ width: 85px; height: 110px; border-radius: 14px; border: 1.5px solid var(--gold); object-fit: cover; box-shadow: 0 4px 10px rgba(0,0,0,0.12); }}
.wed-person-card b {{ display: block; font-size: 13px; color: var(--wine); margin-top: 4px; }}
.wed-person-card small {{ font-size: 10.5px; color: #6B7280; display: block; }}
.wed-mandap-knot {{ font-size: 22px; color: var(--gold); }}
.wed-sacred-quote {{ font-family: var(--serif); font-style: italic; font-size: 14px; color: var(--wine-d); line-height: 1.5; margin: 14px 0; }}
.wed-functions-box {{ text-align: left; margin: 18px 0; }}
.wed-sec-title {{ font-family: var(--serif); font-size: 18px; color: var(--wine); text-align: center; border-bottom: 1px solid rgba(212,175,55,0.3); padding-bottom: 6px; margin-bottom: 12px; }}
.wed-ceremony-item {{ display: flex; gap: 10px; background: #FFF; border: 1px solid #E5E7EB; border-radius: 12px; padding: 10px; margin-bottom: 10px; }}
.wed-c-icon {{ font-size: 16px; color: var(--gold); line-height: 1.2; }}
.wed-ceremony-item b {{ font-size: 13.5px; color: var(--wine); display: block; }}
.wed-ceremony-item p {{ font-size: 12px; color: var(--rose-d); margin: 2px 0; }}
.wed-ceremony-item small {{ font-size: 10.5px; color: #6B7280; display: block; }}
.wed-footer-quote {{ font-family: var(--script); font-size: 22px; color: var(--wine); margin-top: 14px; }}
</style>
</head>
<body class="is-locked">

<div class="top-template-badge">Template #{t['id']:02d} · {t['category']}</div>

<!-- ============ OPENING COVER SCREEN ============ -->
<section class="call" id="call">
  <div class="call__bg" style="background-image:url('{t['hero_img']}')"></div>
  <div class="call__couple" style="background-image:url('{t['cover_img']}')"></div>
  <div class="call__shade"></div>
  <div class="call__status">
    <span>9:41</span>
    <span class="call__icons"><i></i><i></i><i></i><b></b></span>
  </div>
  <div class="call__top">
    <p class="call__label" id="guestCallLabel">Incoming Invitation<span class="dots"><i>.</i><i>.</i><i>.</i></span></p>
    <h1 class="call__names"><span>{t['celebrants']}</span></h1>
    <p class="call__sub">{t['date_str']}</p>
  </div>
  <div class="call__bottom">
    <button class="call__magic" type="button" onclick="answerCall()">✨ Tap or Slide to Open</button>
    <div class="slider" id="slider">
      <div class="slider__fill"></div>
      <div class="slider__text"><b>slide</b>&nbsp;to open</div>
      <button class="slider__knob" id="knob" type="button" aria-label="Slide to open">
        <svg viewBox="0 0 24 24"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z"/></svg>
      </button>
    </div>
    <span class="call__home"></span>
  </div>
</section>

<!-- ============ AMBIENT CANVAS ============ -->
<div class="ambient" aria-hidden="true"><div class="ambient__bg"></div></div>
<canvas class="petals" id="petals" aria-hidden="true"></canvas>

<!-- ============ INVITATION STAGE ============ -->
<div class="inv-main-wrap">
  {header_banner}
  {stage_content}
</div>

<!-- ============ FLOATING ACTION BAR ============ -->
<div id="rpActionBar" style="position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:9999;display:flex;gap:10px;align-items:center;background:rgba(255,255,255,0.96);backdrop-filter:blur(14px);padding:8px 16px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,0.2);border:1.5px solid var(--gold);font-family:var(--sans);">
  <a id="btnCustomize" href="../index.html" style="display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:var(--blush2);color:var(--wine);font-weight:700;font-size:12.5px;text-decoration:none;">
    <span>✎ Customize</span>
  </a>
  <button onclick="openSendModal()" type="button" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:999px;background:var(--wine);color:var(--gold-l);font-weight:700;font-size:12.5px;border:none;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,0.2);">
    <span>💌 Send to Desired Person</span>
  </button>
</div>

<!-- ============ MODAL: SEND TO DESIRED PERSON ============ -->
<div id="sendModal" style="display:none;position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,0.65);backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:16px;">
  <div style="background:#fff;border-radius:24px;max-width:440px;width:100%;padding:24px;box-shadow:0 25px 60px rgba(0,0,0,0.4);border:2px solid var(--gold);font-family:var(--sans);position:relative;color:#111;">
    <button onclick="closeSendModal()" type="button" style="position:absolute;top:16px;right:16px;border:none;background:none;font-size:24px;color:#6B7280;cursor:pointer;">×</button>
    
    <div style="text-align:center;margin-bottom:16px;">
      <div style="width:44px;height:44px;border-radius:50%;background:var(--wine);color:var(--gold-l);display:inline-flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:6px;">💌</div>
      <h3 style="font-family:var(--serif);font-size:24px;color:var(--wine);margin:0;">Send Invitation</h3>
      <p style="font-size:12.5px;color:#6B7280;margin:3px 0 0;">Deliver directly to the correct WhatsApp number or Email</p>
    </div>

    <div style="margin-bottom:12px;text-align:left;">
      <label style="display:block;font-size:11px;font-weight:700;text-transform:uppercase;color:var(--wine);margin-bottom:4px;">Guest / Family Name *</label>
      <input type="text" id="targetGuestName" placeholder="e.g. Priya &amp; Rohan, The Sharma Family" style="width:100%;box-sizing:border-box;padding:9px 12px;border:1.5px solid #D1D5DB;border-radius:10px;font-size:13.5px;outline:none;">
    </div>

    <div style="margin-bottom:14px;text-align:left;">
      <label style="display:block;font-size:11px;font-weight:700;text-transform:uppercase;color:var(--wine);margin-bottom:4px;">Guest Mobile Number *</label>
      <div style="display:flex;gap:6px;">
        <select id="countryCodeSelect" style="width:100px;padding:9px 8px;border:1.5px solid #D1D5DB;border-radius:10px;font-size:13px;background:#F9FAFB;">
          <option value="91">+91 (IN)</option>
          <option value="1">+1 (US/CA)</option>
          <option value="44">+44 (UK)</option>
          <option value="971">+971 (UAE)</option>
          <option value="61">+61 (AU)</option>
          <option value="65">+65 (SG)</option>
        </select>
        <input type="tel" id="targetGuestPhone" placeholder="10-digit number" style="flex:1;padding:9px 12px;border:1.5px solid #D1D5DB;border-radius:10px;font-size:13.5px;outline:none;">
      </div>
    </div>

    <div style="margin-bottom:14px;text-align:left;">
      <label style="display:block;font-size:11px;font-weight:700;text-transform:uppercase;color:var(--wine);margin-bottom:4px;">Guest Email (Optional)</label>
      <input type="email" id="targetGuestEmail" placeholder="guest@example.com" style="width:100%;box-sizing:border-box;padding:9px 12px;border:1.5px solid #D1D5DB;border-radius:10px;font-size:13.5px;outline:none;">
    </div>

    <div style="display:flex;flex-direction:column;gap:8px;">
      <button onclick="sendViaWhatsApp()" type="button" class="btn btn--wa" style="width:100%;padding:11px;border-radius:12px;font-size:13.5px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:6px;">
        <span>Send Directly on WhatsApp</span>
      </button>

      <button onclick="sendViaEmail()" type="button" class="btn btn--soft" style="width:100%;padding:10px;border-radius:12px;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:6px;">
        <span>Send via Email</span>
      </button>

      <button onclick="copyPersonalizedLink()" id="btnCopyPersonal" type="button" class="btn btn--ghost" style="width:100%;padding:10px;border-radius:12px;font-size:13px;font-weight:600;">
        <span>Copy Personalized Link</span>
      </button>
    </div>
  </div>
</div>

<!-- ============ AUDIO ============ -->
<audio id="bgMusic" src="../audio/romantic_piano.mp3" loop preload="auto"></audio>

<script>
var opened = false;
function answerCall() {{
  if (opened) return;
  opened = true;
  document.getElementById('call').classList.add('is-answered');
  document.body.classList.remove('is-locked');
  var m = document.getElementById('bgMusic');
  if (m) {{ m.play().catch(function(){{}}); }}
}}

// FOOLPROOF SLIDER DRAG ENGINE
(function() {{
  var slider = document.getElementById('slider');
  var knob = document.getElementById('knob');
  if (!slider || !knob) return;

  var dragging = false;
  var sx0 = 0;
  var prog = 0;

  function getMaxDist() {{
    var sw = slider.clientWidth || slider.offsetWidth || 300;
    var kw = knob.offsetWidth || knob.clientWidth || 68;
    return Math.max(60, sw - kw - 14);
  }}

  function setProgress(p) {{
    prog = Math.max(0, Math.min(1, p));
    slider.style.setProperty('--p', prog);
    var maxD = getMaxDist();
    knob.style.transform = 'translateX(' + (maxD * prog) + 'px)';
    var fill = slider.querySelector('.slider__fill');
    if (fill) fill.style.width = 'calc(68px + ' + (maxD * prog) + 'px)';
  }}

  function start(cx) {{
    if (opened) return;
    dragging = true;
    sx0 = cx;
    slider.classList.add('is-drag');
    slider.classList.remove('is-back');
  }}

  function move(cx) {{
    if (!dragging || opened) return;
    var maxD = getMaxDist();
    setProgress((cx - sx0) / maxD);
  }}

  function finish(cx) {{
    if (!dragging) return;
    dragging = false;
    slider.classList.remove('is-drag');
    var moved = cx !== undefined ? Math.abs(cx - sx0) : 0;
    if (prog > 0.5 || moved < 8) {{
      setProgress(1);
      answerCall();
    }} else {{
      slider.classList.add('is-back');
      setProgress(0);
    }}
  }}

  knob.addEventListener('pointerdown', function(e) {{
    start(e.clientX);
    try {{ knob.setPointerCapture(e.pointerId); }} catch (_) {{}}
  }});
  knob.addEventListener('touchstart', function(e) {{
    if (e.touches && e.touches[0]) start(e.touches[0].clientX);
  }}, {{ passive: true }});
  knob.addEventListener('click', function(e) {{
    e.stopPropagation();
    answerCall();
  }});

  window.addEventListener('pointermove', function(e) {{ if (dragging) move(e.clientX); }});
  window.addEventListener('pointerup', function(e) {{ if (dragging) finish(e.clientX); }});
  window.addEventListener('pointercancel', function() {{ if (dragging) finish(); }});

  window.addEventListener('touchmove', function(e) {{
    if (dragging && e.touches && e.touches[0]) move(e.touches[0].clientX);
  }}, {{ passive: true }});
  window.addEventListener('touchend', function() {{ if (dragging) finish(); }}, {{ passive: true }});

  slider.addEventListener('click', function() {{
    if (!opened) answerCall();
  }});
}})();

// DYNAMIC OCCASION PARTICLES ENGINE
(function () {{
  var c = document.getElementById('petals');
  if (!c) return;
  var x = c.getContext('2d'), P = [], W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1);
  var cat = "{cat_key}";
  var isBday = cat === "birthday";
  var isHw = cat === "housewarming";
  var isBaby = cat === "babyshower";

  var cols = ['#f4a7b5', '#ee8fa3', '#f9c5cf', '#e77d93']; // Wedding petals
  if (isBday) cols = ['#FFD700', '#00E5FF', '#FF1493', '#00E676', '#FFEB3B', '#D500F9'];
  else if (isHw) cols = ['#FFA000', '#FFD54F', '#FF6D00', '#FFE082'];
  else if (isBaby) cols = ['#81D4FA', '#F48FB1', '#FFF59D', '#B39DDB'];

  function size() {{ W = c.clientWidth; H = c.clientHeight; c.width = W * dpr; c.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0); }}
  function mk() {{
    return {{
      x: Math.random() * W, y: -20 - Math.random() * 80,
      w: isBday ? (8 + Math.random() * 12) : 8, h: isBday ? (4 + Math.random() * 8) : 8,
      r: 5 + Math.random() * 6, vy: isBday ? (1.5 + Math.random() * 2) : (0.8 + Math.random() * 1.2),
      vx: -0.4 + Math.random() * 0.8, a: Math.random() * 6.28, va: 0.04 * (Math.random() > 0.5 ? 1 : -1),
      sw: Math.random() * 6.28, c: cols[(Math.random() * cols.length) | 0]
    }};
  }}
  function draw(p) {{
    x.save(); x.translate(p.x, p.y); x.rotate(p.a); x.fillStyle = p.c; x.globalAlpha = 0.88;
    if (isBday) {{
      x.scale(1, Math.sin(p.sw)); x.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
    }} else {{
      x.scale(1, 0.6 + 0.4 * Math.sin(p.sw)); x.beginPath();
      x.moveTo(0, -p.r); x.bezierCurveTo(p.r, -p.r, p.r, p.r * 0.6, 0, p.r);
      x.bezierCurveTo(-p.r, p.r * 0.6, -p.r, -p.r, 0, -p.r); x.fill();
    }}
    x.restore();
  }}
  function loop() {{
    x.clearRect(0, 0, W, H);
    while (P.length < 16) P.push(mk());
    for (var i = P.length - 1; i >= 0; i--) {{
      var p = P[i]; p.y += p.vy; p.sw += 0.05; p.x += p.vx; p.a += p.va;
      if (p.y > H + 25) P.splice(i, 1); else draw(p);
    }}
    requestAnimationFrame(loop);
  }}
  window.addEventListener('resize', size); size(); requestAnimationFrame(loop);
}})();

function openSendModal() {{
  document.getElementById('sendModal').style.display = 'flex';
}}
function closeSendModal() {{
  document.getElementById('sendModal').style.display = 'none';
}}

function getCleanUrl() {{
  var href = window.location.href.split('#')[0].split('?')[0];
  var guest = document.getElementById('targetGuestName').value.trim();
  return href + (guest ? '?to=' + encodeURIComponent(guest) : '');
}}

function sendViaWhatsApp() {{
  var guest = document.getElementById('targetGuestName').value.trim() || 'Honored Guest';
  var cc = (document.getElementById('countryCodeSelect').value || '91').replace(/\D/g, '');
  var rawPhone = document.getElementById('targetGuestPhone').value.trim().replace(/\D/g, '').replace(/^0+/, '');
  var fullPhone = rawPhone ? (cc + rawPhone) : '';
  var link = getCleanUrl();
  var text = encodeURIComponent("Dearest " + guest + ",\n\nYou are cordially invited to celebrate the " + "{t['title']}" + "! ❦\n\nDate: " + "{t['date_str']}" + "\nVenue: " + "{t['venue']}" + "\n\nOpen your personalized animated invitation here:\n" + link + "\n\nWith love,\n" + "{t['celebrants']}");
  var url = fullPhone ? ('https://api.whatsapp.com/send?phone=' + fullPhone + '&text=' + text) : ('https://api.whatsapp.com/send?text=' + text);
  window.open(url, '_blank');
  closeSendModal();
}}

function sendViaEmail() {{
  var guest = document.getElementById('targetGuestName').value.trim() || 'Honored Guest';
  var email = document.getElementById('targetGuestEmail').value.trim();
  var link = getCleanUrl();
  var subject = encodeURIComponent("Invitation: " + "{t['title']}");
  var body = encodeURIComponent("Dearest " + guest + ",\n\nWe cordially invite you to celebrate the " + "{t['title']}" + " on " + "{t['date_str']}" + " at " + "{t['venue']}" + ".\n\nOpen your interactive invitation here:\n" + link + "\n\nWith love,\n" + "{t['celebrants']}");

  window.location.href = 'mailto:' + (email || '') + '?subject=' + subject + '&body=' + body;
  closeSendModal();
}}

function copyPersonalizedLink() {{
  var link = getCleanUrl();
  navigator.clipboard.writeText(link);
  var btn = document.getElementById('btnCopyPersonal');
  btn.textContent = '✓ Copied Link to Clipboard!';
  setTimeout(function() {{ btn.textContent = 'Copy Personalized Link'; }}, 2200);
}}

window.addEventListener('DOMContentLoaded', function() {{
  var m = /[?&]to=([^&#]+)/.exec(window.location.search);
  if (m) {{
    var g = decodeURIComponent(m[1].replace(/\+/g, ' '));
    var label = document.getElementById('guestCallLabel');
    if (label) label.innerHTML = 'Incoming call for <b>' + g + '</b><span class="dots"><i>.</i><i>.</i><i>.</i></span>';
  }}
}});
</script>
</body>
</html>"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print(f"Successfully generated {len(templates_data)} standalone templates in {TEMPLATES_DIR}!")

md_content = "# GoldenVows — 60 Unique Invitation Templates Catalog\n\n"
md_content += "Each template is an independent, mobile and laptop-friendly animated invitation featuring occasion-specific visual layouts (Royal Rajputana Mandap, Tuscan Minimalist, Starlight Ring Halo, Pastel Baby Cloud, VIP Concert Ticket, Vedic Griha Pravesh Sanctuary), touch-and-drag slider openers, real-time countdown, Google Maps navigation, RSVP, and direct WhatsApp / Email dispatching to the correct recipient number.\n\n"
md_content += "| # | Template Name | Category | Palette | Local URL | Live GitHub Pages URL |\n"
md_content += "|---|---|---|---|---|---|\n"

for t in templates_data:
    local_url = f"http://localhost:8000/templates/{t['slug']}.html"
    gh_url = f"https://urvashizoopcoder-hub.github.io/GoldenVows/templates/{t['slug']}.html"
    md_content += f"| {t['id']:02d} | **{t['name']}** | {t['category']} | {t['palette_name']} | [Open Locally]({local_url}) | [Open on GitHub Pages]({gh_url}) |\n"

with open(r"c:\\Users\\URVASHI BHARTI\\OneDrive\\Desktop\\zoop\\TEMPLATES.md", "w", encoding="utf-8") as f:
    f.write(md_content)
print("Generated TEMPLATES.md catalog table!")
