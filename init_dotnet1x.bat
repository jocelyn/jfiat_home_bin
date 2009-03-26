@echo Calling : init_dotnet1x.bat
call %~dp0\init_ms.bat

@rem Dotnet settings SDK v1.1
@SET FrameworkVersion=v1.1.4322
@SET FrameworkSDKDir=%MSVNETDIR%\SDK\v1.1

@set PATH=%FrameworkSDKDir%\bin;%FrameworkDir%\%FrameworkVersion%;%PATH%
@set INCLUDE=%FrameworkSDKDir%\include;%INCLUDE%
@set LIB=%FrameworkSDKDir%\lib;%LIB%
@set LIBPATH=%FrameworkDir%\%FrameworkVersion%
@set PATH=%PATH%;%FrameworkSDKDir%\GuiDebug

@rem ISE settings for dotnet
set ISE_DOTNET_FRAMEWORK=%FrameworkDir%\%FrameworkVersion%
