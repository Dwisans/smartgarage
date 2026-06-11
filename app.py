import streamlit as st
import re

st.set_page_config(page_title="SmartGarage", page_icon="🔧", layout="wide")

from chatbot.chat_controller import ChatController
from chatbot.session_manager import SessionManager
from chatbot.response_generator import ResponseGenerator
from automata.events import Event
from automata.states import State

if "session" not in st.session_state:
    st.session_state.session = SessionManager()
if "page" not in st.session_state:
    st.session_state.page = "home"
if "service_mode" not in st.session_state:
    st.session_state.service_mode = None

controller = ChatController()

# ── Cek klik kartu layanan ──
try:
    if "service" in st.query_params:
        st.session_state.session = SessionManager()
        st.session_state.service_mode = st.query_params["service"]
        st.session_state.page = "chat"
        st.query_params.clear()
        st.rerun()
except Exception:
    pass

# ═══════ GLOBAL CSS STYLES ═══════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --blue-50:#eff6ff; --blue-100:#dbeafe; --blue-200:#bfdbfe;
    --blue-300:#93c5fd; --blue-400:#60a5fa; --blue-500:#3b82f6;
    --blue-600:#2563eb; --blue-700:#1d4ed8; --blue-800:#1e40af;
    --blue-900:#1e3a8a; --bg:#eef2ff; --surface:#ffffff;
    --border:#e0e8f8; --border2:#c7d5f0; --accent:#2563eb;
    --text:#0f172a; --muted:#64748b; --muted2:#94a3b8; --green:#22c55e;
}

html, body, [class*="css"] { font-family:'Inter',sans-serif !important; }
.stApp { background:var(--bg) !important; }

/* Mengembalikan header bawaan Streamlit agar tombol Deploy & Titik 3 aman */
header[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stDecoration"]   { display:none !important; }

.block-container { padding:2.5rem 3rem 3rem !important; max-width:100% !important; }
h1,h2,h3,h4,h5,h6 { font-family:'Inter',sans-serif !important; font-weight:700 !important; color:var(--text) !important; }
p, li, .stMarkdown { color:var(--text) !important; }

/* NAVBAR UNIVERSAL */
.nav-badge {
    width:38px; height:38px;
    background:linear-gradient(135deg,var(--blue-600),var(--blue-400));
    border-radius:11px; display:flex; align-items:center; justify-content:center;
    font-size:19px; flex-shrink:0; box-shadow:0 3px 8px rgba(37,99,235,.3);
}
/* FIX: Memaksa warna tulisan brand nama bengkel menjadi HITAM PEKAT */
.nav-brand   { font-weight:800; font-size:15px; color:#0f172a !important; letter-spacing:-.4px; }
/* FIX: Memaksa warna tulisan tagline menjadi abu-abu gelap agar kontras */
.nav-tagline { font-size:11px; color:#475569 !important; margin-top:1px; }
.nav-dot { width:6px; height:6px; border-radius:50%; background:var(--green); animation:blink 2s infinite; display:inline-block; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.3} }
.divider { border:none; border-top:1.5px solid var(--border); margin:12px 0 20px; }

/* HAMBURGER MENU */
[data-testid="stMainMenuPopover"],
[data-testid="stMainMenuPopover"] > div,
[data-testid="stMainMenuPopover"] > div > div {
    background:#ffffff !important; background-color:#ffffff !important;
    color:#0f172a !important; border:1.5px solid #e0e8f8 !important;
    border-radius:12px !important; box-shadow:0 8px 24px rgba(37,99,235,.15) !important;
}
[data-testid="stMainMenuPopover"] li,
[data-testid="stMainMenuPopover"] li > div,
[data-testid="stMainMenuPopover"] li span,
[data-testid="stMainMenuPopover"] li p,
[data-testid="stMainMenuPopover"] [role="menuitem"],
[data-testid="stMainMenuPopover"] [role="menuitem"] * { color:#0f172a !important; background:transparent !important; }
[data-testid="stMainMenuPopover"] [role="menuitem"]:hover,
[data-testid="stMainMenuPopover"] li:hover { background:#eff6ff !important; border-radius:8px !important; }
[data-testid="stMainMenuPopover"] hr,
[data-testid="stMainMenuPopover"] [role="separator"] { border-color:#e0e8f8 !important; opacity:1 !important; }
[data-testid="stMainMenuPopover"] kbd { color:#64748b !important; background:#f1f5f9 !important; border-color:#e0e8f8 !important; }

/* HERO */
.hero {
    border-radius:20px; padding:52px 36px 44px; margin-bottom:20px;
    text-align:center; position:relative; overflow:hidden;
    background:linear-gradient(140deg,#1e3a8a 0%,#2563eb 55%,#60a5fa 100%);
    box-shadow:0 8px 32px rgba(37,99,235,.25);
}
.hero::before {
    content:''; position:absolute; top:-60px; right:-60px;
    width:280px; height:280px; background:rgba(255,255,255,.07);
    border-radius:50%; pointer-events:none;
}
.hero::after {
    content:''; position:absolute; bottom:-80px; left:-40px;
    width:220px; height:220px; background:rgba(255,255,255,.05);
    border-radius:50%; pointer-events:none;
}
.hero-badge {
    display:inline-flex; align-items:center; gap:7px;
    background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.22);
    border-radius:999px; padding:5px 16px;
    font-size:11px; color:rgba(255,255,255,.92);
    letter-spacing:.6px; margin-bottom:20px;
    font-family:'JetBrains Mono',monospace; text-transform:uppercase;
}
.hero h1 {
    font-size:36px !important; font-weight:800 !important;
    color:#fff !important; letter-spacing:-.6px;
    line-height:1.2 !important; margin-bottom:14px !important;
}
.hero-sub { color:rgba(255,255,255,.78) !important; font-size:15px; line-height:1.7; max-width:640px; margin:0 auto 24px; text-align:center !important; }
.hero-chips { display:flex; justify-content:center; gap:10px; flex-wrap:wrap; }
.hero-chip {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(255,255,255,.13); border:1px solid rgba(255,255,255,.2);
    border-radius:999px; padding:6px 14px;
    font-size:12px; color:rgba(255,255,255,.9); font-weight:500;
    backdrop-filter:blur(4px);
}

/* STATS */
.stat-row { display:flex; gap:12px; margin-bottom:20px; }
.stat-card {
    flex:1; background:var(--surface); border:1.5px solid var(--border);
    border-radius:14px; padding:18px 12px; text-align:center;
    box-shadow:0 2px 8px rgba(37,99,235,.05); transition:transform .2s,box-shadow .2s;
}
.stat-card:hover { transform:translateY(-3px); box-shadow:0 8px 20px rgba(37,99,235,.12); }
.stat-val {
    font-family:'JetBrains Mono',monospace; font-size:30px; font-weight:600;
    background:linear-gradient(135deg,var(--blue-700),var(--blue-400));
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.stat-lbl { font-size:11px; color:var(--muted); margin-top:4px; }

/* FEATURE CARDS */
.feat-grid { display:flex; gap:14px; margin-bottom:20px; }
.feat-card {
    flex:1; background:var(--surface); border:1.5px solid var(--border);
    border-radius:16px; padding:22px 18px; transition:all .25s;
    position:relative; overflow:hidden;
}
.feat-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,var(--blue-600),var(--blue-400));
    opacity:0; transition:opacity .25s; border-radius:16px 16px 0 0;
}
.feat-card:hover { border-color:var(--blue-300); box-shadow:0 6px 24px rgba(37,99,235,.12); transform:translateY(-3px); }
.feat-card:hover::before { opacity:1; }
.feat-icon-wrap {
    width:44px; height:44px;
    background:linear-gradient(135deg,var(--blue-50),var(--blue-100));
    border:1.5px solid var(--blue-200); border-radius:12px;
    display:flex; align-items:center; justify-content:center;
    font-size:20px; margin-bottom:14px;
}
.feat-title { font-size:14px; font-weight:700; color:var(--text); margin-bottom:6px; }
.feat-desc  { font-size:12px; color:var(--muted); line-height:1.6; }
.feat-card-link { flex:1; display:flex; text-decoration:none; color:inherit; cursor:pointer; }

/* BUTTONS */
.stButton button {
    background:var(--surface) !important; border:1.5px solid var(--border2) !important;
    color:var(--accent) !important; border-radius:10px !important;
    font-family:'Inter',sans-serif !important; font-weight:600 !important;
    font-size:13px !important; transition:all .2s !important;
}
.stButton button:hover {
    border-color:var(--accent) !important; background:var(--blue-50) !important;
    box-shadow:0 0 0 3px rgba(37,99,235,.12) !important; transform:translateY(-1px) !important;
}
.stButton button[kind="primary"] {
    background:linear-gradient(135deg,var(--blue-700),var(--blue-500)) !important;
    color:#fff !important; border-color:transparent !important;
    box-shadow:0 4px 14px rgba(37,99,235,.35) !important;
}
.stButton button[kind="primary"]:hover {
    background:linear-gradient(135deg,var(--blue-800),var(--blue-600)) !important;
    box-shadow:0 6px 20px rgba(37,99,235,.45) !important;
}

/* CHAT BOTTOM BAR */
[data-testid="stBottom"],
[data-testid="stBottom"] > div {
    background:var(--bg) !important;
    border-top:1.5px solid var(--border) !important;
    box-shadow:none !important;
}
[data-testid="stBottom"] > div > div {
    max-width:700px !important; margin:0 auto !important;
}
.stChatInput > div {
    background:var(--surface) !important; border:1.5px solid var(--border2) !important;
    border-radius:14px !important; box-shadow:0 2px 12px rgba(37,99,235,.07) !important;
}
.stChatInput > div:focus-within {
    border-color:var(--accent) !important; box-shadow:0 0 0 3px rgba(37,99,235,.12) !important;
}
.stChatInput textarea { color:var(--text) !important; caret-color:var(--accent) !important; }
.stChatInput textarea::placeholder { color:var(--muted2) !important; }

/* STYLE KHAS HEADER CHAT TERPUSAT */
.chat-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--surface);
    padding: 14px 20px;
    border-radius: 14px;
    border: 1.5px solid var(--border);
    box-shadow: 0 4px 12px rgba(37,99,235,.05);
    margin-bottom: 24px;
}
.chat-bot-info {
    display: flex;
    align-items: center;
    gap: 12px;
}
.chat-bot-avatar {
    width: 38px; height: 38px;
    background: linear-gradient(135deg,var(--blue-600),var(--blue-400));
    border-radius: 10px; display: flex; align-items: center;
    justify-content: center; font-size: 18px;
}
.chat-bot-name { font-weight: 700; font-size: 14px; color: var(--text); }
.chat-bot-sub { font-size: 11px; color: var(--muted); }

/* CHAT MESSAGES CORRECTION FOR CENTERED LAYOUT */
.msg-wrap { margin-bottom:12px; padding: 0 1% !important; }
.msg-lbl { font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:4px; }
.msg-lbl.user { color:var(--muted2); text-align:right; }
.msg-lbl.bot  { color:var(--accent); }
.msg-bubble { padding:14px 18px; border-radius:14px; font-size:14px; line-height:1.68; max-width:80% !important; word-wrap:break-word; display:inline-block; }
.msg-bubble.user { background:linear-gradient(135deg,var(--blue-600),var(--blue-500)); color:#fff; border-bottom-right-radius:4px; box-shadow:0 3px 10px rgba(37,99,235,.25); }
.msg-bubble.bot  { background:var(--surface); border:1.5px solid var(--border); color:var(--text); border-bottom-left-radius:4px; box-shadow:0 2px 6px rgba(0,0,0,.04); }
.msg-wrap.user-wrap { text-align:right; }
.msg-wrap.bot-wrap  { text-align:left; }

/* SCROLLBAR */
::-webkit-scrollbar { width:8px; }
::-webkit-scrollbar-track { background:#dde5f5; border-radius:10px; }
::-webkit-scrollbar-thumb { background:var(--blue-400); border-radius:10px; min-height:40px; }
::-webkit-scrollbar-thumb:hover { background:var(--blue-600); }
html { overflow-y:scroll; scrollbar-gutter:stable; }

/* FOOTER */
.footer-navbar { background:#0f1e3d; border-radius:20px; overflow:hidden; margin-bottom:20px; }
.fn-grid { display:grid; grid-template-columns:1.5fr 1fr 1fr 1.4fr; }
.fn-col { padding:32px 24px; }
.fn-col + .fn-col { border-left:1px solid rgba(255,255,255,.08); }
.fn-col-title { font-size:10px; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:#60a5fa; margin-bottom:14px; }
.fn-brand-icon { width:36px; height:36px; background:linear-gradient(135deg,#2563eb,#60a5fa); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:17px; }
.fn-stat-grid { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.fn-stat-box { background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.1); border-radius:10px; padding:10px; text-align:center; }
.fn-stat-val { font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:600; color:#60a5fa; }
.fn-stat-lbl { font-size:10px; color:rgba(255,255,255,.4); margin-top:3px; }
.fn-link { display:block; font-size:13px; color:rgba(255,255,255,.55); margin-bottom:10px; }
.fn-contact-row { display:flex; align-items:flex-start; gap:10px; margin-bottom:12px; }
.fn-contact-icon { width:30px; height:30px; background:rgba(37,99,235,.2); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:14px; flex-shrink:0; }
.fn-contact-lbl { font-size:10px; color:rgba(255,255,255,.35); text-transform:uppercase; letter-spacing:.5px; }
.fn-contact-val { font-size:12px; color:rgba(255,255,255,.7); margin-top:2px; line-height:1.4; }
.fn-bottom { padding:14px 24px; border-top:1px solid rgba(255,255,255,.08); display:flex; align-items:center; justify-content:space-between; }
.fn-bottom-left  { font-size:12px; color:rgba(255,255,255,.35); }
.fn-bottom-right { font-size:12px; color:rgba(255,255,255,.25); }
</style>
""", unsafe_allow_html=True)


# ═══════ NAVBAR UNIVERSAL (Selalu Muncul Di Atas) ═══════
nav_cols = st.columns([0.55, 5.5, 2])
with nav_cols[0]:
    st.markdown('<div class="nav-badge">🔧</div>', unsafe_allow_html=True)
with nav_cols[1]:
    st.markdown(
        '<div class="nav-brand">SmartGarage</div>'
        '<div class="nav-tagline">Bengkel Pintar Digital</div>',
        unsafe_allow_html=True,
    )
with nav_cols[2]:
    pass
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ═══════ HALAMAN HOME ═══════
if st.session_state.page == "home":

    st.markdown("""
<div class="hero">
<div class="hero-badge">⚙ FSM-Powered Engine</div>
<h1>Bengkel Pintar untuk<br>Kendaraanmu</h1>
<p class="hero-sub">Diagnosa kerusakan, jadwal servis berkala, dan tips perawatan —
diproses sistematis dengan Finite State Machine tanpa tebak-tebakan.</p>
<div class="hero-chips">
  <span class="hero-chip">🔍 Diagnosa Otomatis</span>
  <span class="hero-chip">🛠️ Servis Berkala</span>
  <span class="hero-chip">💡 Tips Perawatan</span>
  <span class="hero-chip">⚡ Berbasis FSM</span>
</div>
</div>
""", unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1.5, 2, 1.5])
    with col_c:
        if st.button("💬  Mulai Konsultasi", type="primary", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="stat-row">
<div class="stat-card"><div class="stat-val">30</div><div class="stat-lbl">State FSM</div></div>
<div class="stat-card"><div class="stat-val">21</div><div class="stat-lbl">Events</div></div>
<div class="stat-card"><div class="stat-val">48+</div><div class="stat-lbl">Transitions</div></div>
<div class="stat-card"><div class="stat-val">3</div><div class="stat-lbl">Layanan Utama</div></div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feat-grid">
<a href="?service=diagnosa" class="feat-card-link">
<div class="feat-card">
<div class="feat-icon-wrap">🔍</div>
<div class="feat-title">Diagnosa Masalah</div>
<div class="feat-desc">Identifikasi kerusakan kendaraan secara sistematis dan akurat, langkah demi langkah.</div>
</div>
</a>
<a href="?service=servis" class="feat-card-link">
<div class="feat-card">
<div class="feat-icon-wrap">🛠️</div>
<div class="feat-title">Servis Berkala</div>
<div class="feat-desc">Rekomendasi perawatan berdasarkan kilometer dan usia kendaraanmu.</div>
</div>
</a>
<a href="?service=tips" class="feat-card-link">
<div class="feat-card">
<div class="feat-icon-wrap">💡</div>
<div class="feat-title">Tips Perawatan</div>
<div class="feat-desc">Panduan merawat mesin, rem, ban, dan komponen penting lainnya.</div>
</div>
</a>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="footer-navbar">
<div class="fn-grid">
<div class="fn-col">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
<div class="fn-brand-icon">🔧</div>
<div style="font-weight:800;font-size:16px;color:#fff;">Smart<span style="color:#60a5fa;">Garage</span></div>
</div>
<div style="font-size:12px;color:rgba(255,255,255,.4);line-height:1.6;">Asisten digital otomotif berbasis Finite State Machine — sistematis, terstruktur, dan akurat.</div>
</div>
<div class="fn-col">
<div class="fn-col-title">Tentang</div>
<div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.6;margin-bottom:16px;">SmartGarage menggunakan FSM untuk memandu diagnosa kendaraan secara logis dan terurut.</div>
<div class="fn-stat-grid">
<div class="fn-stat-box"><div class="fn-stat-val">30</div><div class="fn-stat-lbl">State FSM</div></div>
<div class="fn-stat-box"><div class="fn-stat-val">21</div><div class="fn-stat-lbl">Events</div></div>
<div class="fn-stat-box"><div class="fn-stat-val">48+</div><div class="fn-stat-lbl">Transitions</div></div>
<div class="fn-stat-box"><div class="fn-stat-val">3</div><div class="fn-stat-lbl">Layanan</div></div>
</div>
</div>
<div class="fn-col">
                <div class="fn-col-title">Layanan</div>
                <a href="?service=diagnosa" style="text-decoration:none;display:block;"><div class="fn-link">🔍&nbsp; Diagnosa Masalah</div></a>
                <a href="?service=servis" style="text-decoration:none;display:block;"><div class="fn-link">🛠️&nbsp; Servis Berkala</div></a>
                <a href="?service=tips" style="text-decoration:none;display:block;"><div class="fn-link">💡&nbsp; Tips Perawatan</div></a>
</div>
<div class="fn-col">
<div class="fn-col-title">Hubungi Kami</div>
<div class="fn-contact-row">
<div class="fn-contact-icon">📍</div>
<div><div class="fn-contact-lbl">Alamat</div><div class="fn-contact-val">Jl. Otomotif No. 123, Jakarta</div></div>
</div>
<div class="fn-contact-row">
<div class="fn-contact-icon">📞</div>
<div><div class="fn-contact-lbl">Telepon</div><div class="fn-contact-val">(021) 1234-5678</div></div>
</div>
<div class="fn-contact-row">
<div class="fn-contact-icon">✉️</div>
<div><div class="fn-contact-lbl">Email</div><div class="fn-contact-val">info@smartgarage.id</div></div>
</div>
<div class="fn-contact-row">
<div class="fn-contact-icon">🕐</div>
<div><div class="fn-contact-lbl">Jam Operasional</div><div class="fn-contact-val">Senin – Sabtu, 08:00 – 20:00 WIB</div></div>
</div>
<div class="fn-contact-row" style="margin-bottom:0;">
<div class="fn-contact-icon">🌐</div>
<div><div class="fn-contact-lbl">Website</div><div class="fn-contact-val">www.smartgarage.id</div></div>
</div>
</div>
</div>
<div class="fn-bottom">
<span class="fn-bottom-left">&#169; 2026 SmartGarage &#8211; Tugas Akhir Otomata. All rights reserved.</span>
<span class="fn-bottom-right">Dibangun dengan Python + Streamlit</span>
</div>
</div>
""", unsafe_allow_html=True)


# ═══════ HALAMAN CHAT ═══════
else:
    session = st.session_state.session

    # Membuat layout grid 3 kolom untuk memaksa area chat berkumpul di tengah layar wide
    col_space_l, col_content, col_space_r = st.columns([1.5, 5, 1.5])
    
    with col_content:
        # Baris Header HTML: Info AutoCare di kiri, tombol disiapkan space di kanan
        st.markdown("""
        <div class="chat-top-bar">
            <div class="chat-bot-info">
                <div class="chat-bot-avatar">🤖</div>
                <div>
                    <div class="chat-bot-name">AutoCare Assistant</div>
                    <div class="chat-bot-sub">Tanyakan masalah kendaraanmu</div>
                </div>
            </div>
            <div id="close-btn-place"></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Penempatan tombol Streamlit asli agar pas di dalam kontainer kanan atas chat-top-bar
        header_cols = st.columns([6, 1.5])
        with header_cols[1]:
            # CSS hack margin-top minus untuk menarik tombol naik ke dalam baris header HTML
            st.markdown('<div style="margin-top: -68px; position: relative; z-index: 999;">', unsafe_allow_html=True)
            if st.button("✕ Tutup", key="chat_close_btn", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        # ── LOGIKA & RIWAYAT CHAT MESSAGES ──
        if not session.chat_history:
            service_mode = st.session_state.get("service_mode", None)
            if service_mode:
                st.session_state.service_mode = None
                session.fsm.transition(Event.START_CHAT)
                event_map = {
                    "diagnosa": Event.DIAGNOSA,
                    "servis": Event.SERVIS,
                    "tips": Event.TIPS,
                }
                module_map = {
                    "diagnosa": "diagnosis",
                    "servis": "service",
                    "tips": "maintenance",
                }
                evt = event_map[service_mode]
                session.fsm.transition(evt)
                session.current_module = module_map[service_mode]
                gen = ResponseGenerator()
                response = gen.generate(session.fsm.get_current_state())
                session.add_message("bot", response)
            else:
                welcome = (
                    "Halo, aku **AutoCare Assistant** 👋\n\n"
                    "Aku bisa bantu kamu dengan:\n"
                    "- **Diagnosa** — cari tahu masalah kendaraanmu\n"
                    "- **Servis** — lihat jadwal perawatan berkala\n"
                    "- **Tips** — panduan merawat kendaraan\n\n"
                    "Ada yang bisa aku bantu hari ini?"
                )
                session.add_message("bot", welcome)
                session.fsm.transition(Event.START_CHAT)

        for m in session.chat_history:
            is_user  = m["sender"] == "user"
            cls      = "user" if is_user else "bot"
            label    = "Kamu" if is_user else "AutoCare"
            wrap_cls = "user-wrap" if is_user else "bot-wrap"
            msg = m["message"]
            if not is_user:
                msg = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', msg)
                msg = re.sub(r'\*(.+?)\*',     r'<em>\1</em>',         msg)
                msg = re.sub(r'\n- ',          r'<br>• ',               msg)
                msg = msg.replace('\n', '<br>')
            st.markdown(
                f'<div class="msg-wrap {wrap_cls}">'
                f'<div class="msg-lbl {cls}">{label}</div>'
                f'<div class="msg-bubble {cls}">{msg}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    # ── INPUT CHAT ──
    st.markdown("<br>", unsafe_allow_html=True)
    prompt = st.chat_input("Ketik pesan kamu di sini...")
    if prompt:
        controller.process_input(session, prompt)
        st.rerun()