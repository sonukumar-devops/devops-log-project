import time
import os
import sys

log_file = "/logs/app.log"

print("Analyzer started...", flush=True)

timeout = 15
start_time = time.time()

try:
    while True:

        # ⏱ Stop after timeout
        if time.time() - start_time > timeout:
            print("No ERROR found. Exiting cleanly.", flush=True)
            sys.exit(0)

        if not os.path.exists(log_file):
            print("Waiting for log file...", flush=True)
            time.sleep(1)
            continue

        with open(log_file, "r") as f:
            print("Reading logs...", flush=True)

            # ✅ READ FULL FILE (NO SEEK)
            lines = f.readlines()

            for line in lines:
                if "ERROR" in line:
                    print(f"ALERT: {line.strip()}", flush=True)
                    sys.exit(1)

        time.sleep(1)

except Exception as e:
    print(f"Some error occurred: {e}", flush=True)
    sys.exit(1)
