set SVN_SERVER=jfiatpc
set SVN_DIR=e:\MySvnDir
set SVN_USER=jfiat

set t_OP=%1
psexec \\%SVN_SERVER% "%SVN_DIR%\_admin_\rserver.bat" %t_OP% -u %SVN_USER%  -e %SVN_USER% -w "%SVN_DIR"  -i 
set t_OP=
