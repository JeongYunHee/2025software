import streamlit as st

st.set_page_config(
    page_title="베스킨라빈스 키오스크",
    page_icon="🍨",
    layout="centered",
)

def main():
    st.title("🍨 베스킨라빈스 아이스크림 키오스크")
    st.caption("어서 오세요! 오늘은 어떤 아이스크림을 드릴까요? 🥰")

    st.divider()

    # -----------------------------
    # 1. 매장/포장 선택
    # -----------------------------
    st.header("1. 드시고 가시나요, 가져가시나요? 🏠")
    eat_type = st.radio(
        "원하시는 이용 방식을 선택해주세요.",
        ("매장에서 먹고 갈게요", "포장해서 가져갈게요"),
        horizontal=True,
    )

    # -----------------------------
    # 2. 용기 선택
    # -----------------------------
    st.header("2. 용기를 선택해주세요 🥄")

    containers = {
        "싱글컵 (1스쿱)": {"max_scoops": 1, "price": 3500},
        "더블컵 (2스쿱)": {"max_scoops": 2, "price": 6500},
        "파인트 (3스쿱)": {"max_scoops": 3, "price": 9500},
        "쿼터 (4스쿱)": {"max_scoops": 4, "price": 15500},
    }

    container_names = list(containers.keys())

    selected_container_name = st.selectbox(
        "용기를 골라주세요 😊",
        container_names,
        index=1,
    )

    selected_container = containers[selected_container_name]
    max_scoops = selected_container["max_scoops"]
    base_price = selected_container["price"]

    st.info(
        f"✅ 선택하신 용기: **{selected_container_name}**\n"
        f"- 담을 수 있는 맛: **최대 {max_scoops}가지 이하** 선택 가능\n"
        f"- 기준 가격: **{base_price:,}원**"
    )

    st.divider()

    # -----------------------------
    # 3. 맛 선택
    # -----------------------------
    st.header("3. 아이스크림 맛을 골라주세요 🍦")

    flavors = [
        "엄마는외계인",
        "민트초코",
        "뉴욕치즈케이크",
        "슈팅스타",
        "초코나무숲",
        "베리베리스트로베리",
        "사랑에빠진딸기",
        "레인보우샤베트",
        "아몬드봉봉",
        "쿠키앤크림"
    ]

    selected_flavors = st.multiselect(
        f"원하는 맛을 골라주세요 (최대 {max_scoops}가지 이하) 😋",
        flavors,
        help="용기에 담을 수 있는 수량 이내로만 선택해주세요!",
    )

    # 이하값 적용
    valid_flavors = selected_flavors[:max_scoops]

    if len(selected_flavors) > max_scoops:
        st.warning(
            f"⚠️ 이 용기는 최대 **{max_scoops}가지 맛**만 담을 수 있어요.\n"
            f"앞에서 선택하신 **{', '.join(valid_flavors)}**까지만 주문에 반영됩니다."
        )

    if len(valid_flavors) == 0:
        st.write("👉 아직 맛을 고르지 않으셨어요. 천천히 둘러보시고 골라주세요 🙂")
    else:
        st.success("✨ 선택하신 맛:")
        st.write(", ".join(valid_flavors))

    st.divider()

    # -----------------------------
    # 4. 결제 방법 선택
    # -----------------------------
    st.header("4. 결제 방법을 선택해주세요 💳")

    payment_method = st.radio(
        "어떻게 결제하시겠어요?",
        ("현금 결제", "카드 결제", "기프티콘 결제 🎁"),
        horizontal=True,
    )

    total_price = base_price

    st.subheader("🧾 주문 요약")
    with st.container():
        st.markdown(
            f"""
