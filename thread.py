import threading
import time

a = {}

data = raw_input("Please input some integers using space:\n")
data = data.split()
s = 0
for i in data:
    s += float(i)

##calculate the max of sequence
def max_number():
    time.sleep(1)
    print 'the max of number is :', max(data)


t = threading.Thread(target=max_number)
t.daemon = True
t.run()


def he():
    print 'hello'

##calculate the min of sequence
def min_number():
    # time.sleep(2)
    print 'the min of number is :', min(data)


t = threading.Thread(target=min_number)
t.daemon = True
t.start()

##calculate the average of nubmers
def aver_number():
    # time.sleep(3)
    print 'the average of number is :', s / len(data)


t = threading.Thread(target=aver_number)
t.daemon = True
t.start()

