# simple_app.py
import streamlit as st

# --- 웹 앱 구성 시작 ---

st.title('첫 번째 스트림릿 앱')

# 텍스트 입력 위젯 (사용자 이름 입력받기)
user_name = st.text_input('이름을 입력해주세요:')

# 버튼 위젯
if st.button('인사하기'):
    # 버튼이 클릭되었을 때 실행될 로직
    if user_name:
        st.write(f'안녕하세요, {user_name}님! 스트림릿에 오신 것을 환영합니다.')
    else:
        st.write('이름을 먼저 입력해주세요.')

# --- 웹 앱 구성 끝 ---
import streamlit as st
import pandas as pd
import numpy as np

# --- 페이지 설정 ---
st.set_page_config(page_title="간단한 스트림릿 앱", layout="wide")

# --- 제목 및 텍스트 출력 ---
st.title("안녕하세요, 스트림릿 예제입니다! 👋")
st.write("이 앱은 스트림릿의 다양한 기능을 보여줍니다.")

# --- 사이드바 ---
st.sidebar.header("설정 메뉴")
user_name = st.sidebar.text_input("이름을 입력하세요:")
if user_name:
    st.sidebar.write(f"환영합니다, {user_name}님!")

# --- 버튼 상호작용 ---
if st.button("풍선 날리기!"):
    st.balloons()
    st.success("신나는 풍선!")

# --- 데이터 표시 ---
st.subheader("데이터프레임 예제")
st.write("넘파이(Numpy)를 사용하여 간단한 데이터프레임을 생성합니다.")

df = pd.DataFrame({
    '첫 번째 열': [1, 2, 3, 4],
    '두 번째 열': [10, 20, 30, 40]
})

st.dataframe(df) # 데이터프레임 표시

# --- 차트 표시 ---
st.subheader("라인 차트 예제")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

# --- 코드 블록 표시 ---
st.subheader("코드 블록 보기")
st.code("""
import streamlit as st
st.write("이 코드가 화면에 표시됩니다.")
""", language="python")
