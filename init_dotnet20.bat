@echo Calling : init_dotnet20.bat
call %~dp0\init_ms.bat

@rem Dotnet settings SDK v2.0
@SET FrameworkVersion=v2.0.50727
@SET FrameworkSDKDir=%MSVNETDIR%\SDK\v2.0

@set PATH=%PATH%;%FrameworkDir%64\v3.5
@set PATH=%PATH%;%FrameworkDir%\v3.5
@set PATH=%PATH%;%FrameworkDir%64\%FrameworkVersion%
@set PATH=%PATH%;%FrameworkDir%\%FrameworkVersion%

@set PATH=%PATH%;%FrameworkSDKDir%\bin
@set PATH=%PATH%;%FrameworkSDKDir%\GuiDebug

@set LIB=%LIB%;%FrameworkSDKDir%\lib
@set LIBPATH=%FrameworkDir%\%FrameworkVersion%

@set INCLUDE=%INCLUDE%;%FrameworkSDKDir%\include

@rem ISE settings for dotnet
set ISE_DOTNET_FRAMEWORK=%FrameworkDir%\%FrameworkVersion%
