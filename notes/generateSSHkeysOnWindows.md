## File Formats for SSH Keys
There have been three file formats for SSH keys. According to [PuTTY document](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-conversions), "_SSH-2 private keys have no standard format._" 
- OpenSSH format
- [PuTTY's native format(*.PPK)](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-savepriv)
- SECSH format, [RFC4716](https://tools.ietf.org/html/rfc4716)

## Tools
- [ssh-keygen](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen&sec=1)
  - "[Git for Windows](https://windows.github.com/)" contains it.
- [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  - "[WinSCP(package version)](http://winscp.net/eng/docs/ui_puttygen#obtaining_and_starting_puttygen)" and "[SourceTree for Windows](https://www.sourcetreeapp.com/)" contain it.
- [Tera Term](http://ttssh2.sourceforge.jp/manual/en/usage/ssh.html#generate)

## References
- [SSHの秘密鍵について - 禿散らかしてごめんなさい](http://d.hatena.ne.jp/machua/20110809/1312899353) (in Japanese)
- [Generating SSH keys, GitHub Help](https://help.github.com/articles/generating-ssh-keys/)

## Appendix 1. Tips for SSH
###Convert SECSH(RFC4716) format to others
This is quoted from http://qiita.com/marcie001/items/47a23cfeed00db783d39 (in Japanese).
```
$ ssh-keygen -i -f id_rsa.pub >> ~/.ssh/authorized_keys
```

###Identify a size of SSH key
This is quoted from http://d.hatena.ne.jp/hnw/20140705 (in Japanese).
```
$ ssh-keygen -l -f $HOME/.ssh/id_rsa.pub
```

### Use multiple SSH keys
This is quoted from http://d.hatena.ne.jp/MIZUNO/20080705/1215238138 (in Japanese).
```
$ ssh -i ~/.ssh/id_rsa.hoge hoge@fuga.com
```
The _ssh_ command searchs SSH keys automatically if the SSH keys are set in ~/.ssh/config.
```
IdentityFile ~/.ssh/id_rsa
IdentityFile ~/.ssh/id_rsa.hoge
IdentityFile ~/.ssh/id_rsa.foo
```
