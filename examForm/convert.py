import subprocess

#uiFile = input("Enter ui file name in full\n")

print('Running')

p = subprocess.Popen("pyuic5.bat -x deisgn.ui -o mainDesign.py")

stdout,stderr = p.communicate()

print('Finished')
