
import clr
import System
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.DB import *
from Autodesk.Revit.Attributes import*
from Autodesk.Revit.UI import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import *


import revit_script_util
from revit_script_util import Output

sessionId = revit_script_util.GetSessionId()
uiapp = revit_script_util.GetUIApplication()
app = uiapp.Application
# newProject = app.NewProjectDocument(UnitSystem.Metric)
# newProject = app.NewProjectDocument(r"C:\ProgramData\Autodesk\RVT 2020\Templates\Korea\Construction-DefaultKORKOR.rte")
# newProject.SaveAs(r"D:\code\RBP\newprojectsaveas_unitsystem.rvt")

# NOTE: these only make sense for batch Revit file processing mode.
doc = revit_script_util.GetScriptDocument()
revitFilePath = revit_script_util.GetRevitFilePath()
projectFolderName = revit_script_util.GetProjectFolderName()

# NOTE: these only make sense for data export mode.
sessionDataFolderPath = revit_script_util.GetSessionDataFolderPath()
dataExportFolderPath = revit_script_util.GetDataExportFolderPath()

# TODO: some real work!
Output()
Output("This task script is running!")

worksharingOptions = WorksharingSaveAsOptions()
worksharingOptions.SaveAsCentral = True

SaveOptions = SaveAsOptions()
SaveOptions.MaximumBackups = 50
SaveOptions.SetWorksharingOptions(worksharingOptions)
SaveOptions.OverwriteExistingFile = True
SaveOptions.Compact = True


rOptions = RelinquishOptions(False)
rOptions.StandardWorksets = True
rOptions.ViewWorksets = True
rOptions.FamilyWorksets = True
rOptions.UserWorksets = True
rOptions.CheckedOutElements = True

sOptions = SynchronizeWithCentralOptions()
sOptions.SetRelinquishOptions(rOptions)
sOptions.Compact = True
sOptions.SaveLocalBefore = True
sOptions.SaveLocalAfter = True

tOptions = TransactWithCentralOptions()

TransactionManager.Instance.ForceCloseTransaction()    

filepath = revitFilePath
newdoc = doc #uiapp.ActiveUIDocument
newdoc.SaveAs(filepath,SaveOptions)			
newdoc.SynchronizeWithCentral(tOptions,sOptions)

Output(filepath)


