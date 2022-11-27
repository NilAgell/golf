#imports
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO


st.set_page_config(page_title= 'Golf',page_icon=":eyes:",initial_sidebar_state="collapsed",layout="wide",menu_items={
        'About': "# This is a project for visual analytics."
    })


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output)
    df.to_excel(writer, index=False, sheet_name='Sheet1')
   
  
    writer.save()
    processed_data = output.getvalue()
    return processed_data


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data=pd.read_excel(uploaded_file)

    b=np.zeros(7)
    res=np.zeros(22)
    for x in data.axes[0]:
        a=data.iloc[x,1:]
        for i in range(0, 7):
            b[i]=a[i]
            
        b.sort()
        res[x]=b[6]+b[5]+b[4]
        data.iloc[x,8]=res[x]


    df_xlsx = to_excel(data)
    st.download_button(
        label='📥 Download Current Result',
        data=df_xlsx ,
        file_name= 'Total.xlsx')
   






