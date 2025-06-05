import streamlit as st
import pandas as pd
from PIL import Image

# --- LOGIN PAGE ---
def login():
    st.title("🔐 Login to EV Services")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# --- MAIN APP ---
def main_app():
    st.title("⚡ EV Services")
    vehical = st.radio("Which vehicle do you prefer", ['two_wheel', 'four_wheel'])

    two_wheel = ("Select", "Aether", "Ola", "TVS", "Vida")
    four_wheel = ("Select", "Tata", "MG-Hecter", "Mahindra", "Hundai")

    if vehical == "two_wheel":
        Scooter = st.selectbox("Select the two wheeler you desire", two_wheel)
        if Scooter == "Aether":
            image = Image.open("aether.jpg")
            st.image(image, width=300)
        elif Scooter == "Ola":
            image = Image.open("ola.jpeg")
            st.image(image, width=300)
        elif Scooter == "TVS":
            image = Image.open("iqube.webp")
            st.image(image, width=300)
        elif Scooter == "Vida":
            image = Image.open("vida.jpeg")
            st.image(image, width=300)

    elif vehical == "four_wheel":
        Car = st.selectbox("Select the four wheeler you desire", four_wheel)
        if Car == "Tata":
            image = Image.open("tata.jpeg")
            st.image(image, width=300)
        elif Car == "MG-Hecter":
            image = Image.open("MG-Hector.webp")
            st.image(image, width=300)
        elif Car == "Mahindra":
            image = Image.open("mahndra.webp")
            st.image(image, width=300)
        elif Car == "Hundai":
            image = Image.open("hundai.webp")
            st.image(image, width=300)

    time = st.slider("How much time do you want the vehicle for (in hrs)", 1, 12)

    options = st.radio("Do you want delivery or rent", ['Rent', 'Delivary'])
    Rent = ("Baiyappanahalli", "Swami Vivekananda Road", "Indiranagar", "Halasuru", "Trinity",
            "Mahatma Gandhi Road", "Cubbon Park", "Vidhana Soudha", "Sir M. Visveshwaraya",
            "Majestic", "City Railway Station", "Magadi Road", "Hosahalli", "Vijayanagar",
            "Attiguppe", "Deepanjali Nagar", "Mysore Road")

    if options == "Rent":
        st.selectbox("Select the outlet", Rent)
    elif options == "Delivary":
        Delivary = st.text_input("Enter your address:")
        st.write("The vehicle will be delivered to", Delivary)

    price = 0
    if vehical == "two_wheel":
        price = time * 2000
        st.write("The cost of the vehicle is:", price)
    elif vehical == "four_wheel":
        price = time * 3000
        st.write("The cost of the vehicle is:", price)

    Mode = st.radio("Select the mode of payment:", ['UPI', 'QR'])
    if Mode == "UPI":
        UPI = st.text_input("Enter the UPI ID")
    elif Mode == "QR":
        image = Image.open("scan.jpg")
        st.image(image, width=300)


# --- SESSION HANDLING ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    main_app()
