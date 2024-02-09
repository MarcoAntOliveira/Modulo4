from time import sleep
from threading import Thread

def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=(5, 'hello world1'))    
t1.start()
#t1.join()
'''t2 = Thread(target=vai_demorar, args=(1, 'hello world2'))    
t2.start()

t3 = Thread(target=vai_demorar, args=(9, 'hello world3'))    
t3.start()

for i in range(10):
    print(i)
    sleep(.5)
'''
while t1.is_alive():
    print('Esperando a thread')
    sleep(2)
print("Thread acabou")