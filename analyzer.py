import time
import os
import sys

log_file = "/logs/app.log"

print("Analyzer started...", flush=True)

timeout = 15
start_time = time.time()

while True:
    if time.time() - start_time > timeout:
        print("No ERROR found. Exiting cleanly.")
        sys.exit(0)

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            for line in f:
                if "ERROR" in line:
                    print(f"ALERT: {line.strip()}")
                    sys.exit(1)

    time.sleep(1)
