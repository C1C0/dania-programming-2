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