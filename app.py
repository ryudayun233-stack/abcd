import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="가위바위보 게임", layout="centered")

st.title("✂️RPS 가위바위보 게임✊✋")

# --- 세션 상태 초기화 ---
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'comp_score' not in st.session_state:
    st.session_state.comp_score = 0
if 'message' not in st.session_state:
    st.session_state.message = "게임을 시작해 보세요!"

# 가위/바위/보 옵션
options = {"가위": "✂️", "바위": "✊", "보": "✋"}
options_list = list(options.keys())

# --- 게임 로직 함수 ---
def play_game(user_choice):
    comp_choice = random.choice(options_list)
    user_icon = options[user_choice]
    comp_icon = options[comp_choice]

    # 승패 판정 로직
    if user_choice == comp_choice:
        result = "무승부"
        st.session_state.message = f"{user_icon} vs {comp_icon} : 무승부입니다!"
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        result = "승리"
        st.session_state.user_score += 1
        st.session_state.message = f"{user_icon} vs {comp_icon} : 🎉 축하합니다, 이기셨습니다!"
    else:
        result = "패배"
        st.session_state.comp_score += 1
        st.session_state.message = f"{user_icon} vs {comp_icon} : 😥 아쉽지만 지셨습니다."
    
    # 결과 메시지 및 점수 업데이트는 세션 상태에 저장되어 자동으로 화면에 반영됨

# --- UI 구성 ---

# 점수판
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("나의 점수", st.session_state.user_score)
with col2:
    st.metric("컴퓨터 점수", st.session_state.comp_score)
with col3:
    # 재시작 버튼
    if st.button("점수 초기화"):
        st.session_state.user_score = 0
        st.session_state.comp_score = 0
        st.session_state.message = "점수가 초기화되었습니다. 다시 시작!"
        st.rerun() # 화면 갱신

st.markdown("---")

# 게임 결과 메시지 출력
if "이기셨습니다" in st.session_state.message:
    st.success(st.session_state.message)
elif "지셨습니다" in st.session_state.message:
    st.error(st.session_state.message)
elif "무승부" in st.session_state.message:
    st.info(st.session_state.message)
else:
    st.write(st.session_state.message)

st.markdown("---")

# 사용자 선택 버튼
st.subheader("무엇을 내시겠습니까?")

# 버튼 레이아웃을 위해 컬럼 사용
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button(f"{options['가위']} 가위", use_container_width=True):
        play_game("가위")

with btn_col2:
    if st.button(f"{options['바위']} 바위", use_container_width=True):
        play_game("바위")

with btn_col3:
    if st.button(f"{options['보']} 보", use_container_width=True):
        play_game("보")


