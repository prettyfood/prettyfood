'''我的主页'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('BSH主页', ['BSH简介', '图片处理工具', '我的智慧词典', '我的留言区', '告知时刻'])

with open("Payphone.mp3", 'rb') as f:
    mymp3 = f.read()
st.audio(mymp3, format='audio/mp3', start_time=0)
def page1():
    '''BSH简介'''
    st.title("BSH简介:sunglasses:")
    st.write("      ")
    st.write(':blue[:microphone:你好,欢迎来到BSH官网。某个意外将她们召集起来，未曾想到正是这次意外使她们拥有巨大能量。成为一个组织：BSH:game_die:]')
    st.write(':green[我们组织由稚水、yeji、A、糖糖、小蛋糕组成]')
    st.image("生存.png")

def page2():
    '''图片处理工具'''
    st.title(":art:图片处理小程序:art:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 1, 2, 0))

def page3():
    '''我的智慧词典'''
    st.title('智慧词典')
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    #将列表中的每一项内容再进行分割，分为“编号，单词，解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    #将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    #从本地文件找那个将单词的查询次数读取出来，并存储在列表当中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #将列表转为字典
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
    with open('check_out_times.txt', 'w', encoding='utf-8') as f:
        message = ''
        for k, v in times_dict.items():
            message += str(k) + '#' + str(v) + '\n'
        message = message[:-1]
        f.write(message)
def page4():
    '''我的留言区'''
    st.title('我的留言区')
    st.write(":red[文明发言]")
    #从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split("#")
    for i in message_list:
        if i[1] == '稚水':
            with st.chat_message('📷'):
                st.write(i[1],':',i[2])
        elif i[1] == 'A':
            with st.chat_message('😁'):
                st.write(i[1],':',i[2])
        elif i[1] == 'yeji':
            with st.chat_message('🙄'):
                st.write(i[1],':',i[2])
        elif i[1] == '糖糖':
            with st.chat_message('🍬'):
                st.write(i[1],':',i[2])
        elif i[1] == '小蛋糕':
            with st.chat_message('🎂'):
                st.write(i[1],':',i[2])
                
    name = st.selectbox('我是......', ['稚水', 'A', 'yeji', '糖糖', '小蛋糕'])
    new_message = st.text_input('想要说的话....')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page5():
    '''告知时刻'''
    st.write(":gem:充满高质:gem:")
    st.write('下列哪个名字是BSH创始人的名字?')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        cb1 = st.checkbox('A.稚水')
    with col2:
        cb2 = st.checkbox('B.A')
    with col3:
        cb3 = st.checkbox('C.教科够')
    with col4:
        cb4 = st.checkbox('D.daughter of Ye')
    b1 = st.button('第一题答案')
    if b1:
        if cb1 == True:
            st.write('回答正确！')
        else:
            st.write('再想想')
    #st.button('点我试试')
    def dwss():
        msg = st.toast('等我几秒')
        time.sleep(1)
        msg.toast('准备中...')
        time.sleep(1)
        msg.toast('送你的！', icon = "🌻")
    if st.button('点我试试'):
        dwss()

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height  = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取rgb值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    
if page =='BSH简介':
    page1()
elif page =='图片处理工具':
    page2()
elif page =='我的智慧词典':
    page3()
elif page =='我的留言区':
    page4()
elif page =='告知时刻':
    page5()