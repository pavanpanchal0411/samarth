
import pandas as pd
import streamlit as st
from PIL import Image


st.title("EV Services")
vehical=st.radio("Which vehical do you prefer",['two_wheel','four_wheel'])
two_wheel=("Select","Aether","Ola","TVS","Vida")
four_wheel=("Select","Tata","MG-Hecter","Mahindra","Hundai")
if vehical=="two_wheel":
    Scooter=st.selectbox("Select the two wheeler you desire",two_wheel)
    if Scooter == "Aether":
        image = Image.open("aether.jpg")
        st.image(image,width=300)
    elif Scooter == "Ola":
        image = Image.open("ola.jpeg")
        st.image(image,width=300)
    elif Scooter == "TVS":
        image = Image.open("iqube.webp")
        st.image(image,width=300)
    elif Scooter == "Vida":
        image = Image.open("vida.jpeg")
        st.image(image,width=300)


    
elif vehical=="four_wheel":   
    Car=st.selectbox("Select the four wheeler you desire",four_wheel)
    if Car=="Tata":
        image = Image.open("tata.jpeg")
        st.image(image,width=300)
    elif Car=="MG-Hecter":
        image = Image.open("MG-Hector.webp")
        st.image(image,width=300)
    elif Car=="Mahindra":
        image = Image.open("mahndra.webp")
        st.image(image,width=300)
    elif Car=="Hundai":
        image = Image.open("hundai.webp")
        st.image(image,width=300)
        




time=st.slider("How much time do you want the vehical for(in hrs)",1,12)


options= st.radio("Do you want delivary or rent",['Rent','Delivary'])
Rent=("Baiyappanahalli",
"Swami Vivekananda Road",
"Indiranagar",
"Halasuru",
"Trinity",
"Mahatma Gandhi Road",
"Cubbon Park",
"Vidhana Soudha",
"Sir M. Visveshwaraya",
"Majestic",
"City Railway Station",
"Magadi Road",
"Hosahalli",
"Vijayanagar",
"Attiguppe",
"Deepanjali Nagar",
"Mysore Road")

if options=="Rent":
    st.selectbox("Select the outlet",Rent)
elif options=="Delivary":
    Delivary = st.text_input("Enter some text:")
    st.write("The vehical will be delivered to",Delivary)

price=0

if vehical=="two_wheel":
   price=time*2000
   st.write("The cost of the vehical is:",price)

elif vehical=="four_wheel":
    price=time*3000
    st.write("The cost of the vehical is:",price)


Mode=st.radio("Select the mode of payment:",['UPI','QR'])
if Mode=="UPI":
    UPI=st.text_input("Enter the UPI ID")

elif Mode=="QR":
    image = Image.open("scan.jpg")
    st.image(image,width=300)
    
    
