import time
import os
import sys

log_file = "/logs/app.log"

print("Analyzer started...", flush=True)

try:
    timeout = 10   # seconds
    start_time = time.time()

    while True:
        # ⏱️ Stop after timeout
        if time.time() - start_time > timeout:
            print("No ERROR found. Exiting cleanly.", flush=True)
            sys.exit(0)

        if not os.path.exists(log_file):
            print("Waiting for log file...", flush=True)
            time.sleep(1)
            continue

        with open(log_file, "r") as f:
            print("Reading logs...", flush=True)
            #f.seek(0, os.SEEK_END)

            while True:
                if time.time() - start_time > timeout:
                    print("No ERROR found. Exiting cleanly.", flush=True)
                    sys.exit(0)

                line = f.readline()

                if line:
                    if "ERROR" in line:
                        print(f"ALERT: {line.strip()}", flush=True)
                        sys.exit(1)   # ❌ FAIL
                else:
                    time.sleep(1)

except Exception as e:
    print(f"Some error occurred: {e}", flush=True)
    sys.exit(1)
