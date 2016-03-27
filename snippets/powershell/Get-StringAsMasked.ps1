# Input string as SecureString, and output the string as plaintext
# The purpose: input secret, ex. password, as masked on console
param(
  [string] $prompt = "Please input string as masked"
)
begin{}
end{}
process{
  # https://blogs.technet.microsoft.com/heyscriptingguy/2010/08/11/masking-passwords-in-windows-powershell/
  # http://confrage.jp/powershell%E3%81%A7%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E5%85%A5%E5%8A%9B%E3%81%AB%E6%9C%80%E9%81%A9%E3%81%AAread-host%E3%82%92%E4%BD%BF%E3%81%86/ (in Japanese)
  # http://stackoverflow.com/questions/28352141/convert-a-secure-string-to-plain-text
  $str = Read-Host -prompt $prompt -AsSecureString
  $str_bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($str)
  $str_ptr = [System.Runtime.InteropServices.Marshal]::PtrToStringBSTR($str_bstr)

  return $str_ptr
}
