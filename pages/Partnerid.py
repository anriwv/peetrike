import requests 
from pyspark import SparkConf
from pyspark import SparkContext

import streamlit as st 
from streamlit_lottie import st_lottie

# Set the page configuration
st.set_page_config(
    page_title="Koostööpartnerid",
    page_icon="🚀",
)

url = requests.get( 
    "https://lottie.host/a5888eeb-f34f-4a3a-9e68-1ce6bc4e1e29/8QLSbaMulG.json") 
url_json = dict() 
if url.status_code == 200: 
    url_json = url.json() 
else: 
    print("Error in URL") 

st.markdown("""
<h1 style="text-align: center;">Koostööpartnerid</h1>
""", unsafe_allow_html=True)

st_lottie(url_json, height=200, speed=1, loop=True, quality='high')

st.markdown("""
<div style='text-align: center;'>
    <h4>Nõo Reaalgümnaasium</h4>
    <a href='https://nrg.edu.ee/'><img src='https://nrg.edu.ee/sites/nrg.edu.ee/files/styles/hitsa_core_logo/public/nrg_uus_logo.jpg' alt='Nõo Reaalgümnaasium' style='max-width: 60%; max-height: 60%; display: block; margin-left: auto; margin-right: auto;' /></a>
    <h4>TT Print OÜ</h4>
    <a href='https://ttprint.ee/'><img src='https://raw.githubusercontent.com/anriwv/peetrike/main/ttprint.png' alt='TT Print OÜ' style='max-width: 25%; max-height: 25%; display: block; margin-left: auto; margin-right: auto;' /></a>
</div>
""", unsafe_allow_html=True)

