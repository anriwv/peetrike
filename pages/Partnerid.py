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
  

st.title("Koostööpartnerid") 
  
st_lottie(url_json, 
          reverse=True, # change the direction of our animation 
          height=200, # height and width of animation 
          width=200,
          speed=1, # speed of animation  
          loop=True, # means the animation will run forever like a gif, and not as a still image 
          quality='high', # quality of elements used in the animation, other values are "low" and "medium" 
          )

st.title("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
#conf = SparkConf().setAppName("lecture-lyon2").setMaster("local")
#sc = SparkContext.getOrCreate(conf=conf)
