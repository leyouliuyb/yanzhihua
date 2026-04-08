import streamlit as st

# 页面设置
st.set_page_config(
    page_title="宴志华 | 模特展示",
    page_icon="🌟",
    layout="wide"
)

# 顶部美化样式
st.markdown("""
<style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #f7e1e6;
        margin-bottom: 10px;
    }
    .ename {
        font-size: 20px;
        text-align: center;
        color: #e6b3c1;
        margin-bottom: 30px;
        letter-spacing: 3px;
    }
    .subtitle {
        color: #f0d6dd;
        font-size: 22px;
        margin: 25px 0 15px 0;
        text-align: center;
    }
    .desc {
        font-size: 16px;
        color: #f5e6ea;
        line-height: 1.8;
        text-align: center;
        max-width: 800px;
        margin: 0 auto 30px auto;
    }
    .info-box {
        background: rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 28px;
        margin: 20px auto;
        max-width: 700px;
        backdrop-filter: blur(10px);
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        color: #fce4ec;
    }
    .stTabs [aria-selected="true"] {
        background: #e29cb3;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<div class="title">宴志华</div>', unsafe_allow_html=True)
st.markdown('<div class="ename">YAN ZHIHUA · MODEL PORTFOLIO</div>', unsafe_allow_html=True)

# 赞美文案
st.markdown("""
<div class="desc">
她气质清冷又自带高级感，镜头表现力极强，每一帧都极具氛围感。
身形优越、比例完美，风格多变可甜可酷，无论是清新日常还是时尚大片都能轻松驾驭。
自然灵动的神态与细腻的情绪表达，让每一张作品都充满故事感，极具辨识度与商业价值。
</div>
""", unsafe_allow_html=True)

# 照片
st.markdown('<div class="subtitle">📸 时尚写真</div>', unsafe_allow_html=True)
p1, p2, p3 = st.tabs(["写真 01", "写真 02", "写真 03"])
with p1:
    st.image("https://i.imgur.com/f3DhYUy.jpeg", use_column_width=True)
with p2:
    st.image("https://i.imgur.com/FV4gVwH.jpeg", use_column_width=True)
with p3:
    st.image("https://i.imgur.com/1HMdT4Q.jpeg", use_column_width=True)

# 视频
st.markdown('<div class="subtitle">🎬 动态影像</div>', unsafe_allow_html=True)
v1, v2, v3 = st.tabs(["视频 01", "视频 02", "视频 03"])
with v1:
    st.video("https://streamable.com/776n12")
with v2:
    st.video("https://streamable.com/mc2oiw")
with v3:
    st.video("https://streamable.com/h0dz63")

# 个人信息
st.markdown('<div class="subtitle">👗 个人资料</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
<b>姓名：</b>宴志华<br>
<b>风格：</b>清冷高级 / 甜酷少女 / 清新氛围感<br>
<b>身高：</b>172cm<br>
<b>体重：</b>48kg<br>
<b>优势：</b>镜头感极强、气质独特、可塑性极高、表现力出众<br>
<b>可承接：</b>平面拍摄、短视频创作、时尚走秀、商业广告、品牌代言
</div>
""", unsafe_allow_html=True)

# 结尾
st.markdown("""
<div class="desc" style="margin-top:40px;">
✨ 宴志华 —— 天生属于镜头，未来可期
</div>
""", unsafe_allow_html=True)
