import sys
import subprocess
import os

rcc = os.path.join(os.path.dirname(sys.executable), "pyside2-rcc.exe")
uic = os.path.join(os.path.dirname(sys.executable), "pyside2-uic.exe")

in_file = os.path.abspath("translator.ui")
out_file = os.path.abspath(os.path.join("gen", "ui_translator.py"))

subprocess.call([uic, in_file, '-o', out_file], shell=True)
print(rcc)
subprocess.call([rcc, '-o', in_file, out_file])