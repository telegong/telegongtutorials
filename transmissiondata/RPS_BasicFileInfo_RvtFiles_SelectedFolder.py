"""
BasicFileInfo extracted from rvts at a folder selected
"""
import clr
import os, os.path
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *

# Select a folder
mpath = ""
folderdialog = FolderBrowserDialog()
folderdialog.Description="BIM Model 폴더를 선택하세요."
print folderdialog.Description
if folderdialog.ShowDialog() == DialogResult.OK :
	mpath = folderdialog.SelectedPath
print mpath
print 

# Rvt files in a folder
rvtsFullPath = []
rvtsName = []
for r,d,f in os.walk(mpath):
    if r==mpath:  # root folder only
        for rvt in f :
            if rvt.lower().endswith('.rvt'): # rvt only
                rvtsFullPath.append(os.path.join(r,rvt)) # Full Path
                rvtsName.append(rvt) # File Name

# BasicFileInfo of rvt files
rvtsBasicFileInfo = []

def rvtBasicFileInfo(rvt):
    basicFileInfo = []
    bfi = BasicFileInfo.Extract(rvt)
    print bfi.CentralPath
    for i in dir(bfi):
        if "__" in i: continue
        info = str("%s : %s"%(i,eval("bfi.%s"%i)))
        if "built-in" in info: continue
        basicFileInfo.append(info)
    return basicFileInfo
    
for rvt in rvtsFullPath:
    rvtsBasicFileInfo.append(rvtBasicFileInfo(rvt))

for rvtinfo in rvtsBasicFileInfo:
    print
    for i in rvtinfo: print i


