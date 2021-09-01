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
elif balloons == 'Норвегия':
      st.success( 'Столица Норвегии, Осло 🇳🇴.')
elif balloons == 'Norway':
      st.success( 'The capital of Norway, Oslo 🇳🇴.')
elif balloons == '🇯🇵':
      st.success( 'Столица Японии, Токио 🇯🇵.')
elif balloons == 'Япония':
      st.success( 'Столица Японии, Токио 🇯🇵.')
elif balloons == 'Japan':
      st.success( 'Capital of Japan, Tokyo 🇯🇵.')                
elif balloons == '🇨🇳':
      st.success( "Столица Китайской Народный Республики, Пекин 🇨🇳.")        
elif balloons == 'КНР':
      st.success( 'Столица КНР, Пекин 🇨🇳.')
elif balloons == 'Китайская Народная Республика':
      st.success( 'Столица Китайской Народный Республики, Пекин 🇨🇳.')  
elif balloons == 'Китай':
      st.success( 'Столица Китая, Пекин 🇨🇳.')        
elif balloons == 'PRC':
      st.success( "Capital of the People's Republic of China, Beijing 🇨🇳.")    
elif balloons == "People' s Republic of China":
      st.success( "Capital of the People's Republic of China, Beijing 🇨🇳.")
elif balloons == "China":
      st.success( 'Capital of China, Beijing 🇨🇳.')     
elif balloons == '🇹🇼':
      st.success( 'Столица Китайской Республики (Тайваня), Тайбэй 🇹🇼.')
elif balloons == 'Китайская Республика':
      st.success( 'Столица Китайской Республики (Тайваня), Тайбэй 🇹🇼.')
elif balloons == 'Republic of China':
      st.success( 'Capital of the Republic of China (Taiwan), Taipei 🇹🇼.')    
elif balloons == 'Тайвань':
      st.success( 'Столица Тайваня, Тайбэй 🇹🇼.')     
elif balloons == 'Taiwan':
      st.success( 'Capital of Taiwan, Taipei 🇹🇼.')       
elif balloons == '🇫🇷':
      st.success( 'Столица Франции, Париж 🇫🇷.')
elif balloons == 'Франция':
      st.success( 'Столица Франции, Париж 🇫🇷.')
elif balloons == 'France':
      st.success( 'The capital of France is Paris 🇫🇷.')  
elif balloons == '🇵🇦':
      st.success( 'Столица Панамы, Панама 🇵🇦.')      
elif balloons == 'Панама':
      st.success( 'Столица Панамы, Панама 🇵🇦.') 
elif balloons == 'Panama':
      st.success( 'Capital of Panama, Panama 🇵🇦.')    
elif balloons == '🇦🇹':
      st.success( 'Столица Австрии, Вена 🇦🇹.')           
elif balloons == 'Австрия':
      st.success( 'Столица Австрии, Вена 🇦🇹.')
elif balloons == 'Austria':
      st.success( 'Capital of Austria, Vienna 🇦🇹.')   
elif balloons == '🇧🇾':
      st.success( 'Столица Белоруссии, Минск 🇧🇾.')
elif balloons == 'Белоруссия':
      st.success( 'Столица Белоруссии, Минск 🇧🇾.')
elif balloons == 'Беларусь':
      st.success( 'Столица Белоруссии, Минск 🇧🇾.')   
elif balloons == 'Belarus':
      st.success( 'The capital of Belarus, Minsk 🇧🇾.')
elif balloons == '🇧🇪':
      st.success( 'Столица Бельгии, Брюссель 🇧🇪.')
elif balloons == 'Бельгия':
      st.success( 'Столица Бельгии, Брюссель 🇧🇪.')
elif balloons == 'Belgium':
      st.success( 'The capital of Belgium, Brussels 🇧🇪.')        
elif balloons == '🇧🇬':
      st.success( 'Столица Болгарии, София 🇧🇬.')
elif balloons == 'Болгария':
      st.success( 'Столица Болгарии, София 🇧🇬.')
elif balloons == 'Bulgaria':
      st.success( 'The capital of Bulgaria, Sofia 🇧🇬.')    
elif balloons == '🇻🇦':
      st.success( 'Столица Ватикана, Ватикан 🇻🇦.')
elif balloons == 'Ватикан':
      st.success( 'Столица Ватикана, Ватикан 🇻🇦.')
elif balloons == 'Vatican':
      st.success( 'Capital of the Vatican, Vatican 🇻🇦.')
elif balloons == '🇭🇺':
      st.success( 'Столица Венгрии, Будапешт 🇭🇺.') 
elif balloons == 'Венгрия':
      st.success( 'Столица Венгрии, Будапешт 🇭🇺.')
elif balloons == 'Hungary':
      st.success( 'The capital of Hungary, Budapest 🇭🇺.')
elif balloons == '🇩🇪':
      st.success( 'Столица Германии, Берлин 🇩🇪.')
elif balloons == 'Германия':
      st.success( 'Столица Германии, Берлин 🇩🇪.')
elif balloons == 'Germany':
      st.success( 'The capital of Germany, Berlin 🇩🇪.')
elif balloons == '🇬🇷':
      st.success( 'Столица Греции, Афины 🇬🇷.')    
elif balloons == 'Греция':
      st.success( 'Столица Греции, Афины 🇬🇷.')
elif balloons == 'Greece':
      st.success( 'Capital of Greece, Athens 🇬🇷.')
elif balloons == '🇩🇰':
      st.success( 'Столица Дании, Копенгаген 🇩🇰.')   
elif balloons == 'Дания':
      st.success( 'Столица Дании, Копенгаген 🇩🇰.')
elif balloons == 'Denmark':
      st.success( 'Capital of Denmark, Copenhagen 🇩🇰.')    
elif balloons == '🇮🇸':
      st.success( 'Столица Исландии, Рейкьявик 🇮🇸.')
elif balloons == 'Исландия':
      st.success( 'Столица Исландии, Рейкьявик 🇮🇸.')
elif balloons == 'Iceland':
      st.success( 'Capital of Iceland, Reykjavik 🇮🇸.')
elif balloons == '🇯🇲':
      st.success( 'Столица Ямайки, Кингстон 🇯🇲.')    
elif balloons == 'Ямайка':
      st.success( 'Столица Ямайки, Кингстон 🇯🇲.')
elif balloons == 'Jamaica':
      st.success( 'Capital of Jamaica, Kingston 🇯🇲.')
elif balloons == '🇪🇸':
      st.success( 'Столица Испании, Мадрид 🇪🇸.')    
elif balloons == 'Испания':
      st.success( 'Столица Испании, Мадрид 🇪🇸.')
elif balloons == 'Spain':
      st.success( 'Capital of Spain, Madrid 🇪🇸.')    
elif balloons == '🇮🇹':
      st.success( 'Столица Италии, Рим 🇮🇹.')
elif balloons == 'Италия': 
      st.success( 'Столица Италии, Рим 🇮🇹.')        
elif balloons == 'Italy':
      st.success( 'Capital of Italy, Rome 🇮🇹.')
elif balloons == '🇱🇻':
      st.success( 'Столица Латвии, Рига 🇱🇻.')  
elif balloons == 'Латвия':
      st.success( 'Столица Латвии, Рига 🇱🇻.')  
elif balloons == 'Latvia':
      st.success( 'The capital of Latvia, Riga 🇱🇻.')  
elif balloons == '🇱🇹':
      st.success( 'Столица Литвы, Вильнюс 🇱🇹.')
elif balloons == 'Литва':
      st.success( 'Столица Литвы, Вильнюс 🇱🇹.')    
elif balloons == 'Lithuania':
      st.success( 'The capital of Lithuania, Vilnius 🇱🇹.')   
elif balloons == '🇲🇽':
      st.success( 'Столица Мексики, Мехико 🇲🇽.')
elif balloons == 'Мексика':
      st.success( 'Столица Мексики, Мехико 🇲🇽.') 
elif balloons == 'Mexico':
      st.success( 'The capital of Mexico, Mexico City 🇲🇽.')
elif balloons == '🇵🇱':
      st.success( 'Столица Польши, Варшава 🇵🇱.')
elif balloons == 'Польша':
      st.success( 'Столица Польши, Варшава 🇵🇱.')   
elif balloons == 'Poland':
      st.success( 'The capital of Poland, Warsaw 🇵🇱.')   
elif balloons == '🇵🇹':
      st.success( 'Столица Португалии, Лиссабон 🇵🇹.')
elif balloons == 'Португалия':
      st.success( 'Столица Португалии, Лиссабон 🇵🇹.')    
elif balloons == 'Portugal':
      st.success( 'Capital of Portugal, Lisbon 🇵🇹.')  
elif balloons == '🇱🇮':
      st.success( 'Столица Лихтенштейна, Вадуц 🇱🇮.')
elif balloons == 'Лихтенштейн':
      st.success( 'Столица Лихтенштейна, Вадуц 🇱🇮.')        
elif balloons == 'Liechtenstein':
      st.success( 'Capital of Liechtenstein, Vaduz 🇱🇮.')        
elif balloons == '🇱🇺':
      st.success( 'Столица Люксембурга, Люксембург 🇱🇺.')
elif balloons == 'Люксембург':
      st.success( 'Столица Люксембурга, Люксембург 🇱🇺.')
elif balloons == 'Luxembourg':
      st.success( 'Capital of Luxembourg, Luxembourg 🇱🇺.')
elif balloons == '🇲🇰':
      st.success( 'Столица Македонии, Скопье 🇲🇰.')
elif balloons == 'Македония':
      st.success( 'Столица Македонии, Скопье 🇲🇰.')
elif balloons == 'Macedonia':
      st.success( 'The capital of Macedonia, Skopje 🇲🇰.')    
elif balloons == '🇲🇹':
      st.success( 'Столица Мальты, Валлетта 🇲🇹.')
elif balloons == 'Мальта':
      st.success( 'Столица Мальты, Валлетта 🇲🇹.')    
elif balloons == 'Malta':
      st.success( 'Capital of Malta, Valletta 🇲🇹.')
elif balloons == '🇲🇩':
      st.success( 'Столица Молдавии, Кишинёв 🇲🇩.')
elif balloons == 'Молдавия':
      st.success( 'Столица Молдавии, Кишинёв 🇲🇩.')
elif balloons == 'Moldavia':
      st.success( 'The capital of Moldova, Chisinau 🇲🇩.')
elif balloons == '🇲🇨':
      st.success( 'Столица Монако, Монако 🇲🇨.')
elif balloons == 'Монако':
      st.success( 'Столица Монако, Монако 🇲🇨.')    
elif balloons == 'Monaco':
      st.success( 'Capital of Monaco, Monaco 🇲🇨.')
elif balloons == '🇳🇱':
      st.success( 'Столица Нидерландов, Амстердам 🇳🇱.')
elif balloons == 'Голландия':
      st.success( 'Столица Нидерландов, Амстердам 🇳🇱.')
elif balloons == 'Нидерланды':
      st.success( 'Столица Нидерландов, Амстердам 🇳🇱.')
elif balloons == 'Netherlands':
      st.success( 'The capital of the Netherlands, Amsterdam 🇳🇱.')     
elif balloons == '🇷🇴':
      st.success( 'Столица Румынии, Бухарест 🇷🇴.')    
elif balloons == 'Румыния':
      st.success( 'Столица Румынии, Бухарест 🇷🇴.')
elif balloons == 'Romania':
      st.success( 'Capital of Romania, Bucharest 🇷🇴.')   
elif balloons == '🇷🇸':
      st.success( 'Столица Сербии, Белград 🇷🇸.')
elif balloons == 'Сербия':
      st.success( 'Столица Сербии, Белград 🇷🇸.')
elif balloons == 'Serbia':
      st.success( 'Capital of Serbia, Belgrade 🇷🇸.')
elif balloons == '🇸🇰':
      st.success( 'Столица Словакии, Братислава 🇸🇰.')
elif balloons == 'Словакия':
      st.success( 'Столица Словакии, Братислава 🇸🇰.')
elif balloons == 'Slovakia':
      st.success( 'Capital of Slovakia, Bratislava 🇸🇰.')
elif balloons == '🇸🇮':
      st.success( 'Столица Словении, Любляна 🇸🇮.')
elif balloons == 'Словения':
      st.success( 'Столица Словении, Любляна 🇸🇮.')
elif balloons == 'Slovenia':
      st.success( 'The capital of Slovenia, Ljubljana 🇸🇮.')
elif balloons == '🇳🇬':
      st.success( 'Столица Нигерии, Абуджа 🇳🇬.')   
elif balloons == 'Нигерия':
      st.success( 'Столица Нигерии, Абуджа 🇳🇬.')   
elif balloons == 'Nigeria':
      st.success( 'Capital of Nigeria, Abuja 🇳🇬.')   
elif balloons == '🇦🇷':
      st.success( 'Столица Аргентины, Буэнос-Айрес 🇦🇷.')
elif balloons == 'Аргентина':
      st.success( 'Столица Аргентины, Буэнос-Айрес 🇦🇷.')
elif balloons == '1':
      st.success( 'С любимыми не расставайтесь...\n\nС любимыми не расставайтесь\nС любимыми не расставайтесь\nС любимыми не расставайтесь\nВсей кровью прорастайте в них\n\nИ каждый раз навек прощайтесь\nИ каждый раз навек прощайтесь\nИ каждый раз навек прощайтесь\nКогда уходите на миг\n\nИ если мне укрыться нечем\nОт жалости неисцелимой\nИ если мне укрыться нечем\nОт холода и темноты?\nЗа расставанием будет встреча\nНе забывай меня, любимый\nЗа расставанием будет встреча\nВернемся оба – я и ты\n\nИ если я безвестно кану\nВ короткий свет луча дневного\nНо если я безвестно кану\nЗа звездный пояс в млечный дым\nЯ за тебя молиться стану\nЧтоб не забыл пути земного\nЯ за тебя молиться стану\nЧтоб ты вернулся невредим\n\nС любимыми не расставайтесь\nС любимыми не расставайтесь\nС любимыми не расставайтесь\nВсей кровью прорастайте в них\nИ каждый раз навек прощайтесь\nИ каждый раз навек прощайтесь\nИ каждый раз навек прощайтесь\nКогда уходите на миг...')
                  


      
      
      
      
      
      
      
      
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
