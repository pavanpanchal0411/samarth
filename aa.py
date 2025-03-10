
# import streamlit as st
# from PIL import Image

# st.title("EV Rentals car services")
# st.subheader("to rent or deliver any tyoe of ev you desire")
# st.subheader("tell the options foe the delivary and rent")





# st.subheader("now for which type of vehical")
# scooter_options = ("Ola", "iQube", "Ather")
# car_options = ("Tata", "Tesla", "Porsche")


# st.subheader("Now, select the type of vehicle:")


# scooter_button = st.button("Scooter")
# car_button = st.button("Car")

# if scooter_button:
#     selected_scooter = st.selectbox("Select a scooter:", scooter_options)

    
#     if selected_scooter == "Ola":
#         st.write("The rental price for Ola scooter is ₹12,000")
#     elif selected_scooter == "Ather":
#         st.write("The rental price for Ather scooter is ₹13,000")
#     elif selected_scooter == "iQube":
#         st.write("The rental price for iQube scooter is ₹20,000")

# if car_button:
#     selected_car = st.selectbox("Select a car:", car_options)

    
#     if selected_car == "Tata":
#         st.write("The rental price for Tata car is ₹4,000")
#     elif selected_car == "Tesla":
#         st.write("The rental price for Tesla car is ₹3,000")
#     elif selected_car == "Porsche":
#         st.write("The rental price for Porsche car is ₹35,000")

# if st.button("Submit"):
#     st.write("Your vehical is : {}")
#     st.success(" submitted successfully!")



# rent=("A","B","C")
# M=st.button("delivary")
# M1=st.button("rent")
        
# if M:
#     adress=st.text_input("enter the adress") 
# elif M1:
#      st.write("select the outlet")
#      aa=st.selectbox("rent",rent)
    



# # # if rent:
# # #     st.write("choose which outlet you are renting from")
# # #     st.selectbox("rent:",rent)
# # #     if rent=="a":
# # #         st.write("6000")
# # #     elif rent=="b":
# # #         st.write("6000")
# # #     else:
# # #         st.write("4000")


# st.subheader("Select your payment method")

# payment_methods = ('Select', 'UPI', 'QR Code')
# selected_payment = st.selectbox("Choose your payment method:", payment_methods)

# if selected_payment == 'QR Code':
#     image = Image.open("scan.jpeg")
#     st.image(image, caption='Scan this QR Code using PhonePe', use_column_width=True)

# elif selected_payment == 'UPI':
#     st.title("UPI ID")
#     upi_id = st.text_input("Enter your UPI ID:")

    
#     if st.button("Submit"):
#         st.write(f"Your UPI ID: {upi_id}")
#         st.success("Form submitted successfully!")













# import streamlit as st
# import pandas as pd
# from PIL import Image

# # Initialize session state for the buttons
# if "delivery_button_clicked" not in st.session_state:
#     st.session_state.delivery_button_clicked = False
# if "rent_button_clicked" not in st.session_state:
#     st.session_state.rent_button_clicked = False

# # Title and subtitles
# st.title("EV Rentals Car Services")
# st.subheader("To rent or deliver any type of EV you desire")
# st.subheader("Choose an option below:")

# # Delivery and rent options
# delivery_options = ('Location Q', 'Location W', 'Location E')
# rent_options = ('Outlet A', 'Outlet B', 'Outlet C')

# if st.button("Delivery"):
#     st.session_state.delivery_button_clicked = True
#     st.session_state.rent_button_clicked = False  # Reset the other button

# if st.button("Rent"):
#     st.session_state.rent_button_clicked = True
#     st.session_state.delivery_button_clicked = False  # Reset the other button

# if st.session_state.delivery_button_clicked:
#     selected_delivery = st.selectbox("Select a delivery location:", delivery_options)
#     if selected_delivery == 'Location Q':
#         st.write("The total amount for purchasing is ₹22,900")
#     elif selected_delivery == 'Location W':
#         st.write("The total amount for purchasing is ₹50,888")
#     elif selected_delivery == 'Location E':
#         st.write("The total amount for purchasing is ₹8,099")

# if st.session_state.rent_button_clicked:
#     selected_rent = st.selectbox("Select a rental outlet:", rent_options)
#     if selected_rent == 'Outlet A':
#         st.write("Rental price is ₹6,000")
#     elif selected_rent == 'Outlet B':
#         st.write("Rental price is ₹6,000")
#     elif selected_rent == 'Outlet C':
#         st.write("Rental price is ₹4,000")


# car_data = pd.read_csv('Cheapestelectriccars-EVDatabase 2023 (1).csv')

# car_data['PriceinGermany'] = (
#     car_data['PriceinGermany']
#     .str.replace(',', '', regex=True)
#     .str.extract('(\d+\.?\d*)')[0]
#     .astype(float) / 100
# )

# car_prices = dict(zip(car_data['Name'], car_data['PriceinGermany']))

# st.title("Car Price Selector")

# car_name = st.selectbox("Select a car", list(car_prices.keys()))

# if car_name:
#     st.write(f"The price of {car_name} is {car_prices[car_name]:,.2f}")



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

    