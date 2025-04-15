TRIGGER_WORDS = {
    "안녕": "안녕하세요! 저는 기봇입니다.!! ",
    "정보": "어떤 정보가 필요하세요?? ",
    "기분": "저는 기분이 좋아요!!",
}

FORTUNE_CARDS = [
    {
        "name": "🌞 태양 (The Sun)",
        "description": "오늘은 모든 일이 잘 풀릴 것입니다! 성공과 행복이 가득한 날이에요.",
        "positive": "자신감을 가지세요. 좋은 기회가 올 거예요!",
        "negative": "과신은 금물! 신중함도 필요해요.",
    },
    {
        "name": "🌙 달 (The Moon)",
        "description": "앞날이 불확실할 수 있지만, 직감을 믿으세요.",
        "positive": "감각을 sharpen! 숨겨진 기회가 있어요.",
        "negative": "착각하거나 속을 수 있으니 주의하세요.",
    },
    {
        "name": "⚖️ 저스티스 (Justice)",
        "description": "오늘은 공정한 선택이 중요한 날입니다. 올바른 결정을 내리세요.",
        "positive": "정의롭고 균형 잡힌 선택을 하세요.",
        "negative": "감정적으로 판단하면 안 좋아요!",
    },
    {
        "name": "💀 죽음 (Death)",
        "description": "무언가 끝나지만, 새로운 시작이 기다리고 있습니다!",
        "positive": "과거를 정리하고 새로운 출발을 할 기회!",
        "negative": "변화를 두려워하지 마세요.",
    },
    {
        "name": "🃏 광대 (The Fool)",
        "description": "새로운 모험이 기다리고 있습니다! 두려워하지 마세요.",
        "positive": "도전정신을 가지세요. 흥미로운 일이 생길 거예요!",
        "negative": "신중하지 않으면 낭패를 볼 수도 있어요.",
    },
    {
        "name": "🏰 황제 (The Emperor)",
        "description": "리더십을 발휘할 때입니다. 자신을 믿으세요!",
        "positive": "강한 의지를 가지고 목표를 향해 나아가세요.",
        "negative": "너무 독단적으로 행동하면 주변과 갈등이 생길 수 있어요.",
    },
    {
        "name": "👑 여왕 (The Empress)",
        "description": "풍요로움과 따뜻한 에너지가 가득한 하루입니다.",
        "positive": "창의력이 상승하는 날, 새로운 아이디어를 떠올려 보세요.",
        "negative": "감정에 너무 휩쓸리지 않도록 주의하세요.",
    },
    {
        "name": "⏳ 은둔자 (The Hermit)",
        "description": "내면을 들여다보고 깊이 생각하는 시간이 필요합니다.",
        "positive": "자신을 돌아보면 답을 찾을 수 있습니다.",
        "negative": "너무 고립되지 않도록 하세요.",
    },
    {
        "name": "🎡 운명의 수레바퀴 (Wheel of Fortune)",
        "description": "예상치 못한 변화가 다가오고 있습니다!",
        "positive": "좋은 기회가 찾아올 수 있어요!",
        "negative": "변화를 받아들이는 자세가 필요해요.",
    },
    {
        "name": "🦅 힘 (Strength)",
        "description": "어려움을 이겨낼 힘이 있는 날입니다.",
        "positive": "인내심과 용기를 가지세요!",
        "negative": "화를 다스리지 못하면 문제가 될 수 있어요.",
    },
    {
        "name": "⚡ 번개 (The Tower)",
        "description": "예상치 못한 일이 일어날 수 있습니다!",
        "positive": "위기를 기회로 바꿀 수 있어요.",
        "negative": "너무 급작스러운 변화에 놀라지 마세요.",
    },
    {
        "name": "🕊️ 사랑 (The Lovers)",
        "description": "사랑과 조화로운 관계가 강조되는 날입니다.",
        "positive": "소중한 사람과 좋은 시간을 보낼 수 있어요.",
        "negative": "갈등이 생길 수 있으니 조심하세요.",
    },
    {
        "name": "💰 행운 (Fortune)",
        "description": "재물과 행운이 따르는 날입니다!",
        "positive": "금전적인 기회가 올 수 있어요.",
        "negative": "지출을 조심하세요.",
    },
    {
        "name": "🚶 방랑자 (The Wanderer)",
        "description": "새로운 길을 떠날 시간이 다가옵니다.",
        "positive": "변화를 두려워하지 마세요.",
        "negative": "충동적인 결정은 피하세요.",
    },
    {
        "name": "👁️ 통찰 (Insight)",
        "description": "오늘은 직감이 강하게 작용하는 날입니다.",
        "positive": "자신의 감을 믿으세요.",
        "negative": "사실과 감정을 구별하는 것이 중요합니다.",
    },
    {
        "name": "🛤️ 길 (The Path)",
        "description": "중요한 선택의 기로에 서 있습니다.",
        "positive": "자신이 원하는 방향을 선택하세요.",
        "negative": "망설이면 기회를 놓칠 수 있어요.",
    },
    {
        "name": "🔑 기회 (The Key)",
        "description": "중요한 기회를 잡을 시간이 왔습니다.",
        "positive": "결정적인 순간을 놓치지 마세요!",
        "negative": "기회가 사라지기 전에 행동하세요.",
    },
    {
        "name": "🕰️ 과거 (The Past)",
        "description": "과거의 경험이 현재의 선택에 영향을 줍니다.",
        "positive": "좋은 추억을 떠올리며 힘을 얻으세요.",
        "negative": "과거에 너무 집착하면 앞으로 나아가기 어렵습니다.",
    },
    {
        "name": "🚀 미래 (The Future)",
        "description": "당신의 미래는 스스로 만들어가는 것입니다!",
        "positive": "긍정적인 마음가짐이 중요한 날입니다.",
        "negative": "현재의 선택이 중요한 결과를 가져올 수 있어요.",
    },
    {
        "name": "🔮 마법사 (The Magician)",
        "description": "능력을 발휘하여 원하는 것을 이룰 수 있습니다!",
        "positive": "자신감을 가지고 도전하세요.",
        "negative": "너무 무리하면 오히려 역효과가 날 수 있어요.",
    },
]
