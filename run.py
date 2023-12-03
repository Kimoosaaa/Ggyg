import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('@MHDN313bot.py')#2023-12-03 09:53:14.021768

scripts.append('6788988673.py')#2023-12-03 09:53:14.021768

scripts.append('6023882251.py')#2023-11-25 23:54:37.786794

scripts.append('6830992881.py')#2023-11-25 23:54:37.786794

scripts.append('6853622271.py')#2023-11-25 23:54:37.786794

scripts.append('6919960852.py')#2023-11-25 23:54:37.786794

scripts.append('6505523464.py')#2023-11-25 23:54:37.786794

scripts.append('6919960852.py')#2023-11-25 23:54:37.786794

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

