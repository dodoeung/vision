import streamlit as st

# 앱 제목 설정
st.set_page_config(page_title="감정 기반 푸드 추천", page_icon="🍱")
st.title("🍱 지금 기분에 어울리는 음식은?")

# 감정 목록
emotions = [
    "우울해요",
    "스트레스 받아요",
    "행복해요",
    "지루해요",
    "외로워요",
    "기운이 없어요"
]

# 감정 ➝ 음식 데이터 (일러스트 이미지로 대체)
food_data = {
    "우울해요": {
        "menu": "따뜻한 수프",
        "image": "https://cdn.pixabay.com/photo/2021/08/31/09/19/soup-6589022_1280.png",
        "how_to_eat": "따뜻할 때 천천히, 깊은 숨과 함께 한 숟갈씩 드세요.",
        "effect": "속이 따뜻해지며 마음도 편안해져요."
    },
    "스트레스 받아요": {
        "menu": "매운 떡볶이",
        "image": "https://cdn.pixabay.com/photo/2023/08/13/07/48/tteokbokki-8187943_1280.png",
        "how_to_eat": "매운맛을 음미하면서 스트레스를 날려보세요.",
        "effect": "매운맛이 엔도르핀을 분비시켜 스트레스를 완화해요."
    },
    "행복해요": {
        "menu": "아이스크림",
        "image": "https://cdn.pixabay.com/photo/2020/08/05/16/29/ice-cream-5467355_1280.png",
        "how_to_eat": "좋아하는 맛을 골라서 천천히 즐기세요.",
        "effect": "달콤함이 행복한 기분을 더 높여줘요."
    },
    "지루해요": {
        "menu": "팝콘과 영화",
        "image": "https://cdn.pixabay.com/photo/2021/08/16/10/43/popcorn-6549443_1280.png",
        "how_to_eat": "영화를 보면서 손으로 하나씩 집어먹어보세요.",
        "effect": "오감 자극으로 지루함을 날려줘요."
    },
    "외로워요": {
        "menu": "따뜻한 라멘",
        "image": "https://cdn.pixabay.com/photo/2022/12/04/09/11/ramen-7633470_1280.png",
        "how_to_eat": "국물부터 천천히 음미하며 드세요.",
        "effect": "따뜻한 국물이 외로움을 달래줘요."
    },
    "기운이 없어요": {
        "menu": "삼계탕",
        "image": "https://cdn.pixabay.com/photo/2023/08/24/12/31/chicken-soup-8210466_1280.png",
        "how_to_eat": "밥과 함께 충분히 씹어 드세요.",
        "effect": "단백질과 영양으로 체력이 회복돼요."
    },
}

# 감정 선택
selected_emotion = st.selectbox("당신의 현재 기분을 선택해보세요 👇", emotions)

# 결과 출력
if selected_emotion:
    data = food_data[selected_emotion]
    st.header(f"🥘 추천 메뉴: {data['menu']}")
    st.image(data["image"], caption=data["menu"], use_container_width=True)
    st.markdown(f"**✅ 이렇게 드셔보세요:** {data['how_to_eat']}")
    st.markdown(f"**💛 기분 완화 효과:** {data['effect']}")
