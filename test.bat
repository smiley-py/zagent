@ECHO OFF

:choice
set /P c=Do you want to continue [Y/N]?
if /I "%c%" EQU "Y" goto :yes
if /I "%c%" EQU "N" goto :no

:yes
echo "User has typed yes"
goto :end

:no
echo "User has typed no"
goto :end

:end

