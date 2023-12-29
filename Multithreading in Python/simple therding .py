# simple program 

import threading
import time 

#indicate some tasking being done 

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
 
func(4)
func(2)
func(1)