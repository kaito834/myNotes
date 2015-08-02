## Generate SSH key pairs by ssh-keygen
I generated SSH key pairs whose keys are RSA 2048bits by [ssh-keygen](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen&sec=1) on Windows 10. Then, I used the ssh-keygen installed with git 1.9.5.msysgit.1. Options, '-b 2048' and '-t rsa', are default on this ssh-keygen.
```
$ ssh-keygen -b 2048 -t rsa -C 'Generated at Aug 2, 2015.'
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/kaito/.ssh/id_rsa): /c/Users/kaito/.ssh/id_rsa-20150802
Enter passphrase (empty for no passphrase):***
Enter same passphrase again:***
Your identification has been saved in /c/Users/kaito/.ssh/id_rsa-20150802.
Your public key has been saved in /c/Users/kaito/.ssh/id_rsa-20150802.pub.
The key fingerprint is:
db:a1:1a:(snip) Generated at Aug 2, 2015.
The key's randomart image is:
(snip)
```

## References
### Tools
- [ssh-keygen](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen&sec=1)
  - "[Git for Windows(msysgit)](https://msysgit.github.io/)" and "[GitHub for Windows](https://windows.github.com/)" contain it.
- [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  - "[WinSCP(package version)](http://winscp.net/eng/docs/ui_puttygen#obtaining_and_starting_puttygen)" and "[SourceTree for Windows](https://www.sourcetreeapp.com/)" contain it.
- [Tera Term](http://ttssh2.sourceforge.jp/manual/en/usage/ssh.html#generate)

### File Formats for SSH Keys
There have been three file formats for SSH keys. According to [PuTTY document](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-conversions), "_SSH-2 private keys have no standard format._"
- OpenSSH format
- [PuTTY's native format(*.PPK)](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-savepriv)
- SECSH format, [RFC4716](https://tools.ietf.org/html/rfc4716)

### Others
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

## Appendix 2. How do I know SSH host key on Web services
- GitHub
  - "[_What are GitHub's SSH key fingerprints?_](https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/)" on GitHub Help shows me its SSH host key.
- Amazon EC2
  - According to [Amazon EC2 document](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html), I can know SSH host key on each EC2 instances by AWS CLI or Amazon EC2 CLI.
  - Or, according to [WinSCP document](http://winscp.net/eng/docs/guide_amazon_ec2), I can know SSH host key on _Instances_ page of Amazon EC2 console.
