#!/usr/bin/env python
# coding: utf-8

# In[25]:


from gensim.models.doc2vec import Doc2Vec
from LinkedIn import linkedin_crawler
from datetime import datetime
from ckiptagger import WS
import pandas as pd
import numpy as np
import logging
import getpass
import re
import os


def recommendation():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #模型讀取
    model = Doc2Vec.load("Doc2Vec_104_jobs.model")
  
    #CKIP斷詞資料
    #os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
    #ws = WS('data', disable_cuda=False)
    ws = WS('data') #有使用GPU / Tensorflow-GPU再註解掉這行，啟用上面兩行
    
    data_forName = pd.read_csv('s104_textCombined_seg_0730.csv')
    jobName_list = data_forName['jobName']
    jobDesc_list = data_forName['jobDescription']
    
    #消除符號
    def regularize_(target):
        return re.sub("[0-9【】◎★/◆※⦿\%\[\]\-\"\“\”\(\)（）{}\'=●▲▼《》○]", "", target).replace('\r',' ').replace('\n',' ')

    #定義斷詞功能_這邊是改版給單句用的
    def word_seg(sentence_list): #輸入包含多斷文章(句子)的list
        sepped = ws([sentence_list],
                    sentence_segmentation=True,
                    segment_delimiter_set={'?', '？', '!', '！', '。', ',','，', ';', ':', '、','：','\\n','\\r','.'})
        return sepped[0]

    #比較兩個斷詞組的相似性
    def compare_similarity(p1, p2):
        d2v_similarity = np.dot(model.infer_vector(p1), model.infer_vector(p2)) / (np.linalg.norm(model.infer_vector(p1))*np.linalg.norm(model.infer_vector(p2)))
        return d2v_similarity

    #輸入履歷資料並推薦
    while True:
        
        print('''
1. 以隨機履歷進行推薦功能展示，請輸入1按Enter，並輸入自身LinkedIn網址、帳號及密碼(執行LinkedIn爬蟲用，他們管得嚴)。
2. 欲輸入自身資訊配對工作，請輸入2按Enter，並輸入自身履歷/自傳等描述。範例：

我樂天開朗不怕挑戰、我愛python、java等等的程式碼。我年輕、有新鮮的肝。

        ''')
        
        query = input('請選1或2，或輸入其他字元結束程式: ')
        
        if query == "1":
            url = input('Write your LinkedIn URL here: ')
            uname = input('Write your username here: ')
            pword = getpass.getpass('Write your password here: ')
            doc_origin = linkedin_crawler(url, uname, pword)

        elif query == "2":
            doc_origin = input('Write your resume here: ')
        
        else:
            break
        
        #目標履歷去雜質、斷字斷詞
        doc = regularize_(doc_origin)
        doc = word_seg(doc)

        #輸出目標履歷資料
        print('履歷內容： %s' % (doc_origin))
        print('--------------------------------------------')

        #套用模型到目標履歷詞組
        inferred_vector = model.infer_vector(doc)
        #取得以相似度排列的職缺list
        sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
        #輸出推薦
        for label, index in [('MOST', 0), ('Second', 1), ('Third', 2)]:
            print(u'%s %s %s:\n «%s»\n' % (jobName_list[sims[index][0]], label, sims[index], jobDesc_list[sims[index][0]]))



if __name__ == '__main__':
    
    recommendation()

