This text notes my usage of [7-Zip command line](https://sevenzip.osdn.jp/chm/cmdline/).

# Environments
- Windows 10 Professional
- 7-Zip 16.04

# My Usage of 7-Zip Command line
Execute `7z.exe` with no options, and usage of 7z.exe is shown.
```
C:\Program Files\7-Zip>7z.exe

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Usage: 7z <command> [<switches>...] <archive_name> [<file_names>...]
       [<@listfiles...>]

<Commands>
  a : Add files to archive
  b : Benchmark
  d : Delete files from archive
  e : Extract files from archive (without using directory names)
  h : Calculate hash values for files
  i : Show information about supported formats
  l : List contents of archive
  rn : Rename files in archive
  t : Test integrity of archive
  u : Update files to archive
  x : eXtract files with full paths

<Switches>
  -- : Stop switches parsing
  -ai[r[-|0]]{@listfile|!wildcard} : Include archives
  -ax[r[-|0]]{@listfile|!wildcard} : eXclude archives
  -ao{a|s|t|u} : set Overwrite mode
  -an : disable archive_name field
  -bb[0-3] : set output log level
  -bd : disable progress indicator
  -bs{o|e|p}{0|1|2} : set output stream for output/error/progress line
  -bt : show execution time statistics
  -i[r[-|0]]{@listfile|!wildcard} : Include filenames
  -m{Parameters} : set compression Method
    -mmt[N] : set number of CPU threads
  -o{Directory} : set Output directory
  -p{Password} : set Password
  -r[-|0] : Recurse subdirectories
  -sa{a|e|s} : set Archive name mode
  -scc{UTF-8|WIN|DOS} : set charset for for console input/output
  -scs{UTF-8|UTF-16LE|UTF-16BE|WIN|DOS|{id}} : set charset for list files
  -scrc[CRC32|CRC64|SHA1|SHA256|*] : set hash function for x, e, h commands
  -sdel : delete files after compression
  -seml[.] : send archive by email
  -sfx[{name}] : Create SFX archive
  -si[{name}] : read data from stdin
  -slp : set Large Pages mode
  -slt : show technical information for l (List) command
  -snh : store hard links as links
  -snl : store symbolic links as links
  -sni : store NT security information
  -sns[-] : store NTFS alternate streams
  -so : write data to stdout
  -spd : disable wildcard matching for file names
  -spe : eliminate duplication of root folder for extract command
  -spf : use fully qualified file paths
  -ssc[-] : set sensitive case mode
  -ssw : compress shared files
  -stl : set archive timestamp from the most recently modified file
  -stm{HexMask} : set CPU thread affinity mask (hexadecimal number)
  -stx{Type} : exclude archive type
  -t{Type} : Set type of archive
  -u[-][p#][q#][r#][x#][y#][z#][!newArchiveName] : Update options
  -v{Size}[b|k|m|g] : Create volumes
  -w[{path}] : assign Work directory. Empty path means a temporary directory
  -x[r[-|0]]{@listfile|!wildcard} : eXclude filenames
  -y : assume Yes on all queries
```

## Extract RPM package by 7-Zip
7-Zip allows users to extract RPM package on Windows environment.
2 steps to extract RPM package by `7z.exe` are as following:
1. Extract RPM package into CPIO file
2. Extract the CPIO file

For example, I extracted [golang-1.7.6-1.el6.i686.rpm](http://dl.fedoraproject.org/pub/epel/6Server/i386/golang-1.7.6-1.el6.i686.rpm) by `7z.exe`, and stored files and directories contained in file on local disk.

### Step 1: Extract RPM package into CPIO file
```
C:\Users\kaito\Documents\tmp>dir /B
golang-1.7.6-1.el6.i686.rpm

C:\Users\kaito\Documents\tmp>"C:\Program Files\7-Zip\7z.exe" x golang-1.7.6-1.el6.i686.rpm

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
1 file, 1244080 bytes (1215 KiB)

Extracting archive: golang-1.7.6-1.el6.i686.rpm
--
Path = golang-1.7.6-1.el6.i686.rpm
Type = Rpm
Physical Size = 1244080
Headers Size = 205072
CPU = i686
Host OS = linux
Created = 2017-06-15 21:28:18
----
Path = golang-1.7.6-1.el6.i686.cpio.xz
Size = 1039008
Created = 2017-06-15 21:28:18
--
Path = golang-1.7.6-1.el6.i686.cpio.xz
Type = xz
Physical Size = 1039008
Method = LZMA2:19 SHA256
Streams = 1
Blocks = 1

Everything is Ok

Size:       12217076
Compressed: 1244080

C:\Users\kaito\Documents\tmp>echo %ERRORLEVEL%
0

C:\Users\kaito\Documents\tmp>dir /B
golang-1.7.6-1.el6.i686.cpio
golang-1.7.6-1.el6.i686.rpm
```

If you would like to extract RPM package into CPIO file on other directory, you can use ['-o{Directory}'](https://sevenzip.osdn.jp/chm/cmdline/switches/output_dir.htm) option.
`-o*` means to set a directory named same as target rpm file as {Directory}.
```
C:\Users\kaito\Documents\tmp>dir /S /B
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.rpm

C:\Users\kaito\Documents\tmp>"C:\Program Files\7-Zip\7z.exe" x -ogolang-1.7.6-1.el6.i686 golang-1.7.6-1.el6.i686.rpm

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
1 file, 1244080 bytes (1215 KiB)

Extracting archive: golang-1.7.6-1.el6.i686.rpm
--
Path = golang-1.7.6-1.el6.i686.rpm
Type = Rpm
Physical Size = 1244080
Headers Size = 205072
CPU = i686
Host OS = linux
Created = 2017-06-15 21:28:18
----
Path = golang-1.7.6-1.el6.i686.cpio.xz
Size = 1039008
Created = 2017-06-15 21:28:18
--
Path = golang-1.7.6-1.el6.i686.cpio.xz
Type = xz
Physical Size = 1039008
Method = LZMA2:19 SHA256
Streams = 1
Blocks = 1

Everything is Ok

Size:       12217076
Compressed: 1244080

C:\Users\kaito\Documents\tmp>echo %ERRORLEVEL%
0

C:\Users\kaito\Documents\tmp>dir /S /B
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.rpm
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686\golang-1.7.6-1.el6.i686.cpio

C:\Users\kaito\Documents\tmp>"C:\Program Files\7-Zip\7z.exe" x -o* golang-1.7.6-1.el6.i686.rpm

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
1 file, 1244080 bytes (1215 KiB)

Extracting archive: golang-1.7.6-1.el6.i686.rpm
--
Path = golang-1.7.6-1.el6.i686.rpm
Type = Rpm
Physical Size = 1244080
Headers Size = 205072
CPU = i686
Host OS = linux
Created = 2017-06-15 21:28:18
----
Path = golang-1.7.6-1.el6.i686.cpio.xz
Size = 1039008
Created = 2017-06-15 21:28:18
--
Path = golang-1.7.6-1.el6.i686.cpio.xz
Type = xz
Physical Size = 1039008
Method = LZMA2:19 SHA256
Streams = 1
Blocks = 1

Everything is Ok

Size:       12217076
Compressed: 1244080

C:\Users\kaito\Documents\tmp>dir /S /B
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.rpm
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686\golang-1.7.6-1.el6.i686.cpio
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.cpio\golang-1.7.6-1.el6.i686.cpio
```

### Step 2: Extract the CPIO file
```
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686>dir /B
golang-1.7.6-1.el6.i686.cpio

C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686>"C:\Program Files\7-Zip\7z.exe" x -o* golang-1.7.6-1.el6.i686.cpio

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
1 file, 12217076 bytes (12 MiB)

Extracting archive: golang-1.7.6-1.el6.i686.cpio
--
Path = golang-1.7.6-1.el6.i686.cpio
Type = Cpio
Physical Size = 12217076
SubType = New ASCII

Everything is Ok

Folders: 126
Files: 1507
Size:       11964477
Compressed: 12217076

C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686>cd golang-1.7.6-1.el6.i686

C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686\golang-1.7.6-1.el6.i686>dir /B
etc
usr
```

### Extract Multiple RPM packages at same time
[7-Zip x (Extract with full paths) command](https://sevenzip.osdn.jp/chm/cmdline/commands/extract_full.htm) allows users to multiple RPM packages at same time.
If `7z.exe` is executed with `*.rpm` or `*.cpio`, all of RPM/CPIO packages under current directory including sub directories are extracted.

Please see an example as below:
```
C:\Users\kaito\Documents\tmp>dir /B
golang-1.7.6-1.el6.i686.rpm
golang-docs-1.7.6-1.el6.noarch.rpm

C:\Users\kaito\Documents\tmp>"C:\Program Files\7-Zip\7z.exe" x -o* *.rpm

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
2 files, 3700396 bytes (3614 KiB)

Extracting archive: golang-1.7.6-1.el6.i686.rpm
--
Path = golang-1.7.6-1.el6.i686.rpm
Type = Rpm
Physical Size = 1244080
Headers Size = 205072
CPU = i686
Host OS = linux
Created = 2017-06-15 21:28:18
----
Path = golang-1.7.6-1.el6.i686.cpio.xz
Size = 1039008
Created = 2017-06-15 21:28:18
--
Path = golang-1.7.6-1.el6.i686.cpio.xz
Type = xz
Physical Size = 1039008
Method = LZMA2:19 SHA256
Streams = 1
Blocks = 1

Everything is Ok

Extracting archive: golang-docs-1.7.6-1.el6.noarch.rpm
--
Path = golang-docs-1.7.6-1.el6.noarch.rpm
Type = Rpm
Physical Size = 2456316
Headers Size = 30432
CPU = noarch
Host OS = linux
Created = 2017-06-15 21:29:18
----
Path = golang-docs-1.7.6-1.el6.noarch.cpio.xz
Size = 2425884
Created = 2017-06-15 21:29:18
--
Path = golang-docs-1.7.6-1.el6.noarch.cpio.xz
Type = xz
Physical Size = 2425884
Method = LZMA2:19 SHA256
Streams = 1
Blocks = 1

Everything is Ok

Archives: 2
OK archives: 2
Files: 2
Size:       16094580
Compressed: 3700396

C:\Users\kaito\Documents\tmp>dir /S /B
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.cpio
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.rpm
C:\Users\kaito\Documents\tmp\golang-docs-1.7.6-1.el6.noarch.cpio
C:\Users\kaito\Documents\tmp\golang-docs-1.7.6-1.el6.noarch.rpm
C:\Users\kaito\Documents\tmp\golang-1.7.6-1.el6.i686.cpio\golang-1.7.6-1.el6.i686.cpio
C:\Users\kaito\Documents\tmp\golang-docs-1.7.6-1.el6.noarch.cpio\golang-docs-1.7.6-1.el6.noarch.cpio

C:\Users\kaito\Documents\tmp>"C:\Program Files\7-Zip\7z.exe" x -o* *.cpio

7-Zip [64] 16.04 : Copyright (c) 1999-2016 Igor Pavlov : 2016-10-04

Scanning the drive for archives:
2 folders, 2 files, 16094580 bytes (16 MiB)

Extracting archive: golang-1.7.6-1.el6.i686.cpio\golang-1.7.6-1.el6.i686.cpio
--
Path = golang-1.7.6-1.el6.i686.cpio\golang-1.7.6-1.el6.i686.cpio
Type = Cpio
Physical Size = 12217076
SubType = New ASCII

Everything is Ok

Extracting archive: golang-docs-1.7.6-1.el6.noarch.cpio\golang-docs-1.7.6-1.el6.noarch.cpio
--
Path = golang-docs-1.7.6-1.el6.noarch.cpio\golang-docs-1.7.6-1.el6.noarch.cpio
Type = Cpio
Physical Size = 3877504
SubType = New ASCII

Everything is Ok

Archives: 2
OK archives: 2
Folders: 135
Files: 1652
Size:       15818363
Compressed: 16094580

C:\Users\kaito\Documents\tmp>dir /B
golang-1.7.6-1.el6.i686
golang-1.7.6-1.el6.i686.cpio
golang-1.7.6-1.el6.i686.rpm
golang-docs-1.7.6-1.el6.noarch
golang-docs-1.7.6-1.el6.noarch.cpio
golang-docs-1.7.6-1.el6.noarch.rpm
```
