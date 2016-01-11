@echo off
REM I tested by curl 7.41.0 installed with msysgit 1.9.5

REM The variable %l stores one line entirely if no value is specified as delims.
REM sample.json consists of the results on filltext.com below.
REM http://www.filltext.com/?rows=2&fname={firstName}&lname={lastName}
for /F "delims=" %%l in ( resources\sample.json ) do (
  echo ===
  REM https://docs.python.org/3/library/json.html#json-commandline
  echo %%l | C:\Python34\python.exe -mjson.tool
)
echo ===
