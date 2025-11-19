'''
import streamlit as st

st.title("첫 웹앱 입니다 !")
name = st.text_input("이름을 입력해 주세요! : ")
menu = st.selectbox("좋아하는 맛을 선택해 주세요: ", ["아몬드봉봉", "엄마는 외계인", "레인보우샤베트"])
if st.button("문장 생성"):
  st.write(name + "님 안녕하세요. 좋아하는 맛은 "+ menu + "이군요!")
'''
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="베스킨라빈스 키오스크",
    page_icon="🍨",
    layout="centered"
)

st.title("🍦 베스킨라빈스 셀프 키오스크")
st.caption("천천히 고르셔도 괜찮아요 😊")

st.markdown("### 1. 매장에서 드시나요, 포장해 가시나요?")

order_type = st.radio(
    "이용 방법을 선택해주세요 🙌",
    ("매장에서 먹고 갈게요", "포장해서 가져갈게요")
)

st.markdown("---")
st.markdown("### 2. 용기를 선택해주세요 🧁")

# 용기별 최대 스쿱 수 & 가격 설정 (예시 가격)
containers = {
    "싱글 레귤러 컵 (1스쿱)": {"max_scoops": 1, "price": 3300},
    "더블 레귤러 컵 (2스쿱)": {"max_scoops": 2, "price": 6200},
    "파인트 (3스쿱)": {"max_scoops": 3, "price": 9500},
    "쿼터 (4스쿱)": {"max_scoops": 4, "price": 18000},
}

container_name = st.selectbox(
    "원하시는 용기를 골라주세요 💡",
    list(containers.keys())
)

max_scoops = containers[container_name]["max_scoops"]
base_price = containers[container_name]["price"]

# 포장 시 포장비 (예시)
takeout_fee = 500 if order_type == "포장해서 가져갈게요" else 0

st.markdown("---")
st.markdown(f"### 3. 아이스크림 맛을 골라주세요 🍨 (최대 {max_scoops}가지)")

flavors = [
    "아몬드 봉봉",
    "엄마는 외계인",
    "슈팅스타",
    "민트 초코",
    "베리베리 스트로베리",
    "뉴욕 치즈케이크",
    "초콜릿 무스",
    "포레스트 청포도",
    "사랑에 빠진 딸기",
    "바람과 함께 사라지다"
]

selected_flavors = st.multiselect(
    f"최대 {max_scoops}가지 맛까지 고르실 수 있어요 😋",
    flavors
)

# 선택 개수에 따른 안내
if len(selected_flavors) == 0:
    st.info("👉 드시고 싶은 맛을 하나 이상 선택해주세요!")
elif len(selected_flavors) > max_scoops:
    st.error(f"⚠️ {max_scoops}가지 이하로만 선택할 수 있어요. 맛을 조금만 줄여볼까요?")
else:
    st.success(f"좋아요! {len(selected_flavors)}가지 맛을 선택하셨어요 🤗")

st.markdown("---")
st.markdown("### 4. 결제 방법을 선택해주세요 💰")

payment_method = st.radio(
    "결제 수단을 골라주세요:",
    ("현금 결제", "카드 결제")
)

# 최종 가격 계산
total_price = base_price + takeout_fee

# 추가 안내 문구
price_detail_msg = f"기본 아이스크림 금액 {base_price:,.0f}원"
if takeout_fee > 0:
    price_detail_msg += f" + 포장비 {takeout_fee:,.0f}원"
price_detail_msg += f" = 총 {total_price:,.0f}원"

st.markdown("---")

# 주문 확정 버튼 활성화 조건
order_ready = (len(selected_flavors) > 0) and (len(selected_flavors) <= max_scoops)

order_button = st.button(
    "✅ 주문 확정하기",
    disabled=not order_ready
)

if order_button and order_ready:
    st.success("주문이 완료되었어요! 감사합니다 🥰")
    st.markdown("#### 🧾 주문 내역 확인")
    st.write(f"- 이용 방법: **{order_type}**")
    st.write(f"- 용기: **{container_name}**")
    st.write(f"- 선택한 맛 ({len(selected_flavors)}가지):")
    for f in selected_flavors:
        st.write(f"  - 🍧 {f}")
    st.write(f"- 결제 방법: **{payment_method}**")
    st.write(f"---")
    st.subheader(f"💵 최종 결제 금액: **{total_price:,.0f}원**")
    st.caption(price_detail_msg)
    st.caption("맛있게 드시고, 또 놀러와 주세요 😄")

elif not order_ready:
    st.caption("위 단계들을 순서대로 선택해주시면 주문 버튼이 활성화돼요 ✨")
