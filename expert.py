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


elif balloons == '🇺🇸':
      st.success('Столица США, Вашингтон 🇺🇸.')   
elif balloons == 'сша':
      st.success('Столица США, Вашингтон 🇺🇸.')
elif balloons == 'соединённые штаты америки':
      st.success('Столица Соединённых Штатов Америки, Вашингтон 🇺🇸.')
elif balloons == 'United States of America':
      st.success('Capital of the United States of America, Washington 🇺🇸.')    
elif balloons == '🇳🇦':
      st.success('Столица Намибии Виндхук 🇳🇦.')
elif balloons == 'намибия':
      st.success('Столица Намибии Виндхук 🇳🇦.')



      
