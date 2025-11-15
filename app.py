<가위바위보>
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
<묵찌빠>
import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="묵찌빠 게임", layout="centered")

st.title("✊✋✂️ 묵찌빠 게임")
st.write("먼저 가위바위보로 공격권을 획득하세요! 공격자와 수비자가 같은 것을 내면 공격자가 승리합니다.")

# --- 세션 상태 초기화 ---
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'comp_score' not in st.session_state:
    st.session_state.comp_score = 0
if 'game_stage' not in st.session_state:
    # 'rsp' (가위바위보 단계) 또는 'mjp' (묵찌빠 단계)
    st.session_state.game_stage = 'rsp' 
if 'attacker' not in st.session_state:
    # 0: 무승부/결정 안됨, 1: 사용자 공격, 2: 컴퓨터 공격
    st.session_state.attacker = 0
if 'message' not in st.session_state:
    st.session_state.message = "가위바위보로 공격권을 먼저 획득하세요!"
if 'last_choices' not in st.session_state:
    st.session_state.last_choices = ("", "") # (user, computer)

options = {"묵": "✊", "찌": "✂️", "빠": "✋"}
options_list = list(options.keys())

# --- 게임 로직 함수 ---

def determine_winner(user_choice, comp_choice):
    """승패를 판단하여 결과 코드 반환 (0: 무승부, 1: 사용자 승리, 2: 컴퓨터 승리)"""
    if user_choice == comp_choice:
        return 0
    elif (user_choice == "찌" and comp_choice == "빠") or \
         (user_choice == "묵" and comp_choice == "찌") or \
         (user_choice == "빠" and comp_choice == "묵"):
        return 1 # 사용자 승리
    else:
        return 2 # 컴퓨터 승리

def play_game(user_choice):
    comp_choice = random.choice(options_list)
    st.session_state.last_choices = (user_choice, comp_choice)
    winner_code = determine_winner(user_choice, comp_choice)
    
    if st.session_state.game_stage == 'rsp':
        # --- 1단계: 가위바위보 (공격권 획득) ---
        if winner_code == 0:
            st.session_state.message = f"{options[user_choice]} vs {options[comp_choice]} : 무승부! 다시 가위바위보를 하세요."
            st.session_state.attacker = 0
        elif winner_code == 1:
            st.session_state.attacker = 1 # 사용자 공격권 획득
            st.session_state.game_stage = 'mjp'
            st.session_state.message = f"🎉 {options[user_choice]} vs {options[comp_choice]} : 사용자 공격권 획득! 이제 '묵/찌/빠'를 내세요."
        else:
            st.session_state.attacker = 2 # 컴퓨터 공격권 획득
            st.session_state.game_stage = 'mjp'
            st.session_state.message = f"😥 {options[user_choice]} vs {options[comp_choice]} : 컴퓨터 공격권 획득! 이제 '묵/찌/빠'를 내세요."
            
    elif st.session_state.game_stage == 'mjp':
        # --- 2단계: 묵찌빠 (승부 결정) ---
        
        # 공격자가 이기거나 비기면 즉시 게임 종료 (공격자 승리)
        if winner_code == 0:
            if st.session_state.attacker == 1:
                st.session_state.user_score += 1
                st.session_state.message = f"🥳 {options[user_choice]} vs {options[comp_choice]} : **사용자 승리!** 게임이 종료되었습니다."
            else:
                st.session_state.comp_score += 1
                st.session_state.message = f"😵 {options[user_choice]} vs {options[comp_choice]} : **컴퓨터 승리!** 게임이 종료되었습니다."
            
            # 게임 종료 후 다시 가위바위보 단계로 전환 준비
            st.session_state.game_stage = 'game_over'

        else:
            # 비기지 않았으면 공격권 전환
            if winner_code == 1:
                st.session_state.attacker = 1 # 사용자에게 공격권 이동
                st.session_state.message = f"{options[user_choice]} vs {options[comp_choice]} : 공격권이 사용자에게로! '묵/찌/빠'를 내세요."
            else:
                st.session_state.attacker = 2 # 컴퓨터에게 공격권 이동
                st.session_state.message = f"{options[user_choice]} vs {options[comp_choice]} : 공격권이 컴퓨터에게로! '묵/찌/빠'를 내세요."


# --- UI 구성 ---

# 점수판 및 현재 상태 표시
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("나의 점수", st.session_state.user_score)
with col2:
    if st.session_state.attacker == 1:
        st.info("나의 공격 차례 🎯")
    elif st.session_state.attacker == 2:
        st.warning("컴퓨터 공격 차례 💻")
    else:
        st.markdown("**공격권 없음**")
with col3:
    st.metric("컴퓨터 점수", st.session_state.comp_score)

st.markdown("---")

# 게임 결과 메시지 출력
if st.session_state.game_stage == 'game_over':
    st.balloons()
    if "사용자 승리" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)
else:
    st.info(st.session_state.message)

# 마지막 선택 표시
if st.session_state.last_choices[0]:
    st.markdown(f"**나**: {st.session_state.last_choices[0]} {options[st.session_state.last_choices[0]]} vs **컴퓨터**: {st.session_state.last_choices[1]} {options[st.session_state.last_choices[1]]}")

st.markdown("---")


# 사용자 선택 버튼
if st.session_state.game_stage in ['rsp', 'mjp']:
    st.subheader("무엇을 내시겠습니까?")

    # 버튼 레이아웃
    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        if st.button(f"{options['묵']} 묵 (바위)", use_container_width=True):
            play_game("묵")

    with btn_col2:
        if st.button(f"{options['찌']} 찌 (가위)", use_container_width=True):
            play_game("찌")

    with btn_col3:
        if st.button(f"{options['빠']} 빠 (보)", use_container_width=True):
            play_game("빠")

else:
    # 게임 종료 시 새 게임 버튼 표시
    if st.button("새 게임 시작 (점수 유지)"):
        st.session_state.game_stage = 'rsp'
        st.session_state.attacker = 0
        st.session_state.message = "새로운 게임 시작! 가위바위보로 공격권을 획득하세요."
        st.session_state.last_choices = ("", "")
        st.rerun()
    
    if st.button("점수 및 게임 초기화"):
        st.session_state.user_score = 0
        st.session_state.comp_score = 0
        st.session_state.game_stage = 'rsp'
        st.session_state.attacker = 0
        st.session_state.message = "모든 점수가 초기화되었습니다. 게임 시작!"
        st.session_state.last_choices = ("", "")
        st.rerun()


