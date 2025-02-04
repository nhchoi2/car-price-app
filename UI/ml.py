import numpy as np
import streamlit as st
import joblib

def run_ml():
    # 유저에게 예측에 필요한 데이터를 입력 받는다.
    # 나이, 연봉, 신용카드 부채, 순자산을 입력받는다.
    # 인공지능으로 예측하여, 결과를 화면에 보여준다.

    age = st.number_input('나이를 입력하세요', min_value= 18, max_value=90)
    salary = st.number_input('연봉를 입력하세요',  min_value= 100000, step=100)
    card_debt = st.number_input('신용카드부채를 입력하세요', min_value= 1000, step=100)
    worth = st.number_input('순자산을 입력하세요', min_value=300000, step=50)   
    st.text(f'고객님이 입력하신 정보는')
    st.text(f'나이 :  {age}')
    st.text(f'연봉 : {salary}')
    st.text(f'카드빛: {card_debt}')
    st.text(f'자산 : {worth}')
    st.text(f'맞으면 아래 버튼을 클릭해 주세요')
    if st.button('구매 금액 예측하기'):
        regressor = joblib.load('model/regressor.pkl')
        new_data = np.array([age,salary,card_debt,worth])
        y_pred=regressor.predict(new_data.reshape(1, 4))
        pred_data = y_pred[0]

        if pred_data < 0 :
            st.error('예측이 불가능한 데이터 입니다.')
        else :
            # 소수점은 버리고 정수부분만 가져오는것 
            pred_data = round(pred_data)
            # 숫자에 3자리마다, 콤마를 찍어주는것
            pred_data = format(pred_data, ',')
            print(type(pred_data))
            st.success(f'예측 금액은 {pred_data} 달라 입니다.')
        

        # 숫자를 정수로 바꿔주는 것 라운드 pred_Data= round(pred_data)


        # 숫자에 3자리 마다 콤마를 찎어주는것 pred_data = format(pred_data,',')    