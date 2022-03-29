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

### Functions
```py
active_count() # The number of threads that are currently alive 
current_thread() # Thread object for the calling thread
enumerate() # list of all therad object currently alive 
stack_size([size]) # stack size in bytes
```

## Processing
- involve on multiple cores