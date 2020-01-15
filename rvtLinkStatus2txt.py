import os, System

def print2File(printThis,printStore,printFile):
    print(printThis)
    printStore.append(printThis)
    if printFile != '':
        fs = System.IO.StreamWriter(printFile)
        for line in printStore:
            fs.WriteLine(line)
        print(printFile)
        fs.WriteLine(printFile)
        fs.Close()

printThis = ''
printStore = []
printFile = doc.PathName + '.txt'
print2File(doc.PathName, printStore,'')
# print(doc.PathName)
print2File('', printStore, '')

rvtLinkCollector = FilteredElementCollector(doc).OfClass(RevitLinkInstance)
rvtLinks = rvtLinkCollector.ToElements()
print2File(str(len(rvtLinks))+ " rvt Link Files", printStore,'')
# print(str(len(rvtLinks))+ " rvt Link Files")

for rvt in rvtLinks:
    name = rvt.get_Parameter(BuiltInParameter.RVT_LINK_INSTANCE_NAME).AsString()
    
    rvtType = doc.GetElement(rvt.GetTypeId())
    exRef = rvtType.GetExternalFileReference()
    print2File(name +' : ' + ModelPathUtils.ConvertModelPathToUserVisiblePath(exRef.GetPath()),printStore,'')
    # print(name +' : ' + ModelPathUtils.ConvertModelPathToUserVisiblePath(exRef.GetPath()))
    
    path = ModelPathUtils.ConvertModelPathToUserVisiblePath(exRef.GetAbsolutePath())
    print2File(path, printStore,'')
    # print(path)
    
    linkStatus = exRef.GetLinkedFileStatus()
    print2File(linkStatus, printStore, '')
    print2File('', printStore, '')

print2File("Save to .txt File", printStore, printFile)