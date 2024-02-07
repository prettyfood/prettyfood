import streamlit as st
import time
from PIL import Image
import os
page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的照片处理工具","我的智慧词典","留言","蜂巢","相机"])
def img_change(img,rc,gc,bc):
    w,h=img.size
    array=img.load()
    for x in range(w):
        for y in range(h):
            r=array[x,y][rc]
            g=array[x,y][gc]
            b=array[x,y][bc]
            array[x,y]=(r,g,b)
    return img
def img_change2(img):
    w,h=img.size
    array=img.load()
    for x in range(w):
        for y in range(h):
            r=array[x,y][0]*2
            g=array[x,y][1]*2
            b=array[x,y][2]*2
            print(type(r))
            if int(r)>255:
                r=r-255
            if int(g)>255:
                g=g-255
            if int(b)>255:
                b=b-255
            array[x,y]=(r,g,b)
def page_1():
    imgs_name_lst = ['唐人街探案.jpg', 'th.jpg']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((450, 600))
        imgs_lst.append(img)
    col1, col2 = st.columns([ 1, 1])
    st.header(":blue[**最爱玩的游戏：**]")
    st.subheader(":white[金铲铲之战]")
    st.image("金铲铲之战.jpg")
    with col1:
        st.header(":blue[**最喜欢看的电影：**]")
        st.subheader(":white[唐人街探案系列]")
        st.image(imgs_lst[0])
    with col2:
        st.header(":blue[**最喜欢的歌手：**]")
        st.subheader(":white[周杰伦]")
        st.image(imgs_lst[1])
def page_2():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        if ch:
            img = img_change_ch(img)
        if co:
            img = img_change_co(img)
        if bw:
            img = img_change_bw(img)
        st.image(img)
        mz=st.text_input("输入保存的名字")
        if st.button("保存照片"):
            if mz=="":
                st.write("请输入")
            else:
                img.save(f"{mz}.png")
                st.write("保存成功")
def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img
def page_3():
    tab1,tab2=st.tabs(["词典","单词本"])
    with tab1:
        st.write("词典")
        with open("check_out_times.txt","r",encoding="utf-8")as a:
            check_list=a.read().split("\n")
        for i in range(len(check_list)):
            check_list[i]=check_list[i].split("#")
        check_dict={}
        for i in check_list:
            check_dict[int(i[0])]=int(i[1])
        with open("words_space.txt","r",encoding="utf-8")as f:
            word_list=f.read().split("\n")
        for i in range(len(word_list)):
            word_list[i]=word_list[i].split("#")
        word_dict={}
        for i in word_list:
            word_dict[i[1]]=[int(i[0]),i[2]]
        word=st.text_input("查询单词")
        if word in word_dict:
            st.write("中文意思为"+word_dict[word][1])
            if word=="cbl":
               st.snow()
            elif word=="python":
                st.balloons()
            n=word_dict[word][0]
            if n in check_dict:
                check_dict[n]+=1
            else:
                check_dict[n]=1
            st.text("查询过"+str(check_dict[n]))
            with open("check_out_times.txt","w",encoding="utf-8")as f:
                message=""
                for k,v in check_dict.items():
                    message+=str(k)+"#"+str(v)+"\n"
                message=message[:-1]
                f.write(message)
            if st.button("加入单词本"):
                with open("dcb.txt","r",encoding="utf-8")as f:
                    dcb_list=f.read().split("\n")
                for i in range(len(dcb_list)):
                    dcb_list[i]=dcb_list[i].split("#")
                with open("dcb.txt","a",encoding="utf-8")as f:
                    for i in range(len(dcb_list)):
                        dcb_list2=dcb_list[i][0]
                    if word in dcb_list2:
                        st.write("已经添加过了")
                    else:
                        f.write("\n"+word+"#"+word_dict[word][1])
        else:
            st.write("查询的单词不在字典中")
    with tab2:
        with open("dcb.txt","r",encoding="utf-8")as f:
            dcb_list=f.read().split("\n")
        for i in range(len(dcb_list)):
            dcb_list[i]=dcb_list[i].split("#")
        for i in range(len(dcb_list)):
            print(dcb_list)
            if dcb_list[i]=="":
                pass
            else:
                st.write(str(i+1)+"."+dcb_list[i][0]+"   "+dcb_list[i][1])
        sc=st.text_input("删除那个单词(数字)")
        if st.button("删除"):
            if sc=="":
                pass
            else:
                for i in range(len(dcb_list)):
                    if i==int(sc)-1:
                        pass
                    else:
                        if i==0:
                            tj=dcb_list[i][0]+"#"+dcb_list[i][1]+"\n"
                        elif int(sc)==1 and i==1:
                            tj=dcb_list[i][0]+"#"+dcb_list[i][1]+"\n"
                        else:
                            tj+=dcb_list[i][0]+"#"+dcb_list[i][1]
                            if i+1==len(dcb_list):
                                pass
                            elif int(sc)==len(dcb_list) and i+2==int(sc):
                                pass
                                print(2)
                            else:
                                tj+="\n"
            with open("dcb.txt","w",encoding="utf-8")as f:
                f.write(tj)
                st.write("删除成功") 
def page_4():
    st.write("我的留言区")
    with open("leave_messages.txt","r",encoding="utf-8")as a:
        message_list=a.read().split("\n")
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split("#")
    for i in message_list:
        if i[1]=="阿短":
            with st.chat_message("💯"):
                st.write(i[1],":",i[2])
        elif i[1]=="编程猫":
            with st.chat_message("🍇"):
                st.write(i[1],":",i[2])
    name=st.selectbox("我是......",["阿短","编程猫"])
    new_message=st.text_input("内容")
    if st.button("留言"):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8")as f:
            message=""
            for i in message_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)
def page_5():
    tab1,tab2=st.tabs(["取出","存入"])
    with tab1:
        qjm=st.text_input("请输入取件码")
        if qjm=="":
            pass
        else:
            roading = st.progress(0, '开始加载')
            time.sleep(1)
            for i in range(1, 101, 1):
                time.sleep(0.01)
                roading.progress(i, '正在加载'+str(i)+'%')
            with open("fc.txt","r",encoding="utf-8")as a:
                fc_list=a.read().split("\n")
            for i in range(len(fc_list)):
                fc_list[i]=fc_list[i].split("#")
            fc_dict={}
            for i in fc_list:
                fc_dict[int(i[0])]=[i[1],i[2],i[3],i[4]]
            if int(qjm) in fc_dict:
                st.write("内容：",fc_dict[int(qjm)][0])
                st.write("存件人：",fc_dict[int(qjm)][1])
                st.write("时间：",fc_dict[int(qjm)][2])
                if int(fc_dict[int(qjm)][3])==1:
                    ima=Image.open(f"{qjm}.png")
                    st.image(ima)  
            else:
                st.write("取件码错误")
    with tab2:
        qjmm=st.text_input("请输入取件码（只可为数字,6位数)")
        if qjmm=="":
            st.write("请输入")
        else:
            qjmm=int(qjmm)
            with open("fc.txt","r",encoding="utf-8")as a:
                fc_list=a.read().split("\n")
            for i in range(len(fc_list)):
                fc_list[i]=fc_list[i].split("#")
            fc_dict={}
            for i in fc_list:
                fc_dict[int(i[0])]=[i[1],i[2],i[3]]
            if int(qjmm) in fc_dict:
                st.write("取件码被占用")
            else:
                if 99999<qjmm<1000000:
                    nr=st.text_input("请输入内容")
                    cjr=st.text_input("你是谁")
                    change=st.selectbox("是否提交照片",["是","否"])
                    if change=="否":
                        c=0
                    else:
                        uploaded = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
                        c=1
                    sj=str(time.localtime().tm_year)+"."+str(time.localtime().tm_mon)+"."+str(time.localtime().tm_mday)
                    if uploaded=="" or cjr=="" or nr=="":
                        pass
                    else:
                        if st.button("保存"):
                            roading = st.progress(0, '开始加载0%')
                            gg=st.link_button('🏎️🏎️🏎️加速一下🏎️🏎️🏎️', 'https://shequ.codemao.cn/')
                            time.sleep(3)
                            roading.progress(90, '飞速加载90%')
                            time.sleep(5)
                            for i in range(90, 101, 1):
                                time.sleep(0.5)
                                roading.progress(i, '拼命加载'+str(i)+'%')
                            with open("fc.txt","a",encoding="utf-8")as f:
                                f.write("\n"+str(qjmm)+"#"+nr+"#"+cjr+"#"+sj+"#"+str(c))
                                I=Image.open(uploaded)
                                I.save(f"{qjmm}.png")
                            st.write("保存成功")
                else:
                    st.write("请输入6位数")
def page_6():
    tab1,tab2=st.tabs(["相机","相册"])
    with tab1:
        picture = st.camera_input("拍照")
        if picture:
            zh=st.text_input("输入存入的账号（账号越长越安全）")
            if st.button("保存照片"):
                if zh=="":
                    st.write("请输入账号")
                else:
                    I=Image.open(picture)
                    with open("cs.txt","r",encoding="utf-8")as f:
                        e=f.read()
                        d=int(e)+1
                    with open("cs.txt","w",encoding="utf-8")as f:
                        f.write(str(d))
                    I.save(f"{zh}#自拍{d}.png")
                    st.write("保存成功")
    with tab2:
        zh=st.text_input("输入账号")
        if st.button("查询"):
            if zh=="":
                st.write("还没有输入账号")
            else:
                dir = os.path.dirname(os.path.abspath(__file__))
                dir2=os.listdir(dir)
                ima=""
                for i in dir2:
                    if i.split("#")[0]==zh:
                        ima=Image.open(i)
                        st.image(ima) 
                if ima=="":
                    st.write("该账号没有照片")
if page=="我的兴趣推荐":
    page_1()
if page=="我的照片处理工具":
    page_2()
if page=="我的智慧词典":
    page_3()
if page=="留言":
    page_4()
if page=="蜂巢":
    page_5()
if page=="相机":
    page_6()