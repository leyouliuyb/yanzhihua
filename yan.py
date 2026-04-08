import streamlit as st

# 页面设置
st.set_page_config(page_title="模特展示", page_icon="✨", layout="wide")

# 标题
st.title("✨ 模特形象展示")
st.subheader("Model Portfolio")

# 照片（已经换成你的照片！）
st.subheader("📸 写真照片")
tab1, tab2, tab3 = st.tabs(["照片 1", "照片 2", "照片 3"])

with tab1:
    st.image("https://i.imgur.com/f3DhYUy.jpeg", use_column_width=True)
with tab2:
    st.image("https://i.imgur.com/FV4gVwH.jpeg", use_column_width=True)
with tab3:
    st.image("https://i.imgur.com/1HMdT4Q.jpeg", use_column_width=True)

# 视频（先用示例视频，你传好我再帮你换）
st.subheader("🎬 视频展示")
st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")

# 资料
st.markdown("---")
st.markdown("### 👗 模特资料")
st.write("• 风格：清冷 / 甜酷 / 清新")
st.write("• 身高：172cm")
st.write("• 体重：48kg")
st.write("• 可接：拍摄、短视频、走秀")

st.write("💖 手机/电脑均可打开 · 专属模特展示页")
