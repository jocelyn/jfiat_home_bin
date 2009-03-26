@echo off
set TMP_BAT=%TMP%\__tmp__set_es.bat
python "%~dp0\scripts\set_es.py" %* > %TMP_BAT%
call "%TMP_BAT%"
del "%TMP_BAT%"
@echo on
