import streamlit as st

st.set_page_config(
    page_title="宴志华 | 模特展示",
    page_icon="🌸",
    layout="wide"
)

# 花朵唯美风格样式
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom, #fff9fc, #ffe6f2);
        color: #5d4052;
    }
    .main-title {
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        color: #c71565;
        margin: 20px 0 5px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    .en-name {
        font-size: 20px;
        text-align: center;
        color: #a2437a;
        margin-bottom: 30px;
        letter-spacing: 2px;
    }
    .section-title {
        font-size: 24px;
        color: #922b63;
        text-align: center;
        margin: 30px 0 15px;
    }
    .praise {
        font-size: 17px;
        line-height: 1.9;
        text-align: center;
        color: #633755;
        max-width: 800px;
        margin: 0 auto 30px;
        padding: 0 15px;
    }
    .card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px auto;
        max-width: 750px;
        box-shadow: 0 8px 25px rgba(200, 120, 160, 0.15);
    }
    .stTabs [data-baseweb="tab"] {
        background: #fdf2f8;
        border-radius: 12px;
        color: #922b63;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: #f284b7;
        color: white;
    }
    .footer {
        text-align: center;
        color: #b87398;
        font-size: 16px;
        margin: 40px 0 20px;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<div class="main-title">宴志华</div>', unsafe_allow_html=True)
st.markdown('<div class="en-name">YAN ZHIHUA · MODEL PORTFOLIO</div>', unsafe_allow_html=True)

# 赞美文案
st.markdown("""
<div class="praise">
宴志华气质清透温婉，自带高级镜头感，眉眼温柔又不失气场，
身形修长比例优越，可塑性极强，可甜可酷，可盐可仙。
每一张写真都自带氛围感，神态灵动自然，情绪细腻饱满，
极具辨识度与感染力，是天生属于镜头的优质模特。
颜值与气质并存，专业与灵气兼具，未来发展无可限量。
</div>
""", unsafe_allow_html=True)

# 写真部分
st.markdown('<div class="section-title">🌸 时尚写真</div>', unsafe_allow_html=True)

t1, t2, t3 = st.tabs(["写真 01","写真 02","写真 03"])

with t1:
    st.image("https://i.imgur.com/f3DhYUy.jpeg", use_column_width=True)
with t2:
    st.image("https://i.imgur.com/FV4gVwH.jpeg", use_column_width=True)
with t3:
    st.image("https://i.imgur.com/1HMdT4Q.jpeg", use_column_width=True)

# 个人资料卡片
st.markdown('<div class="section-title">💖 个人资料</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>姓名：</b>宴志华<br><br>
<b>风格：</b>清冷高级 / 温柔甜美 / 时尚酷飒 / 氛围感<br><br>
<b>身高：</b>172cm<br><br>
<b>体重：</b>48kg<br><br>
<b>个人优势：</b>气质独特出众，镜头感极强，体态优美，
情绪表达细腻，可塑性极高，学习能力强，专业认真。<br><br>
<b>可承接：</b>平面拍摄、短视频创作、时尚走秀、商业广告、品牌形象代言
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">✨ 宴志华 · 天生属于镜头 · 未来可期</div>', unsafe_allow_html=True)
