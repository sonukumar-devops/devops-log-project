import time
import os


log_file="/logs/app.log"


for i in range(10):  #run only limited times
    with open(log_file, "a") as f:
        f.write("ERROR: File /tmp/xyz.txt not Found\n")
        print("Writing log: ERROR generated", flush=True)

        time.sleep(1)


print("Generator finished")
