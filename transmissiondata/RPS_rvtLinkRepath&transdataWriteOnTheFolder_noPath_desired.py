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
newProjectPath = "" #os.path.join("D:\\","BIM","CD90")
folderdialog = FolderBrowserDialog()
folderdialog.Description="새로 저장할 BIM Model 폴더를 선택하세요."
print folderdialog.Description
if folderdialog.ShowDialog() == DialogResult.OK :
	newProjectPath = folderdialog.SelectedPath
print newProjectPath
print 
spath = newProjectPath
# spath = os.path.join(mpath,"transmittedFiles")
if not os.path.exists(spath):
    os.makedirs(spath)


    ## 2. rvt fileList1 in folder containing subdir.
    ## 3. rvt fileList2 in this folder not containing subdir.
rvtfiles = []
for r,d,f in os.walk(mpath):
    if r==mpath:
        for rvt in f :
            if rvt.lower().endswith('.rvt'):
                # files.append(os.path.join(r,file)) # Full Path
                rvtfiles.append(rvt)

    ## 4. TransmissionData(rvt in fileList2)
for rvt in rvtfiles:
    print
    print rvt
    rvtPath = os.path.join(mpath,rvt)
    location = ModelPathUtils.ConvertUserVisiblePathToModelPath(rvtPath)
    transdata = TransmissionData.ReadTransmissionData(location)    
    if transdata != None:
# B. rvtLinks in rvt
    # 5. allExternalFileReferenceIds(rvt)
        extFileRefIds = transdata.GetAllExternalFileReferenceIds()        
    # 6. Is RvtLinks in folder
        toBeLoadLinks = []
        notToBeLoadLinks = []
        for extFileRefId in extFileRefIds:
            # extFileRef = transdata.GetLastSavedReferenceData(extFileRefId)
            extFileRef = transdata.GetDesiredReferenceData(extFileRefId)
            if extFileRef.ExternalFileReferenceType != ExternalFileReferenceType.RevitLink:
                continue
            rvtLinkModelPath = extFileRef.GetPath()
            rvtLinkPath = ModelPathUtils.ConvertModelPathToUserVisiblePath(rvtLinkModelPath)
            rvtLinkFile = os.path.basename(rvtLinkPath)
            print rvtLinkPath, "\r\n", rvtLinkFile
    # 7. SetDesiredReferenceData.shouldLoad = True, else False
            # newLinkPath = os.path.join(newProjectPath,rvtLinkFile)
            newLinkPath = rvtLinkFile
            newLinkModelPath = ModelPathUtils.ConvertUserVisiblePathToModelPath(newLinkPath)
            curLinkFileStatus = extFileRef.GetLinkedFileStatus()
            print "Linked File Status :  ", str(curLinkFileStatus)
            if rvtLinkFile in rvtfiles:
                print "파일이 성과물에 있습니다."
                transdata.SetDesiredReferenceData(extFileRefId, newLinkModelPath, PathType.Relative, True if str(curLinkFileStatus)=="Loaded" else False)
                toBeLoadLinks.append(newLinkPath)
            else:
                print "파일이 성과물에 없습니다."
                transdata.SetDesiredReferenceData(extFileRefId, newLinkModelPath, PathType.Relative, False)
                print "다음 번 파일을 열 때에 로드하지 않습니다."
                notToBeLoadLinks.append(newLinkPath)
            print "Desired Linked File Status :  ", str(transdata.GetDesiredReferenceData(extFileRefId).GetLinkedFileStatus())
# C. TransmissionData.Write
        transdata.IsTransmitted = True
    # savelocation = ModelPathUtils.ConvertUserVisiblePathToModelPath(os.path.join(spath,file))
        newRvtPath = os.path.join(spath,rvt)
        shutil.copy(rvtPath,newRvtPath)
        savelocation = ModelPathUtils.ConvertUserVisiblePathToModelPath(newRvtPath)
        TransmissionData.WriteTransmissionData(savelocation,transdata)
    else:
        print "The Document does not have any transmission data."

    print "다음에 로드할 링크 수 : ", len(toBeLoadLinks)
    print "다음에 언로드할 링크 수 : ", len(notToBeLoadLinks)
print
print
print "RVT 처리 파일 수 : ", len(rvtfiles)