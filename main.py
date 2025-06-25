import streamlit as st

# 페이지 설정
st.set_page_config(page_title="기분푸드 🍱", page_icon="🍙", layout="wide")

# 배경 스타일 설정
st.markdown("""
    <style>
        .main {
            background-image: url('https://cdn.pixabay.com/photo/2020/12/19/21/23/lunch-5844675_1280.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        h1, h2, h3 {
            color: #d94f4f;
            font-family: 'Comic Sans MS', cursive;
        }
        .stMarkdown {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 1rem;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.title("🍱 기분푸드 - 감정에 맞는 음식 추천 앱")
st.markdown("기분에 따라 먹고 싶은 음식 추천해드릴게요! 귀여운 음식 캐릭터와 함께해요 😊")

# 감정 선택
emotions = ["우울해요", "스트레스 받아요", "행복해요", "지루해요", "외로워요", "기운이 없어요"]
selected = st.selectbox("👉 지금 당신의 기분은 어떤가요?", emotions)

# 캐릭터 GIF
emotion_gifs = {
    "우울해요": "https://media.giphy.com/media/xT0GqFzH6pRynh1Cco/giphy.gif",
    "스트레스 받아요": "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif",
    "행복해요": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "지루해요": "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "외로워요": "https://media.giphy.com/media/j2mYzN82TNWbm/giphy.gif",
    "기운이 없어요": "https://media.giphy.com/media/SvZTu2gtwd0xW/giphy.gif"
}

# 음식 데이터 (이미지 안정 링크)
food_data = {
    "우울해요": [
        {
            "menu": "🍫 초콜릿 브라우니",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Chocolate_brownie.jpg",
            "how_to_eat": "따뜻하게 데운 후 바닐라 아이스크림과 함께!",
            "effect": "진한 달콤함이 우울한 기분을 녹여줘요."
        }
    ],
    "스트레스 받아요": [
        {
            "menu": "🌶️ 매운 떡볶이",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Tteokbokki_by_stu_spivack.jpg",
            "how_to_eat": "치즈, 당면, 계란을 추가하면 최고!",
            "effect": "화끈한 맛이 스트레스를 날려줘요."
        },
        {
            "menu": "🍗 핫치킨",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Korean_fried_chicken_%2814402349903%29.jpg",
            "how_to_eat": "갈릭 소스를 곁들여 보세요!",
            "effect": "속이 시원해지는 강렬한 자극!"
        }
    ],
    "행복해요": [
        {
            "menu": "🍓 딸기 케이크",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Strawberry_Shortcake_%28259244995%29.jpg",
            "how_to_eat": "홍차와 함께 먹으면 달콤한 조화!",
            "effect": "기쁨이 두 배가 되는 맛이에요."
        }
    ],
    "지루해요": [
        {
            "menu": "🌮 불고기 퀘사디아",
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Quesadilla.jpg",
            "how_to_eat": "사워크림과 살사 소스를 듬뿍!",
            "effect": "이국적인 맛으로 지루함을 싹!"
        }
    ],
    "외로워요": [
        {
            "menu": "🍜 따뜻한 라멘",
            "image": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Tonkotsu_ramen_by_Shun_2007.jpg",
            "how_to_eat": "반숙 계란과 김 토핑 추천!",
            "effect": "뜨끈한 국물이 마음을 녹여줘요."
        },
        {
            "menu": "🍞 달콤한 토스트",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/32/Honey_toast.jpg",
            "how_to_eat": "버터에 구운 뒤 연유를 뿌려 보세요.",
            "effect": "달콤함이 외로움을 달래줘요."
        }
    ],
    "기운이 없어요": [
        {
            "menu": "🥣 한우 미역국",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Korean_seaweed_soup_Miyeokguk.jpg",
            "how_to_eat": "밥을 말아서 따뜻하게 한그릇!",
            "effect": "영양 가득한 국물이 기운을 복돋아줘요."
        }
    ]
}

# 사용자 선택 시 출력
if selected:
    st.image(emotion_gifs[selected], width=180)
    st.markdown(f"## 😊 '{selected}' 기분엔 이런 음식이 어울려요!")

    for item in food_data.get(selected, []):
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(item["image"], use_container_width=True)
        with col2:
            st.markdown(f"### 🍽 {item['menu']}")
            st.markdown(f"**맛있게 먹는 법** 👉 {item['how_to_eat']}")
            st.markdown(f"**기분 효과** 💛 {item['effect']}")
