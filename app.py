
      
import datetime
import urllib.parse
import streamlit as st

# 1. إعداد الصفحة والهوية البصرية المتكاملة (Glassmorphism & Neon Blue Theme)
st.set_page_config(
    page_title="OilSafe - Petro Operations", page_icon="🦺", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #020617 0%, #070e1b 100%);
        color: #FFFFFF;
        font-family: sans-serif;
    }
    .main-card {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
    }
    .card-permits {
        background: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 12px;
        padding: 14px;
        color: white;
    }
    .card-camera {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid rgba(0, 240, 255, 0.3);
        border-radius: 12px;
        padding: 14px;
        color: white;
    }
    .card-injections {
        background: linear-gradient(135deg, #0369a1 0%, #0c4a6e 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 12px;
        padding: 14px;
        color: white;
    }
    .card-samples {
        background: linear-gradient(135deg, #581c87 0%, #3b0764 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        border-radius: 12px;
        padding: 14px;
        color: white;
    }
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #020617;
        border-top: 1px solid rgba(255,255,255,0.1);
        padding: 8px 0;
        display: flex;
        justify-content: space-around;
        z-index: 999;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

# إدارة حالة التنقل والصفحات
if "page" not in st.session_state:
    st.session_state.page = "home"
if "admin_unlocked" not in st.session_state:
    st.session_state.admin_unlocked = False
if "lang" not in st.session_state:
    st.session_state.lang = "English"

# ==========================================
# 1. الشاشة الرئيسية (HOME / DASHBOARD)
# ==========================================
if st.session_state.page == "home":

    h_col1, h_col2, h_col3 = st.columns([1, 5, 1])
    with h_col1:
        if st.button("☰", key="menu_btn"):
            st.session_state.page = "menu"
            st.rerun()
    with h_col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <div style="font-weight: 800; font-size: 15px; letter-spacing: 1px; color: #FFFFFF;">PETRO OPERATIONS</div>
                <div style="font-size: 9px; color: #94a3b8;">Permits • Injections • Samples</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with h_col3:
        if st.button("⚙️", key="settings_btn"):
            st.session_state.page = "settings"
            st.rerun()

    st.write("")

    # بانر صورة الحقل البترولي
    st.markdown(
        """
        <div class='main-card' style='padding:0; overflow:hidden;'>
            <div style='background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80"); background-size: cover; height: 100px; display: flex; align-items: flex-end; padding: 8px;'>
                <span style='color: #fff; font-size: 10px; background: rgba(0,0,0,0.6); padding: 2px 8px; border-radius: 4px;'>Oil & Gas Field Operations</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # صف الأزرار الأول
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class='card-permits'>
                <div style='font-size: 16px;'>📋</div>
                <div style='font-weight: bold; font-size: 14px; margin-top: 3px;'>PERMITS</div>
                <div style='font-size: 9px; color: #a7f3d0;'>Document and manage work permits</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Open Permits", use_container_width=True, key="btn_perm"):
            st.session_state.page = "permits"
            st.rerun()

    with c2:
        st.markdown(
            """
            <div class='card-camera'>
                <div style='font-size: 16px;'>📷</div>
                <div style='font-weight: bold; font-size: 14px; margin-top: 3px;'>CAMERA</div>
                <div style='font-size: 9px; color: #94a3b8;'>Take permit photos<br>1/3 of the panel</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Open Camera", use_container_width=True, key="btn_cam"):
            st.session_state.page = "permits"
            st.rerun()

    # صف الأزرار الثاني
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(
            """
            <div class='card-injections'>
                <div style='font-size: 16px;'>🛢️</div>
                <div style='font-weight: bold; font-size: 14px; margin-top: 3px;'>INJECTIONS</div>
                <div style='font-size: 9px; color: #bae6fd;'>Well injection tracking</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Open Injections", use_container_width=True, key="btn_inj"):
            st.info("Injections panel.")

    with c4:
        st.markdown(
            """
            <div class='card-samples'>
                <div style='font-size: 16px;'>🧪</div>
                <div style='font-weight: bold; font-size: 14px; margin-top: 3px;'>SAMPLES</div>
                <div style='font-size: 9px; color: #e9d5ff;'>Collect and analyze samples</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Open Samples", use_container_width=True, key="btn_sam"):
            st.info("Samples panel.")

    # قسم الـ Induction
    st.markdown(
        """
        <div class='main-card' style='display:flex; justify-content:space-between; align-items:center; padding: 10px 14px;'>
            <div>
                <div style='font-weight: bold; font-size: 12px;'>📖 Induction</div>
                <div style='font-size: 9px; color: #94a3b8;'>Work procedures and safety info</div>
            </div>
            <div style='color: #38bdf8;'>➔</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # العدادات السريعة
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown(
            """
            <div class='main-card' style='text-align:center; padding: 8px;'>
                <div style='font-size: 9px; color: #94a3b8;'>Today's Permits</div>
                <div style='font-size: 18px; font-weight: bold; color: #10b981;'>2</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with sc2:
        st.markdown(
            """
            <div class='main-card' style='text-align:center; padding: 8px;'>
                <div style='font-size: 9px; color: #94a3b8;'>Today's Samples</div>
                <div style='font-size: 18px; font-weight: bold; color: #a855f7;'>3</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # التقرير اليومي
    st.markdown(
        """
        <div class='main-card' style='display:flex; justify-content:space-between; align-items:center; padding: 10px 14px; margin-bottom: 60px;'>
            <div>
                <div style='font-weight: bold; font-size: 12px;'>📅 DAILY REPORT</div>
                <div style='font-size: 9px; color: #94a3b8;'>View and close daily summary</div>
            </div>
            <div style='color: #38bdf8;'>➔</div>
        </div>
    """,
        unsafe_allow_html=True,
    )


# ==========================================
# 2. شاشة التصاريح الكاملة (PERMITS)
# ==========================================
elif st.session_state.page == "permits":
    col_bk1, col_bk2 = st.columns([1, 6])
    with col_bk1:
        if st.button("❮", key="back_home"):
            st.session_state.page = "home"
            st.rerun()
    with col_bk2:
        st.markdown(
            "<h4 style='margin:0; color:#fff; font-size:15px;'>PERMITS</h4><p style='font-size:10px; color:#94a3b8; margin:0;'>Capture - Review - Share</p>",
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size: 11px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;'>1. Capture Permit</div>",
        unsafe_allow_html=True,
    )
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.file_uploader(
            "Open Camera", type=["jpg", "png"], key="cam_up", label_visibility="collapsed"
        )
    with p_col2:
        st.file_uploader(
            "Choose Photos", type=["jpg", "png"], key="gal_up", label_visibility="collapsed"
        )
    st.markdown(
        "<div style='font-size:9px; color:#10b981; margin-top:4px;'>Photo 1 ✓  &nbsp; Photo 2 ✓  &nbsp; <span style='color:#38bdf8;'>Auto Crop & Enhance</span></div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    d_h1, d_h2 = st.columns([4, 1])
    with d_h1:
        st.markdown(
            "<div style='font-size: 11px; font-weight: bold; color: #38bdf8;'>2. Permit Report</div>",
            unsafe_allow_html=True,
        )
    with d_h2:
        if st.button("Edit All", key="edit_all"):
            st.info("Edit mode active")

    p_type = st.text_input("Permit Type", value="HOT WORK PERMIT")
    location = st.text_input("Location", value="T.B. 8/2")
    dc1, dc2 = st.columns(2)
    with dc1:
        date_val = st.text_input("Date", value="15/10/2026")
    with dc2:
        hour_val = st.text_input("Hour", value="2:45 PM")
    permit_no = st.text_input("Permit No", value="0183115")
    task_desc = st.text_area(
        "Permit Task", value="TROUBLESHOOTING FOR E.S.P WELLS AT T.B 8/2(R)"
    )
    st.markdown(
        "<div style='font-size: 10px; color: #94a3b8; margin-top:4px;'>Gas Test Reading: &nbsp;<b style='color:#fff;'>LEL 0% &nbsp; O2 20.8% &nbsp; CO 0 PPM &nbsp; H2S 0 PPM</b></div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size: 11px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;'>3. Attached Photos</div>",
        unsafe_allow_html=True,
    )
    img_c1, img_c2 = st.columns(2)
    with img_c1:
        st.markdown(
            "<div style='background:#1e293b; padding:6px; border-radius:6px; text-align:center; font-size:9px;'>📷 Photo 1 <span style='color:#10b981; float:right;'>[Cropped]</span></div>",
            unsafe_allow_html=True,
        )
    with img_c2:
        st.markdown(
            "<div style='background:#1e293b; padding:6px; border-radius:6px; text-align:center; font-size:9px;'>📷 Photo 2 <span style='color:#10b981; float:right;'>[Cropped]</span></div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='main-card' style='margin-bottom: 60px;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size: 11px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;'>4. WhatsApp Report</div>",
        unsafe_allow_html=True,
    )
    final_msg = f"""*HOT WORK PERMIT*
🌍 *Location* : {location}
📅 *Date* : {date_val}
🕰️ *Hour* : {hour_val}
➡️ *Permit No* : {permit_no}
➡️ *Permit Task* : {task_desc}

*Gas Test Reading :*
➡️ LEL = 0%
➡️ O2 = 20.8%
➡️ CO = 0 PPM
➡️ H2S = 0 PPM"""
    encoded_wa = urllib.parse.quote(final_msg)
    wa_url = f"https://api.whatsapp.com/send?text={encoded_wa}"

    w_btn1, w_btn2, w_btn3 = st.columns([1, 2, 1])
    with w_btn2:
        st.markdown(
            f"""
            <a href="{wa_url}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#10b981; color:white; text-align:center; padding:8px; border-radius:6px; font-weight:bold; font-size:12px;">
                    🟢 Share via WhatsApp
                </div>
            </a>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 3. شاشة إعدادات التطبيق (SETTINGS)
# ==========================================
elif st.session_state.page == "settings":
    if st.button("❮ Back"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown(
        "<h4 style='text-align:center; color:#fff;'>Settings</h4>",
        unsafe_allow_html=True,
    )

    if not st.session_state.admin_unlocked:
        st.markdown(
            """
            <div class='main-card' style='text-align:center; padding:15px;'>
                <div style='font-size: 20px;'>🔒</div>
                <div style='font-weight:bold; font-size:13px; margin-top:4px;'>Restricted Access</div>
                <div style='font-size:10px; color:#94a3b8; margin-bottom:10px;'>Advanced settings are locked. Enter your admin code to continue.</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        entered_pin = st.text_input(
            "Enter admin code", type="password", key="pin_in"
        )
        if st.button("Unlock", use_container_width=True, type="primary"):
            if entered_pin == "1234":
                st.session_state.admin_unlocked = True
                st.success("Unlocked successfully!")
                st.rerun()
            else:
                st.error("Incorrect code. Try 1234")
    else:
        st.success("🟢 Admin Mode Unlocked (Full Access)")

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    if st.button("🌐 Language / اللغة (English / العربية)", use_container_width=True):
        st.session_state.page = "language"
        st.rerun()
    st.markdown("📅 Date & Time &nbsp; (Auto / 24h)")
    st.markdown("ℹ️ App Info &nbsp; (Version 1.0.0)")
    st.markdown("❓ Help & Support &nbsp; (Contact support)")
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 4. شاشة اختيار اللغة (LANGUAGE)
# ==========================================
elif st.session_state.page == "language":
    if st.button("❮ Back"):
        st.session_state.page = "settings"
        st.rerun()

    st.markdown(
        "<h4 style='color:#fff;'>Language</h4><p style='font-size:10px; color:#94a3b8;'>Choose your preferred language</p>",
        unsafe_allow_html=True,
    )
    if st.button("🇬🇧 English (Default)", use_container_width=True):
        st.session_state.lang = "English"
    if st.button("🇸🇦 العربية (Arabic)", use_container_width=True):
        st.session_state.lang = "Arabic"
    st.info(f"Current Language: {st.session_state.lang}")


# ==========================================
# 5. شاشة القائمة الجانبية (SIDE MENU)
# ==========================================
elif st.session_state.page == "menu":
    st.markdown(
        "<h4 style='color:#fff; margin:0;'>PETRO OPERATIONS</h4><p style='font-size:10px; color:#38bdf8; margin:0;'>Oil & Gas Field Operations</p>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    if st.button("📋 Permits", use_container_width=True):
        st.session_state.page = "permits"
        st.rerun()
    if st.button("⚙️ Settings", use_container_width=True):
        st.session_state.page = "settings"
        st.rerun()
    st.markdown("---")
    if st.button("❌ Close Menu", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --- شريط التنقل السفلي الثابت ---
st.markdown(
    """
    <div class='bottom-nav'>
        <div style='text-align:center; font-size:9px; color:#38bdf8;'>🏠<br>Home</div>
        <div style='text-align:center; font-size:9px; color:#94a3b8;'>📋<br>Permits</div>
        <div style='text-align:center; font-size:9px; color:#94a3b8;'>🛢️<br>Injection</div>
        <div style='text-align:center; font-size:9px; color:#94a3b8;'>🧪<br>Samples</div>
        <div style='text-align:center; font-size:9px; color:#94a3b8;'>📅<br>Daily</div>
        <div style='text-align:center; font-size:9px; color:#94a3b8;'>⚙️<br>Settings</div>
    </div>
""",
    unsafe_allow_html=True,
)
