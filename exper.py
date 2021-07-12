from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Страновед')
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
elif balloons == 'Cша':
      st.success('Столица США, Вашингтон 🇺🇸.')
elif balloons == 'соединённые штаты америки':
      st.success('Столица Соединённых Штатов Америки, Вашингтон 🇺🇸.')
elif balloons == '🇳🇦':
      st.success('Столица Намибии Виндхук 🇳🇦.')
elif balloons == 'намибия':
      st.success('Столица Намибии Виндхук 🇳🇦.')
elif balloons == '':
      st.success('M')      
