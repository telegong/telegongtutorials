# RPS Revit uidoc
# A. rvts in folder
    ## 1. select Folder by Browser
    ## 2. rvt fileList1 in folder containing subdir.
    ## 3. rvt fileList2 in this folder not containing subdir.
    ## 4. TransmissionData(rvt in fileList2)
# B. rvtLinks in rvt
    # 5. allExternalFileReferenceIds(rvt)
    # 6. IsNotRvtLinks in folder
    # 7. SetDesiredReferenceData.shouldLoad = False
# C. TransmissionData.Write


# A. rvts in folder
    ## 1. select Folder by Browser
import clr
import os, os.path
import shutil
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
mpath = ""
folderdialog = FolderBrowserDialog()
folderdialog.Description="BIM Model 폴더를 선택하세요."
print folderdialog.Description
if folderdialog.ShowDialog() == DialogResult.OK :
	mpath = folderdialog.SelectedPath
print mpath
print 
    ## 1.1 savelocation
# newProjectPath = "" #os.path.join("D:\\","BIM","CD90")
# folderdialog = FolderBrowserDialog()
# folderdialog.Description="새로 저장할 BIM Model 폴더를 선택하세요."
# print folderdialog.Description
# if folderdialog.ShowDialog() == DialogResult.OK :
# 	newProjectPath = folderdialog.SelectedPath
# print newProjectPath
# print 
# spath = newProjectPath
# # spath = os.path.join(mpath,"transmittedFiles")
# if not os.path.exists(spath):
#     os.makedirs(spath)


    ## 2. rvt fileList1 in folder containing subdir.
    ## 3. rvt fileList2 in this folder not containing subdir.
rvtfiles = []
rvts = []
for r,d,f in os.walk(mpath):
    if r==mpath:
        for rvt in f :
            if rvt.lower().endswith('.rvt'):
                rvtfiles.append(os.path.join(r,rvt)) # Full Path
                rvts.append(rvt)

    ## 4. TransmissionData(rvt in fileList2)
for rvtname, rvt in zip(rvts, rvtfiles):
    print
    print "'", rvtname, ",'",BasicFileInfo.Extract(rvt).CentralPath
    # print "'", rvtname, ",'",BasicFileInfo.Extract("프로젝트 All.rvt").CentralPath