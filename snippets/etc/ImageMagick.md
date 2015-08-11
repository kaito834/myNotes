### Create image which contain text
```
$> convert.exe -size 128x128 xc:gray -pointsize 20 -draw "text 10,64 sample" test.png
```
- [-size](http://www.imagemagick.org/script/command-line-options.php#size)
- [xc:somecolor](http://www.imagemagick.org/script/command-line-options.php#poly)
- [-pointsize](http://www.imagemagick.org/script/command-line-options.php#pointsize)
- [-draw](http://www.imagemagick.org/script/command-line-options.php#draw)


### Reference
- [ImageMagick: Install from Binary Distribution](http://www.imagemagick.org/script/binary-releases.php#windows)
- [ImageMagickでテスト用画像を大量に作成する | GENDOSU@NET](http://gendosu.jp/archives/1108) (in Japanese)
