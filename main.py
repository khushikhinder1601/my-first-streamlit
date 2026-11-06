import streamlit as st
st.title("shopping bill calculator ")
st.header("welcome")
n=st.selectbox('choose product',['pen','pencil','earser'])
p=st.number_input('enter price  ',min_value=0)



x=st.slider('CHOOSE quantity ',0,500)
t=p*x
st.write(f'YOUR Total bill is {t}')




