from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

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
elif balloons == '':
      st.success('Здесь появится ответ.')    

      
elif balloons == '🇺🇸':
      st.success('Столица США, Вашингтон 🇺🇸.')   
elif balloons == 'США':
      st.success('Столица США, Вашингтон 🇺🇸.') 
elif balloons == 'USA':
      st.success('Capital of the USA, Washington 🇺🇸.')   
elif balloons == 'Соединённые Штаты Америки':
      st.success('Столица Соединённых Штатов Америки, Вашингтон 🇺🇸.')      
elif balloons == 'United States of America':
      st.success('Capital of the United States of America, Washington 🇺🇸.') 
elif balloons == '🇳🇦':
      st.success('Столица Намибии Виндхук 🇳🇦.')
elif balloons == 'Намибия':
      st.success('Столица Намибии Виндхук 🇳🇦.')
elif balloons == 'Namibia':
      st.success('The capital of Namibia is Windhoek 🇳🇦.')
elif balloons == 'Russia':
      st.success('Capital of Russia, Moscow 🇷🇺.')
elif balloons == '🇬🇧':
      st.success('Столица Великобритании, Лондон 🇬🇧.')
elif balloons == 'Англия':
      st.success('Англия — страна, являющаяся крупнейшей административно-политической частью Соединённого Королевства Великобритании и Северной Ирландии.')
elif balloons == 'Великобритания':
      st.success('Столица Великобритании, Лондон 🇬🇧.')
elif balloons == 'Great Britain':
      st.success('The capital of the Great Britain is London 🇬🇧.')   
elif balloons == '🇨🇦':
      st.success('Столица Канады, Оттава 🇨🇦.')
elif balloons == 'Канада':
      st.success('Столица Канады, Оттава 🇨🇦.')
elif balloons == 'Canada':             
      st.success('Ottawa, the capital of Canada 🇨🇦.')     
elif balloons == "🇳🇴":
      st.success( 'Столица Норвегии, Осло 🇳🇴.')
      
      
      
      
      
      
      
      
      
      
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
