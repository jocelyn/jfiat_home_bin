@echo off
setlocal
set myiptxt=%TEMP%\~my-ip.txt
wget -q -O %myiptxt% http://djoce.net/whatismyip/
cat %myiptxt%
del %myiptxt%
@echo on
