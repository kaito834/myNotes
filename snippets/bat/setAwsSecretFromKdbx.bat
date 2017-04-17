@echo off
REM This batch file was tested on Windows 10

set Exe_KPScript=C:\Users\kaito\Documents\mydata\KeePass\KPScript.exe
set KdbxFile=C:\Users\kaito\Documents\mydata\kdbx\myDatabase.kdbx

REM http://keepass.info/help/v2_dev/scr_sc_index.html#masterkey
REM http://keepass.info/help/v2_dev/scr_sc_index.html#getentrystring
REM You need to save this batch file by Shift_JIS encoding if specify Japanese title at -ref-Title
set Cmd_KPScript=%Exe_KPScript% -guikeyprompt -c:GetEntryString "%KdbxFile%" -Field:Password -ref-Title:"aws_iam-kaito834-program"

for /f "usebackq delims=" %%a in (`%Cmd_KPScript%`) do (
  set Cmd_KPScript_Result=%%a
  REM The output of %Cmd_KPScript% consists of two line, but only first line is necessary
  REM https://technet.microsoft.com/en-us/library/bb490914.aspx
  goto exit_loop
)

:exit_loop
REM https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-environment
REM https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html
REM set HTTPS_PROXY and HTTP_PROXY if necessary
set AWS_ACCESS_KEY_ID=xxx
set AWS_SECRET_ACCESS_KEY=%Cmd_KPScript_Result%

REM Unset some environment variables which are not necessary
set Exe_KPScript=
set KdbxFile=
set Cmd_KPScript=
set Cmd_KPScript_Result=

REM pause
