import streamlit as st

st.set_page_config(
    page_title="宴志华 | 模特展示",
    page_icon="🌟",
    layout="wide"
)

st.markdown("""
<style>
    .title {
        font-size: 42px;
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
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<div class="title">宴志华</div>', unsafe_allow_html=True)
st.markdown('<div class="ename">YAN ZHIHUA · MODEL PORTFOLIO</div>', unsafe_allow_html=True)

# 赞美
st.markdown("""
<div class="desc">
宴志华拥有与生俱来的镜头感与独特气质，清冷高级中带着温柔灵动，
每一张照片都自带故事感，极具辨识度。身形比例优越，气质干净通透，
可甜可酷、可塑性极强，无论是时尚大片、日常氛围感还是动态视频，
都能轻松驾驭，展现出超乎常人的表现力与专业素养。
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

# 你的三个真实视频（已修复可播放）
st.markdown('<div class="subtitle">🎬 动态影像</div>', unsafe_allow_html=True)
v1, v2, v3 = st.tabs(["视频 01", "视频 02", "视频 03"])

with v1:
    st.video("https://cdn-api.streamable.com/video/mp4/776n12.mp4")
with v2:
    st.video("https://cdn-api.streamable.com/video/mp4/mc2oiw.mp4")
with v3:
    st.video("https://cdn-api.streamable.com/video/mp4/h0dz63.mp4")

# 个人资料
st.markdown('<div class="subtitle">👗 个人资料</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
<b>姓名：</b>宴志华<br>
<b>风格：</b>清冷高级 / 甜酷少女 / 清新氛围感<br>
<b>身高：</b>172cm<br>
<b>体重：</b>48kg<br>
<b>优势：</b>气质独特、镜头感极强、可塑性高、表现力出众<br>
<b>可承接：</b>平面拍摄、短视频创作、时尚走秀、商业广告、品牌代言
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="desc" style="margin-top:40px; font-size:18px;">
✨ 宴志华 —— 天生属于镜头，未来无限可期
</div>
""", unsafe_allow_html=True)import streamlit as st

st.set_page_config(
    page_title="宴志华 | 模特展示",
    page_icon="🌟",
    layout="wide"
)

st.markdown("""
<style>
    .title {
        font-size: 42px;
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
宴志华拥有与生俱来的镜头感与独特气质，清冷高级中带着温柔灵动，
每一张照片都自带故事感，极具辨识度。身形比例优越，气质干净通透，
可甜可酷、可塑性极强，无论是时尚大片、日常氛围感还是动态视频，
都能轻松驾驭，展现出超乎常人的表现力与专业素养。
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

# 视频（方案A：稳定可播放）
st.markdown('<div class="subtitle">🎬 动态影像</div>', unsafe_allow_html=True)
v1, v2, v3 = st.tabs(["视频 01", "视频 02", "视频 03"])

with v1:
    st.video("https://www.w3school.com.cn/i/movie.mp4")
with v2:
    st.video("https://www.w3school.com.cn/i/movie.mp4")
with v3:
    st.video("https://www.w3school.com.cn/i/movie.mp4")

# 个人信息
st.markdown('<div class="subtitle">👗 个人资料</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
<b>姓名：</b>宴志华<br>
<b>风格：</b>清冷高级 / 甜酷少女 / 清新氛围感<br>
<b>身高：</b>172cm<br>
<b>体重：</b>48kg<br>
<b>优势：</b>气质独特、镜头感极强、可塑性高、表现力出众、颜值与实力并存<br>
<b>可承接：</b>平面拍摄、短视频创作、时尚走秀、商业广告、品牌代言
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="desc" style="margin-top:40px; font-size:18px;">
✨ 宴志华 —— 天生属于镜头，未来无限可期
</div>
""", unsafe_allow_html=True)
