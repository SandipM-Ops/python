import time

wait_time=1
max_tries=5
attempts=0

while attempts<max_tries:
    print("attempts ", attempts+1,"-wait time is",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
    