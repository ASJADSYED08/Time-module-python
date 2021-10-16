import time
initial=time.time()
print(initial)
k=0
while(k<10):
    print("asjad")
    time.sleep(3)
    k=k+1
print("WHILE LOOP TIME",time.time()-initial)    

initial2=time.time()
for i in range(10):
    print("ASJAD")
print("FOR LOOP TIME",time.time()-initial2)    

localtime=time.asctime(time.localtime(time.time()))
print(localtime)    