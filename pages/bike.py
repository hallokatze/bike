import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"] # 메인에서 사용한 session_state 가져오기
with st.sidebar:
    st.caption(f'{ID}님 접속중')

data = pd.read_csv("공공자전거.csv") # 같은 폴더내 없지만 app.py와 공공자전거.csv가 같은 폴더에 있으면 작동됨

data['total'] = 5*(data['LCD'] + data['QR'])+6
data

st.title('공공자전거 어디있지?')


data = data.copy().fillna(0)
# data.loc[:,'size'] = 5*(data['LCD']+data['QR'])
# data


color = {'QR':'#37eb91',
         'LCD':'#ebbb37'}
data['color'] = data.copy()['운영방식'].map(color)


st.map(data,
       latitude="위도",
       longitude="경도",
       size="total",
       color="color")
