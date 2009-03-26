@echo off
rem echo Cleaning path ...
set TMP_BAT=%TMP%\__tmp__clean_path%RANDOM%.bat
python "%~dp0\scripts\clean_path.py" %1    > %TMP_BAT%
@echo off
rem vi %TMP_BAT%
call %TMP_BAT%
del %TMP_BAT%
@echo on
