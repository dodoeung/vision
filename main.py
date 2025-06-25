import streamlit as st

# 페이지 설정
st.set_page_config(page_title="기분푸드 🍱", page_icon="🍙", layout="wide")

# 사용자 정의 CSS (배경이미지 제거, stMarkdown 투명도 조정)
st.markdown("""
    <style>
        body {
            background-color: #fffbe6;
        }
        h1, h2, h3 {
            color: #d94f4f;
            font-family: 'Comic Sans MS', cursive;
        }
        .stMarkdown {
            background-color: rgba(255, 255, 255, 0.6);
            padding: 1rem;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🍱 기분푸드 - 감정에 맞는 음식 추천 앱")
st.markdown("귀엽고 맛있는 음식으로 기분을 힐링해보세요 😊")

# 감정 목록
emotions = [
    "우울해요",
    "스트레스 받아요",
    "행복해요",
    "지루해요",
    "외로워요",
    "기운이 없어요"
]

# 감정별 캐릭터 GIF
emotion_gifs = {
    "우울해요": "https://media.giphy.com/media/xT0GqFzH6pRynh1Cco/giphy.gif",
    "스트레스 받아요": "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif",
    "행복해요": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "지루해요": "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "외로워요": "https://media.giphy.com/media/j2mYzN82TNWbm/giphy.gif",
    "기운이 없어요": "https://media.giphy.com/media/SvZTu2gtwd0xW/giphy.gif"
}

# 감정별 음식 데이터
food_data = {
    "우울해요": [
        {
            "menu": "🍫 초콜릿 브라우니",
            "image": "https://cdn.pixabay.com/photo/2022/04/13/20/02/brownies-7130781_1280.png",
            "how_to_eat": "따뜻하게 데운 후 바닐라 아이스크림과 함께!",
            "effect": "진한 달콤함이 우울한 기분을 녹여줘요."
        }
    ],
    "스트레스 받아요": [
        {
            "menu": "🌶️ 매운 떡볶이",
            "image": "https://cdn.pixabay.com/photo/2023/09/04/09/58/tteokbokki-8231986_1280.png",
            "how_to_eat": "치즈, 당면, 계란을 추가하면 최고!",
            "effect": "화끈한 맛이 스트레스를 확 날려줘요!"
        },
        {
            "menu": "🔥 핫 치킨",
            "image": "https://cdn.pixabay.com/photo/2020/04/02/18/26/chicken-4993171_1280.png",
            "how_to_eat": "갈릭 소스와 함께 드세요!",
            "effect": "속까지 시원해지는 자극적인 맛!"
        }
    ],
    "행복해요": [
        {
            "menu": "🍓 딸기 케이크",
            "image": "https://cdn.pixabay.com/photo/2021/10/11/11/29/cake-6699601_1280.png",
            "how_to_eat": "홍차와 함께 먹으면 달콤한 완벽한 조화!",
            "effect": "행복한 기분을 오래 유지시켜줘요."
        }
    ],
    "지루해요": [
        {
            "menu": "🌮 불고기 퀘사디아",
            "image": "https://cdn.pixabay.com/photo/2021/01/19/18/11/quesadilla-5931211_1280.png",
            "how_to_eat": "사워크림과 살사 소스와 함께!",
            "effect": "이국적인 맛으로 지루함을 날려줘요!"
        }
    ],
    "외로워요": [
        {
            "menu": "🍜 따뜻한 라멘",
            "image": "https://cdn.pixabay.com/photo/2023/01/09/20/55/ramen-7708873_1280.png",
            "how_to_eat": "반숙 계란과 김가루를 추가해보세요.",
            "effect": "뜨끈한 국물이 마음을 녹여줘요."
        },
        {
            "menu": "🍞 우유 토스트",
            "image": "https://cdn.pixabay.com/photo/2020/08/13/08/11/pancake-5484164_1280.png",
            "how_to_eat": "버터에 구워 연유나 꿀을 뿌려보세요.",
            "effect": "달콤한 맛이 외로움을 달래줘요."
        }
    ],
    "기운이 없어요": [
        {
            "menu": "🥣 한우 미역국",
            "image": "https://cdn.pixabay.com/photo/2021/02/18/02/43/soup-6024961_1280.png",
            "how_to_eat": "밥 말아서 든든하게 한 그릇!",
            "effect": "영양 가득한 국물이 기운을 북돋아줘요."
        }
    ]
}

# 사용자 입력
selected = st.selectbox("👉 지금 당신의 기분은 어떤가요?", emotions)

if selected:
    st.image(emotion_gifs[selected], width=200)
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
