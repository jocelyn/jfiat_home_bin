@echo Calling init_ms.bat
call %~dp0\init_local.bat
if '%MS_PLATFORM%' == '' set MS_PLATFORM=win64
rem @echo env MS_PLATFORM=%MS_PLATFORM%

set PATH=%PATH%;%MSVSIDEDIR%\Common7\IDE
if '%MS_PLATFORM%' == 'win64' set PATH=%PATH%;%WINSDKDIR%\bin\x64
set PATH=%PATH%;%WINSDKDIR%\bin
set PATH=%PATH%;%WINSDKDIR%\VC\bin
set PATH=%PATH%;%MSVSDIR%\VC
if '%MS_PLATFORM%' == 'win64' set PATH=%PATH%;%MSVSDIR%\VC\bin\amd64
set PATH=%PATH%;%MSVSDIR%\VC\bin
set PATH=%PATH%;%MSVSDIR%\VC\vcpackages

if '%MS_PLATFORM%' == 'win64' set LIB=%LIB%;%WINSDKDIR%\Lib\x64
set LIB=%LIB%;%WINSDKDIR%\VC\Lib
set LIB=%LIB%;%WINSDKDIR%\Lib
if '%MS_PLATFORM%' == 'win64' set LIB=%LIB%;%MSVSDIR%\VC\lib\amd64
set LIB=%LIB%;%MSVSDIR%\VC\Lib
set LIB=%LIB%;%MSVSDIR%\Lib

set INCLUDE=%INCLUDE%;%MSVSIDEDIR%\Include
set INCLUDE=%INCLUDE%;%MSVSDIR%\VC\Include
set INCLUDE=%INCLUDE%;%WINSDKDIR%\Include
set INCLUDE=%INCLUDE%;%WINSDKDIR%\Include\gl
set INCLUDE=%INCLUDE%;%WINSDKDIR%\VC\Include
set INCLUDE=%INCLUDE%;%WINSDKDIR%\VC\Include\Sys


rem C:\WINDOWS\system32\cmd.exe /E:ON /V:ON /T:0E /K "%WINSDKDIR%\Bin\SetEnv.Cmd /x64"
