import os, json

OUTPUT_DIR = r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\templates"
ASSETS_DIR = r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 60 distinct wedding themes
templates = [
    # 1. Royal Rajputana Mandap
    {"id": 1, "slug": "01-royal-rajputana-mandap", "name": "Royal Rajputana Mandap", "style": "rajputana",
     "wine": "#064E3B", "wine_d": "#022C22", "rose": "#047857", "rose_d": "#065F46", "gold": "#D4AF37", "gold_l": "#FDE68A", "blush": "#F6F3EB", "blush2": "#EFEAD8", "ivory": "#FCFBF7", "ink": "#132A13",
     "title": "Aarav & Ananya — Royal Rajputana Wedding", "subtitle": "Auspicious Heritage Mandap Ceremony", "eyebrow": "॥ Shree Ganeshaya Namah ॥ Together with their families",
     "groom": "Aarav", "groom_full": "Aarav Malhotra", "groom_par": "Son of Mr. Rajiv & Mrs. Neelam Malhotra",
     "bride": "Ananya", "bride_full": "Ananya Kapoor", "bride_par": "Daughter of Mr. Vikram & Mrs. Shalini Kapoor",
     "date_str": "Sunday, 14th February 2027", "time_str": "7:30 PM", "venue": "Jag Mandir Island Palace, Udaipur", "venue_addr": "Lake Pichola, Udaipur, Rajasthan 313001",
     "quote": "Two souls, one sacred vow, united forever in love, faith and Rajputana royal grace.", "closing": "Your presence and blessings are our greatest treasure.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 2. Udaipur Pichola Water Pavilion
    {"id": 2, "slug": "02-udaipur-lake-pichola", "name": "Udaipur Pichola Water Pavilion", "style": "udaipur",
     "wine": "#1E3A8A", "wine_d": "#172554", "rose": "#3B82F6", "rose_d": "#1D4ED8", "gold": "#F59E0B", "gold_l": "#FDE68A", "blush": "#EFF6FF", "blush2": "#DBEAFE", "ivory": "#F8FAFC", "ink": "#0F172A",
     "title": "Kabir & Tara — Lake Pichola Waterscape", "subtitle": "Shimmering Palace Floating Waters", "eyebrow": "Under the celestial Udaipur sky · Royal Wedding of",
     "groom": "Kabir", "groom_full": "Kabir Singhania", "groom_par": "Son of Mr. Devendra & Mrs. Sunita Singhania",
     "bride": "Tara", "bride_full": "Tara Raichand", "bride_par": "Daughter of Mr. Harsh & Mrs. Gayatri Raichand",
     "date_str": "Friday, 19th February 2027", "time_str": "6:00 PM", "venue": "The Oberoi Udaivilas, Lake Pichola", "venue_addr": "Haridas Ji Ki Magri, Udaipur 313001",
     "quote": "Reflected in the golden ripples of Pichola, our journey of eternity begins.", "closing": "Grace our royal celebration with your heartfelt blessings.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 3. Jaipur Hawa Mahal Regal Pink
    {"id": 3, "slug": "03-jaipur-hawa-mahal-pink", "name": "Jaipur Hawa Mahal Regal Pink", "style": "jaipur",
     "wine": "#831843", "wine_d": "#500724", "rose": "#BE185D", "rose_d": "#9D174D", "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FDF2F8", "blush2": "#FCE7F3", "ivory": "#FFF1F2", "ink": "#4C0519",
     "title": "Ranveer & Isha — The Pink City Royal Union", "subtitle": "Heritage Jharokha Mandap Ceremony", "eyebrow": "Padharo Mhare Desh · Royal Wedding of",
     "groom": "Ranveer", "groom_full": "Ranveer Rathore", "groom_par": "Son of Late Maharaja Digvijay Rathore",
     "bride": "Isha", "bride_full": "Isha Shekhawat", "bride_par": "Daughter of Thakur Raghuvir Shekhawat",
     "date_str": "Saturday, 27th February 2027", "time_str": "7:00 PM", "venue": "Rambagh Palace, Jaipur", "venue_addr": "Bhawani Singh Rd, Jaipur 302005",
     "quote": "Amidst pink sandstone jharokhas and royal trumpets, love finds its forever palace.", "closing": "With loving pranaam and royal hospitality.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 4. Mughal Shahi Bagh & Cypress
    {"id": 4, "slug": "04-mughal-gardens-cypress", "name": "Mughal Shahi Bagh & Cypress", "style": "mughal",
     "wine": "#14532D", "wine_d": "#052E16", "rose": "#15803D", "rose_d": "#166534", "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#F0FDF4", "blush2": "#DCFCE7", "ivory": "#F7FEE7", "ink": "#022C22",
     "title": "Zayn & Mehr — Shahi Bagh Matrimony", "subtitle": "Scent of Jasmine & Marble Fountains", "eyebrow": "In the name of the Divine · The Royal Wedding of",
     "groom": "Zayn", "groom_full": "Zayn Mirza", "groom_par": "Son of Nawab Hamid Mirza & Begum Shahnaz",
     "bride": "Mehr", "bride_full": "Mehr Siddiqui", "bride_par": "Daughter of Dr. Tariq Siddiqui & Mrs. Yasmeen",
     "date_str": "Sunday, 7th March 2027", "time_str": "6:30 PM", "venue": "Taj Falaknuma Palace, Hyderabad", "venue_addr": "Engine Bowli, Fatima Nagar, Falaknuma, Hyderabad 500053",
     "quote": "Two fragrant flowers blossomed in the celestial garden of destiny.", "closing": "Shukran for gracing our auspicious union.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 5. Jodhpur Mehrangarh Royal Indigo
    {"id": 5, "slug": "05-jodhpur-sun-city-indigo", "name": "Jodhpur Mehrangarh Royal Indigo", "style": "jodhpur",
     "wine": "#1E1B4B", "wine_d": "#0F0E2A", "rose": "#4338CA", "rose_d": "#3730A3", "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#EEF2FF", "blush2": "#E0E7FF", "ivory": "#F8FAFC", "ink": "#1E1B4B",
     "title": "Vikramaditya & Radhika — Sun City Vivah", "subtitle": "Under the Majestic Mehrangarh Fort", "eyebrow": "Shree Karni Kripa · An Auspicious Wedding",
     "groom": "Vikramaditya", "groom_full": "Vikramaditya Singh", "groom_par": "Son of Mr. Sumer Singh & Mrs. Gayatri Devi",
     "bride": "Radhika", "bride_full": "Radhika Bhati", "bride_par": "Daughter of Mr. Mohan Bhati & Mrs. Pushpa Bhati",
     "date_str": "Saturday, 13th March 2027", "time_str": "7:00 PM", "venue": "Umaid Bhawan Palace, Jodhpur", "venue_addr": "Circuit House Rd, Cantt Area, Jodhpur 342006",
     "quote": "Where desert sands touch golden sunrays, our vows stand strong as Mehrangarh.", "closing": "Padharo sa to bless the couple.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 6. South Indian Temple Kanjeevaram
    {"id": 6, "slug": "06-south-temple-kanjeevaram", "name": "South Indian Temple Kanjeevaram", "style": "south_temple",
     "wine": "#7C2D12", "wine_d": "#431407", "rose": "#C2410C", "rose_d": "#9A3412", "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FFFBEB", "blush2": "#FEF3C7", "ivory": "#FFFDF5", "ink": "#451A03",
     "title": "Karthik & Meenakshi — Kalyana Mahotsavam", "subtitle": "Sacred Nadaswaram & Mangalyam", "eyebrow": "॥ Hari Om ॥ Shree Venkateshwara Prasanna",
     "groom": "Karthik", "groom_full": "Karthik Subramanian", "groom_par": "Son of Sri K. Subramanian & Smt. Lakshmi",
     "bride": "Meenakshi", "bride_full": "Meenakshi Iyer", "bride_par": "Daughter of Sri R. Narayanan & Smt. Saraswathi",
     "date_str": "Monday, 22nd March 2027", "time_str": "8:30 AM", "venue": "The Leela Kovalam, Trivandrum", "venue_addr": "Kovalam Beach Rd, Trivandrum 695527",
     "quote": "Tied with sacred yellow thread and blessed by holy mantras, two souls merge into one.", "closing": "Seeking your warm blessings and Mangalya Prarthana.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 7. Kerala Backwaters Greenery
    {"id": 7, "slug": "07-kerala-backwaters-greenery", "name": "Kerala Backwaters & Jasmine", "style": "kerala",
     "wine": "#064E3B", "wine_d": "#022C22", "rose": "#059669", "rose_d": "#047857", "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#ECFDF5", "blush2": "#D1FAE5", "ivory": "#F0FDF4", "ink": "#064E3B",
     "title": "Madhav & Anupama — Backwater Vows", "subtitle": "Swaying Palms & Coconut Grove Mandap", "eyebrow": "With the divine grace of Guruvayurappan",
     "groom": "Madhav", "groom_full": "Madhav Menon", "groom_par": "Son of Sri Balachandran Menon & Smt. Geetha",
     "bride": "Anupama", "bride_full": "Anupama Nair", "bride_par": "Daughter of Sri Jayakumar Nair & Smt. Shylaja",
     "date_str": "Sunday, 28th March 2027", "time_str": "10:15 AM", "venue": "Kumarakom Lake Resort, Kottayam", "venue_addr": "Vembanad Lake, Kumarakom 686566",
     "quote": "Like gentle waves of Vembanad lake, our love flows peaceful, deep and timeless.", "closing": "Please join us for a traditional sadhya and auspicious blessings.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 8. Maratha Royal Peshwa Shahi
    {"id": 8, "slug": "08-maratha-peshwa-shahi", "name": "Maratha Royal Peshwa Shahi", "style": "maratha",
     "wine": "#581C87", "wine_d": "#3B0764", "rose": "#7E22CE", "rose_d": "#6B21A8", "gold": "#D97706", "gold_l": "#FDE68A", "blush": "#FAF5FF", "blush2": "#F3E8FF", "ivory": "#FCFBF7", "ink": "#3B0764",
     "title": "Shantanu & Sai — Shahi Maratha Vivah", "subtitle": "A Royal Peshwai Wedding Ceremony", "eyebrow": "॥ श्री महालक्ष्मी प्रसन्न ॥ शुभ विवाह",
     "groom": "Shantanu", "groom_full": "Shantanu Deshmukh", "groom_par": "Son of Srimant Prataprao Deshmukh",
     "bride": "Sai", "bride_full": "Sai Jadhav", "bride_par": "Daughter of Srimant Anandrao Jadhav",
     "date_str": "Thursday, 1st April 2027", "time_str": "11:30 AM", "venue": "Fort JadhavGADH, Pune", "venue_addr": "Hadapsar-Saswad Rd, Pune 412301",
     "quote": "Bowed in front of Bhavani Mata, we pledge an unbreakable lifetime of honor and devotion.", "closing": "Your blessings will crown our royal auspicious wedding.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 9. Bengali Zamindar Rajbari Alta
    {"id": 9, "slug": "09-bengali-zamindar-rajbari", "name": "Bengali Zamindar Rajbari Alta", "style": "bengali",
     "wine": "#881337", "wine_d": "#4C0519", "rose": "#BE123C", "rose_d": "#9F1239", "gold": "#CA8A04", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FFE4E6", "ivory": "#FFFDF5", "ink": "#4C0519",
     "title": "Devrat & Debolina — Shuvo Bibaho", "subtitle": "Heritage Rajbari Sindoor & Shankha Pola", "eyebrow": "॥ শ্রী শ্রী দুর্গা সহায় ॥ শুভ বিবাহ",
     "groom": "Devrat", "groom_full": "Devrat Banerjee", "groom_par": "Son of Sri Subhashish Banerjee & Smt. Sharmila",
     "bride": "Debolina", "bride_full": "Debolina Mukherjee", "bride_par": "Daughter of Sri Arindam Mukherjee & Smt. Pampa",
     "date_str": "Monday, 5th April 2027", "time_str": "7:00 PM", "venue": "The Rajbari Bawali, Kolkata", "venue_addr": "Bawali, 24 Parganas South, West Bengal 700137",
     "quote": "To the sound of conch shells and ulu dhwani, our souls unite for seven lifetimes.", "closing": "Please grace our Boron & reception dinner with your love.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"},

    # 10. Punjabi Anand Karaj & Kalire
    {"id": 10, "slug": "10-punjabi-anand-karaj-kalire", "name": "Punjabi Anand Karaj & Kalire", "style": "punjabi",
     "wine": "#9F1239", "wine_d": "#700A25", "rose": "#E11D48", "rose_d": "#BE123C", "gold": "#EAB308", "gold_l": "#FEF08A", "blush": "#FFF1F2", "blush2": "#FDE047", "ivory": "#FFFBEB", "ink": "#374151",
     "title": "Gurbaaz & Simran — Anand Karaj Splendor", "subtitle": "Phulkari, Dhol & Golden Kalire Ceremony", "eyebrow": "Ek Onkar Satnam · Together with their families",
     "groom": "Gurbaaz", "groom_full": "Gurbaaz Singh Dhillon", "groom_par": "Son of Sardar Harpreet Singh Dhillon & Sardarni Manjeet",
     "bride": "Simran", "bride_full": "Simran Kaur Grewal", "bride_par": "Daughter of Sardar Jagtar Singh Grewal & Sardarni Jasbir",
     "date_str": "Saturday, 10th April 2027", "time_str": "10:30 AM", "venue": "The Taj Swarna, Amritsar", "venue_addr": "Majitha Rd, Amritsar 143001",
     "quote": "Two bodies walking the four sacred Lavan, taking root as one pure soul.", "closing": "Sachi khushi hundi jad tussi aande ho! Looking forward to your warm presence.",
     "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"}
]

# Additional 50 Distinct Wedding Themes
themes_pool = [
    ("11-gujarati-lagan-mandvo", "Gujarati Lagan Mandvo & Patola", "gujarati", "#7C2D12", "#431407", "#EA580C", "#C2410C", "#CA8A04", "#FEF08A", "#FFFBEB", "#FEF3C7", "#FFFDF5", "#451A03", "Harsh", "Krishna", "Mangal Fera & Patola Mandap", "Surat Silk Heritage Haveli"),
    ("12-kashmiri-chinar-shikara", "Kashmiri Chinar & Shikara Autumn", "kashmiri", "#78350F", "#451A03", "#B45309", "#92400E", "#D97706", "#FDE68A", "#FEF3C7", "#FDE68A", "#FFFBEB", "#451A03", "Zubair", "Nida", "Chinar Autumn Nikah & Vivah", "The Lalit Grand Palace, Srinagar"),
    ("13-tuscan-sunlit-vineyard", "Tuscan Sunlit Vineyard & Cypress", "tuscan", "#365314", "#1A2E05", "#4D7C0F", "#3F6212", "#CA8A04", "#FEF08A", "#F7FEE7", "#ECFCCB", "#FDFBF7", "#1A2E05", "Matteo", "Sofia", "Olive Groves & Rustic Linen Vows", "Villa Cetinale, Tuscany"),
    ("14-santorini-aegean-sunset", "Santorini Aegean Blue & Pearl", "santorini", "#0C4A6E", "#082F49", "#0284C7", "#0369A1", "#F59E0B", "#FDE68A", "#F0F9FF", "#E0F2FE", "#FCFBF7", "#082F49", "Lucas", "Elena", "Whitewashed Caldera & Azure Waters", "Canaves Oia Suites, Santorini"),
    ("15-bali-tropical-ocean-palms", "Bali Tropical Palms & Lotus", "bali", "#064E3B", "#022C22", "#059669", "#047857", "#D97706", "#FDE68A", "#ECFDF5", "#D1FAE5", "#F0FDF4", "#064E3B", "Aron", "Maya", "Frangipani Canopy & Ocean Breeze", "Alila Villas Uluwatu, Bali"),
    ("16-french-chateau-bordeaux", "French Chateau Bordeaux & Gilt", "chateau", "#4A044E", "#2E0234", "#701A75", "#581C87", "#D4AF37", "#FDE68A", "#FAF5FF", "#F3E8FF", "#FCFBF7", "#2E0234", "Henri", "Camille", "Baroque Gold Gilt & Champagne", "Château de Chambord, France"),
    ("17-amalfi-coast-lemon-blossom", "Amalfi Coast Lemon Blossom", "amalfi", "#075985", "#0369A1", "#0284C7", "#0369A1", "#EAB308", "#FEF08A", "#F0F9FF", "#E0F2FE", "#FFFBEB", "#0C4A6E", "Marco", "Chiara", "Sunlit Citron Groves & Cliffside Vows", "Belmond Hotel Caruso, Amalfi"),
    ("18-dubai-desert-golden-oasis", "Dubai Desert Golden Dune Oasis", "dubai", "#78350F", "#451A03", "#B45309", "#92400E", "#D4AF37", "#FEF08A", "#FEF3C7", "#FDE68A", "#FFFDF5", "#451A03", "Sameer", "Layla", "Arabian Oud & Burnished Gold Mandap", "Bab Al Shams Desert Resort, Dubai"),
    ("19-swiss-alps-snow-white", "Swiss Alps Snow White Glamour", "swiss", "#1E293B", "#0F172A", "#334155", "#1E293B", "#94A3B8", "#E2E8F0", "#F8FAFC", "#F1F5F9", "#FFFFFF", "#0F172A", "Adrian", "Nicole", "Frosted Mountain Crystal & White Fur", "Badrutt's Palace Hotel, St. Moritz"),
    ("20-maldives-turquoise-lagoon", "Maldives Turquoise Lagoon Coral", "maldives", "#115E59", "#042F2E", "#0D9488", "#0F766E", "#F59E0B", "#FDE68A", "#F0FDFA", "#CCFBF1", "#FCFBF7", "#042F2E", "Rohan", "Rhea", "Barefoot Luxury Overwater Pavilion", "Soneva Fushi, Maldives"),
    ("21-vogue-editorial-minimalist", "Vogue Minimalist Monochrome", "editorial", "#18181B", "#09090B", "#27272A", "#18181B", "#D4AF37", "#FDE68A", "#FAFAFA", "#F4F4F5", "#FFFFFF", "#09090B", "Neil", "Tanya", "Haute Couture Monolith & Clean Serif", "The Pierre, New York City"),
    ("22-art-deco-gatsby-champagne", "Art Deco Great Gatsby 1920s", "artdeco", "#000000", "#18181B", "#27272A", "#18181B", "#FFD700", "#FFE57F", "#1C1917", "#292524", "#FAFAFA", "#FFD700", "Jay", "Daisy", "Geometric Brass Fans & Roaring Jazz", "The Plaza Hotel, Fifth Avenue"),
    ("23-starlight-constellation-navy", "Starlight Constellation Midnight", "starlight", "#0F172A", "#020617", "#1E293B", "#0F172A", "#38BDF8", "#BAE6FD", "#0F172A", "#1E293B", "#F8FAFC", "#38BDF8", "Sid", "Kriti", "Cosmic Stardust & Deep Midnight Sky", "The Glasshouse on the Creek"),
    ("24-champagne-toast-golden-glam", "Champagne Toast Golden Shimmer", "champagne", "#713F12", "#422006", "#854D0E", "#713F12", "#D4AF37", "#FEF08A", "#FEFCE8", "#FEF9C3", "#FFFDF5", "#422006", "Aryan", "Natasha", "Liquid Gold Glow & Crystal Flutes", "The Ritz-Carlton Grand Ballroom"),
    ("25-english-country-rose-garden", "English Country Garden Roses", "english_rose", "#831843", "#500724", "#9D174D", "#701A75", "#D4AF37", "#FDE68A", "#FDF2F8", "#FCE7F3", "#FFF1F2", "#500724", "Oliver", "Charlotte", "Walled Rose Gardens & Antique Lace", "Cliveden House, Berkshire"),
    ("26-bohemian-pampas-terracotta", "Boho Pampas Grass & Terracotta", "boho", "#9A3412", "#7C2D12", "#C2410C", "#9A3412", "#D97706", "#FDE68A", "#FFF7ED", "#FFEDD5", "#FFFDF5", "#7C2D12", "Noah", "Isla", "Wildflower Sunburst & Terracotta Arch", "Joshua Tree Desert Sanctuary"),
    ("27-renaissance-dark-moody-velvet", "Renaissance Dark Velvet Romance", "renaissance", "#4C0519", "#2D030F", "#700A25", "#4C0519", "#D4AF37", "#FEF08A", "#1C1917", "#292524", "#F5F5F4", "#D4AF37", "Sebastian", "Genevieve", "Dramatic Candlelight & Oil Canvas", "Palazzo Corsini, Florence"),
    ("28-victorian-botanical-wax-seal", "Victorian Fern & Wax Seal", "victorian", "#14532D", "#052E16", "#166534", "#14532D", "#B45309", "#FDE68A", "#F0FDF4", "#DCFCE7", "#FCFBF7", "#052E16", "Arthur", "Victoria", "Pressed Botanical Ferns & Gold Crest", "Highclere Castle, Hampshire"),
    ("29-sakura-cherry-blossom-zen", "Sakura Cherry Blossom & Zen", "sakura", "#9D174D", "#700A25", "#BE185D", "#9D174D", "#D4AF37", "#FEF08A", "#FFF1F2", "#FFE4E6", "#FCFBF7", "#700A25", "Ren", "Aoi", "Gentle Spring Petals & Stone Courtyard", "Hoshinoya Kyoto Sanctuary"),
    ("30-moroccan-riad-majorelle", "Moroccan Riad Majorelle & Brass", "moroccan", "#1E3A8A", "#172554", "#1D4ED8", "#1E3A8A", "#D97706", "#FDE68A", "#EFF6FF", "#DBEAFE", "#FFFDF5", "#172554", "Tariq", "Soraya", "Cobalt Mosaic Zellige & Pierced Brass", "La Mamounia Palace, Marrakech"),
    ("31-celestial-crescent-moon-gold", "Celestial Moon & Starry Glow", "celestial", "#1E1B4B", "#0F0E2A", "#312E81", "#1E1B4B", "#F59E0B", "#FDE68A", "#EEF2FF", "#E0E7FF", "#F8FAFC", "#0F0E2A", "Leo", "Celeste", "Golden Crescent Moon & Constellations", "Starlight Observatory Pavilion"),
    ("32-provence-lavender-fields", "Provence Lavender & Soft Lilac", "provence", "#4C1D95", "#2E1065", "#6D28D9", "#5B21B6", "#CA8A04", "#FEF08A", "#F5F3FF", "#EDE9FE", "#FAF5FF", "#2E1065", "Julien", "Chloe", "Purple Lavender Hills & Limestone Bastide", "Bastide de Gordes, Provence"),
    ("33-peacock-feather-royal-teal", "Peacock Feather Royal Teal", "peacock", "#064E3B", "#022C22", "#0F766E", "#115E59", "#D4AF37", "#FEF08A", "#F0FDFA", "#CCFBF1", "#FCFBF7", "#022C22", "Dev", "Ishita", "Mor Pankh Shahi Velvet Mandap", "Laxmi Vilas Palace, Vadodara"),
    ("34-sunset-coral-amber-ombre", "Sunset Coral & Amber Ombre", "sunset_ombre", "#9F1239", "#700A25", "#BE123C", "#9F1239", "#F59E0B", "#FDE68A", "#FFF1F2", "#FFE4E6", "#FFFBEB", "#700A25", "Sam", "Maya", "Golden Twilight Warm Coral Gradient", "Sunset Cliff Pavilion, Goa"),
    ("35-retro-70s-warm-nostalgia", "Retro 70s Honey & Warm Ochre", "retro70", "#78350F", "#451A03", "#B45309", "#92400E", "#EAB308", "#FEF08A", "#FFFBEB", "#FEF3C7", "#FFFDF5", "#451A03", "Sonny", "Cherie", "Warm Vintage Honey & Golden Curves", "Palm Springs Sun Villa"),
    ("36-nordic-winter-pine-amber", "Nordic Winter Pine & Diya", "nordic", "#064E3B", "#022C22", "#166534", "#14532D", "#D97706", "#FDE68A", "#F0FDF4", "#DCFCE7", "#F8FAFC", "#022C22", "Erik", "Freja", "Snow Fir Forests & Warm Diya Hearth", "Kakslauttanen Arctic Estate"),
    ("37-pastel-peony-peach-silk", "Pastel Peony & Peach Silk", "peony", "#831843", "#500724", "#BE185D", "#9D174D", "#D4AF37", "#FEF08A", "#FFF1F2", "#FFE4E6", "#FFFDF5", "#500724", "Aakash", "Pooja", "Layered Peonies & Organza Drapes", "ITC Grand Bharat, Gurugram"),
    ("38-mysore-silk-sandalwood", "Mysore Royal Silk & Sandalwood", "mysore", "#7C2D12", "#431407", "#9A3412", "#7C2D12", "#D4AF37", "#FEF08A", "#FFFBEB", "#FEF3C7", "#FFFDF5", "#431407", "Kiran", "Divya", "Chamundeshwari Krupa & Sandalwood", "Lalitha Mahal Palace, Mysore"),
    ("39-modern-abstract-slate-gold", "Modern Abstract Slate & Gold", "slate_gold", "#1E293B", "#0F172A", "#334155", "#1E293B", "#D4AF37", "#FEF08A", "#F8FAFC", "#F1F5F9", "#FFFFFF", "#0F172A", "Kunal", "Neha", "Contemporary Architectural Lines & Foil", "The St. Regis Ballroom, Mumbai"),
    ("40-golden-hour-city-rooftop", "Golden Hour Skyline Rooftop", "rooftop", "#4C0519", "#2D030F", "#881337", "#4C0519", "#F59E0B", "#FDE68A", "#FFF1F2", "#FFE4E6", "#FCFBF7", "#2D030F", "Dhruv", "Simran", "City Lights Romance & Fairy Light Canopy", "Aer Rooftop, Four Seasons Mumbai"),
    ("41-riviera-yacht-nautical-navy", "Riviera Yacht Nautical Navy", "riviera", "#1E3A8A", "#172554", "#1D4ED8", "#1E3A8A", "#D4AF37", "#FEF08A", "#EFF6FF", "#DBEAFE", "#FFFFFF", "#172554", "Christian", "Valerie", "White Deck Ocean Breeze & Champagne", "Hotel du Cap-Eden-Roc, Antibes"),
    ("42-botanical-glasshouse-fern", "Botanical Glasshouse & Fern", "glasshouse", "#064E3B", "#022C22", "#047857", "#065F46", "#CA8A04", "#FEF08A", "#F0FDF4", "#DCFCE7", "#FCFBF7", "#022C22", "Varun", "Rhea", "Victorian Conservatory & Tropics", "Kew Gardens Glasshouse, London"),
    ("43-royal-crimson-zardozi-gold", "Royal Crimson & Zardozi Gold", "zardozi", "#881337", "#4C0519", "#9F1239", "#881337", "#FFD700", "#FEF08A", "#FFF1F2", "#FFE4E6", "#FCFBF7", "#4C0519", "Aditya", "Sanjana", "Velvet Brocade & Basra Pearls Vivah", "City Palace Durbar Hall, Jaipur"),
    ("44-twilight-desert-lanterns", "Twilight Desert Brass Lanterns", "desert_lantern", "#3B0764", "#1E0338", "#581C87", "#3B0764", "#D97706", "#FDE68A", "#FAF5FF", "#F3E8FF", "#FCFBF7", "#1E0338", "Farhan", "Alizeh", "Dusk Horizon & Filigree Brass Glow", "Al Maha Desert Pavilion, Dubai"),
    ("45-whispering-eucalyptus-sage", "Whispering Eucalyptus & Sage", "eucalyptus", "#14532D", "#052E16", "#15803D", "#14532D", "#A16207", "#FEF08A", "#F0FDF4", "#DCFCE7", "#FCFBF7", "#052E16", "Liam", "Harper", "Sage Foliage, White Linen & Candlelight", "Meadowood Estate, Napa Valley"),
    ("46-midnight-electric-orchid", "Midnight Electric Orchid Glam", "orchid", "#581C87", "#3B0764", "#7E22CE", "#6B21A8", "#E2E8F0", "#F8FAFC", "#0F172A", "#1E1B4B", "#FAFAFA", "#E2E8F0", "Rishi", "Trisha", "Deep Midnight Velvet & Silver Shimmer", "The Taj Mahal Palace, Colaba"),
    ("47-sacred-golden-lotus-pond", "Sacred Golden Lotus Sanctuary", "lotus_sanctuary", "#064E3B", "#022C22", "#047857", "#065F46", "#D4AF37", "#FEF08A", "#ECFDF5", "#D1FAE5", "#FFFDF5", "#022C22", "Anand", "Shreya", "Golden Water Lily & Sacred Kund Mandap", "Wildflower Hall, Shimla"),
    ("48-rosewood-amber-inlay-luxe", "Rosewood & Amber Inlay Luxe", "rosewood", "#78350F", "#451A03", "#92400E", "#78350F", "#D4AF37", "#FEF08A", "#FEF3C7", "#FDE68A", "#FFFDF5", "#451A03", "Chaitanya", "Nupur", "Carved Rosewood & Brass Aarti Bells", "Chidambara Vilas, Chettinad"),
    ("49-coral-reef-pearl-aquamarine", "Coral Reef Pearl & Aquamarine", "coral_pearl", "#0E7490", "#083344", "#06B6D4", "#0891B2", "#FB7185", "#FECDD3", "#ECFEFF", "#CFFAFE", "#FFF1F2", "#083344", "Vivaan", "Kyra", "Mother-of-Pearl & Aquamarine Shimmer", "Qualia Resort, Great Barrier Reef"),
    ("50-imperial-sapphire-platinum", "Imperial Sapphire & Platinum", "sapphire", "#1E3A8A", "#172554", "#1D4ED8", "#1E3A8A", "#94A3B8", "#E2E8F0", "#EFF6FF", "#DBEAFE", "#FFFFFF", "#172554", "Raghav", "Gayatri", "Imperial Sapphire Pillars & Chandeliers", "Blenheim Palace Grand Saloon"),
    ("51-autumn-maple-chestnut-woods", "Autumn Maple & Chestnut Woods", "maple", "#7C2D12", "#431407", "#9A3412", "#7C2D12", "#CA8A04", "#FEF08A", "#FFF7ED", "#FFEDD5", "#FFFDF5", "#431407", "Rohan", "Megha", "Golden Maple Canopy & Rustic Timber", "The Fairmont Banff Springs, Alberta"),
    ("52-swiss-monochrome-typography", "Swiss Typographic Monolith", "swiss_mono", "#09090B", "#000000", "#18181B", "#09090B", "#71717A", "#E4E4E7", "#FAFAFA", "#F4F4F5", "#FFFFFF", "#000000", "Jai", "Maya", "Pristine Swiss Grid & Minimal Monolith", "Kunsthaus Zurich Hall"),
    ("53-vintage-kodak-sepia-grain", "Vintage Kodak Sepia & Grain", "kodak_sepia", "#78350F", "#451A03", "#B45309", "#92400E", "#D97706", "#FDE68A", "#FEF3C7", "#FDE68A", "#FFFDF5", "#451A03", "Aman", "Tara", "Grainy 35mm Film Love & Sepia Letters", "Heritage Haveli, Mandawa"),
    ("54-boho-sunburst-clay-arch", "Boho Sunburst & Clay Arch", "boho_sunburst", "#9A3412", "#7C2D12", "#C2410C", "#9A3412", "#D97706", "#FDE68A", "#FFF7ED", "#FFEDD5", "#FFFDF5", "#7C2D12", "Devansh", "Aashi", "Terracotta Clay Arches & Sunburst", "Suryagarh Desert Citadel, Jaisalmer"),
    ("55-banarasi-brocade-zari-weave", "Banarasi Brocade & Zari Weave", "banarasi", "#881337", "#4C0519", "#BE123C", "#881337", "#FFD700", "#FEF08A", "#FFF1F2", "#FFE4E6", "#FFFDF5", "#4C0519", "Kartikeya", "Shivani", "Ganga Ghat Diyas & Pure Zari Weave", "BrijRama Palace, Varanasi"),
    ("56-pichola-starry-reflections", "Pichola Starry Reflections", "pichola_night", "#0F172A", "#020617", "#1E293B", "#0F172A", "#F59E0B", "#FDE68A", "#0F172A", "#1E293B", "#FCFBF7", "#F59E0B", "Manish", "Preeti", "Midnight Waters & Floating Golden Diyas", "Taj Lake Palace Royal Courtyard"),
    ("57-crystal-chandelier-ballroom", "Crystal Chandelier Ballroom", "chandelier", "#3B0764", "#1E0338", "#4C1D95", "#3B0764", "#D4AF37", "#FEF08A", "#FAF5FF", "#F3E8FF", "#FFFFFF", "#1E0338", "Siddharth", "Avni", "Prismatic Crystal Cascades & Golden Waltz", "The Imperial Ballroom, New Delhi"),
    ("58-vintage-passport-wax-seal", "Vintage Passport & Airmail Seal", "passport", "#78350F", "#451A03", "#92400E", "#78350F", "#CA8A04", "#FEF08A", "#FEF3C7", "#FDE68A", "#FCFBF7", "#451A03", "Yash", "Natasha", "Airmail Border, Stamp & Passport Knot", "Grand Hotel Tremezzo, Lake Como"),
    ("59-tropical-hibiscus-mango", "Tropical Hibiscus & Mango Sunrise", "hibiscus", "#9F1239", "#700A25", "#BE123C", "#9F1239", "#F59E0B", "#FDE68A", "#FFF1F2", "#FFE4E6", "#FFFDF5", "#700A25", "Armaan", "Tara", "Red Hibiscus, Mango Twilight & Palms", "Rayavadee Resort, Krabi"),
    ("60-eternal-solitaire-diamond-gold", "Eternal Solitaire Diamond & Gold", "solitaire", "#0F172A", "#020617", "#1E293B", "#0F172A", "#D4AF37", "#FEF08A", "#F8FAFC", "#F1F5F9", "#FFFFFF", "#0F172A", "Aryaveer", "Sanaya", "Flawless Solitaire Halo & 24K Gold Vows", "The Leela Palace Grand Ballroom")
]

for idx, item in enumerate(themes_pool):
    tid = idx + 11
    slug, name, style, wine, wine_d, rose, rose_d, gold, gold_l, blush, blush2, ivory, ink, g_name, b_name, sub, venue = item
    templates.append({
        "id": tid, "slug": slug, "name": name, "style": style,
        "wine": wine, "wine_d": wine_d, "rose": rose, "rose_d": rose_d, "gold": gold, "gold_l": gold_l, "blush": blush, "blush2": blush2, "ivory": ivory, "ink": ink,
        "title": f"{g_name} & {b_name} — Royal Wedding Celebration", "subtitle": sub, "eyebrow": "॥ Shree Ganeshaya Namah ॥ Together with their families",
        "groom": g_name, "groom_full": f"{g_name} Singhania", "groom_par": f"Son of Mr. Rajesh & Mrs. Sunita {g_name} family",
        "bride": b_name, "bride_full": f"{b_name} Kapoor", "bride_par": f"Daughter of Mr. Vikram & Mrs. Shalini {b_name} family",
        "date_str": f"Saturday, {(10 + (tid % 18))}th February 2027", "time_str": "7:00 PM", "venue": venue, "venue_addr": "Lakeside Royal Heritage Estate, Udaipur",
        "quote": "Two souls united by destiny, blessed by elders, bound forever in sacred love.", "closing": "Your warm presence and blessings are our greatest gift.",
        "hero_img": "../assets/img/hero_palace.webp", "cover_img": "../assets/img/couple_call.webp", "c1_img": "../assets/img/groom.webp", "c2_img": "../assets/img/bride.webp"
    })

print(f"Total verified wedding templates to generate: {len(templates)}")

# Generate 60 unique wedding templates with distinctive visual designs and color themes
for t in templates:
    filename = f"{t['slug']}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Standard wedding ceremonies
    events = [
        {"name": "Haldi Ceremony", "date": "10:00 AM", "venue": "Lakeside Sun Courtyard", "dress": "Shades of Turmeric Yellow", "note": "Marigolds, dholak beats and joyous turmeric blessings."},
        {"name": "Mehendi & Sangeet", "date": "5:30 PM", "venue": "Grand Durbar Hall", "dress": "Indo-Western Celebration Glam", "note": "Henna art, choreographed musical performances and live DJ."},
        {"name": "The Royal Wedding (Pheras)", "date": "7:30 PM", "venue": t['venue'], "dress": "Regal Indian Traditional", "note": "Seven sacred pheras around the holy fire amidst Vedic mantras."},
        {"name": "Grand Reception & Dinner", "date": "8:30 PM", "venue": "Crystal Island Ballroom", "dress": "Black Tie / Royal Ethnic", "note": "An evening of toasts, lavish banquet dinner and dancing."}
    ]

    events_html = ""
    for ev in events:
        events_html += f"""
        <div class="wed-event-card">
          <div class="wed-ev-bullet">✦</div>
          <div class="wed-ev-info">
            <b>{ev['name']}</b>
            <span class="wed-ev-time">⏰ {ev['date']} · 📍 {ev['venue']}</span>
            <small>Dress: {ev['dress']}</small>
            <p>{ev['note']}</p>
          </div>
        </div>"""

    # Distinct layout styling based on style category
    style_key = t['style']
    layout_class = f"style-{style_key}"

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{t['title']} — GoldenVows #{t['id']:02d}</title>
<meta name="description" content="{t['subtitle']} - {t['groom_full']} & {t['bride_full']}">
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
html::-webkit-scrollbar, body::-webkit-scrollbar, ::-webkit-scrollbar, *::-webkit-scrollbar {{
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
  padding: 5px 14px;
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

.wed-header-banner {{
  text-align: center;
  margin-bottom: 16px;
}}
.wed-sloka-line {{
  font-family: var(--serif);
  font-size: 14px;
  color: var(--wine);
  font-weight: 700;
  letter-spacing: 1px;
  margin-bottom: 4px;
}}
.wed-orn-divider {{
  font-size: 16px;
  color: var(--gold);
  margin: 2px 0 6px;
}}
.wed-main-title {{
  font-family: var(--serif);
  font-size: 34px;
  color: var(--wine-d);
  letter-spacing: 2px;
  margin: 4px 0;
}}
.wed-sub-title {{
  font-family: var(--cap);
  font-size: 13.5px;
  color: var(--rose-d);
  text-transform: uppercase;
  letter-spacing: 2px;
}}

.wed-stage-card {{
  background: #FFFDF9;
  border: 2px solid var(--gold);
  border-radius: 26px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.14);
  max-width: 440px;
  width: 100%;
  padding: 24px 20px;
  text-align: center;
  box-sizing: border-box;
}}

.wed-hero-box {{
  position: relative;
  width: 100%;
  height: 220px;
  border-radius: 20px;
  overflow: hidden;
  border: 2px solid var(--gold);
  margin-bottom: 16px;
}}
.wed-hero-box img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}}
.wed-hero-tag {{
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(0,0,0,0.65);
  color: var(--gold-l);
  font-size: 10.5px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 999px;
  letter-spacing: 1px;
}}

.wed-couple-title {{
  font-family: var(--serif);
  font-size: 30px;
  color: var(--wine);
  margin: 6px 0;
}}
.wed-date-ribbon {{
  font-family: var(--cap);
  font-size: 14px;
  color: var(--rose-d);
  font-weight: 700;
  margin: 4px 0;
}}
.wed-venue-tag {{
  font-size: 13px;
  color: #4B5563;
  margin: 2px 0 16px;
}}

.wed-couple-row {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  background: rgba(212,175,55,0.08);
  border: 1px solid rgba(212,175,55,0.35);
  border-radius: 18px;
  padding: 14px;
  margin: 14px 0;
}}
.wed-person-card {{
  flex: 1;
  text-align: center;
}}
.wed-person-card img {{
  width: 85px;
  height: 110px;
  border-radius: 14px;
  border: 1.5px solid var(--gold);
  object-fit: cover;
  margin: 0 auto 6px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.12);
}}
.wed-person-card b {{
  display: block;
  font-size: 13px;
  color: var(--wine);
}}
.wed-person-card small {{
  font-size: 10.5px;
  color: #6B7280;
  display: block;
}}
.wed-mandap-knot {{
  font-size: 24px;
  color: var(--gold);
}}

.wed-quote {{
  font-family: var(--serif);
  font-style: italic;
  font-size: 14px;
  color: var(--wine-d);
  line-height: 1.5;
  margin: 14px 0;
}}

.wed-timeline {{
  text-align: left;
  margin: 18px 0;
}}
.wed-sec-head {{
  font-family: var(--serif);
  font-size: 18px;
  color: var(--wine);
  text-align: center;
  border-bottom: 1px solid rgba(212,175,55,0.3);
  padding-bottom: 6px;
  margin-bottom: 12px;
}}
.wed-event-card {{
  display: flex;
  gap: 10px;
  background: #FFF;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 12px;
  margin-bottom: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}}
.wed-ev-bullet {{
  font-size: 16px;
  color: var(--gold);
  line-height: 1.2;
}}
.wed-ev-info b {{
  display: block;
  font-size: 13.5px;
  color: var(--wine);
}}
.wed-ev-time {{
  display: block;
  font-size: 11.5px;
  color: var(--rose-d);
  font-weight: 600;
  margin: 2px 0;
}}
.wed-ev-info small {{
  display: block;
  font-size: 11px;
  color: #6B7280;
}}
.wed-ev-info p {{
  font-size: 11px;
  color: #9CA3AF;
  margin: 3px 0 0;
}}

.wed-map-card {{
  background: rgba(212, 175, 55, 0.1);
  border: 1px dashed var(--gold);
  border-radius: 14px;
  padding: 14px;
  margin: 14px 0;
}}
.wed-map-card h4 {{
  margin: 0 0 4px;
  font-size: 13.5px;
  color: var(--wine);
}}
.wed-map-card p {{
  font-size: 12px;
  color: #4B5563;
  margin: 0 0 10px;
}}
.btn-wed-map {{
  display: inline-block;
  background: var(--wine);
  color: var(--gold-l);
  font-size: 12px;
  font-weight: 700;
  padding: 8px 18px;
  border-radius: 999px;
  text-decoration: none;
}}

.wed-closing {{
  font-family: var(--script);
  font-size: 24px;
  color: var(--wine);
  margin-top: 14px;
}}
</style>
</head>
<body class="is-locked">

<div class="top-template-badge">Template #{t['id']:02d} · Wedding</div>

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
    <p class="call__label" id="guestCallLabel">Incoming Royal Wedding Call<span class="dots"><i>.</i><i>.</i><i>.</i></span></p>
    <h1 class="call__names"><span>{t['groom']} &amp; {t['bride']}</span></h1>
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
<div class="inv-main-wrap {layout_class}">
  <div class="wed-header-banner">
    <p class="wed-sloka-line">{t['eyebrow']}</p>
    <div class="wed-orn-divider">✦ ❦ ✦</div>
    <h2 class="wed-main-title">{t['groom']} &amp; {t['bride']}</h2>
    <p class="wed-sub-title">{t['subtitle']}</p>
  </div>

  <div class="wed-stage-card">
    <div class="wed-hero-box">
      <img src="{t['hero_img']}" alt="Wedding Pavilion">
      <span class="wed-hero-tag">Royal Matrimony</span>
    </div>

    <h1 class="wed-couple-title">{t['groom_full']} &amp; {t['bride_full']}</h1>
    <p class="wed-date-ribbon">✦ {t['date_str']} · {t['time_str']} ✦</p>
    <p class="wed-venue-tag">📍 {t['venue']}<br><small>{t['venue_addr']}</small></p>

    <div class="wed-couple-row">
      <div class="wed-person-card">
        <img src="{t['c1_img']}" alt="{t['groom']}">
        <b>{t['groom_full']}</b>
        <small>{t['groom_par']}</small>
      </div>
      <div class="wed-mandap-knot">❦</div>
      <div class="wed-person-card">
        <img src="{t['c2_img']}" alt="{t['bride']}">
        <b>{t['bride_full']}</b>
        <small>{t['bride_par']}</small>
      </div>
    </div>

    <blockquote class="wed-quote">“{t['quote']}”</blockquote>

    <div class="wed-timeline">
      <h3 class="wed-sec-head">Sacred Functions &amp; Ceremonies Itinerary</h3>
      {events_html}
    </div>

    <div class="wed-map-card">
      <h4>📍 Google Maps Navigation Route</h4>
      <p>{t['venue']} · {t['venue_addr']}</p>
      <a href="https://maps.google.com/?q={t['venue']}" target="_blank" rel="noopener" class="btn-wed-map">➤ Open Live Navigation Map</a>
    </div>

    <p class="wed-closing">“{t['closing']}”</p>
  </div>
</div>

<!-- ============ FLOATING ACTION BAR ============ -->
<div id="rpActionBar" style="position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:9999;display:flex;gap:10px;align-items:center;background:rgba(255,255,255,0.96);backdrop-filter:blur(14px);padding:8px 16px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,0.2);border:1.5px solid var(--gold);font-family:var(--sans);">
  <a id="btnCustomize" href="../index.html" style="display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:var(--blush2);color:var(--wine);font-weight:700;font-size:12.5px;text-decoration:none;">
    <span>✎ Customize</span>
  </a>
  <button id="btnAutoScroll" onclick="toggleAutoScroll()" type="button" style="display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:var(--blush);color:var(--wine);font-weight:700;font-size:12.5px;border:1px solid var(--gold);cursor:pointer;">
    <span>📜 Auto-Scroll</span>
  </button>
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
var autoScrolling = false;
var scrollTimer = null;

function toggleAutoScroll() {{
  if (autoScrolling) {{
    stopAutoScroll();
  }} else {{
    startAutoScroll();
  }}
}}

function startAutoScroll() {{
  autoScrolling = true;
  var btn = document.getElementById('btnAutoScroll');
  if (btn) btn.innerHTML = '<span>⏸ Pause</span>';
  if (scrollTimer) clearInterval(scrollTimer);
  scrollTimer = setInterval(function() {{
    if ((window.innerHeight + window.scrollY) >= (document.body.offsetHeight - 5)) {{
      stopAutoScroll();
      return;
    }}
    window.scrollBy({{ top: 1.5, behavior: 'auto' }});
  }}, 25);
}}

function stopAutoScroll() {{
  autoScrolling = false;
  var btn = document.getElementById('btnAutoScroll');
  if (btn) btn.innerHTML = '<span>📜 Auto-Scroll</span>';
  if (scrollTimer) {{
    clearInterval(scrollTimer);
    scrollTimer = null;
  }}
}}

window.addEventListener('touchstart', function() {{ if (autoScrolling) stopAutoScroll(); }}, {{ passive: true }});
window.addEventListener('wheel', function() {{ if (autoScrolling) stopAutoScroll(); }}, {{ passive: true }});

function answerCall() {{
  if (opened) return;
  opened = true;
  document.getElementById('call').classList.add('is-answered');
  document.body.classList.remove('is-locked');
  var m = document.getElementById('bgMusic');
  if (m) {{ m.play().catch(function(){{}}); }}
  setTimeout(startAutoScroll, 1200);
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

// PETALS ANIMATION
(function () {{
  var c = document.getElementById('petals');
  if (!c) return;
  var x = c.getContext('2d'), P = [], W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1);
  var cols = ['#f4a7b5', '#ee8fa3', '#f9c5cf', '#e77d93', '#fbd9de'];
  function size() {{ W = c.clientWidth; H = c.clientHeight; c.width = W * dpr; c.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0); }}
  function mk() {{
    return {{
      x: Math.random() * W, y: -20 - Math.random() * 80, r: 5 + Math.random() * 6,
      vy: 0.8 + Math.random() * 1.2, vx: -0.4 + Math.random() * 0.8,
      a: Math.random() * 6.28, va: 0.03 * (Math.random() > 0.5 ? 1 : -1),
      sw: Math.random() * 6.28, c: cols[(Math.random() * cols.length) | 0]
    }};
  }}
  function draw(p) {{
    x.save(); x.translate(p.x, p.y); x.rotate(p.a); x.fillStyle = p.c; x.globalAlpha = 0.85;
    x.scale(1, 0.6 + 0.4 * Math.sin(p.sw)); x.beginPath();
    x.moveTo(0, -p.r); x.bezierCurveTo(p.r, -p.r, p.r, p.r * 0.6, 0, p.r);
    x.bezierCurveTo(-p.r, p.r * 0.6, -p.r, -p.r, 0, -p.r); x.fill();
    x.restore();
  }}
  function loop() {{
    x.clearRect(0, 0, W, H);
    while (P.length < 15) P.push(mk());
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
  var cc = (document.getElementById('countryCodeSelect').value || '91').replace(/\\D/g, '');
  var rawPhone = document.getElementById('targetGuestPhone').value.trim().replace(/\\D/g, '').replace(/^0+/, '');
  var fullPhone = rawPhone ? (cc + rawPhone) : '';
  var link = getCleanUrl();
  var text = encodeURIComponent("Dearest " + guest + ",\\n\\nYou are cordially invited to celebrate the Royal Wedding of " + "{t['groom']} & {t['bride']}" + "! ❦\\n\\nDate: " + "{t['date_str']}" + "\\nVenue: " + "{t['venue']}" + "\\n\\nOpen your personalized animated invitation here:\\n" + link + "\\n\\nWith love,\\n" + "{t['groom']} & {t['bride']}");
  var url = fullPhone ? ('https://api.whatsapp.com/send?phone=' + fullPhone + '&text=' + text) : ('https://api.whatsapp.com/send?text=' + text);
  window.open(url, '_blank');
  closeSendModal();
}}

function sendViaEmail() {{
  var guest = document.getElementById('targetGuestName').value.trim() || 'Honored Guest';
  var email = document.getElementById('targetGuestEmail').value.trim();
  var link = getCleanUrl();
  var subject = encodeURIComponent("Royal Wedding Invitation: " + "{t['groom']} & {t['bride']}");
  var body = encodeURIComponent("Dearest " + guest + ",\\n\\nWe cordially invite you to celebrate the Royal Wedding of " + "{t['groom']} & {t['bride']}" + " on " + "{t['date_str']}" + " at " + "{t['venue']}" + ".\\n\\nOpen your interactive invitation here:\\n" + link + "\\n\\nWith love,\\n" + "{t['groom']} & {t['bride']}");

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
    var g = decodeURIComponent(m[1].replace(/\\+/g, ' '));
    var label = document.getElementById('guestCallLabel');
    if (label) label.innerHTML = 'Incoming call for <b>' + g + '</b><span class="dots"><i>.</i><i>.</i><i>.</i></span>';
  }}
}});
</script>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print(f"Generated all 60 standalone Wedding templates in {OUTPUT_DIR}!")

# Update assets/templates-data.js
js_templates = []
for t in templates:
    js_templates.append({
        "id": t["id"],
        "slug": t["slug"],
        "name": t["name"],
        "category": "Wedding",
        "category_key": "wedding",
        "title": t["title"],
        "subtitle": t["subtitle"],
        "palette_name": t["name"],
        "wine": t["wine"],
        "wine_d": t["wine_d"],
        "rose": t["rose"],
        "gold": t["gold"],
        "gold_l": t["gold_l"],
        "blush": t["blush"],
        "blush2": t["blush2"],
        "ivory": t["ivory"],
        "ink": t["ink"],
        "celebrants": f"{t['groom']} & {t['bride']}",
        "date_str": t["date_str"],
        "time_str": t["time_str"],
        "venue": t["venue"],
        "hero_img": t["hero_img"],
        "cover_img": t["cover_img"],
        "c1_name": t["groom_full"],
        "c1_par": t["groom_par"],
        "c2_name": t["bride_full"],
        "c2_par": t["bride_par"],
        "quote": t["quote"],
        "closing": t["closing"],
        "eyebrow": t["eyebrow"],
        "hashtag": f"#{t['groom']}Weds{t['bride']}",
        "date_iso": "2027-02-14T19:30",
        "events": events
    })

with open(os.path.join(ASSETS_DIR, "templates-data.js"), "w", encoding="utf-8") as f:
    f.write("window.GOLDENVOWS_TEMPLATES = " + json.dumps(js_templates, indent=2) + ";\n")
print("Updated assets/templates-data.js")

# Update TEMPLATES.md
md_content = "# GoldenVows — 60 Unique Royal Wedding Invitation Templates\n\n"
md_content += "Every single template is an independent, mobile and laptop-friendly animated Royal Wedding invitation with its own distinct visual design, bespoke color palette, touch-and-drag slider unlock, live countdown, Google Maps route, RSVP, and direct WhatsApp / Email guest delivery to the desired person.\n\n"
md_content += "| # | Template Name | Aesthetic Style | Theme Palette | Local URL | Live GitHub Pages URL |\n"
md_content += "|---|---|---|---|---|---|\n"

for t in templates:
    local_url = f"http://localhost:8000/templates/{t['slug']}.html"
    gh_url = f"https://urvashizoopcoder-hub.github.io/GoldenVows/templates/{t['slug']}.html"
    md_content += f"| {t['id']:02d} | **{t['name']}** | {t['style']} | `{t['wine']}` / `{t['gold']}` | [Open Locally]({local_url}) | [Open on GitHub Pages]({gh_url}) |\n"

with open(r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\TEMPLATES.md", "w", encoding="utf-8") as f:
    f.write(md_content)
print("Updated TEMPLATES.md with all 60 Wedding Templates!")
