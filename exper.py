import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import time
import streamlit as st
import plotly.express as px

st.title('Страновед 🌐')
st.subheader('Этот сайт знает столицу любой страны.')
st.markdown('  https://t.me/NikiBombinoBot')

balloons = st.text_input("Напишите ниже страну или её флаг.")
if balloons == "Россия":
   st.success("Столица России, Москва 🇷🇺.")
elif balloons == "Россия ":
      st.success("Столица России, Москва 🇷🇺.")
elif balloons == "россия":
      st.success("Столица России, Москва 🇷🇺.")
elif balloons == "россия ":
      st.success("Столица России, Москва 🇷🇺.")
elif balloons == "🇷🇺":
      st.success("Столица России, Москва 🇷🇺.")
elif balloons == "🇷🇺 ":
      st.success("Столица России, Москва 🇷🇺.")


