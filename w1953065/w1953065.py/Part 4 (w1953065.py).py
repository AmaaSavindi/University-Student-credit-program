#Basic
P = T = R = E = 0
listP = []
listT = []
listR = []
listE = []
CreditRange = [0,20,40,60,80,100,120]
IDdictionary = {
    }
ListProgress = [[120,0,0]]
ListProgressMT = [[100,20,0],[100,0,20]]
ListDoNotProgressMR = [[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[20,100,0],[20,80,20],[20,60,40],[20,40,60],[0,120,0],[0,80,40],[0,60,60]]
ListExclude = [[40,0,80],[20,20,80],[20,0,100],[0,40,80],[0,20,100],[0,0,120]]



#function defining

##################################
#def progression status
def Progression(List):
    global P,T,R,E,listP,listR,listT,listE,ListProgress,ListProgressMT,ListDoNotProgressMR,ListExclude
    if ListProgress.count(List) == 1 :
        P=P+1
        listP.append(List)
        fileP = open('fileP.txt','a')
        fileP.write(str(List[0])+', '+str(List[1])+', '+str(List[2])+'\n')
        fileP.close()
        return 'Progress'
        
    elif ListProgressMT.count(List) == 1 :
        T=T+1
        listT.append(List)
        fileT = open('fileT.txt','a')
        fileT.write(str(List[0])+', '+str(List[1])+', '+str(List[2])+'\n')
        fileT.close()
        return 'Progress(module trailer)'
        
    elif ListDoNotProgressMR.count(List) == 1 :
        R=R+1
        listR.append(List)
        fileR = open('fileR.txt','a')
        fileR.write(str(List[0])+', '+str(List[1])+', '+str(List[2])+'\n')
        fileR.close()
        return 'Do Not Progress(module retriever)'
        
    elif ListExclude.count(List) == 1 :
        E=E+1
        listE.append(List)
        fileE = open('fileE.txt','a')
        fileE.write(str(List[0])+', '+str(List[1])+', '+str(List[2])+'\n')
        fileE.close()
        return 'Exclude'

#######################################
#def list retrieve    
def ProgressionRetrieve(LP,LT,LR,LE) :
    n=len(LP)
    for i in range(n) :
        print('Progress - ',LP[i][0],',',LP[i][1],',',LP[i][2])

    n=len(LT)
    for i in range(n) :
        print('Progress (module trailer) - ',LT[i][0],',',LT[i][1],',',LT[i][2])

    n=len(LR)
    for i in range(n) :
        print('Module retriever - ',LR[i][0],',',LR[i][1],',',LR[i][2])

    n=len(LE)
    for i in range(n) :
        print('Exclude - ',LE[i][0],',',LE[i][1],',',LE[i][2])

##########################################
#def fileHandle
def FileHandle():
    P = open('fileP.txt','r')
    T = open('fileT.txt','r')
    R = open('fileR.txt','r')
    E = open('fileE.txt','r')
    
    while True :
        line = P.readline()
        if len(line) == 0 :
            break
        else :
            print('Progress -',line)
    

    while True :
        line = T.readline()
        if len(line) == 0 :
            break
        else :
            print('Progress (module trailer) -',line)
    
 
    while True :
        line = R.readline()
        if len(line) == 0 :
            break
        else :
            print('Module retriever -',line)
    
        
    while True :
        line = E.readline()
        if len(line) == 0 :
            break
        else :
            print('Exclude -',line)

    P.close()
    T.close()
    R.close()
    E.close()

##########################################
#progression status
def status(List) :
    global ListProgress,ListProgressMT,ListDoNotProgressMR,ListExclude
    if ListProgress.count(List) == 1 :
        return 'Progress'
        
    elif ListProgressMT.count(List) == 1 :
        return 'Progress(module trailer)'
        
    elif ListDoNotProgressMR.count(List) == 1 :
        return 'Do Not Progress(module retriever)'
        
    elif ListExclude.count(List) == 1 :
        return 'Exclude'

##########################################
#entering items for dictionary
def dictionary():
    global ID,p,d,f,IDdictionary
    value = status(creditList)+' - '+str(p)+', '+str(d)+', '+str(f)
    IDdictionary[ID] = value

##########################################
#retrieving items from dictionary
def ReadDict(IDdictionary) :
    key_list = list(IDdictionary.keys())
    value_list = list(IDdictionary.values())
    for i in range(len(key_list)) :
        print(key_list[i]+' : '+value_list[i])


        
#Process
fileP = open('fileP.txt','w')
fileT = open('fileT.txt','w')
fileR = open('fileR.txt','w')
fileE = open('fileE.txt','w')
while True :
    #taking inputs(credits)
    ID = input('\nEnter the student ID : ')
    
    p = input('\nPlease enter your credit at pass: ')
    
    try :
        int(p)
    except :
        print('Integer required')
        continue
    if CreditRange.count(int(p)) == 0:
        print('Out of range')
        continue
    
    d = input('Please enter your credit at defer: ')
    
    try :
        int(d)
    except :
        print('Integer required')
        continue
    if CreditRange.count(int(d)) == 0:
        print('Out of range')
        continue
    
    f = input('Please enter your credit at fail: ')
    
    try :
        int(f)
    except :
        print('Integer required')
        continue
    if CreditRange.count(int(f)) == 0:
        print('Out of range')
        continue
    
    #checking total
    if int(p)+int(d)+int(f) != 120 :
        print('Total incorrect')
        continue
    
    creditList = [int(p),int(d),int(f)]
    
    print(Progression(creditList))
    dictionary()

    #asking whether the repitition is needed
    cnd = input("\n\nWould you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
    if cnd =='q' :
        break
    elif cnd =='y' :
        continue


fileP.close()
fileT.close()
fileR.close()
fileE.close()

############################################
#histogram
print('\n---------------------------------------------------------')
print('Histogram\n','Progress',P,':','*'*P,'\n','Trailer',T,':','*'*T,'\n','Retriever',R,':','*'*R,'\n','Excluded',E,':','*'*E,'\n','\n',P+T+R+E,'outcomes in total.\n')
print('\n---------------------------------------------------------')

#retrieving from the list
print('Part 2:\n')
print(ProgressionRetrieve(listP,listT,listR,listE))
print('\n---------------------------------------------------------')


#retrieving from the file
print('\nPart 3:\n')
FileHandle()
print('\n---------------------------------------------------------')

#retrieving from the dictionary
print('\nPart 4:\n')
ReadDict(IDdictionary)












    
    
