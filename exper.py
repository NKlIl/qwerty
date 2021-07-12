from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def remote_css(url):
    st.markdown('<style src="{}"></style>'.format(url), unsafe_allow_html=True)

def icon_css(icone_name):
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

def icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)      
      
st.title('Страновед')
st.subheader('Этот сайт знает столицу любой страны.')

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
      st.success('Здесь появится ответ.')    
      
else:
      st.error('Error')    

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.subheader('Бот в Telegram: https://t.me/NikiBombinoBot')





