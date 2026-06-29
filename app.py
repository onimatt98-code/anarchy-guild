import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Guild Passwords
MEMBER_PASSWORD = "anarchy2026"
ADMIN_PASSWORD = "anarchyadmin" 

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# 3. Styling
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    .stButton>button { background-color: #ff4500; color: white; border-radius: 5px; width: 100%; font-weight: bold; }
    .whatsapp-btn { display: block; background-color: #25D366; color: white !important; text-align: center; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; margin: 15px auto; width: 80%; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.title("🛡️ ♱ ANARCHY 🛡️")
    st.write("### ⚔️ Clan Verification")
    
    user_name = st.text_input("Your Free Fire Name")
    input_password = st.text_input("Enter Guild Password", type="password")

    if st.button("Access Dashboard"):
        if user_name.strip() == "":
            st.error("Please enter your name.")
        elif input_password == ADMIN_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True
            st.session_state["username"] = user_name
            st.rerun()
        elif input_password == MEMBER_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = False
            st.session_state["username"] = user_name
            st.rerun()
        else:
            st.error("Incorrect password.")

# --- DASHBOARD ---
else:
    st.title(f"⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️")
    st.subheader(f"Welcome back, {st.session_state['username']} ⚔️")
    
    if st.button("Disconnect Session"):
        st.session_state["logged_in"] = False
        st.session_state["is_admin"] = False
        st.rerun()
        
    st.divider()
    
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER", "💬 COMMUNITY HUBS"])
    
    with portal_tabs[0]:
        st.write("### Sup gamers 🤯.")
        st.markdown("""
        **1.)** Avoid insults/lust messages. **2.)** 1k guild points weekly or kick. **3.)** 10-day name change policy. 
        **4.)** Guild war: 7pm-11pm Fri/Sat. **5.)** Requirements: Lvl 60+, Prime 3+. **6.)** Daily training 10pm. 
        **7.)** Zero Tolerance policy. **8.)** Performance cuts. **9.)** Chain of command. **10.)** Fear the elders 🗿
        """)

    with portal_tabs[1]:
        st.write("### 📢 OFFICIAL MEMBERS ROSTER")
        st.write("**Core Leadership Group:**")
        st.markdown("* 👑 **♱  DARK** (Guild Leader)\n* 🛡️ **♱ KUROTŚUI** (Admin)\n* 🛡️ **♱  PRIDE** (Admin)\n* 🛡️ **♱  EMMA** (Admin)\n* 🛡️ **♱  YENG** (Admin)")
        st.write("**Active Roster Enforcers:**")
        st.markdown("* ⚔️ **♱  KAISER**\n* ⚔️ **♱  SAVAGE.**\n* ⚔️ **♱ﾠDAMZY🪶**\n* ⚔️ **♱ﾠHEMJAY**")

    with portal_tabs[2]:
        st.markdown(f'<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP GC</a>', unsafe_allow_html=True)

    # --- ADMIN ONLY SECTION ---
    if st.session_state["is_admin"]:
        st.divider()
        st.warning("🛡️ ADMIN MANAGEMENT CONSOLE")
        st.write("Authorized access verified. You can now oversee guild operations.")
