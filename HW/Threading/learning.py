import threading, time

def func():
    print("ran")
    time.sleep(1)
    print("done")
    
t1 = threading.Thread(target=func)

t1.start()

if __name__ == '__main__':
    print(threading.active_count())