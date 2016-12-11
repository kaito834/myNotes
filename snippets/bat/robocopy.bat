REM Copy local folder to remote folder
REM I executed this batch on Windows 8.1
REM
REM Target folder had 'hidden' and 'system' attributes if drive (e.g. d:\) would be set as source folder
REM Ref. https://social.technet.microsoft.com/Forums/ja-JP/eb3bc943-f249-4641-80fb-d378cb91d043/robocopy?forum=windowsserver2008ja (in Japanese)

set /P answer="Do you synchronize your data to remote host? (y/n): "
if /i "%answer%" == "y" (
robocopy "C:\Users\sample\Documents\mydata" "\\192.168.0.120\backup\" /E /FFT /R:3 /W:5 /NP /TEE /LOG+:"\\192.168.0.120\backup\robocopy.log"
) else if /i "%answer%" == "n" (
  echo ** Cancelled the synchronization.
) else (
  echo !! Invalid input. exit.
)

pause
