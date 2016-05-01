# https://github.com/kaito834/myNotes/blob/master/snippets/powershell/Get-StringAsMasked.ps1
$secret = Read-Host -prompt "Please input X_SECRET" -AsSecureString
$secret_bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
$secret_ptr = [System.Runtime.InteropServices.Marshal]::PtrToStringBSTR($secret_bstr)

# https://gallery.technet.microsoft.com/scriptcenter/64471023-f0f4-4195-8b57-8d16ca80a535
$env:X_SECRET = $secret_ptr

# http://qiita.com/mmorita/items/4c44363faf74a7105199 (in Japanese)
# https://msdn.microsoft.com/en-US/en-su/library/96xafkes(v=vs.110).aspx
# 
# If you would like to set something to environment variables for user or machine,
# Use Environment.SetEnvironmentVariable().
