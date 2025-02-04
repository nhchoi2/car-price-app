import streamlit as st

def run_home():
    st.subheader("🚗 자동차 가격 예측 앱")
    st.markdown("""
    - 데이터를 분석하고 머신러닝 모델을 활용하여 **자동차 구매 가격을 예측**하는 애플리케이션입니다.
    - 📊 **EDA (탐색적 데이터 분석)** : 데이터를 시각적으로 분석합니다.
    - 🤖 **ML (머신러닝 모델)** : 사용자의 입력값을 기반으로 자동차 가격을 예측합니다.
    """)

    # 자동차 이미지 표시
    st.image("image/자동차.png", use_container_width=True)

    st.info("📌 상단의 메뉴를 사용하여 분석을 시작하세요!")
