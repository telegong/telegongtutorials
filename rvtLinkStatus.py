print(doc.PathName)
rvtLinkCollector = FilteredElementCollector(doc).OfClass(RevitLinkInstance)
rvtLinks = rvtLinkCollector.ToElements()
print(str(len(rvtLinks))+ " rvt Link Files")
for rvt in rvtLinks:
    name = rvt.get_Parameter(BuiltInParameter.RVT_LINK_INSTANCE_NAME).AsString()
    rvtType = doc.GetElement(rvt.GetTypeId())
    exRef = rvtType.GetExternalFileReference()
    print(name +' : ' + ModelPathUtils.ConvertModelPathToUserVisiblePath(exRef.GetPath()))
    path = ModelPathUtils.ConvertModelPathToUserVisiblePath(exRef.GetAbsolutePath())
    print(path)
    linkStatus = exRef.GetLinkedFileStatus()
    print(linkStatus)
    print