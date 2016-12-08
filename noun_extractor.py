# noun_extractor.py
# script to get nouns from text 

from nltk.tag.stanford import StanfordPOSTagger
from nltk import sent_tokenize
import csv
from DistUpgrade.DistUpgradeViewText import readline


def extractor():
    st = StanfordPOSTagger('../stanford-postagger-full-2015-12-09/models/english-bidirectional-distsim.tagger', '../stanford-postagger-full-2015-12-09/stanford-postagger-3.6.0.jar')
    nouns = []
    pnouns = []
    i = 0

    with open('../data/scraped_text_NYT.txt', 'r', encoding='utf-8') as inputFile:
        comment = inputFile.readline()
        while comment != "":             
            sentences = sent_tokenize(comment, 'english')
            
            for sent in sentences:
                if(sent.strip() ==""):
                    continue
                pos_tags = st.tag(sent.split())
                for pos_tag in pos_tags:
                    if(pos_tag[1] == 'NN' or pos_tag[1] == 'NNS'):
                        nouns = nouns + [pos_tag[0]]
                    elif(pos_tag[1] == 'NNP' or pos_tag[1] == 'NNPS'):
                        pnouns = pnouns + [pos_tag[0]]
            i = i+1
            print(i)
            print(comment)
            comment = inputFile.readline()
    
    outFile = open('../data/nouns_scraped_text_NYT.txt','a')
    outFile.write('NOUNS:\n')
    for noun in nouns:
        outFile.write(noun + "\n")
    outFile.write('\n\nPNOUNS:\n')
    for pnoun in pnouns:
        outFile.write(pnoun + '\n')
    
extractor()
