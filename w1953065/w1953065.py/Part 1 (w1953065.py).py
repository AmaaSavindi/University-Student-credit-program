#for histogram
#P=Progress, T=Progress(module trailer), R=Do not progress(module retriever), E=Exclude
P=0
T=0
R=0
E=0


#function defining
def Progression(List):
    global P,T,R,E
    ListProgress = [[120,0,0]]
    ListProgressMT = [[100,20,0],[100,0,20]]
    ListDoNotProgressMR = [[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[20,100,0],[20,80,20],[20,60,40],[20,40,60],[0,120,0],[0,80,40],[0,60,60]]
    ListExclude = [[40,0,80],[20,20,80],[20,0,100],[0,40,80],[0,20,100],[0,0,120]]
    if ListProgress.count(List) == 1 :
        print('Progress')
        P=P+1
    elif ListProgressMT.count(List) == 1 :
        print('Progress(module trailer)')
        T=T+1
    elif ListDoNotProgressMR.count(List) == 1 :
        print('Do Not Progress-module retriever')
        R=R+1
    elif ListExclude.count(List) == 1 :
        print('Exclude')
        E=E+1

CreditRange = [0,20,40,60,80,100,120]

while True :
    #taking inputs(credits)
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
    
    creditList = [int(p),int(d),int(f)]

    #checking total
    if int(p)+int(d)+int(f) != 120 :
        print('Total incorrect')
        cnd = input("\n\nWould you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
        if cnd =='q' :
            break
        else :
            continue
    else :
        Progression(creditList)
        

    #asking whether the repitition is needed
    cnd = input("\n\nWould you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
    if cnd =='q' :
        break
    else :
        continue


#histogram
print('\n---------------------------------------------------------')
print('Histogram\n','Progress',P,':','*'*P,'\n','Trailer',T,':','*'*T,'\n','Retriever',R,':','*'*R,'\n','Excluded',E,':','*'*E,'\n','\n',P+T+R+E,'outcomes in total.')
print('\n---------------------------------------------------------')
    
    
    
    















    
    
