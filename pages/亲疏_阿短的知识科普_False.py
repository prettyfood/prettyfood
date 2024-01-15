import streamlit as st

page = st.sidebar.radio('阿短的首页', ['阿短的兴趣推荐', '阿短的图片处理工具', '阿短的智慧词典', '阿短的留言区', '阿短的知识科普'])

def page_1():
    '''阿短的兴趣推荐'''
    pass

def page_2():
    '''阿短的图片处理工具'''
    pass

def page_3():
    '''阿短的智慧词典'''
    pass

def page_4():
    '''阿短的留言区'''
    pass

def page_5():
    '''阿短的互联网知识科普'''
    st.write('阿短的互联网知识科普大讲堂')
    st.write('先来做两个测试题吧，看看你对互联网了解多少')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    col1_1, col1_2, col1_3, col1_4 = st.columns([1, 1, 1, 1])
    with col1_1:
        cb1_1 = st.checkbox('易于管理')
    with col1_2:
        cb1_2 = st.checkbox('效率高')
    with col1_3:
        cb1_3 = st.checkbox('网速快')
    with col1_4:
        cb1_4 = st.checkbox('安全性好')

    st.write('你了解吗：可以通过哪些地址找到一个网站？')
    col2_1, col2_2, col2_3, col2_4 = st.columns([1, 1, 1, 1])
    with col2_1:
        cb2_1 = st.checkbox('IPv4地址')
    with col2_2:
        cb2_2 = st.checkbox('IPv6地址')
    with col2_3:
        cb2_3 = st.checkbox('域名地址')
    with col2_4:
        cb2_4 = st.checkbox('经纬度地址')

if page == '阿短的兴趣推荐':
    page_1()
elif page == '阿短的图片处理工具':
    page_2()
elif page == '阿短的智慧词典':
    page_3()
elif page == '阿短的留言区':
    page_4()
elif page == '阿短的知识科普':
    page_5()