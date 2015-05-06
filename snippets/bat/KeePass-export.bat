@echo off

setlocal
set originalKdbxFile=KeePass\myDatabase.kdbx
set exportedKdbxFile=KeePass\myDatabaseProtableGroup.kdbx

REM ToDo: mask password on command prompt by Powershell
REM https://gallery.technet.microsoft.com/scriptcenter/59807ef4-f17a-4a12-a389-f9bb407c4e5a
set /P originalKdbxFile_pass="%originalKdbxFile% password: "
set /P exportedKdbxFile_pass="%exportedKdbxFile% password: "

REM Use KPScript plugin, http://keepass.info/help/v2_dev/scr_index.html
KeePass\KPScript -c:Export "%originalKdbxFile%" -pw:"%originalKdbxFile_pass%" -Format:"KeePass KDBX (2.x)" -Outfile:"%exportedKdbxFile%"
KeePass\KPScript -c:ChangeMasterKey "%exportedKdbxFile%" -pw:"%originalKdbxFile_pass%" -newpw:"%exportedKdbxFile_pass%"
KeePass\KPScript -c:DeleteEntry -pw:"%exportedKdbxFile_pass%" "%exportedKdbxFile%" -refx-GroupPath:HomeGroup
KeePass\KPScript -c:DeleteEntry -pw:"%exportedKdbxFile_pass%" "%exportedKdbxFile%" -refx-GroupPath:HomeGroup/Network
KeePass\KPScript -c:DeleteEntry -pw:"%exportedKdbxFile_pass%" "%exportedKdbxFile%" -refx-GroupPath:HomeGroup/eMail
KeePass\KPScript -c:DeleteEntry -pw:"%exportedKdbxFile_pass%" "%exportedKdbxFile%" -refx-GroupPath:HomeGroup/Homebanking

REM pause
exit