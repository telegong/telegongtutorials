clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *

foundId = RevitCommandId.LookupPostableCommandId(PostableCommand.Close)
__revit__.PostCommand(foundId)