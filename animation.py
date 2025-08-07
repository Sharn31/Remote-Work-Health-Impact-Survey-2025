import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(layout="right")
st.title("🎉 Welcome to Remote Work Wellbeing App")

lottie_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")

if lottie_animation:
    st_lottie(lottie_animation, height=300, key="remote-health")
