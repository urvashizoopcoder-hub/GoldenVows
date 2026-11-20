import os, json

with open(r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\generate_templates.py", "r", encoding="utf-8") as f:
    orig = f.read()

idx_data = orig.find("templates_data = [")
idx_gen = orig.find("# Standalone HTML Template Generator")
if idx_gen == -1:
    idx_gen = orig.find("# HTML Template Generator for each of the 60 unique templates")

templates_data_str = orig[idx_data:idx_gen]

script_content = '''import os, json

TEMPLATES_DIR = r"c:\\\\Users\\\\URVASHI BHARTI\\\\OneDrive\\\\Desktop\\\\zoop\\\\templates"
ASSETS_DIR = r"c:\\\\Users\\\\URVASHI BHARTI\\\\OneDrive\\\\Desktop\\\\zoop\\\\assets"
os.makedirs(TEMPLATES_DIR, exist_ok=True)

''' + templates_data_str + '''

# Write assets/templates-data.js so index.html can render the full interactive gallery
js_content = "window.GOLDENVOWS_TEMPLATES = " + json.dumps(templates_data, indent=2) + ";\\n"
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
  var cc = (document.getElementById('countryCodeSelect').value || '91').replace(/\\D/g, '');
  var rawPhone = document.getElementById('targetGuestPhone').value.trim().replace(/\\D/g, '').replace(/^0+/, '');
  var fullPhone = rawPhone ? (cc + rawPhone) : '';
  var link = getCleanUrl();
  var text = encodeURIComponent("Dearest " + guest + ",\\n\\nYou are cordially invited to celebrate the " + "{t['title']}" + "! ❦\\n\\nDate: " + "{t['date_str']}" + "\\nVenue: " + "{t['venue']}" + "\\n\\nOpen your personalized animated invitation here:\\n" + link + "\\n\\nWith love,\\n" + "{t['celebrants']}");
  var url = fullPhone ? ('https://api.whatsapp.com/send?phone=' + fullPhone + '&text=' + text) : ('https://api.whatsapp.com/send?text=' + text);
  window.open(url, '_blank');
  closeSendModal();
}}

function sendViaEmail() {{
  var guest = document.getElementById('targetGuestName').value.trim() || 'Honored Guest';
  var email = document.getElementById('targetGuestEmail').value.trim();
  var link = getCleanUrl();
  var subject = encodeURIComponent("Invitation: " + "{t['title']}");
  var body = encodeURIComponent("Dearest " + guest + ",\\n\\nWe cordially invite you to celebrate the " + "{t['title']}" + " on " + "{t['date_str']}" + " at " + "{t['venue']}" + ".\\n\\nOpen your interactive invitation here:\\n" + link + "\\n\\nWith love,\\n" + "{t['celebrants']}");

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

print(f"Successfully generated {len(templates_data)} standalone templates in {TEMPLATES_DIR}!")

md_content = "# GoldenVows — 60 Unique Invitation Templates Catalog\\n\\n"
md_content += "Each template is an independent, mobile and laptop-friendly animated invitation featuring occasion-specific visual layouts (Royal Rajputana Mandap, Tuscan Minimalist, Starlight Ring Halo, Pastel Baby Cloud, VIP Concert Ticket, Vedic Griha Pravesh Sanctuary), touch-and-drag slider openers, real-time countdown, Google Maps navigation, RSVP, and direct WhatsApp / Email dispatching to the correct recipient number.\\n\\n"
md_content += "| # | Template Name | Category | Palette | Local URL | Live GitHub Pages URL |\\n"
md_content += "|---|---|---|---|---|---|\\n"

for t in templates_data:
    local_url = f"http://localhost:8000/templates/{t['slug']}.html"
    gh_url = f"https://urvashizoopcoder-hub.github.io/GoldenVows/templates/{t['slug']}.html"
    md_content += f"| {t['id']:02d} | **{t['name']}** | {t['category']} | {t['palette_name']} | [Open Locally]({local_url}) | [Open on GitHub Pages]({gh_url}) |\\n"

with open(r"c:\\\\Users\\\\URVASHI BHARTI\\\\OneDrive\\\\Desktop\\\\zoop\\\\TEMPLATES.md", "w", encoding="utf-8") as f:
    f.write(md_content)
print("Generated TEMPLATES.md catalog table!")
'''

with open(r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\generate_templates.py", "w", encoding="utf-8") as f:
    f.write(script_content)

print("generate_templates.py cleanly updated with occasion-specific layouts and dynamic celebration particles!")
