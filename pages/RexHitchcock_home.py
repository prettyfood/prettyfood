import turtle
import streamlit as st
from PIL import Image
import requests

page = st.sidebar.radio("©R.Hitch :v✨纷繁中的一隅",["文选","图片处理","词典","评论","百科问题","让我们摇滚！","超链接口"])
def page1():
    st.title(':orange[文选：精选文集]')
    st.subheader("版权所有，禁止复制，违者必究")
    tab1,tab2,tab3,tab4=st.tabs(["章节1：那难以忘却的容颜","章节2：那一切都是如此陌生","独立散文:四季的松，永远的松","🎚️宗教颂词：希明教∩"])
    with tab1:
        st.write(''' 她的外表是特别的，至少
                 在我所认识的大部分的中老年妇女中，她是鹤立鸡群的存
                 在。她的嘴唇上永远的抹着口红，说话时有一种奇怪的口音，她的头
                 发永远是那样的柔顺，总是略微的向内弯曲，我想她定是每天都坚持打
                 理头发。她的衣服十分具有季节性，比如在冬天，她永远都穿着那件鲜橙色的外套，让
                 人老远都能看到她。就如同绝大多数的老年人，她的脸上也被岁月留下了深深浅浅的印记，饱经沧桑。''')
    with tab2:
        st.write('''曾记得那天学校刚有了学生的欢笑。
                 一切都是百废待兴，充满生机的状态。这是我们初二的开始，经过陆
                 氏政治教学一年的洗礼后，我们的政治水平可以说是"绝无仅有"的级别，不出意外
                 地，我们将在本学期的测试中，又一次的"第十"桂冠。但其实这一切的一切都是陆氏政
                 治教学的"功劳"，经过一年的总结，陆氏政治教学的执政纲领大概是"不强求，不
                 管理，不反馈"。在这样的环境下，我们会有什么进步可言？因此即使路无论如何费
                 心，我们始终提高不了成绩。其实我们早有察觉，政治的位子好像要易主了!但我们并
                 没有认为我们的成绩会有提高。其实这纯属正常，毕竟连开学第一天都没有上课，我们
                 并没有改变原来的态度。不过很快我们就被好好的治了一治。在上课以前，我们仍在三三两
                 两的说话，这时，她进来了。她把书放在讲台上，然后喝住了我们，顿时是死一般的宁静。她
                 究竟说了什么，我早已淡忘，但不免是痛斥我们的自由散漫，介绍了自己。而后，她让我们一
                 个一个的介绍自己。不得不说，这可是稀奇的，因为从来没有一个老师推行过这样的活动。大
                 家感到的是稀奇，便开开心心的介绍完了。随后她对我们提出了如何学习政治的要求。不过在她
                 第一次发火前，我们并没有把他当约法三章当回事。那次作业，我们没有按着她的要求去做，她
                 为此大发雷霆，于是我们就再不敢糊弄作业了，她这大刀阔斧的改革好像卓有成效。在第一次月考
                 中，我们总算不是"第十"了，这成绩的背后是她的一系列改革。在初一时我们从来没有上课默写
                 的经历，但她认为不默写怎么能检验我们的背诵情况呢？此后每次课前，我们都在准备默写，有人
                 滥竽充数，有人早已滚瓜烂熟，虽然卓有成效，可这还不足以弥补我们那烂到根里的政治。也许是时
                 代的影响，她的管理方式有一种家庭联产承包责任制的味道，她按着上次的成绩为全班划分了许多小组
                 ，而这只是前提，为了追加动力，她让组与组，组里的个人之间都展开竞争，今天再去想想这个决策是有多么正确''')
    with tab3:
        st.write('''春去冬来，寒暑易节。
                 漫步于校园之中，有许多的事物在悄然中消失，有许多事物如雨后春笋般出现。
                 但却有一样东西始终没有改变——那挺拔雄伟的苍松。这颗树的寿命我无从得知
                 ，沧桑的树皮上刻写着岁月的痕迹，粗壮的主干更需两人合围，硕大的树冠向四周伸展，直
                 挺的树干更是无旁逸斜出的，正如茅盾所言"像加过人工似的"。春天时，万物竞发，松也不甘人后。温暖的春风
                 拂过，它一改冬天的庄严肃穆，舒展自己的枝干，为这一年之计做好准备。沐浴在和熙的暖阳中，万
                 物有了生气，万物有了活力。姹紫嫣红的花陆续回到大地上，一展自己的风采，但当你的眼睛倦了，对大红
                 大紫的颜色感到生厌时，去回望那苍翠的颜色吧，感受朴素淡雅的美好。盛夏，火辣的烈阳炙烤着大地，蝉展
                 开了漫长的演唱，燥热席卷了全身。松的针叶显得更加苍翠欲滴，枝叶葳蕤，与这燥热形成鲜明的反差，仅仅
                 是一望，便似有寒意袭来，课间时，和同学三五成群的在树下畅谈人生，确是另一种人生乐趣。到了秋天时，
                 万物似有枯败之相，纷纷褪去华丽的花枝绿叶，但松依然是翠绿的，不改春夏的荣光，只是稍收敛锋芒，全不俱
                 秋风，算得上鹤立鸡群一般的存在。时值寒冬，大雪飘飞下，似"撒盐空中"，又似"柳絮因风起"，洁白的雪纷纷
                 飘落，在树上落上了厚厚的一层，雪和树之间仿佛有一种微妙的平衡，雪之洁白与松之苍绿相互映衬，相互依托而又相
                 得益彰。待到几只飞鸟停息，轻点树枝，震落些许碎雪，悄悄的它们走了，正如它们轻轻地来，挥一挥翅膀，不带走一
                 片白雪。这洁白的世界和宛然神工的松构成了灵巧的图画。松在四季都傲然的挺立，不因天寒而褪去光彩，不因他人的
                 艳丽而动摇最朴质的美。我高声赞美松树，赞美他那不屈的精神，赞美他那高洁傲岸的态度。松因为有了如此的品质，
                 才是永远的，永远不灭的松。''')
    with tab4:
        st.write('''啊！主。您赐予我们每日的食粮，给予我们希望，降下光明和美好！:v
                啊！主。您的关爱是强大的，您是抚慰我们的良药。:v
                啊！主。您法力无边，您无所不至。:v
                啊！主。您在危难之时，给予我们互助的力量，让我们满怀希望。:v
                啊！主。请给予我们，至深的力量，我们将让世界更美好。:v
                啊！主。请给予我们，纯洁的力量，我们将洗濯自身罪恶。:v
                啊！主。请给予我们，您的教导，无论多么漫长，我们都始终跟随您的步伐。:v
                啊！主。我们感悟您的哲学，感悟您的所见所想。:v
                啊！主。我们遵守您的指引，无论有多少艰辛，我们都坚定不渝。:v
                啊！主。请给予我们，您的原谅，我们至切的忏悔，希望弥补过错。:v
                啊！主。我们向你祈祷，愿您的大爱散布人间。:v
                啊！主。我们向您赞美，礼赞您的方方面面。:v
                啊！主。我们向您叙说，净化吾之内心。:v
                啊！主。我们向您表露真心，愿您能听见这微小的呐喊。:v
                啊！主。我们向您祝圣，愿您的圣光永不消散。:v
                啊！主。我们感恩大爱，您让我们认识到自身的渺小和您的伟大。:v
                啊！主。我们关怀万物，您创造了世间一切。:v
                啊！主。我们劝诫万生，您的教徒将一一归化。:v
                啊！主。我们奔行世间，为朝圣而生，为您而生。:v
                啊！主。我们教化蛮夷，为天下大爱而遵行您的教导。:v
                啊！主。我们诚实，不弄虚作假，不背弃自心。:v
                啊！主。我们谦卑，不向他人索要赞美，只遵循您的声音。:v
                啊！主。我们友爱，无论对任何人都一视同仁。:v
                啊！主。我们守信，不背离诺言，一如既往。:v
                啊！主。我们善良，对于他人，我们互帮互助。:v
                啊！主。我们清白，不污染自我，不损己声誉。:v
                啊！主。我们永追随您，不离不弃。:v
                啊！主。您统辖一切，是人世的神。:v
                啊！主。您在天国款待善人，是天国的主。:v
                啊！主。您将恶人打入炼狱，是公正的神。:v
                啊！主。您在无形中助力您的信徒，我们礼赞您！:v
                啊！主。您无处不在，关怀万物，我们礼赞您！:v
                啊！主。您在我们的路途中，给予我们信念和勇气，我们礼赞您！:v
                啊！主。您即永恒，见证我们的信仰。:v
                啊！主。您即公理，断决我们的是非。:v
                啊！主。您即智识，赐予至上的智慧。:v
                啊！主。您是崇高的，纯洁的。:v
                啊！主。您是我们唯一的神。:v
                啊！主。我们永远不背弃您。:v
                啊！主。我们永远赞美您的荣光！:v
                ''')
def page2():
    st.subheader(':globe_with_meridians:图片处理应用')
    uploaded_file = st.file_uploader("传入图片（仅png，jpg，jpeg格式）",type=["png","jpg","jpeg"])
    if uploaded_file:
        name = uploaded_file.name
        size = uploaded_file.size
        type = uploaded_file.type
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["原图","方案1","方案2","方案3","方案4","方案5"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(imagechange(img,0,2,1))
        with tab3:
            st.image(imagechange(img,2,0,1))
        with tab4:
            st.image(imagechange(img,1,2,0))
        with tab5:
            st.image(imagechange(img,1,0,2))
        with tab6:
            st.image(imagechange(img,2,1,0))

def page3():
    st.title("REX DICTIONARY 2024:V v 1.20.23")
    with open("Rex.txt","r",encoding="utf-8") as f:
        wordslist=f.read().split("\n")
    for i in range(len(wordslist)):
        wordslist[i] = wordslist[i].split('#')
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        timeslist = f.read().split('\n')
    wordsdict = {}
    for i in wordslist:
        wordsdict[i[1]] = [int(i[0]), i[2]]
    for i in range(len(timeslist)):
        timeslist[i] = timeslist[i].split('#')
    timesdict = {}
    for i in timeslist:
        timesdict[int(i[0])] = int(i[1])
    word = st.text_input('输入需查询的单词：')
    if word in wordsdict:
        list_yuan=wordsdict[word][1].split(' ')
        list_xiao=[]
        for i in range(len(list_yuan)):
            if list_yuan[i]!="":
                list_xiao.append(list_yuan[i])
        st.write("词性、词义",list_xiao)
        st.text('词典（第二版）中第' + str(wordsdict[word][0]) + '个单词')
        n=wordsdict[word][0]
        if n in timesdict:
            timesdict[n] += 1
        else:
            timesdict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in timesdict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.text('单词的查询次数：' + str(timesdict[n]))
    elif word not in wordsdict:
        st.write("该词典仅收录了单词的基本形式，我们未找到您输入的单词 :v :orange[(如未输入单词,请输入后再试)]")
def page4():
    st.subheader("评论")
    st.write("请在此处留下你的意见，这对我们来说很重要，或直接向我们发送邮件：1745967348@qq.com")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list=f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="S.Harge":
            with st.chat_message('🌞'):
                st.write(i[1],":",i[2])
        elif i[1]=="visitors":
            with st.chat_message('🌐'):
                st.write(i[1],":",i[2])
        elif i[1]=="R.Hitch":
            with st.chat_message('🎭'):
                st.write(i[1],":",i[2])        
    name=st.selectbox("I'm",["S.Harge","visitors"])
    newmess=st.text_input("Text you message here")
    if st.button("评论"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,newmess])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def page5():
    st.title("百科问答")
    st.subheader('1.普朗克常数的表达式为？')
    cb1 = st.checkbox('h=6.62606896（23）×10^（-34） J·s')
    cb2 = st.checkbox('h=6.63606896（33）×10^（-34） J·s')
    cb3 = st.checkbox('h=6.62606896（33）×10^（-54） J·s')
    cb4 = st.checkbox('h=6.62606876（33）×10^（-34） J·s')
    l = [cb1,cb2,cb3,cb4]
    if st.button('确认答案1'):
        if True in l:
            st.write('知识就是力量，而你没有力量')
        else:
            st.write('不错，加10分，答案是：h=6.62606896（33）×10^（-34） J·s')

    st.title(" ")
    
    st.subheader('2."大秦"是中国古代对于哪国的称谓？')
    cb1 = st.checkbox('古罗马')
    cb2 = st.checkbox('古希腊')
    cb3 = st.checkbox('古波斯（今伊朗）')
    cb4 = st.checkbox('古埃及')
    l = [cb2,cb3,cb4]
    k=[cb1]
    if st.button('确认答案2'):
        if True in l:
            st.write('知识就是力量，而你没有力量')
        elif False in k:
            st.write('知识就是力量，而你没有力量')   
        else:
            st.write('不错，加10分')
            
    st.title(" ")
    
    st.subheader('3.麦哲伦海峡位于哪国领海内？')
    cb1 = st.checkbox('古巴')
    cb2 = st.checkbox('智利')
    cb3 = st.checkbox('阿根廷')
    cb4 = st.checkbox('巴拉圭')
    l = [cb1,cb3,cb4]
    k=[cb2]
    if st.button('确认答案3'):
        if True in l:
            st.write('知识就是力量，而你没有力量')
        elif False in k:
            st.write('知识就是力量，而你没有力量')   
        else:
            st.write('不错，加10分')

    st.title(" ")
    
    st.subheader('4.下面哪一项不是杜甫所写？')
    cb1 = st.checkbox('《岁晏行》')
    cb2 = st.checkbox('《丽人行》')
    cb3 = st.checkbox('《致酒行》')
    cb4 = st.checkbox('《兵车行》')
    l = [cb1,cb2,cb4]
    k = [cb3]
    if st.button('确认答案4'):
        if True in l:
            st.write('知识就是力量，而你没有力量')
        elif False in k:
            st.write('知识就是力量，而你没有力量')            
        else:
            st.write('不错，加10分')
    st.title(" ")
    st.subheader('5.小明用天平测量一块斑岩的ρ时（不吸水），先测出V，再测出m，其密度不可能是？')
    cb1 = st.checkbox('ρ=2.584g/cm³')
    cb2 = st.checkbox('ρ=2.801g/cm³')
    cb3 = st.checkbox('ρ=2.799g/cm³')
    cb4 = st.checkbox('ρ=2.811g/cm³')
    l = [cb2,cb3,cb4]
    k = [cb1]
    if st.button('确认答案5'):
        if True in l:
            st.write('知识就是力量，而你没有力量')
        elif False in k:
            st.write('知识就是力量，而你没有力量')            
        else:
            st.write('不错，加10分')    
def page6():
    st.title("摇滚！专栏:vThe Rolling Stones乐队金曲")
    st.subheader("野马")
    with open("野马.mp3","rb") as f:
        mp30=f.read()
    st.audio(mp30,format='audio/mp3',start_time=0)
    st.subheader("有时你不能得偿所愿")
    with open("You c't always get what ya want.mp3","rb") as f:
        mp31=f.read()    
    st.audio(mp31,format='audio/mp3',start_time=0)
    st.subheader("活泼的杰克·弗莱士")
    with open("Jumpin Jack Flash.mp3","rb") as f:
        mp32=f.read()    
    st.audio(mp32,format='audio/mp3',start_time=0)
    st.subheader("我不能停下取乐")
    with open("Satfaction.mp3","rb") as f:
        mp33=f.read()    
    st.audio(mp33,format='audio/mp3',start_time=0)
def page7():
    st.subheader('访问其他的页面')
    go = st.selectbox('求求看看我的视频吧,你也可以去看看电影（如链接失效，请联系me：15330736103）', ["🎬“正经”电影1","🎬“正经”电影2",'Bilibili'])
    if go == '🎬“正经”电影1':
        st.link_button('不要有非分之想哦', 'https://www.555dyy.top/')
    elif go == '🎬“正经”电影2':
        st.link_button('不要有非分之想哦', 'https://www.dmdyy.cc/')
    elif go == 'Bilibili':
        st.link_button('帮我一键三连', 'https://b23.tv/OoPNndB')
def imagechange(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=r,g,b
    return img
if (page == '文选'):
    page1()
elif (page == '图片处理') :
    page2()
elif (page == '词典') :
    page3()
elif (page == '评论') :
    page4()
elif (page == '百科问题') :
    page5()
elif (page == "让我们摇滚！") :
    page6()
elif (page == "超链接口") :
    page7()