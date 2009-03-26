setlocal
set WGET=%HOME%\bin\wget
set _PURL=http://the.earth.li/~sgtatham/putty/latest/x86
set _BINDIR=%HOME%\bin

FOR %%f IN ( ^
	putty.exe ^
	pageant.exe ^
	plink.exe ^
	pscp.exe ^
	psftp.exe ^
	puttygen.exe ^
	) DO echo "Fetching %%f" && %WGET% %_PURL%/%%f -O %_BINDIR%\%%f% 	

endlocal
