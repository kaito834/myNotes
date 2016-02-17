# Get affected packages from Red Hat CVE database by CVE identity
# Affected packages are a section, "Affected Packages State," in each Web pages
#
# References
# http://winscript.jp/powershell/253 (in Japanese)
# http://winscript.jp/powershell/305 (in Japanese)
# http://tech.blog.aerie.jp/entry/2014/04/21/115311 (in Japanese)
param(
  [Parameter(ValueFromPipeline=$true,Mandatory=$true)]
  [ValidatePattern('^[cC][vV][eE]\-[0-9]{4}\-[0-9]{4}$')]
  [string]
  $Cve
)

begin{
  # Ref. http://blogs.msdn.com/b/kebab/archive/2013/06/09/an-introduction-to-error-handling-in-powershell.aspx
  $ErrorActionPreference = "Stop"
}

process{
  $RHCveDatabaseUrl = 'https://access.redhat.com/security/cve/' + $Cve
  $targetClass = 'field field-name-field-affected-state-package-txt field-type-text-long field-label-above '
  Write-Host $RHCveDatabaseUrl
  Write-Host '==='

  try{
    $res = Invoke-WebRequest $RHCveDatabaseUrl

    # References
    # https://superwidgets.wordpress.com/tag/read-html-via-powershell-powershell/
    # http://www.leeholmes.com/blog/2015/01/05/extracting-tables-from-powershells-invoke-webrequest/
    $divElement = $res.ParsedHtml.getElementsByTagName('div') | Where { $_.className -eq 'field field-name-field-affected-state-package-txt field-type-text-long field-label-above ' }
    $trElements = $divElement.getElementsByTagName('tr')
    foreach ( $trElement in $trElements ) {
      $cells = @()
      $trElement.getElementsByTagName('th') | select innerText | foreach { $cells += $_.innerText }
      $trElement.getElementsByTagName('td') | select innerText | foreach { $cells += $_.innerText }
      Write-Host -Separator ', ' $cells
    }
  }
  catch{
    write-host "Caught an exception:" -ForegroundColor Red
    write-host "Exception Type: $($_.Exception.GetType().FullName)" -ForegroundColor Red
    write-host "Exception Message: $($_.Exception.Message)" -ForegroundColor Red
  }

  Write-Host ''
}

end{}
