@echo off
REM I tested by curl 7.41.0 installed with msysgit 1.9.5

set cURL="C:\Program Files\Git\bin\curl.exe"
set timeOutSeconds=10

REM https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/for.mspx
REM According to this document, two % are necessary in a batch file.
for /L %%i in (1, 1, 10) do (
  %cURL% -d a=test%%i http://127.0.0.1/
  timeout /T %timeOutSeconds%
)

REM Infinite loop with *for* statement is below:
REM for /L %i in (0) do <cmd> & timeout /T <sec>
REM https://twitter.com/kaito834/status/283865298715701248
