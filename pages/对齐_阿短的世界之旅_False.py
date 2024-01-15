import streamlit as st
from PIL import Image

page = st.sidebar.radio('阿短的首页', ['阿短的兴趣推荐', '阿短的图片处理工具', '阿短的智慧词典', '阿短的留言区'])

def page_1():
    '''阿短的兴趣推荐'''
    st.write('阿短的世界之旅')
    st.write('我在各种假期中可没闲着，而是在世界各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
    st.write('')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image('去海边游泳.png')
        st.write('去海边游泳')
        st.write('在海边游泳和在游泳池游泳感觉完全不同，海面有波浪，脚下是软软的沙子，在水里什么都看不清，而且，海水咸得发苦，别问我是怎么知道的……')
    with col2:
        st.image('去森林里露营.png')
        st.write('去森林里露营')
        st.write('森林里的夏天真的出乎意料的凉爽，甚至晚上还得加衣服，和家人们一起来顿野炊也是别有一番风味，即使是蚊虫的骚扰也无法赶走好心情！~')
    with col3:
        st.image('去沙漠看金字塔.png')
        st.write('去沙漠看金字塔')
        st.write('沙漠的白天非常热，但是当地人都把自己裹得严严实实，我们在这里看到了金字塔，比想象中要大得多，真实太壮观了！')
    with col4:
        st.image('去雪山上滑雪.png')
        st.write('去雪山上滑雪')
        st.write('装备多到好半天才能穿上，飞吹在脸上就像刀割，人摔在雪上也非常狼狈，但当你掌握了技巧你会发现这一切都是值得的，太刺激了！')

def page_2():
    '''阿短的图片处理工具'''
    pass

def page_3():
    '''阿短的智慧词典'''
    pass

def page_4():
    '''阿短的留言区'''
    pass

if page == '阿短的兴趣推荐':
    page_1()
elif page == '阿短的图片处理工具':
    page_2()
elif page == '阿短的智慧词典':
    page_3()
elif page == '阿短的留言区':
    page_4()