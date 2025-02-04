import streamlit as st

from UI.eda import run_eda
from UI.ml import run_ml
from UI.home import run_home



def main():
    st.title('자동차 예측 가격 앱')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()







if __name__ == '__main__':
    main()