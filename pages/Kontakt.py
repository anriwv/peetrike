import streamlit as st
import pandas as pd


st.title("Kontakt")

st.subheader("Aadress: Kalju Aigro 5")

with st.expander("Tahan olla 'Peetrike' liige!!!"):
    st.write(
        """Võta meiega ühendust:
         Peetrikese email: nrgpeetrike@gmail.com"""
    )


# Create a DataFrame with one row and two columns (latitude and longitude)
data = {'lat': [58.2798126], 'lon': [26.5345858]}

# Display the map using the DataFrame
st.map(pd.DataFrame(data), zoom=13, color='#c18383')

# HTML code with CSS for the glowing effect
glowing_instagram_logo = """
<style>
.img-glow {
  animation: glow 1s ease-in-out infinite alternate;
}
@keyframes glow {
  0% {
    filter: drop-shadow(0 0 5px #c18383);
  }
  100% {
    filter: drop-shadow(0 0 15px #c18383);
  }
}
</style>
"""

# Display clickable icons with specified sizes
st.markdown("Vaata insta kontot <a href='https://www.instagram.com/nrgpeetrike/'><img src='https://github.com/anriwv/peetrike/blob/main/Instagram_logo_2022.svg.png?raw=true' width='50' class='img-glow'></a>" + glowing_instagram_logo, unsafe_allow_html=True)
