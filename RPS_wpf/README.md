# RevitPythonShell WPF

## Window WPF with work in Revit

https://forum.dynamobim.com/t/window-wpf-with-work-in-revit/73564/7.

https://github.com/architecture-building-systems/revitpythonshell/releases/tag/1.0.1 설치용 배포본

https://github.com/architecture-building-systems/revitpythonshell/archive/refs/tags/1.0.1.zip 소스코드

revitpythonshell-1.0.1\RequiredLibraries 폴더에서 다음 .dll 들을
- IronPython.Wpf.dll, 
- IronPython.SQLite.dll,
 
%appdata%/Autodesk/Revit/Addins/2023/RevitPythonShell 폴더로 복사한다.
- "C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.Wpf.dll"
- "C:\Users\teleg\AppData\Roaming\Autodesk\Revit\Addins\2023\RevitPythonShell\IronPython.SQLite.dll"

**Old story**

IronPython Command Shell(REPL) and RevitPythonShell just Window().ShowDialog() enough,
Don't need Application().Run(Window()) ...(Only Command Line : >ipy run_your_wpf.py)
