import pandas as pd
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    
    st.subheader('탐색적 데이터 분석')

    st.info('데이터를 분석 합니다.')

    df=pd.read_csv('data/Car_Purchasing_Data.csv')
    st.dataframe(df)

    if st.button('통계 데이터 보기'):
        st.dataframe(df.describe())

    if st.checkbox('상관관계분석'):
        st.dataframe(df.corr(numeric_only=True))

    st.info('상관관계분석')
    menu = ['차트로보기','수치로보기']
    choice = st.radio('선택하세요',menu)
    if choice == menu[0]:
        fig1 = plt.figure()
        sb.heatmap(data=df.corr(numeric_only=True), annot=True, cmap='coolwarm' , linecolor='black', linewidths=0.5)
        st.pyplot(fig1)
    elif choice == menu[1]:
        st.dataframe(df.corr(numeric_only=True))

        # 컬럼을 선택하면 회당 컬럼에 대한 최댓값과 최소값을 알려주는것
    st.info('최대.최소 데이터 확인하기')
    menu2=['Age','Annual Salary','Credit Card Debt','Net Worth']
    selected_columns = st.selectbox('컬럼선택', menu2)

    st.dataframe(df.loc[df[selected_columns]==df[selected_columns].max()])


    