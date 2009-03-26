@echo off
Rem python "%~dp0\scripts\init.py" %1 %2 %3 %4 %5 %6 %7 %8 %9
@set INIT_TMP_BAT=%TMP%\__tmp__init.bat
@echo off
python "%~dp0\scripts\init.py" %1 %2 %3 %4 %5 %6 %7 %8 %9  > %INIT_TMP_BAT%
call %INIT_TMP_BAT%
@del %INIT_TMP_BAT%
@set INIT_TMP_BAT=
