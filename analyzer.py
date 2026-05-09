import time
import os

log_file = "app.log"

print("Analyzer started...", flush=True)

try:
    while True:
        if not os.path.exists(log_file):
            print("Waiting for log file...", flush=True)
            time.sleep(2)
            continue

        with open(log_file, "r") as f:
            print("Reading logs...", flush=True)

            f.seek(0, os.SEEK_END)   # go to end

            while True:
                line = f.readline()

                if line:
                    if "ERROR" in line:
                        print(f"ALERT: {line.strip()}", flush=True)
                else:
                    time.sleep(1)

except Exception as e:
    print(f"Some error occurred: {e}", flush=True)
