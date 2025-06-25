import streamlit as st

st.set_page_config(page_title="감정 기반 푸드 추천", page_icon="🍱")
st.title("🍱 지금 기분에 어울리는 음식은?")

# 감정 리스트
emotions = [
    "우울해요",
    "스트레스 받아요",
    "행복해요",
    "지루해요",
    "외로워요",
    "기운이 없어요"
]

# 감정별 귀여운 캐릭터 애니메이션 GIF
emotion_gifs = {
    "우울해요": "https://media.giphy.com/media/xT0GqFzH6pRynh1Cco/giphy.gif",
    "스트레스 받아요": "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif",
    "행복해요": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "지루해요": "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "외로워요": "https://media.giphy.com/media/j2mYzN82TNWbm/giphy.gif",
    "기운이 없어요": "https://media.giphy.com/media/SvZTu2gtwd0xW/giphy.gif"
}

# 감정별 음식 추천 데이터 (일러스트 포함)
food_data = {
    "스트레스 받아요": [
        {
            "menu": "매운 떡볶이",
            "image": "https://cdn.pixabay.com/photo/2023/09/04/09/58/tteokbokki-8231986_1280.png",
            "how_to_eat": "치즈, 당면, 삶은 계란을 추가해 매콤하고 부드럽게 즐기세요!",
            "effect": "화끈한 매운맛이 스트레스를 날려줘요!"
        },
        {
            "menu": "핫치킨",
            "image": "https://cdn.pixabay.com/photo/2020/04/02/18/26/chicken-4993171_1280.png",
            "how_to_eat": "갈릭 소스를 곁들여 더 자극적으로 즐기세요!",
            "effect": "화끈함이 속을 시원하게 해줘요!"
        }
    ],
    "외로워요": [
        {
            "menu": "따뜻한 라멘",
            "image": "https://cdn.pixabay.com/photo/2023/01/09/20/55/ramen-7708873_1280.png",
            "how_to_eat": "반숙 계란과 김가루를 올려보세요!",
            "effect": "뜨끈한 국물이 마음을 위로해줘요."
        },
        {
            "menu": "우유식빵 토스트",
            "image": "https://cdn.pixabay.com/photo/2020/08/13/08/11/pancake-5484164_1280.png",
            "how_to_eat": "버터에 구워서 꿀이나 연유를 뿌려 먹어보세요.",
            "effect": "달콤함이 외로움을 달래줘요."
        }
    ],
    "행복해요": [
        {
            "menu": "딸기 케이크",
            "image": "https://cdn.pixabay.com/photo/2021/10/11/11/29/cake-6699601_1280.png",
            "how_to_eat": "따뜻한 홍차와 함께 드셔보세요!",
            "effect": "기분 좋은 순간을 더 달콤하게!"
        }
    ],
    "우울해요": [
        {
            "menu": "초콜릿 브라우니",
            "image": "https://cdn.pixabay.com/photo/2022/04/13/20/02/brownies-7130781_1280.png",
            "how_to_eat": "따뜻하게 데우고 아이스크림과 함께 드세요.",
            "effect": "진한 초콜릿이 우울한 기분을 녹여줘요."
        }
    ],
    "기운이 없어요": [
        {
            "menu": "한우 미역국",
            "image": "https://cdn.pixabay.com/photo/2021/02/18/02/43/soup-6024961_1280.png",
            "how_to_eat": "밥을 말아서 든든하게 먹어요.",
            "effect": "영양 가득한 국물이 에너지를 채워줘요."
        }
    ],
    "지루해요": [
        {
            "menu": "불고기 퀘사디아",
            "image": "https://cdn.pixabay.com/photo/2021/01/19/18/11/quesadilla-5931211_1280.png",
            "how_to_eat": "사워크림과 살사를 곁들여 먹어보세요!",
            "effect": "이색적인 맛이 지루함을 날려줘요!"
        }
    ]
}

# 사용자 입력
selected = st.selectbox("당신의 현재 기분을 선택해보세요 👇", emotions)

if selected:
    st.image(emotion_gifs[selected], width=200)
    st.subheader(f"😋 '{selected}' 기분에 어울리는 음식 추천")

    for item in food_data.get(selected, []):
        st.markdown("---")
        st.image(item["image"], caption=item["menu"], use_container_width=True)
        st.markdown(f"**🍽 메뉴:** {item['menu']}")
        st.markdown(f"**✅ 맛있게 먹는 팁:** {item['how_to_eat']}")
        st.markdown(f"**💛 기분 완화 효과:** {item['effect']}")
