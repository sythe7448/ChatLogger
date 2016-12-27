awesome = open('C:/Users/Sythe/Desktop/awesome.txt', 'r')

import time
def follow(awesome):
    awesome.seek(0,2)      # Go to the end of the file
    while True:
         line = awesome.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         yield line

chatreader = follow(awesome)

for line in chatreader:
    print line,