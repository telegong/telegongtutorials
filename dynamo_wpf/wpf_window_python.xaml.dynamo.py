# Python 표준 및 DesignScript 라이브러리 로드
import sys
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')
clr.AddReference('WindowsBase')
import System
from System.IO import File, FileStream, FileMode
from System.Windows import *

from System.Windows.Markup import XamlReader

# 이 노드에 대한 입력값은 IN 변수에 리스트로 저장됩니다.
#dataEnteringNode = IN

# 코드를 이 선 아래에 배치

xamlPath = IN[0]

def buttonClick(*args):
    window.Close()

file = File.OpenRead(xamlPath.ToString())
window = XamlReader.Load(file)
btn = LogicalTreeHelper.FindLogicalNode(window,"button")
btn.Click += buttonClick
window.Show()

# 출력을 OUT 변수에 지정합니다.
OUT = 0