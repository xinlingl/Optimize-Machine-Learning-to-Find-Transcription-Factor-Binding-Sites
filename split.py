import numpy as np
import random
def ReadFASTA(filename):
    fp=open(filename, 'r')
    Sequences={}
    tmpname=""
    tmpseq=""
    for line in fp:
        if line[0]==">":
            if len(tmpseq)!=0:
                Sequences[tmpname]=tmpseq
            tmpname=line.strip().split()[0][1:]
            tmpseq=""
        else:
            tmpseq+=line.strip()
    Sequences[tmpname]=tmpseq
    fp.close()
    return Sequences

def complement_strand(oriseq):
    seq = ''
    for i in oriseq:
         if i == 'A':
             seq = seq + 'T'
         elif i == 'T':
             seq = seq + 'A'
         elif i == 'C':
             seq = seq + 'G'
         elif i == 'G':
             seq = seq + 'C'
         elif i == 'a':
             seq = seq + 't'
         elif i == 't':
             seq = seq + 'a'
         elif i == 'c':
             seq = seq + 'g'
         elif i == 'g':
             seq = seq + 'c'
    return seq         
    
def get_perf_dataset(rawfile):
     raw_sequences = ReadFASTA(rawfile)
     #sequences = [0 for i in range(0,15)]
     f_train = open('human_perf_trainset.txt','w')
     f_val = open('human_perf_validation.txt','w')
     f_test = open('human_perf_test.txt','w')
     index = 0
     for key in raw_sequences.keys():
         a = random.randrange(0,35)
         b = random.randrange(65,80)
         c = random.randrange(2)
         seq = raw_sequences[key]
         if index < 19000:        
             f_train.write(seq[50:65] + '\n')
             index = index + 1
         elif index >= 19000 and index < 20000:
             f_val.write(seq[50:65] + '\n')
             index = index + 1
         elif index >= 2000:
             f_test.write(seq[50:65] + '\n')
             index = index + 1
         
         if index < 19000:
             if c == 1:
                f_train.write(str(seq[a: a + 15]) + '\n')
                index = index + 1
             else: 
                f_train.write(str(seq[b: b + 15]) + '\n')
                index = index + 1
         elif index >= 19000 and index < 20000:
             if c == 1:
                f_val.write(str(seq[a: a + 15]) + '\n')
                index = index + 1
             else: 
                f_val.write(str(seq[b: b + 15]) + '\n')
                index = index + 1
         else:
             if c == 1:
                f_test.write(str(seq[a: a + 15]) + '\n')
                index = index + 1
             else: 
                f_test.write(str(seq[b: b + 15]) + '\n')
                index = index + 1
             

        
def get_imperf_dataset(rawfile):  
    raw_sequences = ReadFASTA(rawfile)
    index = 0
    f_train = open('human_imperf_trainset.txt','w')
    f_val = open('human_imperf_validation.txt','w')
    f_test = open('human_imperf_test.txt','w')
    
    for key in raw_sequences.keys():
        a = random.randrange(0,80)
        while a == 50:
            a = random.randrange(0,80)
        seq = raw_sequences[key]
        if index < 19000:        
             f_train.write(seq[50:65] + '\n')
             index = index + 1
        elif index >= 19000 and index < 20000:
             f_val.write(seq[50:65] + '\n')
             index = index + 1
        else:
             f_test.write(seq[50:65] + '\n')
             index = index + 1
        
        
        if index < 19000:
            f_train.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
           
        elif index >= 19000 and index < 20000:
            f_val.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
        else:
            f_test.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
    
    index = 0 
    for key in raw_sequences.keys():
        a = random.randrange(0,80)
        while a == 35:
            a = random.randrange(0,80)
        seq = raw_sequences[key]
        if index < 9500:
            f_train.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
        elif index >= 9500 and index < 10000:
            f_val.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
        else:
            f_test.write(str(seq[a: a + 15]) + '\n')
            index = index + 1
        


if __name__=="__main__":

    get_imperf_dataset('MA0007.2.sites')
    get_perf_dataset('MA0007.2.sites')
    
    