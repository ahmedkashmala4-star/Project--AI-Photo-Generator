import streamlit as st
from PIL import Image
from model_logic import process_image
import io

st.set_page_config(page_title="Neon AI Photo", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    header { visibility: hidden; }
    
    /* Globe aur Login line fix */
    .top-nav { display: flex; justify-content: flex-end; align-items: center; gap: 15px; }
    
    div.stButton > button#login_btn {
        background: linear-gradient(90deg, #ff9a8b, #ff6a88) !important;
        border-radius: 20px !important; color: white !important; border: none !important;
        padding: 5px 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

t_col1, t_col2 = st.columns([0.85, 0.15])
with t_col2:
    nav_c1, nav_c2 = st.columns([0.3, 0.7])
    with nav_c1: st.markdown("<h3 style='margin:0;'>🌐</h3>", unsafe_allow_html=True)
    with nav_c2: 
        if st.button("Login", key="login_btn"): st.write("Login Popup")

st.markdown("<h1 style='text-align:center; color:#00f2ff;'>AI Photo Generator</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")

with c1:
    st.subheader("📤 Image")
    file = st.file_uploader("Upload", type=["jpg", "png"], label_visibility="collapsed")
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)

with c2:
    st.subheader("✍️ Command")
    prompt = st.text_area("Example:Gold watch, moody, orange slices", height=100)
    
    if st.button("RUN GENERATION", use_container_width=True):
        if file and prompt:
            res = process_image(img, prompt, "🚀 Cloud API (Fast)")
            st.markdown("### ✨ Result")
            st.image(res, use_container_width=True)
            
            buf = io.BytesIO()
            res.save(buf, format="PNG")
            st.download_button("💾 Download HD", buf.getvalue(), "output.png", "image/png", use_container_width=True)
        else:
            st.error("Upload image and type prompt first!")