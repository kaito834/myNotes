# https://technet.microsoft.com/ja-jp/scriptcenter/powershell_owner06.aspx (in Japanese)
# New-Item -path $profile -type file -force
# notepad $profile
#
# https://technet.microsoft.com/ja-jp/scriptcenter/powershell_owner05.aspx#EEAA (in Japanese)
# Run Set-ExecutionPolicy cmdlet on powershell prompt as administrator
# Set-ExecutionPolicy RemoteSigned
# 
# tested by PowerShell 4.0 on Windows 8.1


# https://msdn.microsoft.com/en-us/library/system.web.httputility.aspx
Add-Type -AssemblyName System.Web
function urlEncode(){
	[Web.Httputility]::UrlEncode($args[0])
}

function urlDecode(){
	[Web.Httputility]::UrlDecode($args[0])
}


# Windows PowerShell Blog: Base64 Encode/Decode a string
# http://blogs.msdn.com/b/powershell/archive/2006/04/25/583265.aspx
function encodeBase64(){
	# https://msdn.microsoft.com/en-us/library/system.text.encoding.aspx
	# [System.Text.Encoding]::UTF8 is UTF-8 encoding
	# [System.Text.Encoding]::UNICODE is UTF-16 encoding
	[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($args[0]))
}

function decodeBase64(){
	[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($args[0]))
}


# PowerTip: Create a New GUID by Using PowerShell
# http://blogs.technet.com/b/heyscriptingguy/archive/2013/07/25/powertip-create-a-new-guid-by-using-powershell.aspx
function guid(){
	[guid]::NewGuid()
}


# We need to Powershell 4.0 or later version to use Get-FileHash cmdlet.
# https://technet.microsoft.com/en-us/library/dn520872.aspx
# http://d.hatena.ne.jp/kaito834/20140208/1391869073
function md5sum(){
	#Get-FileHash $args[0] -Algorithm MD5 | Format-List
	# https://technet.microsoft.com/ja-JP/library/dd315291.aspx#sectionSection2
	Get-FileHash $args[0] -Algorithm MD5 | Select-Object -Expandproperty hash
}

function sha1sum(){
	#Get-FileHash $args[0] -Algorithm SHA1 | Format-List
	Get-FileHash $args[0] -Algorithm SHA1 | Select-Object -Expandproperty hash
}
