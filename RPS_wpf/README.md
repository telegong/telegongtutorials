# RevitPythonShell WPF
## import wpf 

### RevitPythonShell 2 (IronPython 3.4)

1. RPS Configure.. > You need to add the path where RPS is installed to the SearchPath. 
>( %APPDATA%\Autodesk\Revit\Addins\202x\RevitPythonShell )
  <br>Or 


```python
   import os,sys
   sys.path.append(\
	 os.path.expandvars(\
	 fr'%appdata%\Autodesk\Revit\Addins\{doc.Application.VersionNumber}\RevitPythonShell'))
   #sys.path.append(os.path.join(os.environ['APPDATA'],r'Autodesk\Revit\Addins\2023\RevitPythonShell'))
   
```

2. AddReferenceToFile
```python
   clr.AddReferenceToFile("IronPython.Wpf.dll") #clr.AddReference("IronPython.Wpf") then Version=2.7.7. ??WHY??
   import wpf
```
> <IronPython.Wpf, Version=**3.4.0.0**, Culture=neutral, PublicKeyToken= ...

### Window WPF with work in Revit (old RevitPythonShell 1..)

https://forum.dynamobim.com/t/window-wpf-with-work-in-revit/73564/7.

https://github.com/architecture-building-systems/revitpythonshell/releases/tag/1.0.1 설치용 배포본

https://github.com/architecture-building-systems/revitpythonshell/archive/refs/tags/1.0.1.zip 소스코드

revitpythonshell-1.0.1\RequiredLibraries 폴더에서 다음 .dll 들을
- IronPython.Wpf.dll, 
- IronPython.SQLite.dll,
 
%appdata%/Autodesk/Revit/Addins/2023/RevitPythonShell 폴더로 복사한다.
- "C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.Wpf.dll"
- "C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.SQLite.dll"

%programfiles(x86)%/RevitPythonShell/2023 폴더로 복사해야 할 수 있다.
- "C:\Program Files (x86)\RevitPythonShell\2023\IronPython.Wpf.dll"
- "C:\Program Files (x86)\RevitPythonShell\2023\IronPython.SQLite.dll"



**Old story**

IronPython Command Shell(REPL) and RevitPythonShell just Window().ShowDialog() enough,
Don't need Application().Run(Window()) ...(Only Command Line : >ipy run_your_wpf.py)
