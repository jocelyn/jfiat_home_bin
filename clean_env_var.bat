@echo off
rem echo cleaning env var %1
set TMP_BAT=%TMP%\__tmp__clean_env_var.bat
python "%~dp0\scripts\clean_env_var.py" %1 %1   > %TMP_BAT%
@echo off
call %TMP_BAT%
del %TMP_BAT%
@echo on

