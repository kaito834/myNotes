REM Copy local folder to remote folder
REM I executed this batch on Windows 8.1
robocopy "C:\Users\sample\Documents\mydata" "\\192.168.0.120\backup\" /E /FFT /R:3 /W:5 /NP /TEE /LOG+:"\\192.168.0.120\backup\robocopy.log"