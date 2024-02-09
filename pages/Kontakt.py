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



# Display clickable icons with specified sizes
st.markdown("""Vaata insta kontot <a href='https://www.instagram.com/nrgpeetrike/'><img src='https://upload.wikimedia.org/wikipedia/commons/3/3e/Instagram_simple_icon.svg' width='50'></a>""", unsafe_allow_html=True)
