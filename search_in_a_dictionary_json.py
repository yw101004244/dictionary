import json

def into_json():
    #字典读入dictionary.json
    dic_name = 'ox-edict-utf8.txt'
    dictionary = {}
    test=1          #奇数则是单词，偶数则是解释
    with open(dic_name,encoding='UTF-8') as file_object:
        for line in file_object:
            if line != '\n':    #跳过空行
                if test%2==1:
                    dictionary[line]='' #创建单词（键）
                    temp=line
                else:
                    dictionary[temp]=line #给单词对应意思（值）
                test=test+1
    
    filename='dictionary.json'
    with open(filename,'w') as file_object:
        if file_object is not None:
            json.dump(dictionary,file_object)


def search_in_a_dictionary(usr_input):
    #查字典
    filename='dictionary.json'
    with open(filename) as file_object:
        dictionary=json.load(file_object)

    #退出,函数返回0
    if usr_input == 'q\n':
        return 0

    #查字典
    elif usr_input not in dictionary.keys():#查不到，函数返回输入错误
        print("error! It's not in the dictionary!")
        return "input error"
    else:#查到了，函数返回单词意思
        print(dictionary[usr_input])
        return dictionary[usr_input]
        
'''
while(True):
    #处理用户输入的字符串
    usr_inputs = input("Please input a word: ")
    usr_inputs = usr_inputs.split('""',1) #去掉字符串两边的双引号
    usr_inputs = usr_inputs[0]+"\n" #加上换行符便于查询
    search_in_a_dictionary(usr_inputs) #查询'''