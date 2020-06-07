class SearchDictionary():
    def __init__(self):
        self.dictionary={}
        test=0
        dic_name='mini_dictionary.txt'
        with open(dic_name,encoding='UTF-8') as file_object:
            for line in file_object:
                if line != '\n':    #跳过空行
                    if test%4==0:
                        self.dictionary[line]=[] #创建单词（键）
                        temp=line
                    elif test%4==1:
                        self.dictionary[temp].append(line) #单词音标
                    elif test%4==2:
                        self.dictionary[temp].append(line) #单词词性
                    elif test%4==3:
                        self.dictionary[temp].append(line) #单词意思与例句
                    test=test+1
    
    def search_soundmark(self,input): #单词音标
        if input in self.dictionary.keys():
            print(self.dictionary[input][0])
            return self.dictionary[input][0]
        else:
            return "input error"

    def search_character(self,input): #单词词性
        if input in self.dictionary.keys():
            print(self.dictionary[input][1])
            return self.dictionary[input][1]
        else:
            return "input error"

    def search_explaination(self,input): #单词意思与例句
        if input in self.dictionary.keys():
            print(self.dictionary[input][2])
            return self.dictionary[input][2]
        else:
            return "input error"
    
    def search_all(self,input): #查询该单词所有信息
        if input in self.dictionary.keys():
            print(self.dictionary[input])
            return self.dictionary[input]
        else:
            return "input error"

#处理用户输入的字符串
def handle_input(usr_inputs):
    usr_inputs = usr_inputs.split('""',1) #去掉字符串两边的双引号
    usr_inputs = usr_inputs[0]+"\n" #加上换行符便于查询
    return usr_inputs