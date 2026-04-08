import streamlit as st

# 页面全局配置（手机适配+高级风格）
st.set_page_config(
    page_title="模特形象展示",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS（暗黑高级风，手机超好看）
st.markdown("""
<style>
    /* 全局样式 */
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #1a1a1a 100%);
        color: #f0f0f0;
    }
    /* 主标题 */
    .main-title {
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #f5c8ca, #e8a8b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 20px 0 8px 0;
    }
    /* 副标题 */
    .sub-title {
        font-size: 16px;
        text-align: center;
        color: #a0a0a0;
        margin-bottom: 30px;
        letter-spacing: 2px;
    }
    /* 标签栏样式 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        justify-content: center;
        background-color: #222222;
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 8px;
        background-color: #333333;
        color: #f0f0f0;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e68fa8;
        color: white;
    }
    /* 图片容器 */
    .img-container {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin: 0 auto;
        max-width: 90%;
    }
    /* 信息卡片 */
    .info-card {
        background: #222222;
        border-radius: 16px;
        padding: 24px;
        margin: 30px auto;
        max-width: 90%;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    .info-title {
        font-size: 20px;
        font-weight: 700;
        color: #f5c8ca;
        margin-bottom: 16px;
    }
    .info-item {
        font-size: 16px;
        color: #d0d0d0;
        margin: 8px 0;
        line-height: 1.6;
    }
    /* 底部版权 */
    .footer {
        text-align: center;
        color: #666666;
        font-size: 14px;
        margin: 40px 0 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题
st.markdown('<div class="main-title">✨ 模特形象展示</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">MODEL PORTFOLIO</div>', unsafe_allow_html=True)

# ------------------- 照片展示区（用你发的3张图） -------------------
st.subheader("📸 形象写真")
tab1, tab2, tab3 = st.tabs(["写真一", "写真二", "写真三"])

# 第一张图：白衬衫氛围感自拍
with tab1:
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image("https://imgur.com/a/GU4GF3f",
             caption="氛围感自拍 · 清冷气质", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 第二张图：花墙背影照
with tab2:
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image("https://imgur.com/a/GU4GF3f",
             caption="户外写真 · 清新氛围感", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 第三张图：棒球帽酷飒写真
with tab3:
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image("https://imgur.com/a/GU4GF3f",
             caption="酷飒造型 · 时尚感拉满", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------- 视频播放区（预留位置，换链接即用） -------------------
st.subheader("🎬 视频展示")
st.markdown('<div class="img-container">', unsafe_allow_html=True)
# 这里替换成你上传的视频在线链接即可直接播放
st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
st.markdown('</div>', unsafe_allow_html=True)

# ------------------- 模特信息卡（可自定义修改） -------------------
st.markdown("""
<div class="info-card">
    <div class="info-title">👗 模特资料</div>
    <div class="info-item">▪️ 风格：清冷氛围感 / 甜酷 / 清新</div>
    <div class="info-item">▪️ 身高：172cm</div>
    <div class="info-item">▪️ 体重：48kg</div>
    <div class="info-item">▪️ 鞋码：37</div>
    <div class="info-item">▪️ 可接：平面拍摄 / 短视频拍摄 / 走秀 / 商演</div>
</div>
""", unsafe_allow_html=True)

# 底部信息
st.markdown('<div class="footer">✨ 专属模特展示页 · 手机/电脑全适配</div>', unsafe_allow_html=True)