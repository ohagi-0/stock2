import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門2')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

st.write('Intereactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右からカラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')  

text = st.text_input('あなたの趣味を教えてください')
condition = st.slider('あんたの今の調子は',0,100,50)
option = st.selectbox(
    'あなたが好きな数字を教えてください、',
             list(range(1,10)))

st.write('あなたの趣味:',text)
st.write('コンディション',condition)
st.write('あなたの好きな数字は、',option,'です。')


if st.checkbox("Show Image"):

    img = Image.open('霜降り.jpg')
    st.image(img,caption='霜降り明星',use_column_width=True)
    st.write('Data Frame')

if st.checkbox("Show Map"):
    df = pd.DataFrame(
        np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
        columns=["lat","lon"])
    st.map(df)


