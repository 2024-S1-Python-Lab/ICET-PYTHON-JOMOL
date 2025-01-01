f1=open('jomol','r')
f2=open('jomol2','w')
cont=f1.readlines()
for i in range(0,len(cont)):
        if(i%2==0):
            f2.write(cont[i])
        else:
            pass
f2.close()
        
            
