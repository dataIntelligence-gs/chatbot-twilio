import os
#from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
stop_words_sp = set(stopwords.words('spanish'))

def createWordCloud():
    responses = []
    conversations = []
    f_result = open("results_interesed.txt", "a", encoding="utf8")
    for i in os.listdir('division de clientes'):
        if i.endswith('.txt'):
            responses.append(i)

    for conversation in responses:
        f = open("conversations_interesed/"+conversation, "r", encoding="utf8")
        chat = f.readlines()
        #print(chat)
        conversations.append(chat)
        f_result.write(str(str(conversation)+","+str(chat))+'\n')
    #print(responses)
    print(conversations)


import pandas as pd


#createWordCloud()


results_1 = []
results_2 = []
results_3 = []
results_4 = []
results_marked_1 = []

f = open(f"division de clientes/clients_1_total.txt", "r")
clients_1 = f.readlines()
f.close()
f = open(f"division de clientes/clients_2_total.txt", "r")
clients_2 = f.readlines()
f.close()
f = open(f"division de clientes/clients_3_total.txt", "r")
clients_3 = f.readlines()
f.close()
f = open(f"division de clientes/clients_4_total.txt", "r")
clients_4 = f.readlines()
f.close()

# f = open(f"marcaron1.txt", "r")
# marked_1_total = f.readlines()
# f.close()

df = pd.read_csv("resultados.csv", sep=";", encoding='latin-1')
clients_cleaned_1 = []
clients_cleaned_2 = []
clients_cleaned_3 = []
clients_cleaned_4 = []
marked_1 = []

for value in clients_1:
    res = value.replace("\n", "")
    clients_cleaned_1.append(res)

for value in clients_2:
    res = value.replace("\n", "")
    clients_cleaned_2.append(res)

for value in clients_3:
    res = value.replace("\n", "")
    clients_cleaned_3.append(res)

for value in clients_4:
    res = value.replace("\n", "")
    clients_cleaned_4.append(res)

# for value in marked_1_total:
#     res = value.replace("\n", "")
#     marked_1.append(res)

for i in range(len(df)):    
    if str(df.iloc[i]['NUMBER']) in str(clients_cleaned_1):
        results_1.append(df.iloc[i]['CONTENT'])
        f_1 = open("results_1.txt", "a", encoding="utf8")
        f_1.write(str(df.iloc[i]['NUMBER']+'\n'))
        f_1.close()

    if str(df.iloc[i]['NUMBER']) in str(clients_cleaned_2):
        results_2.append(df.iloc[i]['CONTENT'])
        f_2 = open("results_2.txt", "a", encoding="utf8")
        f_2.write(df.iloc[i]['NUMBER']+","+df.iloc[i]['CONTENT']+'\n')
        f_2.close()


    if str(df.iloc[i]['NUMBER']) in str(clients_cleaned_3):
        results_3.append(df.iloc[i]['CONTENT'])
        f_3 = open("results_3.txt", "a", encoding="utf8")
        f_3.write(df.iloc[i]['NUMBER']+","+df.iloc[i]['CONTENT']+'\n')
        f_3.close()


    if str(df.iloc[i]['NUMBER']) in str(clients_cleaned_4):
        results_4.append(df.iloc[i]['CONTENT'])
        f_4 = open("results_4.txt", "a", encoding="utf8")
        f_4.write(df.iloc[i]['NUMBER']+","+df.iloc[i]['CONTENT']+'\n')
        f_4.close()

    # if str(df.iloc[i]['NUMBER']) in str(marked_1):
    #     results_marked_1.append(df.iloc[i]['CONTENT'])
    #     f_4 = open("results_marked_1.txt", "a", encoding="utf8")
    #     f_4.write(df.iloc[i]['CONTENT']+'\n')
    #     f_4.close()

# df=open("results_2.txt", encoding="utf8").read()
# print(type(df))
# df = df.replace("\n", "")
# df = df.replace("n'", "")
# df = df.replace("norberto", "")
# df = df.replace(".txt", "")
# df = df.replace(".txt", "")
# df = df.replace("que", "")
# df = df.replace("de", "")
# df = df.replace("y", "")
# wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
#                             random_state= 1,
#                             stopwords = stop_words_sp,
#                             background_color = 'white',
#                             width = 1200,
#                             height = 1000,
#                             ).generate(df)

# plt.imshow(wordcloud, interpolation='bilInear')
# plt.axis('off')
# plt.show()