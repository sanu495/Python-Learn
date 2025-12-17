# Streamlit 

import Streamlit_app as St   
   # Its used for develop web app in python without using a HTML, CSS, and JavaScript

St.title("StreamLit App")
St.header("welcome to the App")
St.write("This is a simple app bulit with Streamlit")

# Interactive element

name=St.text_input("What is your name")

if name:
    St.success(f"HELLO, {name}")

# Slider example

age=St.slider("Select your age", 1, 100, 25)
St.write("You selected:", age)



