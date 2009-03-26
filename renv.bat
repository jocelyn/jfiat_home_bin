@echo off
set TMP_BAT=%TMP%\__tmp__rainbow_env.bat
python "%~dp0\scripts\renv.py" %TMP_BAT% none %1 %2 %3 %4 %5 %6 %7 %8 %9
call %TMP_BAT%
@echo off
del %TMP_BAT%
@echo on
