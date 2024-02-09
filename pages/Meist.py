import streamlit as st

custom_text_color = "#FAFAFA"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{

background-color: #31333F;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #31333F 40px ), repeating-linear-gradient( #f46d6d55, #f46d6d );

}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("PEETRIKESE AJALUGU - MEIST")


st.write(
    """
    Peetrike asutati 1992 aasta kevadel. 
    Koolilehe asutajaks on Martin Pau, kes alustas koolilehe välja andmist olles ise NRG 11.klassis.
    Päris alguses oli koolilehe nimeks Sirp ja Peetrike. Nõukogude ajal ilmus kultuurileht Sirp ja Vasar ning arvatavasti pärines Sirp sealt.
    Peetrikese nimi sai pandud koolilehe teise asutaja Priit Einmanni poolt, meenutades ühte lasteraamatut või filmi.
    Ühel hetkel kadus Sirp sealt eest ära ning jäi alles ainult nimi Peetrike.
    Sirbi ja Peetrikese nime all on ilmunud 1992. aasta kevadel ainult kolm-neli numbrit, kuid kahjuks pole ükski numbritest säilinud.
    Peetrikese asutaja Martin Pau on öelnud: 
    'Peetrikese nimi oli täiesti ambitsioonitu, tähendusetu, suisa mõttetu. 
    Võib-olla sellepärast osutuski heaks nimeks ja võib-olla on sellepärast siiamaani püsima jäänud.
    On imetlusväärne, et 23 aasta jooksul ei ole tahetud paremat panna.'
    """)


