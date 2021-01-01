from json import loads,dumps
import time
import os
temp_d={}
extra=[]
l={}
print('\n\n If this is the first time press y or you will be overwriting all the datas\n\nto continue with old data press any key to start\n\n')
ans=input('ans\n')
#Creating the datafile for the first time
if (ans=='y'):
    
    sheet=open('database.txt','w')
    sheet.close()
c='database.txt'
stop=os.stat(c).st_size

    

if stop!=0:
    
    with open (c,'r') as re:
        
        kc=re.read()
        uf=loads(kc)
        extra=uf.keys()

#functions
def Create(ke,va):
    if ke not in extra:
        
        temp_d[ke]=va
        print('\n\nyour key has been stored temporarily\n\nPress 4 to save it permanently\n')
    else:
        print('\n\n sorry\n, the key already exists')
            


def Read(ke):
    with open (c,'r') as re:
        file=re.read()
        p=loads(file)
        if ke not in p.keys():
            print('The key does not exists')
        else:

            str1=str(ke)+':'+str(p[ke])
            return str1

            
    
def Delete(ke):
    with open (c,'r') as de:
        file=de.read()
        p=loads(file)
        if ke not in p.keys():
            print('The key does not exists')
        else:
            del p[ke]
            return p
                


def pretty(obj):
    return dumps(obj,indent=2)



 #to run   
print('Welcome to the database\n\nPlease save the keys, before checking if it already exists\n\n')
v=1
while((1024*1024*1024)>stop):
    
    while(v!=0):
        print('\n\npress 1 to create a key \n\n press 2 to read/display a key \n\n press 3 to delete a key and update the data\n\n press 4 to save the data after all the inputs \n\n press 5 to view the whole data\n\n  press 0 to exit  \n\n')
        i=int(input('\npress now'))
        value={}
    
        if (i==1):
        

            key=input('enter key for input')
            value=input('enter value in json format')
            Create(key,value)
            

        if (i==2):

            key=input('Give the key')
            print(Read(key))

        if (i==3):

            key=input('Enter the key you want to delete from Database')
            new=Delete(key)
            z=dumps(new)
            with open (c,'w') as f:
                f.write(z)
            print('\n\n\nYour key has been deleted')

        if (i==0):

            v=0
            print('thank you! good bye')

#file saving
        if (i==4):
            if stop>0:
                
                with open (c,'r') as x:
                    lol=x.read()
                    l=loads(lol)
                    temp_d.update(l)
                    print('you saved all the datas into the txt file,thank you')
                    p=dumps(temp_d)
                    l.clear()
                with open (c,'w') as m:
                    m.write(p)
                    temp_d.clear()
            else:
                pod=dumps(temp_d)
                l.clear()
                with open (c,'w') as huh:
                    huh.write(pod)
                    temp_d.clear()
        if (i==5):
            try:
                
                l.clear()
                with open(c,'r') as f:
                    file=f.read()
                    l=loads(file)
                    x=pretty(l)
                    print(x)
            except Exception as e:
                print(e)


    
    

            
               
              
            

        



