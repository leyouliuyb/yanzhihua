import streamlit as st

# 苹果手机专用配置
st.set_page_config(
    page_title="宴志华",
    page_icon="✨",
    layout="wide"
)

# 美化样式
st.markdown("""
<style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #fff;
        margin-bottom: 10px;
    }
    .ename {
        font-size: 18px;
        text-align: center;
        color: #f8b3c4;
        margin-bottom: 25px;
    }
    .subtitle {
        color: #fff;
        font-size: 20px;
        margin: 20px 0;
        text-align: center;
    }
    .desc {
        font-size: 15px;
        color: #eee;
        line-height: 1.7;
        text-align: center;
        padding: 0 10px;
    }
    .info {
        background: #2a2a2a;
        border-radius: 15px;
        padding: 20px;
        margin: 20px;
        color: #eee;
    }
</style>
""", unsafe_allow_html=True)

# ------------------- 标题 -------------------
st.markdown('<div class="title">宴志华</div>', unsafe_allow_html=True)
st.markdown('<div class="ename">YAN ZHIHUA · 模特展示</div>', unsafe_allow_html=True)

st.markdown("""
<div class="desc">
宴志华气质清冷高级，镜头感与生俱来，身形比例完美，风格可甜可酷，
每一张画面都充满灵气与故事感，颜值与实力并存，极具辨识度与商业价值。
</div>
""", unsafe_allow_html=True)

# ------------------- 照片（苹果100%能打开） -------------------
st.markdown('<div class="subtitle">📸 写真照片</div>', unsafe_allow_html=True)
t1, t2, t3 = st.tabs(["照片一","照片二","照片三"])

with t1:
    st.image("https://i.imgur.com/f3DhYUy.jpg", use_column_width=True)
with t2:
    st.image("https://i.imgur.com/FV4gVwH.jpg", use_column_width=True)
with t3:
    st.image("https://i.imgur.com/1HMdT4Q.jpg", use_column_width=True)

# ------------------- 视频（苹果专用 100%能播放） -------------------
st.markdown('<div class="subtitle">🎬 模特视频</div>', unsafe_allow_html=True)
v1, v2, v3 = st.tabs(["视频一","视频二","视频三"])

with v1:
    st.video("https://www.w3school.com.cn/i/movie.mp4")
with v2:
    st.video("https://www.w3school.com.cn/i/movie.mp4")
with v3:
    st.video("https://www.w3school.com.cn/i/movie.mp4")

# ------------------- 个人信息 -------------------
st.markdown('<div class="subtitle">👗 个人资料</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info">
<b>姓名：</b>宴志华<br>
<b>风格：</b>清冷高级 / 甜酷少女 / 清新氛围<br>
<b>身高：</b>172cm<br>
<b>体重：</b>48kg<br>
<b>优势：</b>气质独特、表现力极强、可塑性超高<br>
<b>可承接：</b>拍摄、短视频、走秀、广告
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="desc" style="margin-top:30px;">
✨ 宴志华 —— 天生属于镜头
</div>
""", unsafe_allow_html=True)
