# 1
def first_exercise():
    import time 
    import random 

    def calc_algorithm1(list): 
        print("Calculating result 1")
        for i in list:
            time.sleep(0.2)
            print("Result 1", i*i*i+i-i*i)

    def calc_algorithm2(list): 
        print("Calculating result 2")
        for i in list:
            time.sleep(0.2)
            print("Result 2", i*i*i-i+i*i)


    array = random.sample(range(0,100),50)

    t = time.time()
    calc_algorithm1(array)
    calc_algorithm2(array)

    print("Time used", time.time()-t)
    print("Jobs done! ")  
    
#
def second_exercise():
    import time 
    import random 
    import threading 

    def calc_algorithm1(list): 
        print("Calculating result 1")
        for i in list:
            time.sleep(0.2)
            print("Result 1", i*i*i+i-i*i)

    def calc_algorithm2(list): 
        print("Calculating result 2")
        for i in list:
            time.sleep(0.2)
            print("Result 2", i*i*i-i+i*i)


    array = random.sample(range(0,100),50)

    t = time.time()
    t1 = threading.Thread(target=calc_algorithm1, args=(array,))
    t2 = threading.Thread(target=calc_algorithm2, args=(array,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Time used", time.time()-t)
    print("Jobs done! ")  

# 3
def third_exercise(maxFactorials: int):
    import threading
    
    def factorial(num: int):
        return num * (factorial(num - 1) if num - 1 > 0 else 1)
    
    def callFactorial(num: int):
        print("Factorial to calculate:", num)
        print(f"Factorial of {num} is {factorial(num)}")
    
    factorialsToCalculate = list(range(1, maxFactorials + 1))
    
    threads: list = []
    
    for num in factorialsToCalculate:
        t = threading.Thread(target=callFactorial, args=(num, ))
        threads.append(t)
        t.start()
        t.join()
        
# 4
def fourth_exercise_point_one(maxFactorialsGroups: int):
    import time
    
    t1 = time.time()
    for i in range(1, maxFactorialsGroups + 1):
        third_exercise(i)
    
    print("time needed: ", time.time() - t1)
    
def fourth_exercise_with_multiprocessing(maxFactorialsGroups: int):
    import time
    import multiprocessing

    t1 = time.time()
    processes: list = []
    
    for i in range(1, maxFactorialsGroups + 1):
        p = multiprocessing.Process(target=third_exercise, args=(i, ))
        processes.append(p)
        p.start()
        p.join()
    
    print("time needed: ", time.time() - t1)
    
    
if __name__ == '__main__':
    # first_exercise()
    # second_exercise()
    # third_exercise(8)
    fourth_exercise_point_one(250)
    # fourth_exercise_with_multiprocessing(250)