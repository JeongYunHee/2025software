import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

DATA_PATH = "countriesMBTI_16types.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def make_bar_chart(df, country):
    # MBTI 컬럼 추출
    mbti_cols = [c for c in df.columns if c != "Country"]

    row = df[df["Country"] == country].iloc[0]
    values = [row[c] * 100 for c in mbti_cols]  # 퍼센트로 변환

    data = pd.DataFrame({
        "MBTI": mbti_cols,
        "value": values
    })

    # 값 기준 내림차순 정렬
    data = data.sort_values("value", ascending=False).reset_index(drop=True)

    # 색상 설정: 1등은 빨간색, 나머지는 그라데이션
    n = len(data)
    colors = ["red"]  # 1등

    if n > 1:
        base_colors = px.colors.sequential.Blues  # 그라데이션용 색상 리스트
        k = len(base_colors)
        others_count = n - 1

        for i in range(others_count):
            # 0~k-1 사이 인덱스로 균등 배치
            if others_count == 1:
                idx = k - 1
            else:
                idx = int(i * (k - 1) / (others_count - 1))
            colors.append(base_colors[idx])

    fig = go.Figure(
        data=[
            go.Bar(
                x=data["MBTI"],
                y=data["value"],
                marker=dict(color=colors),
                hovertemplate="<b>%{x}</b><br>%{y:.2f}%<extra></extra>",
            )
        ]
    )

    fig.update_layout(
        title=f"{country}의 MBTI 유형 분포",
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        yaxis=dict(ticksuffix="%"),
        template="plotly_white",
        margin=dict(l=40, r=40, t=60, b=40),
    )

    return fig


def main():
    st.set_page_config(
        page_title="세계 국가별 MBTI 시각화",
        layout="wide",
    )

    st.title("🌏 국가별 MBTI 분포 대시보드")
    st.write("Plotly + Streamlit으로 각 국가의 MBTI 비율을 인터랙티브하게 확인해보세요.")

    # 데이터 로드
    try:
        df = load_data()
    except FileNotFoundError:
        st.error(
            f"`{DATA_PATH}` 파일을 찾을 수 없습니다. "
            "Streamlit Cloud에 이 CSV 파일을 함께 업로드했는지 확인해주세요."
        )
        return

    # 사이드바 국가 선택
    st.sidebar.header("⚙️ 설정")
    countries = sorted(df["Country"].unique().tolist())
    default_country = "South Korea" if "South Korea" in countries else countries[0]

    selected_country = st.sidebar.selectbox(
        "국가를 선택하세요",
        countries,
        index=countries.index(default_country),
    )

    st.subheader(f"선택한 국가: **{selected_country}**")

    fig = make_bar_chart(df, selected_country)
    st.plotly_chart(fig, use_container_width=True)

    # 원본 데이터 보기 옵션
    with st.expander("원본 데이터 보기"):
        st.dataframe(df)


if __name__ == "__main__":
    main()
