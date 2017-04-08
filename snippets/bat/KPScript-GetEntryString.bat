@echo off
REM This batch file was tested on Windows 10

REM https://technet.microsoft.com/en-US/library/bb491001.aspx
setlocal

set Exe_KPScript=KPScript.exe
set KdbxFile=myDatabase.kdbx
set /P kdbx_masterkey="Input Master key for kdbx: "

REM http://keepass.info/help/v2_dev/scr_sc_index.html#getentrystring
set Cmd_KPScript=%Exe_KPScript% -c:GetEntryString "%KdbxFile%" -pw:"%kdbx_masterkey%" -Field:Password -ref-Title:"twitter.com"

for /f "usebackq delims=" %%a in (`%Cmd_KPScript%`) do (
  set Cmd_KPScript_Result=%%a
  REM The output of %Cmd_KPScript% consists of two line, but only first line is necessary
  REM https://technet.microsoft.com/en-us/library/bb490914.aspx
  goto exit_loop
)

:exit_loop
echo %Cmd_KPScript_Result%

REM pause
