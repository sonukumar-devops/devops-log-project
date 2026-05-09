import time
from datetime import datetime

logs = ["ERROR: File /tmp/xyx.txt not Found",
 "WARNING: Failed Login attempt for user root",
 "MESSAGE: deprecated value in sshd_config",
 "ERROR: Out of memory",
 "WARNING: 'tmhook' module taints kernel",
 "ERROR: Splunkd Can't connect to deployment server",
 "ERROR: Password expired for user sonu"
 ]

try:
    while True:
        with open("app.log", "a") as f:
            for log in logs:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{now} {log}\n")
                f.flush()
                print(f"Writing log:{log}", flush=True)
                time.sleep(3)
except Exception as e:
    print(f"Some error occured: ({e})")
