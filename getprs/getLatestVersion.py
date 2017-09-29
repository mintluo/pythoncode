import re

DATA_FILE = './Report-700U-7000.csv'#当前目录下待处理文件
#DATA_FILE = './test.csv'
STORED_FILE = './test_out.csv'#处理结果保存到当前目录下目标文件
DEALING_FILENAME = set()
listVersion = []
outputText = []

#获取版本列表中日期最新的版本
def getnewversion(versionList):
    datelist=[]
    result=""
    for versionline in versionList:
        datelist+=re.findall(r"(?<!SZ)(\d{8}|\d{7}|\d{6})", versionline)#零宽负向断言，排除SZ开头的合同号
    if len(datelist) == 0:#如果未匹配出日期，直接返回
        return "无匹配日期"
    else:
        for index in range(len(datelist)):
            if len(str(datelist[index]))==8:
                result+=""
            elif len(datelist[index])==6:#如果是六位日期，先补齐为8位
                datelist[index]='20'+datelist[index]
            else:#如果是其他位数（7位）的日期，提示
                result+="请检查%s日期格式."%datelist[index]
        return result+versionList[datelist.index(max(datelist))]#返回提示信息+最新版本


with open(DATA_FILE) as input_file:
    for line in input_file:
        Index, fileIndex, filePath, fileName, locate, contract, version, editDate, match, fileSize, fileType, creatTime, visitTime, fileExtent, fileRow, fileText = line.split(';')
        #print(Index+','+fileName+','+fileText)
        if fileIndex == '1':#如果第一次处理该文件
            #先处理上一个文件（判断结果输出到每个文件组的最后一行）
            outputText.append(getnewversion(listVersion))#将上一个文件的最新版本信息保存到输出列表
            listVersion.clear()#清空版本信息列表，以保存下一个文件的版本信息

            #再处理本行文件
            matchV=re.findall(r"((PRS-700U|PRS-7000).+?(?<!SZ)(\d{8}|\d{7}|\d{6}))", fileText, re.MULTILINE)#非贪婪（懒惰）匹配，匹配尽量少的内容，以免将两条版本信息匹配为一条
            for matchVersion in matchV:#findall会匹配所有()分组，取第一个，即最外层()的匹配
                listVersion.append(matchVersion[0])
            #print(listVersion)

        else:#如果不是该文件的首行
            matchV=re.findall(r"((PRS-700U|PRS-7000).*?(?<!SZ)(\d{8}|\d{7}|\d{6}))", fileText, re.MULTILINE)
            for matchVersion in matchV:
                listVersion.append(matchVersion[0])
            #print(listVersion)
            outputText.append('子行')#如果不是文件首行，指明为子行

    #处理最后一个文件
    outputText.append(getnewversion(listVersion))

    outputText.pop(0)#//剔除表头第0行
with open(STORED_FILE, 'w') as output_file:
    str_list = [line + '\n' for line in outputText]  # 在list中加入换行符
    output_file.writelines(str_list)