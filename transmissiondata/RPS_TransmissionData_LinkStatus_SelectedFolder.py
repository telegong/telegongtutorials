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

# fpath = ""
# fdialog = OpenFileDialog()
# if fdialog.ShowDialog() == DialogResult.OK :
# 	fpath = fdialog.FileName
# rvtPath = fpath
# print
# print rvtPath
# print

def rvtLinkStatus(rvtPath):
    rvtModelPath = ModelPathUtils.ConvertUserVisiblePathToModelPath(rvtPath)
    transdata = TransmissionData.ReadTransmissionData(rvtModelPath) #doc.PathName))
    extFileRefIds = transdata.GetAllExternalFileReferenceIds()
    #extFileRefs = [transdata.GetLastSavedReferenceData(extFileRefId) for extFileRefId in extFileRefIds]
    extFileRefs = list(map(lambda id : transdata.GetLastSavedReferenceData(id), extFileRefIds))
    rvtLinks = list(filter(lambda eFRef: eFRef.ExternalFileReferenceType == ExternalFileReferenceType.RevitLink, extFileRefs))
    rvtLinkPaths = list(map(lambda rvtLink: ModelPathUtils.ConvertModelPathToUserVisiblePath(rvtLink.GetPath()), rvtLinks))
    rvtLinkAbsPaths = list(map(lambda rvtLink: ModelPathUtils.ConvertModelPathToUserVisiblePath(rvtLink.GetAbsolutePath()), rvtLinks))
    curLinkStatus = list(map(lambda rvtLink: rvtLink.GetLinkedFileStatus(), rvtLinks))

    rvtLinkIds = list(map(lambda rvtLink: rvtLink.GetReferencingId(), rvtLinks))
    eFRsDesireds = list(map(lambda rvtLinkId: transdata.GetDesiredReferenceData(rvtLinkId), rvtLinkIds))
    dsrLinkPaths = list(map(lambda eFRsDesired: ModelPathUtils.ConvertModelPathToUserVisiblePath(eFRsDesired.GetPath()), eFRsDesireds))
    dsrLinkAbsPaths = list(map(lambda eFRsDesired: ModelPathUtils.ConvertModelPathToUserVisiblePath(eFRsDesired.GetAbsolutePath()), eFRsDesireds))
    dsrLinkStatus = list(map(lambda eFRsDesired: eFRsDesired.GetLinkedFileStatus(), eFRsDesireds))

    # rvtLinkStatusReport = list(map(lambda rvt,cur,dsr: "".join(map(str,[rvt," :  curLinkStatus=",cur,", DesiredLinkStatus=",dsr])), rvtLinkPaths,curLinkStatus,dsrLinkStatus))
    rvtLinkStatusReport = list(map(lambda rvt,cur,abs: "".join(map(str,[",",rvt," ,  curLinkStatus=",cur,", absolutePath=",abs])), rvtLinkPaths,curLinkStatus,rvtLinkAbsPaths))
    dsrLinkStatusReport = list(map(lambda rvt,cur,abs: "".join(map(str,[",",rvt," ,  dsrLinkStatus=",cur,", absolutePath=",abs])), dsrLinkPaths,dsrLinkStatus,dsrLinkAbsPaths))
    for c,d in zip(rvtLinkStatusReport,dsrLinkStatusReport):
        print c
        print d
        print 

for rvtFullPath in rvtsFullPath:
    print rvtFullPath
    rvtLinkStatus(rvtFullPath)

#sId = 1
#for sId in range(len(rvtLinks)):
#transdata.SetDesiredReferenceData(rvtLinkIds[sId],rvtLinks[sId].GetPath(),PathType.Relative,True) # curLinkStatus[sId])
#transdata.SetDesiredReferenceData(rvtLinkIds[sId],rvtLinks[sId].GetPath(),PathType.Relative,True if str(curLinkStatus[sId])=="Loaded" else False)
#transdata.SetDesiredReferenceData(rvtLinkIds[sId],rvtLinks[sId].GetPath(),PathType.Relative,False if str(curLinkStatus[sId])=="Loaded" else True) 
#TransmissionData.WriteTransmissionData(rvtModelPath,transdata)