location = ModelPathUtils.ConvertUserVisiblePathToModelPath(r"revitProject1.rvt")
transdata = TransmissionData.ReadTransmissionData(location)
if transdata != None:
    extrefs = transdata.GetAllExternalFileReferenceIds()
    for refId in extrefs:
        extref = transdata.GetLastSavedReferenceData(refId)
        if extref.ExternalFileReferenceType == ExternalFileReferenceType.RevitLink:
            print("refId : %s" %refId)
            print("extref.GetPath() : %s" %ModelPathUtils.ConvertModelPathToUserVisiblePath(extref.GetPath()))
            print("extref.PathType : %s" %extref.PathType)
            print
            # ShouldLoad = False
            # transdata.SetDesiredReferenceData(refId, extref.GetPath(), extref.PathType, False)
    print("transdata.IsTransmitted : %s" %transdata.IsTransmitted)
    print("Setting... IsTransmitted to False!")
    transdata.IsTransmitted = False # True
    print("transdata.IsTransmitted : %s" %transdata.IsTransmitted)
    TransmissionData.WriteTransmissionData(location, transdata)
else:
    Autodesk.Revit.UI.TaskDialog.Show("Unload Links", "The document dose not have any transmission data")
