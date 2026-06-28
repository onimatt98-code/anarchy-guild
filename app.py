import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", layout="centered")

# 2. Security Credentials
MEMBER_PASS = "anarchy2026"
ADMIN_PASS = "anarchyadmin"  # The secret key for admin features

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False

# --- LOGIN SCREEN ---
if not st.session_state["logged_in"]:
    st.title("🛡️ ♱ ANARCHY Portal")
    user_name = st.text_input("Free Fire Name")
    password = st.text_input("Password", type="password")
    
    if st.button("Sync Dashboard"):
        if password == ADMIN_PASS:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True
            st.session_state["username"] = user_name
            st.rerun()
        elif password == MEMBER_PASS:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = False
            st.session_state["username"] = user_name
            st.rerun()
        else:
            st.error("Invalid password. Please check the clan GC.")

# --- DASHBOARD ---
else:
    st.title(f"⚔️ Welcome, {st.session_state['username']}")
    if st.button("Disconnect Session"):
        st.session_state["logged_in"] = False
        st.session_state["is_admin"] = False
        st.rerun()
    
    st.divider()
    st.write("### 📜 Guild Orders")
    st.info("Here are the official orders for the current season.")
    
    # --- ADMIN ONLY SECTION ---
    if st.session_state["is_admin"]:
        st.divider()
        st.warning("🛡️ ADMIN CONSOLE UNLOCKED")
        st.write("You have full control over the portal.")
        # Admin tools go here
        if st.button("View Live Logs"):
            st.write("Displaying active connections...")
    else:
        st.write("Standard Member View.")
