# Multithreading and Multiprocessing

## Threading
- doesn't involve on multiple cores

```py
import threading
t1 = thrading.Thread(target=METHOD, args(PARAMETER1, ))
```

### Starting
```py
t1.start()
```

### Joining
```py
t1.join(<optional: Timeout>)
```

### Concurrent.futures
```py
import concurrent.futures
...
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(callback_reference, ...*params)

    # to get return value
    f1.result()

    ...
    # when working with multiple (X) threads
    results = [executor.submit(do_something, ...*params) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
```
- can return values from thread

#### Using executor.map()
```py
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]

    # runs threads and adds results to the list of "results"
    results = executor.map(slepp_for_sec, secs)

    for result in results:
        print(result)
```

### Functions
```py
active_count() # The number of threads that are currently alive 
current_thread() # Thread object for the calling thread
enumerate() # list of all therad object currently alive 
stack_size([size]) # stack size in bytes
```

### Questions
- Does it have something like Mutexes in `C` ? So you can LOCK / UNLOCK variable before being accessed by thread ?

## Processing
- involve on multiple cores