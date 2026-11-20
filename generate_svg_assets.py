import os

IMG_DIR = r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\assets\img"
os.makedirs(IMG_DIR, exist_ok=True)

# 1. Housewarming Hero Entrance: Auspicious Gateway with Toran, Diyas & Sacred Arch
house_hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="60%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <linearGradient id="pillarGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#B45309"/>
      <stop offset="50%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FDE68A"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#996515"/>
    </linearGradient>
    <radialGradient id="diyaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FDE047" stop-opacity="0.9"/>
      <stop offset="40%" stop-color="#F59E0B" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#B45309" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect width="800" height="600" fill="url(#skyGrad)"/>

  <!-- Sunken Courtyard Arch -->
  <path d="M 120 600 L 120 220 Q 400 80 680 220 L 680 600 Z" fill="#FFFDF8" stroke="url(#goldGrad)" stroke-width="4"/>
  
  <!-- Sacred Toran Garland (Marigolds & Mango Leaves) -->
  <path d="M 100 220 Q 250 290 400 230 Q 550 290 700 220" fill="none" stroke="#D97706" stroke-width="6"/>
  <!-- Marigold flowers along toran -->
  <g fill="#F59E0B" stroke="#B45309" stroke-width="1.5">
    <circle cx="160" cy="245" r="14"/><circle cx="200" cy="265" r="15"/><circle cx="250" cy="275" r="16"/>
    <circle cx="300" cy="270" r="15"/><circle cx="350" cy="250" r="15"/><circle cx="400" cy="235" r="16"/>
    <circle cx="450" cy="250" r="15"/><circle cx="500" cy="270" r="15"/><circle cx="550" cy="275" r="16"/>
    <circle cx="600" cy="265" r="15"/><circle cx="640" cy="245" r="14"/>
  </g>
  <!-- Mango Leaves -->
  <g fill="#15803D">
    <path d="M 180 255 Q 185 295 180 310 Q 175 295 180 255 Z"/>
    <path d="M 275 273 Q 280 315 275 330 Q 270 315 275 273 Z"/>
    <path d="M 375 240 Q 380 285 375 300 Q 370 285 375 240 Z"/>
    <path d="M 475 258 Q 480 300 475 315 Q 470 300 475 258 Z"/>
    <path d="M 575 273 Q 580 315 575 330 Q 570 315 575 273 Z"/>
  </g>

  <!-- Ornate Pillars -->
  <rect x="90" y="200" width="45" height="400" fill="url(#pillarGrad)" rx="8"/>
  <rect x="665" y="200" width="45" height="400" fill="url(#pillarGrad)" rx="8"/>
  <rect x="75" y="180" width="75" height="25" fill="url(#goldGrad)" rx="6"/>
  <rect x="650" y="180" width="75" height="25" fill="url(#goldGrad)" rx="6"/>

  <!-- Central Sanctuary Door / Golden Gateway -->
  <rect x="290" y="270" width="220" height="330" fill="#78350F" rx="16" stroke="url(#goldGrad)" stroke-width="4"/>
  <rect x="305" y="285" width="90" height="135" fill="#451A03" rx="8" stroke="url(#goldGrad)" stroke-width="2"/>
  <rect x="405" y="285" width="90" height="135" fill="#451A03" rx="8" stroke="url(#goldGrad)" stroke-width="2"/>
  <rect x="305" y="435" width="90" height="150" fill="#451A03" rx="8" stroke="url(#goldGrad)" stroke-width="2"/>
  <rect x="405" y="435" width="90" height="150" fill="#451A03" rx="8" stroke="url(#goldGrad)" stroke-width="2"/>

  <!-- Auspicious Kalash on Pedestal (Right) -->
  <g transform="translate(560, 420)">
    <circle cx="40" cy="50" r="60" fill="url(#diyaGlow)"/>
    <!-- Brass Pot -->
    <path d="M 20 60 Q 40 40 60 60 Q 75 90 40 100 Q 5 90 20 60 Z" fill="url(#goldGrad)" stroke="#B45309" stroke-width="2"/>
    <!-- Coconut -->
    <circle cx="40" cy="46" r="16" fill="#78350F"/>
    <!-- Diya Flame -->
    <path d="M 40 15 Q 48 30 40 38 Q 32 30 40 15 Z" fill="#F59E0B"/>
    <circle cx="40" cy="28" r="5" fill="#FEF08A"/>
  </g>

  <!-- Auspicious Kalash on Pedestal (Left) -->
  <g transform="translate(140, 420)">
    <circle cx="40" cy="50" r="60" fill="url(#diyaGlow)"/>
    <!-- Brass Pot -->
    <path d="M 20 60 Q 40 40 60 60 Q 75 90 40 100 Q 5 90 20 60 Z" fill="url(#goldGrad)" stroke="#B45309" stroke-width="2"/>
    <!-- Coconut -->
    <circle cx="40" cy="46" r="16" fill="#78350F"/>
    <!-- Diya Flame -->
    <path d="M 40 15 Q 48 30 40 38 Q 32 30 40 15 Z" fill="#F59E0B"/>
    <circle cx="40" cy="28" r="5" fill="#FEF08A"/>
  </g>

  <!-- Sacred Toran Bell in Center Arch -->
  <g transform="translate(380, 150)">
    <path d="M 20 0 L 20 40" stroke="url(#goldGrad)" stroke-width="4"/>
    <path d="M 5 40 Q 20 30 35 40 L 38 60 Q 20 65 2 60 Z" fill="url(#goldGrad)"/>
    <circle cx="20" cy="65" r="4" fill="#B45309"/>
  </g>

  <!-- Header Blessing Banner -->
  <text x="400" y="70" text-anchor="middle" font-family="'Cinzel', serif, Georgia" font-size="22" font-weight="bold" fill="#78350F" letter-spacing="4">॥ SHREE GANESHAYA NAMAH ॥</text>
  <text x="400" y="100" text-anchor="middle" font-family="'Marcellus', serif, Georgia" font-size="15" fill="#92400E" letter-spacing="2">GRIHA PRAVESH &amp; AUSPICIOUS ABODE</text>
</svg>'''

# 2. Housewarming Cover: Sacred Kalash & Diya Pedestal (for incoming call / cover screen)
house_cover_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 700" width="500" height="700">
  <defs>
    <radialGradient id="covGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="50%" stop-color="#FDE68A"/>
      <stop offset="100%" stop-color="#D97706"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="40%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>
    <radialGradient id="flameGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FEF08A"/>
      <stop offset="50%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#EA580C" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="500" height="700" fill="url(#covGlow)"/>

  <!-- Decorative Sacred Mandala in background -->
  <g transform="translate(250, 350)" stroke="rgba(212,175,55,0.4)" stroke-width="2" fill="none">
    <circle r="180"/><circle r="140"/><circle r="100"/>
    <path d="M 0 -180 L 0 180 M -180 0 L 180 0"/>
    <path d="M -127 -127 L 127 127 M -127 127 L 127 -127"/>
  </g>

  <!-- Big Sacred Kalash -->
  <g transform="translate(250, 360)">
    <!-- Aura glow -->
    <circle cx="0" cy="0" r="160" fill="url(#flameGlow)"/>

    <!-- Lotus Base -->
    <g fill="#D97706" opacity="0.8">
      <path d="M -70 120 Q 0 100 70 120 Q 50 140 0 145 Q -50 140 -70 120 Z"/>
      <path d="M -100 125 Q -60 100 -20 125 Q -60 150 -100 125 Z"/>
      <path d="M 100 125 Q 60 100 20 125 Q 60 150 100 125 Z"/>
    </g>

    <!-- Brass Pitcher Body -->
    <path d="M -60 20 Q -90 90 0 115 Q 90 90 60 20 Q 30 -5 -60 20 Z" fill="url(#gold)" stroke="#78350F" stroke-width="3"/>

    <!-- Swastik & Auspicious symbol on Kalash -->
    <g stroke="#991B1B" stroke-width="5" stroke-linecap="round" fill="none">
      <line x1="-15" y1="65" x2="15" y2="65"/>
      <line x1="0" y1="50" x2="0" y2="80"/>
      <line x1="15" y1="65" x2="15" y2="52"/>
      <line x1="-15" y1="65" x2="-15" y2="78"/>
      <line x1="0" y1="50" x2="-13" y2="50"/>
      <line x1="0" y1="80" x2="13" y2="80"/>
    </g>

    <!-- Mango Leaves (Ashoka/Amra) -->
    <g fill="#166534" stroke="#14532D" stroke-width="1.5">
      <path d="M -50 15 Q -90 -40 -60 -70 Q -40 -30 -30 10 Z"/>
      <path d="M -25 10 Q -40 -60 -10 -90 Q 0 -40 0 10 Z"/>
      <path d="M 0 10 Q 0 -60 10 -90 Q 40 -40 25 10 Z"/>
      <path d="M 30 10 Q 40 -30 60 -70 Q 90 -40 50 15 Z"/>
    </g>

    <!-- Sacred Coconut (Shripal) -->
    <ellipse cx="0" cy="-45" rx="35" ry="42" fill="#78350F" stroke="#451A03" stroke-width="3"/>
    <path d="M -15 -85 L 0 -115 L 15 -85 Z" fill="#92400E"/>

    <!-- Top Auspicious Akhand Jyoti Diya -->
    <ellipse cx="0" cy="-115" rx="28" ry="12" fill="url(#gold)"/>
    <path d="M 0 -155 Q 16 -130 0 -118 Q -16 -130 0 -155 Z" fill="#F59E0B"/>
    <circle cx="0" cy="-132" r="7" fill="#FEF08A"/>
  </g>

  <!-- Text -->
  <text x="250" y="580" text-anchor="middle" font-family="'Cinzel', serif, Georgia" font-size="28" font-weight="bold" fill="#78350F" letter-spacing="3">GRIHA PRAVESH</text>
  <text x="250" y="615" text-anchor="middle" font-family="'Marcellus', serif, Georgia" font-size="16" fill="#92400E" letter-spacing="2">A SANCTUARY OF PEACE &amp; BLESSINGS</text>
</svg>'''

# 3. Head of Family / Hosts Illustration (Warm, respectful family host portrait)
house_family_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="bgG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <linearGradient id="goldB" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FDE68A"/>
      <stop offset="50%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>
  </defs>
  <rect width="300" height="400" fill="url(#bgG)"/>

  <!-- Ornate Arch Frame -->
  <path d="M 20 380 L 20 120 Q 150 20 280 120 L 280 380 Z" fill="#FFFDF8" stroke="url(#goldB)" stroke-width="4"/>

  <!-- Family / Elder Host Illustration -->
  <g transform="translate(150, 190)">
    <!-- Halo glow -->
    <circle cx="0" cy="-30" r="70" fill="rgba(253, 230, 138, 0.5)"/>

    <!-- Host 1 (Father / Patriarch) in Kurta -->
    <path d="M -70 190 L -50 90 Q -25 70 0 85 Q 25 70 50 90 L 70 190 Z" fill="#78350F"/>
    <!-- Kurta Collar & Dupatta/Stole -->
    <path d="M -30 90 Q 0 110 30 90 L 35 190 L 15 190 L 0 120 L -15 190 L -35 190 Z" fill="#D97706"/>

    <!-- Head & Tilak -->
    <circle cx="0" cy="30" r="32" fill="#FDE68A" stroke="#B45309" stroke-width="1.5"/>
    <path d="M -32 20 Q 0 -15 32 20 Q 25 -2 0 -5 Q -25 -2 -32 20 Z" fill="#451A03"/>
    <!-- Sacred Chandan & Kumkum Tilak -->
    <line x1="0" y1="18" x2="0" y2="30" stroke="#DC2626" stroke-width="3"/>
    <circle cx="0" cy="33" r="2.5" fill="#DC2626"/>

    <!-- Hands folded in Namaste (Anjali Mudra) -->
    <g fill="#FDE68A" stroke="#B45309" stroke-width="1.5" transform="translate(0, 115)">
      <path d="M -12 25 L 0 0 L 12 25 Z"/>
    </g>
  </g>

  <!-- Caption Label -->
  <text x="150" y="340" text-anchor="middle" font-family="'Marcellus', serif, Georgia" font-size="16" font-weight="bold" fill="#78350F" letter-spacing="1">THE HOST FAMILY</text>
  <text x="150" y="365" text-anchor="middle" font-family="'Josefin Sans', sans-serif" font-size="12" fill="#92400E">Warmly Welcoming You</text>
</svg>'''

# 4. New Residence Sanctuary ('Anandam' Abode Facade)
house_residence_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="bgH" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <linearGradient id="goldH" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FDE68A"/>
      <stop offset="50%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>
  </defs>
  <rect width="300" height="400" fill="url(#bgH)"/>

  <!-- Ornate Arch Frame -->
  <path d="M 20 380 L 20 120 Q 150 20 280 120 L 280 380 Z" fill="#FFFDF8" stroke="url(#goldH)" stroke-width="4"/>

  <!-- Abode Illustration -->
  <g transform="translate(150, 200)">
    <!-- Villa Roof -->
    <polygon points="0,-70 -105,0 105,0" fill="#92400E" stroke="url(#goldH)" stroke-width="3"/>
    
    <!-- Villa Walls -->
    <rect x="-90" y="0" width="180" height="130" fill="#FEF3C7" stroke="#B45309" stroke-width="2"/>
    
    <!-- Balcony & Windows -->
    <rect x="-70" y="15" width="40" height="45" fill="#451A03" rx="4" stroke="url(#goldH)" stroke-width="2"/>
    <rect x="30" y="15" width="40" height="45" fill="#451A03" rx="4" stroke="url(#goldH)" stroke-width="2"/>

    <!-- Grand Entrance Door -->
    <rect x="-26" y="60" width="52" height="70" fill="#78350F" rx="8" stroke="url(#goldH)" stroke-width="2"/>

    <!-- Golden Nameplate 'ANANDAM' -->
    <rect x="-45" y="-18" width="90" height="24" fill="url(#goldH)" rx="6" stroke="#78350F" stroke-width="1.5"/>
    <text x="0" y="-2" text-anchor="middle" font-family="'Cinzel', serif, Georgia" font-size="11" font-weight="bold" fill="#451A03" letter-spacing="1">ANANDAM</text>

    <!-- Toran & Diyas at Door -->
    <path d="M -26 60 Q 0 72 26 60" fill="none" stroke="#D97706" stroke-width="3"/>
    <circle cx="-32" cy="120" r="5" fill="#F59E0B"/>
    <circle cx="32" cy="120" r="5" fill="#F59E0B"/>
  </g>

  <!-- Caption Label -->
  <text x="150" y="340" text-anchor="middle" font-family="'Marcellus', serif, Georgia" font-size="16" font-weight="bold" fill="#78350F" letter-spacing="1">OUR NEW ABODE</text>
  <text x="150" y="365" text-anchor="middle" font-family="'Josefin Sans', sans-serif" font-size="12" fill="#92400E">Built with Love &amp; Elder Blessings</text>
</svg>'''

# 5. Baby Shower Hero & Cover
baby_hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <defs>
    <linearGradient id="babySky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="50%" stop-color="#FFF1F2"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#babySky)"/>
  <!-- Clouds -->
  <g fill="#FFFFFF" opacity="0.9">
    <ellipse cx="200" cy="180" rx="90" ry="50"/>
    <ellipse cx="270" cy="160" rx="70" ry="45"/>
    <ellipse cx="140" cy="190" rx="60" ry="40"/>
    <ellipse cx="600" cy="160" rx="100" ry="55"/>
    <ellipse cx="670" cy="180" rx="70" ry="40"/>
    <ellipse cx="530" cy="180" rx="60" ry="40"/>
  </g>
  <!-- Hot Air Balloon -->
  <g transform="translate(400, 220)">
    <ellipse cx="0" cy="-60" rx="65" ry="80" fill="#F472B6"/>
    <path d="M -40 -60 Q 0 -130 40 -60 Q 0 10 -40 -60 Z" fill="#60A5FA" opacity="0.7"/>
    <line x1="-25" y1="15" x2="-15" y2="55" stroke="#9CA3AF" stroke-width="2"/>
    <line x1="25" y1="15" x2="15" y2="55" stroke="#9CA3AF" stroke-width="2"/>
    <rect x="-18" y="55" width="36" height="28" fill="#D97706" rx="4"/>
  </g>
  <text x="400" y="420" text-anchor="middle" font-family="'Cinzel', serif" font-size="28" font-weight="bold" fill="#BE185D" letter-spacing="3">BABY SHOWER &amp; GODH BHARAI</text>
  <text x="400" y="455" text-anchor="middle" font-family="'Marcellus', serif" font-size="16" fill="#6B7280" letter-spacing="2">A SWEET LITTLE MIRACLE IS ON THE WAY</text>
</svg>'''

baby_cover_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 700" width="500" height="700">
  <defs>
    <radialGradient id="bCov" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF1F2"/>
      <stop offset="60%" stop-color="#FCE7F3"/>
      <stop offset="100%" stop-color="#FBCFE8"/>
    </radialGradient>
  </defs>
  <rect width="500" height="700" fill="url(#bCov)"/>
  <!-- Golden Cradle with soft bunting -->
  <g transform="translate(250, 340)">
    <circle cx="0" cy="0" r="140" fill="#FFFFFF" opacity="0.6"/>
    <!-- Cradle -->
    <path d="M -90 -20 Q 0 90 90 -20 Q 70 60 0 65 Q -70 60 -90 -20 Z" fill="#F472B6"/>
    <ellipse cx="0" cy="-20" rx="90" ry="25" fill="#FBCFE8"/>
    <!-- Rocking legs -->
    <path d="M -60 55 Q 0 105 60 55" fill="none" stroke="#D97706" stroke-width="6" stroke-linecap="round"/>
    <line x1="-50" y1="40" x2="-50" y2="70" stroke="#D97706" stroke-width="4"/>
    <line x1="50" y1="40" x2="50" y2="70" stroke="#D97706" stroke-width="4"/>
    <!-- Baby teddy in cradle -->
    <circle cx="0" cy="-35" r="24" fill="#FBBF24"/>
    <circle cx="-18" cy="-52" r="10" fill="#FBBF24"/>
    <circle cx="18" cy="-52" r="10" fill="#FBBF24"/>
    <circle cx="-8" cy="-38" r="3" fill="#451A03"/>
    <circle cx="8" cy="-38" r="3" fill="#451A03"/>
    <circle cx="0" cy="-28" r="5" fill="#F472B6"/>
  </g>
  <text x="250" y="550" text-anchor="middle" font-family="'Cinzel', serif" font-size="26" font-weight="bold" fill="#9D174D" letter-spacing="2">GODH BHARAI</text>
  <text x="250" y="585" text-anchor="middle" font-family="'Marcellus', serif" font-size="15" fill="#BE185D" letter-spacing="1">WELCOMING OUR LITTLE BLESSING</text>
</svg>'''

# 6. Birthday Hero & Cover
bday_hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <defs>
    <radialGradient id="bdaySky" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#3B0764"/>
      <stop offset="50%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#09090B"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bdaySky)"/>
  <!-- Confetti and stars -->
  <g fill="#FDE047">
    <circle cx="120" cy="80" r="4"/><circle cx="240" cy="150" r="5"/><circle cx="680" cy="120" r="6"/>
    <circle cx="560" cy="90" r="4"/><circle cx="180" cy="300" r="5"/><circle cx="640" cy="280" r="5"/>
  </g>
  <!-- Balloons -->
  <g transform="translate(200, 220)">
    <ellipse cx="0" cy="0" rx="40" ry="52" fill="#E11D48"/>
    <line x1="0" y1="52" x2="-10" y2="120" stroke="#9CA3AF" stroke-width="1.5"/>
  </g>
  <g transform="translate(600, 220)">
    <ellipse cx="0" cy="0" rx="40" ry="52" fill="#CA8A04"/>
    <line x1="0" y1="52" x2="10" y2="120" stroke="#9CA3AF" stroke-width="1.5"/>
  </g>
  <text x="400" y="380" text-anchor="middle" font-family="'Cinzel', serif" font-size="34" font-weight="bold" fill="#FDE047" letter-spacing="4">VIP BIRTHDAY BASH</text>
  <text x="400" y="420" text-anchor="middle" font-family="'Marcellus', serif" font-size="18" fill="#F43F5E" letter-spacing="2">A NIGHT OF CELEBRATION, MUSIC &amp; CHEERS</text>
</svg>'''

bday_cover_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 700" width="500" height="700">
  <defs>
    <radialGradient id="bdCov" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#4C1D95"/>
      <stop offset="70%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#09090B"/>
    </radialGradient>
  </defs>
  <rect width="500" height="700" fill="url(#bdCov)"/>
  <!-- Multi-tier Cake -->
  <g transform="translate(250, 360)">
    <circle cx="0" cy="0" r="150" fill="rgba(244,63,94,0.15)"/>
    <!-- Bottom tier -->
    <rect x="-90" y="40" width="180" height="60" rx="8" fill="#F43F5E"/>
    <!-- Mid tier -->
    <rect x="-65" y="-15" width="130" height="55" rx="6" fill="#FBBF24"/>
    <!-- Top tier -->
    <rect x="-40" y="-60" width="80" height="45" rx="5" fill="#38BDF8"/>
    <!-- Candles -->
    <line x1="-20" y1="-60" x2="-20" y2="-80" stroke="#FFF" stroke-width="3"/>
    <circle cx="-20" cy="-86" r="6" fill="#FDE047"/>
    <line x1="0" y1="-60" x2="0" y2="-85" stroke="#FFF" stroke-width="3"/>
    <circle cx="0" cy="-91" r="7" fill="#FDE047"/>
    <line x1="20" y1="-60" x2="20" y2="-80" stroke="#FFF" stroke-width="3"/>
    <circle cx="20" cy="-86" r="6" fill="#FDE047"/>
  </g>
  <text x="250" y="550" text-anchor="middle" font-family="'Cinzel', serif" font-size="28" font-weight="bold" fill="#FDE047" letter-spacing="3">BIRTHDAY GALA</text>
  <text x="250" y="585" text-anchor="middle" font-family="'Marcellus', serif" font-size="16" fill="#F472B6" letter-spacing="2">TIME TO CELEBRATE &amp; POP CHAMPAGNE</text>
</svg>'''

files_to_write = {
    "house_hero.svg": house_hero_svg,
    "house_cover.svg": house_cover_svg,
    "house_family.svg": house_family_svg,
    "house_residence.svg": house_residence_svg,
    "baby_hero.svg": baby_hero_svg,
    "baby_cover.svg": baby_cover_svg,
    "bday_hero.svg": bday_hero_svg,
    "bday_cover.svg": bday_cover_svg,
}

for name, content in files_to_write.items():
    p = os.path.join(IMG_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {name}")

print("All occasion visual assets created successfully!")
