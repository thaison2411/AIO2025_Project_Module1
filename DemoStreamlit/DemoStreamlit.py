from re import I
from turtle import color
import streamlit as st

st.title("Project 1")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.caption("I love AIVN")

st.divider()

st.markdown("#Heading 1")
st.markdown("##Heading 2")
st.markdown("[AIVN](http:ss)")
st.markdown("""
1. Machine Learning
2. Deep Learning
""")
st.markdown(r"$sqrt{2x+2}$")
st.latex(r"$\sqrt{2x+2}$")

st.code(
"""
import numpy as np
arr = np.array([1.0, 2.0])
"""
, language="python")

st.divider()
st.write("Hello")
st.write("##Heading 2")
st.write(r"$\sqrt{2x}$")

#st.divider()
#Media
#st.logo("")
#st.image("")
#st.audio("")
#st.video("")

st.divider()
#Input
status = st.checkbox("I agree")
if status:
    st.write("You agreed!")
st.radio(
    "Color",
    ["Yellow", "Blue"],
    captions=["Vang", "Xanh"])
st.selectbox(
    "Contact", ("Email", "Address"))

colors = st.multiselect(
    "Colors",
    ["GPT", "Gemini", "Claude"]
)
st.write(color)

st.divider()
number = st.select_slider(
    "Number:",
    option=[10, 30, 50, 70, 100]
)
st.write(number)

st.slider(
    "Values:",
    0.0, 100.0
)

st.divider()
name = st.text_input("Your name:")
st.write(name)

st.divider()
# Button
if st.button("Say hello"):
    st.write("Hello!")
else:
    st.write("Goodbye!")

st.link_button(
    "Go to AIVN",
    "http://"
    )

# Chatbot
st.chat_input("Say something")
st.file_uploader(
    "Choose a file", 
    accept_multiple_files=True
)
for uploaded_file in uploaded_file:
    st.write(uploaded_file.name)

st.divider()
import pandas as pd
import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)


