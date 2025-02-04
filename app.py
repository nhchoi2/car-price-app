import streamlit as st
from UI.eda import run_eda
from UI.ml import run_ml
from UI.home import run_home

# Streamlit 스타일 적용
st.set_page_config(
    page_title="자동차 가격 예측 앱",
    layout="wide",
    page_icon="🚗"
)

# 사이드바에 로고 추가
st.sidebar.image("image.webp", use_container_width=True)

# 메인 앱 실행
def main():
    st.title("🚗 자동차 가격 예측 앱")
    st.markdown("### 📊 머신러닝을 활용한 가격 예측 및 데이터 분석")

    menu = ["🏠 Home", "📊 EDA", "🤖 ML"]
    choice = st.sidebar.radio("메뉴 선택", menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()
