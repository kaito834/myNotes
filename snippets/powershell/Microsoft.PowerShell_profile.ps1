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


# If Get-FileHash cmdlet exists, this function computes hash by the cmdlet.
# And, if not, computes hash by System.Security.Cryptography.MD5 instance.
# https://technet.microsoft.com/en-us/library/dn520872.aspx
# http://d.hatena.ne.jp/kaito834/20140208/1391869073
function md5sum(){
	# http://stackoverflow.com/questions/3919798/how-to-check-if-a-cmdlet-exists-in-powershell-at-runtime-via-script
	# http://blogs.msdn.com/b/kebab/archive/2013/06/09/an-introduction-to-error-handling-in-powershell.aspx
	if (Get-Command -Name Get-FileHash -ErrorAction SilentlyContinue) {
		#Get-FileHash $args[0] -Algorithm MD5 | Format-List
		# https://technet.microsoft.com/ja-JP/library/dd315291.aspx#sectionSection2
		Get-FileHash $args[0] -Algorithm MD5 | Select-Object -Expandproperty hash
	}else{
		[string]::concat(([security.cryptography.MD5]::create().computehash((Get-Item $args[0]).openread())|ForEach-Object {$_.toString('X2')}))
	}
}

function sha1sum(){
	if (Get-Command -Name Get-FileHash -ErrorAction SilentlyContinue) {
		#Get-FileHash $args[0] -Algorithm SHA1 | Format-List
		Get-FileHash $args[0] -Algorithm SHA1 | Select-Object -Expandproperty hash
	}else{
		[string]::concat(([security.cryptography.SHA1]::create().computehash((Get-Item $args[0]).openread())|ForEach-Object {$_.toString('X2')}))
	}
}
