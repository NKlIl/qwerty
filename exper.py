from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
/*
-----------------------
    MAIN APP
-----------------------
*/
body {
  margin: 0;
  font-family: 'Poppins', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.6;
  color: #ffffff;
  background-color: #12D8FA;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(38,39,48,0);
}
/*
----------------------
      BUTTONS
----------------------
*/
.stButton > button {
  background-color: #000000;
  border-style:none;
  z-index: 4;
}
.stButton > button:hover {
  background-color: #333333;
  color: #ffffff;
}

/*
-------------------------------
   SideBar DropDown Menu Box
-------------------------------
*/
.st-c3 {
  background: #84F9F0;
  border: none;
}
/*
-----------------------------
    Down Chevron Button
------------------------------
*/
.st-d0
{
  background: #84F9F0;
  border: none;
}
/*
-------------------------------
  Border of the Dropdown Box
-------------------------------
*/
.st-bb {
  border: none;
}
/*

*/
.stTextInput
{
  color: #000000;
}
.stTextInput > div > div > input {
  color: #000000;
}
/* 
-----------------
     Sidebar 
-----------------
*/
.css-1aumxhk {
  background-color: #011839;
  background-image: none;
  color: #ffffff;
  border: none;
  }
.css-1aumxhk:hover{
    background-color: #011839;
    background-image: none;
    color: #ffffff;
    border: none;
    }
/* 
----------------
    ICONS
----------------
*/
.css-3xqji8{
      background-color: #111;
      color: #fff;
      border: none;
  }
.css-3xqji8:active{
      background-color: #fff;
      color: #111;
      border: none;
  }
.css-3xqji8:hover{
      background-color: #fff;
      color: #111;
      border: none;
    }
/* 
-----------------
   Sidebar Menu
-----------------
*/
.css-145kmo2 {
  font-size: 0.8rem;
  color:#ffffff;
  margin-bottom: 0.4rem;
}

.css-l7x2nz:hover{
  background-color: #111;
  color: #fff;
}
/* 
-----------------
    Main Menu
-----------------
*/
.css-13qyw8b:hover {
  margin: 0px;
  padding: 0.25rem 1.5rem;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  cursor: pointer;
  background-color: rgb(240, 242, 246);
}

.css-1vbb94r {
  border-top: 1px solid rgb(213, 218, 229);
  border-bottom: 1px solid rgb(213, 218, 229);
  vertical-align: middle;
  padding: 0.75rem;
  color: #fff;
  font-family: 'Poppins',sans-serif;
}
/* 
-----------------
   Table Color
-----------------
*/
table{
  background-color: #011839;
}
/* 
-----------------
    Headings
-----------------
*/
h1,h2,h3,h4,h5
{
  font-family: 'Poppins', sans-serif;
}
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





