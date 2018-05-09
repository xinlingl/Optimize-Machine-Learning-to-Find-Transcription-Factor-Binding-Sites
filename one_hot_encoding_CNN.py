import numpy as np

def get_list1(filename):
    
    dictionary={'A':[1,0,0,0],'T':[0,1,0,0],'C':[0,0,1,0],'G':[0,0,0,1],\
                'a':[1,0,0,0],'t':[0,1,0,0],'c':[0,0,1,0],'g':[0,0,0,1]}
    #print("dictionary "+str(dictionary))
    #f = open('C:/Python27/MA0007.2.sites', 'r')
    f_tr = filename
    sequences=np.loadtxt(f_tr,dtype = str)
    #print(sequences)  
    listl=[[[[0 for i in range(4)] for j in range(5)]for k in range(3)]for l in range(len(sequences))]
    #print("newsequences[0] "+str(newsequences[0]))
    #sequences=sequences.split()
    #print("length of sequences "+str(len(sequences)))
    #print(newsequences[0][50:65])
    #print(np.shape(listl))
    for i in range(len(sequences)):
        index = 0
        for j in range(len(listl[0])):
            for k in range(len(listl[0][0])):
                #print(index)
                listl[i][j][k] = dictionary[sequences[i][index]]
                index = index + 1
        index = 0 
    listl = np.array(listl)
    return listl

def get_list2(filename):
    dictionary={'A':[1,0,0,0],'T':[0,1,0,0],'C':[0,0,1,0],'G':[0,0,0,1],\
                'a':[1,0,0,0],'t':[0,1,0,0],'c':[0,0,1,0],'g':[0,0,0,1]}
    #print("dictionary "+str(dictionary))
    #f = open('C:/Python27/MA0007.2.sites', 'r')
    f_tr = filename
    f_sequence = open(filename,'r')
    sequences = f_sequence.readlines()
    #print(sequences)
    for i in range(len(sequences)):
        sequences[i] = sequences[i].strip('\n')
        
    listl = [[] for j in range(len(sequences))]
    for i in range(len(sequences)):
        count = 0
        for index in range(0,len(sequences[i])):
            '''
            if sequences[i][index]=='C' or sequences[i][index]=='G' or \
            sequences[i][index]=='c' or sequences[i][index]=='g':
                count=count+1
            '''    
            #percentage=float(count)/float(len(sequences[i]))
            
            listl[i] = listl[i] + dictionary[sequences[i][index]]
            
        #listl[i].append(percentage)
    #print(listl)
    listl = np.array(listl)
    return listl


    
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

#if __name__ == "__main__":
#	listl = revised_get_list('MA0007.2.sites')