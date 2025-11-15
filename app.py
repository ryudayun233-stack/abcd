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
