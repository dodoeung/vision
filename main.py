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

# 감정별 귀여운 애니메이션 캐릭터 gif
emotion_gifs = {
    "우울해요": "https://media.giphy.com/media/xT0GqFzH6pRynh1Cco/giphy.gif",
    "스트레스 받아요": "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif",
    "행복해요": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "지루해요": "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "외로워요": "https://media.giphy.com/media/j2mYzN82TNWbm/giphy.gif",
    "기운이 없어요": "https://media.giphy.com/media/SvZTu2gtwd0xW/giphy.gif"
}

# 감정 ➝ 음식 리스트 (일러스트 포함)
food_data = {
    "우울해요": [
        {
            "menu": "따뜻한 수프",
            "image": "https://www.pngitem.com/pimgs/m/51-513195_transparent-cute-soup-cartoon-png-cute-soup-png.png",
            "how_to_eat": "따뜻할 때 식지 않게 마셔보세요. 크래커를 곁들이면 좋아요!",
            "effect": "속이 따뜻해지고 마음도 편안해져요."
        },
        {
            "menu": "죽",
            "image": "https://cdn.pixabay.com/photo/2023/01/17/13/06/porridge-7722451_1280.png",
            "how_to_eat": "참기름과 김가루를 살짝 얹어 먹으면 고소함이 배가돼요.",
            "effect": "부드럽고 따뜻해서 위로받는 기분이 들어요."
        }
    ],
    "스트레스 받아요": [
        {
            "menu": "매운 떡볶이",
            "image": "https://cdn.pixabay.com/photo/2023/09/04/09/58/tteokbokki-8231986_1280.png",
            "how_to_eat": "치즈나 당면, 삶은 달걀을 추가해서 매콤하고 부드럽게 즐겨보세요!",
            "effect": "화끈한 맛이 스트레스를 날려줘요!"
        },
        {
            "menu": "매운 치킨",
            "image": "https://cdn.pixabay.com/photo/2021/07/12/07/23/fried-chicken-6405447_1280.png",
            "how_to_eat": "마요네즈+핫소스 콤보로 찍어 먹으면 스트레스가 사라져요!",
            "effect": "입안이 얼얼해질수록 기분도 후련해져요."
        }
    ],
    "행복해요": [
        {
            "menu": "아이스크림",
            "image": "https://www.pngitem.com/pimgs/m/51-513515_cute-ice-cream-png-cartoon-transparent-png.png",
            "how_to_eat": "와플콘에 담아 천천히 녹여 먹으면 행복감이 오래가요!",
            "effect": "행복한 기분을 달콤하게 유지시켜줘요."
        },
        {
            "menu": "팬케이크",
            "image": "https://cdn.pixabay.com/photo/2020/08/13/08/11/pancake-5484164_1280.png",
            "how_to_eat": "메이플 시럽과 과일을 올려 먹으면 맛이 풍성해져요!",
            "effect": "기쁨에 기쁨을 더해줘요."
        }
    ],
    "지루해요": [
        {
            "menu": "팝콘",
            "image": "https://www.pngitem.com/pimgs/m/150-1502734_popcorn-cartoon-png-png-download-cartoon-popcorn.png",
            "how_to_eat": "달콤이+카라멜 섞어서 영화 보며 톡톡 씹어요!",
            "effect": "오감 자극으로 지루함을 탈출!"
        },
        {
            "menu": "젤리",
            "image": "https://cdn.pixabay.com/photo/2022/10/20/15/19/jelly-7533829_1280.png",
            "how_to_eat": "냉장고에 잠깐 넣어 차게 먹으면 식감이 더 좋아요!",
            "effect": "톡톡 터지는 재미로 기분 전환!"
        }
    ],
    "외로워요": [
        {
            "menu": "따뜻한 라멘",
            "image": "https://www.pngitem.com/pimgs/m/30-302776_cartoon-ramen-cute-png-hd-png-download.png",
            "how_to_eat": "김가루와 반숙 계란을 올려서 먹어보세요.",
            "effect": "따뜻한 국물에 위로받는 느낌이에요."
        },
        {
            "menu": "만두국",
            "image": "https://cdn.pixabay.com/photo/2023/02/01/12/30/dumpling-soup-7758952_1280.png",
            "how_to_eat": "김치랑 함께 곁들여 먹으면 풍미가 배가돼요.",
            "effect": "포근한 한끼로 외로움을 달래줘요."
        }
    ],
    "기운이 없어요": [
        {
            "menu": "삼계탕",
            "image": "https://www.pngitem.com/pimgs/m/35-352385_chicken-soup-cartoon-png-download-chicken-soup-cartoon.png",
            "how_to_eat": "인삼, 대추와 함께 푹 끓인 국물과 닭고기를 함께 떠먹어요.",
            "effect": "기력을 회복하고 몸이 따뜻해져요."
        },
        {
            "menu": "계란죽",
            "image": "https://cdn.pixabay.com/photo/2023/01/13/15/59/porridge-7715923_1280.png",
            "how_to_eat": "참기름 한 방울과 깨소금을 더해보세요.",
            "effect": "기운 없을 때 위를 편하게 해줘요."
        }
    ]
}

# 감정 선택
selected_emotion = st.selectbox("당신의 현재 기분을 선택해보세요 👇", emotions)

# 캐릭터 이미지 표시
if selected_emotion:
    st.image(emotion_gifs[selected_emotion], width=200)
    st.subheader(f"😋 '{selected_emotion}' 기분에 어울리는 음식들")
    for item in food_data[selected_emotion]:
        st.markdown("---")
        st.image(item["image"], caption=item["menu"], use_container_width=True)
        st.markdown(f"**🍽 메뉴:** {item['menu']}")
        st.markdown(f"**✅ 이렇게 드세요:** {item['how_to_eat']}")
        st.markdown(f"**💛 기분 완화 효과:** {item['effect']}")
