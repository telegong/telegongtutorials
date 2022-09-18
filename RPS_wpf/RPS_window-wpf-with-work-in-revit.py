#SelectionAllDoorAndWindow
### Window WPF with work in Revit
# https://forum.dynamobim.com/t/window-wpf-with-work-in-revit/73564/7.
# https://github.com/architecture-building-systems/revitpythonshell/releases/tag/1.0.1 설치용 배포본
# https://github.com/architecture-building-systems/revitpythonshell/archive/refs/tags/1.0.1.zip 소스코드
# revitpythonshell-1.0.1\RequiredLibraries 폴더에서 다음 .dll 들을
# IronPython.Wpf.dll, 
# IronPython.SQLite.dll,
# %appdata%/Autodesk/Revit/Addins/2023/RevitPythonShell 폴더로 복사한다.
#"C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.Wpf.dll"
#"C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.SQLite.dll"

import clr	
import sys
import System
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\DLLs')

#import Revit API
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
import Autodesk.Revit.DB as DB

#import net library
from System.Collections.Generic import List

# 원래 소스에서 다이나모 부분용 참조부분은 주석처리
#import transactionManager and DocumentManager (RevitServices is specific to Dynamo)
#clr.AddReference('RevitServices')
#import RevitServices
#from RevitServices.Persistence import DocumentManager
#from RevitServices.Transactions import TransactionManager

#doc = DocumentManager.Instance.CurrentDBDocument
#uiapp = DocumentManager.Instance.CurrentUIApplication
#uidoc = uiapp.ActiveUIDocument
#app = uiapp.Application
#sdkNumber = int(app.VersionNumber)

#doc = DB.Document #RPS Shell에서 실행할때만

#set the active Revit application and document : 리본패널에서 실행할때만 
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

try:
	clr.AddReference("IronPython.Wpf")
	clr.AddReference('System.Core')
	clr.AddReference('System.Xml')
	clr.AddReference('PresentationCore')
	clr.AddReference('PresentationFramework')
except IOError:
	raise
	
from System.IO import StringReader
from System.Windows.Markup import XamlReader, XamlWriter
from System.Windows import Window, Application


try:
	import wpf
except ImportError:
	raise
	
class MyForm(Window):

	LAYOUT = """
		<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
			Title="Window2"
			Width="404"
			Height="419">
			<Grid>
				<Label
					Grid.Column="0"
					Grid.Row="0"
					HorizontalAlignment="Left"
					VerticalAlignment="Top"
					Margin="14,16,0,0"
					Width="130"
					Height="29"
					x:Name="ClickSelect"
					Content="Click to Select" />
				<Button
					Content="Close"
					Grid.Column="1"
					Grid.Row="0"
					HorizontalAlignment="Right"
					VerticalAlignment="Bottom"
					Margin="0,0,16,16"
					Width="96"
					Height="24"
					x:Name="button1"
					Click="button1_Click" />
				<ListBox
					x:Name="listBox1"
					SelectionChanged="listBox1_SelectionChanged"
					Grid.Column="0"
					Grid.ColumnSpan="2"
					Grid.Row="0"
					Margin="14,53,16,61" />
				<Grid.ColumnDefinitions>
					<ColumnDefinition
						Width="0.503474042268444*" />
					<ColumnDefinition
						Width="0.496202531645569*" />
				</Grid.ColumnDefinitions>
			</Grid>
		</Window>"""
				
	def __init__(self):
		self.ui = wpf.LoadComponent(self, StringReader(MyForm.LAYOUT))
		collElems = FilteredElementCollector(doc, uidoc.Document.ActiveView.Id).OfClass(FamilyInstance).ToElements()
		collElems = sorted(collElems, key = lambda x : x.Name)
		for e in collElems:
			item = System.Windows.Controls.ListBoxItem()
			item.Content = e.Name 
			item.Tag = e.Id
			self.ui.listBox1.Items.Add(item)

	
	def button1_Click(self, sender, e):
		self.Close()
	
	def listBox1_SelectionChanged(self, sender, e):
		itemId = self.ui.listBox1.SelectedItem.Tag
		print(self.ui.listBox1.SelectedItem.Tag)
		elem = doc.GetElement(itemId)
		uidoc.ShowElements(elem)
		uidoc.Selection.SetElementIds(List[ElementId]([itemId]))

form = MyForm()
#form.ShowDialog() #Modal 창으로 열린다
form.Show()  # Non Modal 모드로 작동시킨다
#exit()  # 창을 닫으면 RPS 셸을 끝낸다
__window__.Close() # 리본패널에서 실행시 console output을 닫는다.