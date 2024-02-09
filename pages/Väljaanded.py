import streamlit as st
from streamlit_gsheets import GSheetsConnection

def embed_pdf(pdf_url):
    pdf_iframe = f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={pdf_url}#toolbar=0&scrollbar=0" width="100%" height="800" style="border: none"></iframe>'
    return pdf_iframe


st.title("Peetrike Arhiiv")

# Alapealkiri
st.subheader("Tere tulemast avastama minevikku ja lugema läbi 'Peetrike' koolilehe ajalugu.")

# Arhiivi tekstiblokk
st.markdown("""
'Peetrike' on Nõo Reaalgümnaasiumi koolileht, mis on jäädvustanud meie kooli elu ja arengut aastate jooksul.
Siin saate sirvida vanu numbreid ning avastada kooliperes toimunud olulisi hetki.

Leiate palju huvitavaid lugusid, pilte ja mälestusi, mis annavad aimu meie kooli mitmekesisest ajaloost.

Täname, et jagate meiega huvi meie kooli pärandi vastu ning avastate koos meiega 'Peetrike' koolilehe rikkalikku ajalugu.
""")



# Establish connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Cache all data from the sheets
@st.cache_data
def cache_all_data():
    data = {}
    list_data = conn.read(worksheet="LIST")
    sheet_names = list_data.iloc[:, 0].dropna().astype(int).tolist()[::-1]
    for sheet_name in sheet_names:
        data[sheet_name] = conn.read(worksheet=str(sheet_name))
    return data

# Read all data
data_cache = cache_all_data()

# Create a dropdown menu to choose the sheet
selected_sheet = st.sidebar.selectbox("Select a sheet:", list(data_cache.keys()))

# Read the data from the selected sheet
selected_sheet_data = data_cache[selected_sheet]

# Extract values from columns A and B, excluding NaN values
names = selected_sheet_data.iloc[:, 0].dropna().tolist()
pdf_urls = selected_sheet_data.iloc[:, 1].dropna().tolist()

# Create tabs dynamically based on the names
tabs = st.tabs(names)

# Iterate through tabs to embed PDFs
for i in range(min(len(names), len(pdf_urls))):
    with tabs[i]:
        st.markdown(embed_pdf(pdf_urls[i]), unsafe_allow_html=True)
