setlocal
set TIME=%1
if .%TIME. == .. set TIME=5
psshutdown -s -c -t %TIME
endlocal
