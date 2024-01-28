import streamlit as st
from PIL import Image
import time
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','网站查询','红色的开始'])
def page1():
    '''兴趣推荐'''
    st.write(":sunglasses:兴趣推荐:sunglasses:")
    st.write("今天，我们会来一场非常有意思的冒险")
    col1,col2 = st.columns([1,1])
    with col1:
        cb1 = st.write("你想要处理图片吗？")
    with col2:
        cb2 = st.image("三国鼎立.png")  
    col3,col4 = st.columns([1,1])
    with col3:
        cb3 = st.write("你想要快捷的词典吗？")
    st.write("那你就快来我们的网站吧")
def page2():
    '''图片'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        '''获取文件名字，类型，大小'''
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        #tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        # with tab1:
        #     st.image(img)   
        # with tab2:
        #     st.image(img_change(img,1,1,2))
        # with tab3:
        #     st.image(img_change(img,0,2,1))
        # with tab4:
        #     st.image(img_change(img,1,0,2))
        # 应用：图片_功能判断开关
        x = st.toggle('原图')
        ch = st.toggle('反色滤镜')
        bw = st.toggle('黑白滤镜')
        co = st.toggle('增强对比度') 
        if x:
            st.image(img)
        if ch:
            st.image(img_change(img,1,0,2))
        if bw:
            st.image(img_change(img,1,1,2))
        if co:
            st.image(img_change(img,0,2,1))
        # with tab1:
        #     st.image(img)   
        # with tab2:
        #     st.image(img_change(img,1,1,2))
        # with tab3:
        #     st.image(img_change(img,0,2,1))
        # with tab4:
        #     st.image(img_change(img,1,0,2))
def page3():
    '''智慧词典'''
    st.write(":sunglasses:智慧词典:sunglasses:")
    with open("words_space.txt",'r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
       words_list[i] = words_list[i].split('#')
    #将列表重点内容导入词典，方便查询，格式为“单词：编号，解释”
    words_dict = {} 
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    #从本地文件读取查询次数
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split("\n")
        message = ''
        
     # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])


    #创建输入框
    word = st.text_input('请输入要查询的单词')
    #显示查询内容
    if word in words_dict:  
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        
        st.write('查询次数：',times_dict[n])
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
    if word == 'python':
        st.code('''# 恭喜你触发彩蛋，这是一行python代码
               print('hello world')''')
    st.balloons()
    
        
def page4():
    '''留言区'''
    st.write(":sunglasses:留言区:sunglasses:")
    with open('leave_messages.txt',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])        
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load() 
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def page5():
# 应用：兴趣推广_分享链接指引
    st.write('这里可以去到其他网站哦')
    go = st.selectbox('点击按钮即可跳转', ['我的贴吧', '我的bilibili','我的原神'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
    elif go == '我的原神':
        st.link_button('原神，启动','https://mhyy.mihoyo.com/')
def page6():
    st.write("你知道中国共产党是什么时候成立的吗？")
    col1,col2 = st.columns([1,1])
    with col1:
        cb1 = st.checkbox("A.1921年")
    with col2:
        cb2 = st.checkbox("A.1922年")
    col3,col4 = st.columns([1,1])
    with col3:
        cb3 = st.checkbox("C.七月")
    with col4:
        cb4 = st.checkbox("D.八月")
    b1 = st.button("第一题答案")
    if b1:
        if cb1 == True and cb3 == True and cb2==False and cb4==False:
            
            st.write("回答正确")
            
        else:
            st.write("再想想")
def page7():
    st.write("那么你知道新中国是什么时候成立的吗？")
    col5,col6 = st.columns([1,1])
    with col5:
        cb5 = st.checkbox("A.1949")
    with col6:
        cb6 = st.checkbox("B.1937")
    col7,col8 = st.columns([1,1])
    with col7:
        cb7 = st.checkbox("C.十月")
    with col8:
        cb8 = st.checkbox("D.十一月")
    b2 = st.button("第二题答案")
    if b2:
        if cb5 == True and cb7 == True and cb8==False and cb6==False:
            st.write("回答正确")
            st.write("鉴于你回答对了问题，奖励你一张中华人民共和国的地图")
            st.image("16f5f6822da22052_600_0.jpeg")
        else:
            st.write("再想想")
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '网站查询':
    page5()
elif page == '红色的开始':
    page6()
    page7()