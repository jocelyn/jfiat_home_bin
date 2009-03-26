setlocal
set UNZIP=7za.exe e -y
set WGET=wget
set FTPDIR=%HOME%\bin\tmp\ftp
set BINDIR=%HOME%\bin\sysinternals

mkdir %FTPDIR%
mkdir %BINDIR%
rem PortMonNt

FOR %%z IN ( ^
	Autoruns ^
	ProcessExplorerNt ^
	PsTools ^
	RootkitRevealer ^
	TcpView ^
	RegmonNt ^
	FilemonNt ^
	DiskMon ^
	) DO echo "Processing %%z"  && %WGET% http://www.sysinternals.com/Files/%%z.zip -O %FTPDIR%\%%z.zip  && %UNZIP% %FTPDIR%\%%z.zip -o%BINDIR%

endlocal
