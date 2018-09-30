#!/bin/sh
# Refer to https://qiita.com/magicant/items/f3554274ee500bddaca8
set -eu

# mktemp command is a safe way if you need to create temporary file at shell script
# References:
# https://fumiyas.github.io/2013/12/06/tempfile.sh-advent-calendar.html
# http://www.usupi.org/sysad/180.html
tmpFile=`mktemp`
outputFile='sortedFile.txt'

echo 'Please input text for sorting:'
# Example:
# abc
# aaa
# acd
cat > ${tmpFile}
echo ''
echo "* Created temp file: ${tmpFile}"

sort ${tmpFile} > ${outputFile}
echo "* Sorted ${tmpFile} and outputted the result into ${outputFile}"

rm ${tmpFile}
echo "* Deleted temp file: ${tmpFile}"
