# NOTE: Repath rvtLinks
rvtLinkCollector = FilteredElementCollector(doc).OfClass(RevitLinkType)
rvtLinks = rvtLinkCollector.ToElements()

from System.IO import Directory, SearchOption
import os, os.path
fileDirectoryPath = os.path.dirname(doc.PathName) #revitFilePath)
#rvt = rvtLinks[0]
for rvt in rvtLinks:
	rvtName = Element.Name.GetValue(rvt)
	rvtPath = Directory.GetFiles(fileDirectoryPath, rvtName.Split(':')[0], SearchOption.AllDirectories)
	print rvtName, rvtPath[0]

	rvtxref = rvt.GetExternalFileReference()
	rvtxrefAbsPath = rvtxref.GetAbsolutePath()
	print("ExternalFileReferenceType : %s" %rvtxref.ExternalFileReferenceType)
	print("GetAbsolutePath : %s" %ModelPathUtils.ConvertModelPathToUserVisiblePath(rvtxrefAbsPath))
	print("GetLinkedFileStatus : %s" %rvtxref.GetLinkedFileStatus())
	print("GetPath : %s" %ModelPathUtils.ConvertModelPathToUserVisiblePath(rvtxref.GetPath()))
	print("GetReferencingId : %s" %rvtxref.GetReferencingId())
	print("GetType : %s" %rvtxref.GetType())
	print("IsValidExternalFileReference : %s" %ExternalFileReference.IsValidExternalFileReference(rvtxref))
	print("IsValidObject : %s" %rvtxref.IsValidObject)
	print("IsValidPathTypeForExternalFileReference (?Relative) : %s" %rvtxref.IsValidPathTypeForExternalFileReference(PathType.Relative))
	print("PathType : %s" %rvtxref.PathType)
	print("\r\n" *2)
#	for i in dir(rvtxref): print("%s : %s"%(i,eval("rvtxref.%s"%i)))
#for i in dir(rvtabspath): print("%s : %s"%(i,eval("rvtabspath.%s"%i)))