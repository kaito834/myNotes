This text is notes for John the Ripper(JtR) on Windows.

# Environment
- Windows 10 Pro
- Git for windows 2.22.0
  * Use Git Bash
- John the Ripper jumbo release: [1.9.0-jumbo-1](https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip)
  * Download the ZIP file and extract it into prompt folder

# Crack PKZIP2 (ZipCrypto) password hash
## Hardware environment in this use case
- [ThinkPad X1 Extreme](https://www.lenovo.com/jp/ja/notebooks/thinkpad/x-series/ThinkPad-X1-Extreme/p/22TP2TXX1E1)
  * CPU: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz 2.59GHz
  * Memory: 32.0GB

## Procedures
Prepare ZIP file which is compressed by PKZIP2 with password: `test1234`
```
$ file john-1.9.0-jumbo-1-win64-with-password.zip
john-1.9.0-jumbo-1-win64-with-password.zip: Zip archive data, at least v2.0 to extract
```

Extract PKZIP2 password hash from the ZIP file into file: `zip.hash`
```
$> zip2john.exe john-1.9.0-jumbo-1-win64-with-password.zip > zip.hash
john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/ is not encrypted!
john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/ is not encrypted!
john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/doc/ is not encrypted!
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/ is not encrypted, or stored with non-handled compression type
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/ is not encrypted, or stored with non-handled compression type
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/doc/ is not encrypted, or stored with non-handled compression type
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/doc/Auditing-Kerio-Connect.md PKZIP Encr: cmplen=2754, decmplen=9177, crc=DFB8ED84
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/doc/Auditing-Openfire.md PKZIP Encr: cmplen=1271, decmplen=2700, crc=C1A05339
(snip)
ver 2.0 john-1.9.0-jumbo-1-win64-with-password.zip/john-1.9.0-jumbo-1-win64/john-1.9.0-jumbo-1-win64/run/zip2john.exe PKZIP Encr: cmplen=2484, decmplen=9216, crc=6D4F2D24
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
```

Run `john` to crack password against `zip.hash`. In this use case, completed password crack about **2 minutes and 30 seconds**
```
$> john.exe zip.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 6 candidates buffered for the current salt, minimum 12 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Warning: Only 7 candidates buffered for the current salt, minimum 12 needed for performance.
Proceeding with wordlist:password.lst, rules:Wordlist
Proceeding with incremental:ASCII
0g 0:00:00:27  3/3 0g/s 12871Kp/s 12871Kc/s 12871KC/s ljc68e8..ljf823!
test1234         (john-1.9.0-jumbo-1-win64-with-password.zip)
1g 0:00:02:26 DONE 3/3 (2019-07-15 23:33) 0.006824g/s 30645Kp/s 30645Kc/s 30645KC/s tedosas2..teslticu
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

## Related Tool
- [HashCat](https://hashcat.net/hashcat/)
  * According to [HashCat forum thread on May, 2017](https://hashcat.net/forum/archive/index.php?thread-6586.html), HashCat doesn't support to crack PKZIP2 hash

## Related Link
- [［How-to］ Cracking ZIP and RAR protected files with John the Ripper](https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html)
  * via [パス付きRARファイルをJohn The Ripperで解析](https://dorapon2000.hatenablog.com/entry/2016/02/28/075951) (in Japanese)
- [セキュリティレポート｜第1回：そのパスワードで大丈夫？ ～ GPGPUによる高速パスワード解析「パスワード解析と解析マシン」 ](https://www.dit.co.jp/report/security_report/forensic_center/20140901.html) (in Japanese)
- [Tweet by @kitagawa_takuji](https://twitter.com/kitagawa_takuji/status/980711963234729986) (in Japanese)
- [Why is Windows Compressed Folders (Zip folders) support stuck at the turn of the century?](https://devblogs.microsoft.com/oldnewthing/?p=98755)
