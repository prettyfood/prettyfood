import streamlit as st

page = st.sidebar.radio('阿短的首页', ['阿短的兴趣推荐', '阿短的图片处理工具', '阿短的智能词典', '阿短的留言区'])

def page_1():
    '''阿短的兴趣推荐'''
    pass

def page_2():
    '''阿短的图片处理工具'''
    pass

def page_3():
    '''阿短的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        # 输出查询的单词内容
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
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
        st.text('单词被查询次数为：' + str(times_dict[n]))

def page_4():
    '''阿短的留言区'''
    pass

if page == '阿短的兴趣推荐':
    page_1()
elif page == '阿短的图片处理工具':
    page_2()
elif page == '阿短的智能词典':
    page_3()
elif page == '阿短的留言区':
    page_4()