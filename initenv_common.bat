@echo ### Calling : initenv_common.bat
@call %~dp0\init_local.bat
@call %~dp0\init_eposix.bat
rem @call %~dp0\init_cygwin.bat
rem @call %~dp0\init_gobo.bat
set ECLOP=f:\third_party\eclop
set PATH=%PATH%;%EIFFEL_SRC%\..\..\bin
set DOCUMENT_DIR=%EIFFEL_SRC%\Delivery
