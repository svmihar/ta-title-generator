import os 
import time

os.system('python pusher.py')

for _ in range(500):
    time.sleep(1800)
    os.system('python pusher.py')
    print(f'hour {_}')