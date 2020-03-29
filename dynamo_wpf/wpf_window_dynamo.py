# Python 표준 및 DesignScript 라이브러리 로드
import sys
import System
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("PresentationFramework")
from System.Windows import * 

# 이 노드에 대한 입력값은 IN 변수에 리스트로 저장됩니다.
dataEnteringNode = IN[0]

# 코드를 이 선 아래에 배치
window = Window()
window.Title = "Hello WPF!"
button = Controls.Button()
button.Content = "Push Me!  "+ str(dataEnteringNode)
panel = Controls.StackPanel()
window.Content = panel
panel.Children.Add(button)
window.Show()
	
# 출력을 OUT 변수에 지정합니다.
OUT = 0