import os
from collections import Counter
import string
import socket
import sys

original_stdout = sys.stdout

#folder paths
result=r'/home/output/result.txt'
dirPath = r'/home/data/'
ifFilePath=r'/home/data/IF.txt'
resultFile=open(result, 'w+')
with resultFile as f:

    #List to store files
    res = []

    #List name of all the text file at location: /home/data
    for path in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, path)):
            res.append(path)
    resultFile.write("Files at location /home/data are:\n")
    
    #total number of words in each text files
    sum=0
    for path in res:
        resultFile.write("->"+path+"\n")
        file = open("/home/data/"+path, 'r')
        read_data = file.read()
        per_word = read_data.split()
        abc="Total Words in " + path + ": " +str(len(per_word))   
        resultFile.write(abc+"\n")
        sum=sum+len(per_word)


    resultFile.write("Total number of words in the files combined"+str(sum)+"\n")


    #Top 3 words with maximum number of counts in IF.txt
    file = open(ifFilePath, 'r')
    read_data = file.read()
    per_word = read_data.split()

    word=[];
    for i in per_word:
        a=i.translate(str.maketrans('', '', string.punctuation))
        a=a.capitalize()
        word.append(a)
    Counter = Counter(word)
    most_occur = Counter.most_common(3)
    resultFile.write("The top 3 words with maximum number of counts in IF.txt "+str(most_occur)+"\n")



    #Getting computer's IP Address
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    resultFile.write("Computer's IP Address :"+IPAddr+"\n")
    sys.stdout = original_stdout
resultFile.close()

file = open(result, 'r',encoding='utf-8')
print(file.read())








