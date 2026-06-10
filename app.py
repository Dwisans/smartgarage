import streamlit as st

st.set_page_config(page_title="SmartGarage", page_icon="🔧", layout="centered")

from chatbot.chat_controller import ChatController
from chatbot.session_manager import SessionManager
from automata.events import Event

if "session" not in st.session_state:
    st.session_state.session = SessionManager()
if "page" not in st.session_state:
    st.session_state.page = "home"

controller = ChatController()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #0d0d0d;
    --surface: #1a1a1a;
    --surface2: #242424;
    --border: #2e2e2e;
    --accent: #f97316;
    --accent2: #f59e0b;
    --text: #f5f5f5;
    --muted: #9ca3af;
}

#root > div:first-child { background: var(--bg); }

.stApp > header { background: transparent !important; }
.stApp > header:before { display: none !important; }

.block-container { padding: 3.5rem 1.5rem 0.75rem !important; max-width: 800px !important; }

h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: var(--text) !important;
}

p, li, .stMarkdown {
    color: var(--text) !important;
}

.hdr { display: flex; align-items: center; gap: 10px; padding: 8px 0 4px; }
.hdr-icon { font-size: 24px; line-height: 1; }
.hdr-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 18px; color: var(--accent); letter-spacing: -0.3px; }
.hdr-status { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--muted); letter-spacing: 1px; text-transform: uppercase; margin-left: auto; }
.hdr-dot { display: inline-block; width: 6px; height: 6px; background: #22c55e; border-radius: 50%; margin-right: 4px; animation: pls 2s infinite; }
@keyframes pls { 0%,100%{opacity:1} 50%{opacity:.3} }

.hr { border: none; border-top: 1px solid var(--border); margin: 8px 0 12px; }

.msg-wrapper { margin-bottom: 10px; }
.msg-label { font-family: 'JetBrains Mono', monospace; font-size: 9px; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 3px; }
.msg-label.user { color: var(--muted); text-align: right; }
.msg-label.bot { color: var(--accent); }
.msg-bubble {
    padding: 10px 14px; border-radius: 10px;
    font-size: 14px; line-height: 1.6;
    max-width: 88%;
    word-wrap: break-word;
}
.msg-bubble.user {
    background: var(--accent); color: #fff;
    margin-left: auto; border-bottom-right-radius: 4px;
}
.msg-bubble.bot {
    background: var(--surface); border: 1px solid var(--border);
    color: var(--text); border-bottom-left-radius: 4px;
}
.msg-bubble.bot strong { color: var(--accent2); }
.msg-bubble.bot em { color: var(--muted); }

.home-hero { text-align: center; padding: 32px 0 16px; }
.home-hero h1 { font-size: 28px; letter-spacing: -0.5px; margin-bottom: 8px; }
.home-hero h1 span { color: var(--accent); }
.home-hero p { color: var(--muted); font-size: 14px; max-width: 500px; margin: 0 auto; line-height: 1.6; }

.card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; padding: 16px;
    transition: border-color .2s;
}
.card:hover { border-color: var(--accent); }
.card-icon { font-size: 22px; margin-bottom: 4px; }
.card-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 14px; color: var(--accent); }
.card-desc { font-size: 12px; color: var(--muted); margin-top: 4px; line-height: 1.5; }

.stButton button {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    transition: all .2s !important;
}
.stButton button:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    background: rgba(249,115,22,.1) !important;
}
.stButton button[kind="primary"] {
    background: var(--accent) !important;
    color: #fff !important;
    border-color: var(--accent) !important;
}

.stChatInput { border: 1px solid var(--border) !important; border-radius: 10px !important; background: var(--surface) !important; }
.stChatInput:focus-within { border-color: var(--accent) !important; box-shadow: 0 0 0 2px rgba(249,115,22,.15) !important; }
.stChatInput input { color: var(--text) !important; caret-color: var(--accent) !important; }
.stChatInput input::placeholder { color: #555 !important; }

.metric {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 12px; text-align: center;
}
.metric-val { font-family: 'JetBrains Mono', monospace; font-size: 22px; color: var(--accent); font-weight: 600; }
.metric-label { font-size: 11px; color: var(--muted); margin-top: 2px; }

.footer { text-align: center; padding: 20px 0; }
.footer span { font-size: 11px; color: #444; }
</style>
""", unsafe_allow_html=True)

hdr = st.columns([1, 8, 3])
with hdr[0]:
    st.markdown('<div class="hdr-icon">🔧</div>', unsafe_allow_html=True)
with hdr[1]:
    st.markdown('<div class="hdr-title">SmartGarage</div>', unsafe_allow_html=True)
with hdr[2]:
    label = "✖ Tutup" if st.session_state.page == "chat" else "💬"
    if st.button(label, use_container_width=True):
        st.session_state.page = "chat" if st.session_state.page == "home" else "home"
        st.rerun()

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ═══════ HOME ═══════
if st.session_state.page == "home":
    st.markdown("""
    <div class="home-hero">
        <h1>Bengkel Pintar untuk <span>Kendaraanmu</span></h1>
        <p>Asisten digital berbasis FSM: diagnosa kerusakan, servis berkala, dan tips perawatan — semuanya dalam satu chatbot.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💬 Mulai Konsultasi", type="primary", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    c = st.columns(3)
    cards = [
        ("🔍", "Diagnosa", "Cari tahu masalah kendaraan secara sistematis."),
        ("🛠️", "Servis Berkala", "Rekomendasi servis berdasarkan kilometer."),
        ("💡", "Tips Perawatan", "Panduan merawat mesin, rem, ban, dan lainnya."),
    ]
    for i, (icon, title, desc) in enumerate(cards):
        with c[i]:
            st.markdown(
                f'<div class="card"><div class="card-icon">{icon}</div>'
                f'<div class="card-title">{title}</div>'
                f'<div class="card-desc">{desc}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br><div class='hr'></div>", unsafe_allow_html=True)
    st.markdown("### Tentang")
    st.markdown(
        "SmartGarage menggabungkan **Finite State Machine (FSM)** "
        "dengan layanan otomotif. Setiap alur diagnosa diverifikasi "
        "sistematis — tidak ada tebak-tebakan."
    )
    st.markdown(
        '<div class="metric"><div class="metric-val">30</div>'
        '<div class="metric-label">Total State FSM · 21 Events · 48+ Transitions</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    st.markdown("### Kontak")
    k = st.columns(4)
    for i, (e, l, v) in enumerate([
        ("📍", "Alamat", "Jl. Otomotif No. 123"),
        ("📞", "Telepon", "(021) 1234-5678"),
        ("✉️", "Email", "info@smartgarage.id"),
        ("🕐", "Jam", "Sen–Sab 08:00–20:00"),
    ]):
        with k[i]:
            st.markdown(f"**{e} {l}**", unsafe_allow_html=True)
            st.caption(v)
    st.markdown("<div class='footer'><span>SmartGarage — Tugas Akhir Otomata © 2026</span></div>", unsafe_allow_html=True)

# ═══════ CHAT ═══════
else:
    session = st.session_state.session

    if not session.chat_history:
        welcome = (
            "Halo, aku AutoCare Assistant.\n\n"
            "Aku bisa bantu:\n"
            "- **Diagnosa** \u2014 cari tahu masalah kendaraanmu\n"
            "- **Servis** \u2014 lihat jadwal perawatan berkala\n"
            "- **Tips** \u2014 panduan merawat kendaraan\n\n"
            "Ada yang bisa aku bantu?"
        )
        session.add_message("bot", welcome)
        session.fsm.transition(Event.START_CHAT)

    st.markdown(
        '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">'
        '<span style="font-size:18px;">💬</span>'
        '<span style="font-family:\'Plus Jakarta Sans\',sans-serif;font-weight:700;font-size:16px;color:var(--text);">AutoCare Assistant</span>'
        '<span class="hdr-dot"></span>'
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;">Online</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    for m in session.chat_history:
        is_user = m["sender"] == "user"
        label = "Kamu" if is_user else "Bot"
        cls = "user" if is_user else "bot"
        st.markdown(
            f'<div class="msg-wrapper">'
            f'<div class="msg-label {cls}">{label}</div>'
            f'<div class="msg-bubble {cls}">{m["message"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    prompt = st.chat_input("Ketik pesan...")
    if prompt:
        controller.process_input(session, prompt)
        st.rerun()
