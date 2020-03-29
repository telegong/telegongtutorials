import clr
import sys

clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')
clr.AddReference('WindowsBase')

from System.IO import File
from System.Windows.Markup import XamlReader
from System.Windows import *

## FileBrowserDialog()
flDiag = OpenFileDialog()
if flDiag.ShowDialog(topMostForm) == DialogResult.OK :
	print flDiag.FileName
xamlPath = flDiag.FileName #IN[0]

def buttonClick(*args):
    window.Close()

file = File.OpenRead(xamlPath.ToString())
window = XamlReader.Load(file)
btn = LogicalTreeHelper.FindLogicalNode(window,"button")
btn.Click += buttonClick
window.Show()