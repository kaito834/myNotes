## ConvertFrom-Json / ConvertTo-Json
### Indent compressed JSON object
You can use [ConvertFrom-Json](https://technet.microsoft.com/en-us/library/hh849898.aspx) and [ConvertTo-Json](https://technet.microsoft.com/en-us/library/hh849922.aspx) cmdlets to indent compressed JSON object.
You should execute ConvertTo-Json cmdlet with Depth parameter if the JSON object consists of over 3 level nested objects.
```
Get-Content -Encoding utf8 .\a.json | ConvertFrom-Json | ConvertTo-Json
```

You can pipe [Out-File](https://technet.microsoft.com/en-us/library/hh849882.aspx) cmdlet if you would like to store the output as a file.
```
Get-Content -Encoding utf8 .\a.json | ConvertFrom-Json | ConvertTo-Json | Out-File -Encoding utf8 b.json
```

[ForEach-Object](https://technet.microsoft.com/en-us/library/hh849731.aspx) cmdlet allows you to indent compressed JSON objects per a line if a.json has some compressed JSON objects; foreach is alias for ForEach-Object cmdlet.
```
Get-Content -Encoding utf8 .\a.json | foreach { ConvertFrom-Json $_ | ConvertTo-Json }
```

Note: PowerShell encodes bytes by UTF-16 internally, so you should execute Get-Content or Out-File cmdlets with Encoding parameter.

### Compress/Minify JSON object
You can use [ConvertFrom-Json](https://technet.microsoft.com/en-us/library/hh849898.aspx) and [ConvertTo-Json](https://technet.microsoft.com/en-us/library/hh849922.aspx) cmdlets to compress/minify JSON object. ConvertTo-Json with Compress parameter outputs compressed JSON object as string.

You must execute [Get-Content](https://technet.microsoft.com/en-us/library/hh849787.aspx) cmdlet with Raw parameter. The Raw parameter can pipe entire contents on the file as String object, so ConvertFrom-Json cmdlet can parses JSON object consists of multiple lines.

```
Get-Content -Encoding utf8 -Raw .\b.json | ConvertFrom-Json | ConvertTo-Json -Compress
```
