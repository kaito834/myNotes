#!/bin/sh
#
# this script was executed on CentOS 6.5.
# $ sh --version
# GNU bash, version 4.1.2(1)-release (x86_64-redhat-linux-gnu)

# pp.74-75 3.2.12 readコマンド, 入門UNIXシェルプログラミング, http://www.amazon.co.jp/gp/product/4797321946
echo -n 'Please input url: '
read url
echo -n 'Please input User-Agent: '
read user_agent

# pp.69-72 3.2.7 evalコマンド, 入門UNIXシェルプログラミング
# http://labs.opentone.co.jp/?p=5651
# pp.12-13 1.5.3 ダブルクォーテーション("), 入門UNIXシェルプログラミング
curlStr="curl -v -n -X POST -d a=aaa -d b=aaa -H \"User-Agent: $user_agent\" $url"
echo '==='
echo $curlStr
eval $curlStr
echo ''
echo '==='
