# Python 표준 및 DesignScript 라이브러리 로드
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import System.Windows
from System.Threading import Thread, ThreadStart, ApartmentState
clr.AddReference('PresentationFramework')
from System.Windows import *

# 이 노드에 대한 입력값은 IN 변수에 리스트로 저장됩니다.
if __name__== '__main__': IN = True
dataEnteringNode = IN

# 코드를 이 선 아래에 배치

# Initialization Constants
Window = System.Windows.Window
Application = System.Windows.Application
def appThread():
	window = Window()
	window.Title = "Hello WPF!"
	button = Controls.Button()
	button.Content = "Push Me!  "+ str(dataEnteringNode)
	panel = Controls.StackPanel()
	window.Content = panel
	panel.Children.Add(button)
	window.Show()
if System.Diagnostics.Process.GetCurrentProcess().ProcessName == "Revit":
	thread = appThread()
else:
	thread = Application.Current.Dispatcher.Invoke(appThread)
# 출력을 OUT 변수에 지정합니다.
OUT = 0