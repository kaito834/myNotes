This is my notes associated with [Secure Shell(SSH)](https://en.wikipedia.org/wiki/Secure_Shell).

# Public Key Authentication
## Register public key for someone on remote host
"13.2.4. Using Key-Based Authentication" on [Red Hat Enterprise Linux 6
Deployment Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/s2-ssh-configuration-keypairs.html)
> 5.
> Copy the content of ~/.ssh/id_rsa.pub into the ~/.ssh/authorized_keys on the machine to which you want
> to connect, appending it to its end if the file already exists.

## Use multiple SSH keys
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

## Ignore validation of SSH host key
The *ssh* command will validate SSH host key of remote host by default, then
it compares the host key with one recorded in known_hosts.
If the validation fails, SSH connection refused by the *ssh* command itself.

This validation is good to protect man-in-the-middle attack. But, it is not
efficient for developing environment on localhost like [CentOS on Virtualbox](https://github.com/kaito834/myNotes/blob/master/notes/myTutorialForVagrantOnWindows.md#setup-centos-653-by-vagrant).
The SSH host key will change whenever CentOS virtual machine is created,
so the validation of SSH host key will fail once the first SSH host key is
registered in known_hosts; Please see the example below:
```
$ ssh -i .vagrant/machines/default/virtualbox/private_key -p 2222 vagrant@127.0.0.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
fc:9b:3f:5a:1a:25:b2:c2:c6:1e:6e:86:64:ed:63:e6.
Please contact your system administrator.
Add correct host key in /c/Users/kaito/.ssh/known_hosts to get rid of this message.
Offending RSA key in /c/Users/kaito/.ssh/known_hosts:7
RSA host key for [127.0.0.1]:2222 has changed and you have requested strict checking.
Host key verification failed.
```

Ignoring known_hosts is useful in this situation. The options '-o StrictHostKeyChecking=no' and
'-o UserKnownHostsFile=/dev/null' allow you to ignore known_hosts. For *StrictHostKeyChecking* and
*UserKnownHostsFile*, please see the [manual for sshd_config](http://man.openbsd.org/OpenBSD-current/man5/ssh_config.5).

When *ssh* command with these two options is executed below, you can connect remote host
by SSH without the validation of SSH host key. Then, the *ssh* command write the host key to
/dev/null; equal to do nothing.
```
$ ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i .vagrant/machines/default/virtualbox/private_key -p 2222 vagrant@127.0.0.1
Warning: Permanently added '[127.0.0.1]:2222' (RSA) to the list of known hosts.
[vagrant@vagrant-centos65 ~]$
```

# SSH Key Operation
## File Formats for SSH Keys
There have been three file formats for SSH keys. According to [PuTTY document](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-conversions), "_SSH-2 private keys have no standard format._"
- OpenSSH format
- [PuTTY's native format(*.PPK)](http://the.earth.li/~sgtatham/putty/0.64/htmldoc/Chapter8.html#puttygen-savepriv)
- SECSH format, [RFC4716](https://tools.ietf.org/html/rfc4716)

## Key Generation
### Tools to generate SSH key pair
- [ssh-keygen](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen&sec=1)
  - "[Git for Windows(msysgit)](https://msysgit.github.io/)" and "[GitHub for Windows](https://windows.github.com/)" contain it.
- [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  - "[WinSCP(package version)](http://winscp.net/eng/docs/ui_puttygen#obtaining_and_starting_puttygen)" and "[SourceTree for Windows](https://www.sourcetreeapp.com/)" contain it.
- [Tera Term](http://ttssh2.sourceforge.jp/manual/en/usage/ssh.html#generate)

#### Example: Generate SSH key pairs by ssh-keygen
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
$ echo "IdentityFile ~/.ssh/id_rsa-20150802" >> ~/.ssh/config
```

## Tips for SSH Key Operation
### Convert SECSH(RFC4716) format to others
This is quoted from http://qiita.com/marcie001/items/47a23cfeed00db783d39 (in Japanese).
```
$ ssh-keygen -i -f id_rsa.pub >> ~/.ssh/authorized_keys
```

### Identify a size of SSH key
This is quoted from http://d.hatena.ne.jp/hnw/20140705 (in Japanese).
```
$ ssh-keygen -l -f $HOME/.ssh/id_rsa.pub
```

### Calculate the fingerprint for SSH key
You can use '[ssh-keygen](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh-keygen.1?query=ssh-keygen)' command with options '-l' and '-f' if you would like know the fingerprint for a SSH key. Then, the option '-E' allows you to change hash algorithm for fingerprint; I know this from [the post](http://superuser.com/questions/421997/what-is-a-ssh-key-fingerprint-and-how-is-it-generated) on superuser.
```
$ ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub
$ ssh-keygen -l -E md5 -f ~/.ssh/id_rsa.pub
```

# Use SSH key pair on Web services
## How do I know SSH host key on Web services
- GitHub
  - "[_What are GitHub's SSH key fingerprints?_](https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/)" on GitHub Help shows me its SSH host key.
- Amazon EC2
  - According to [Amazon EC2 document](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html), I can know SSH host key on each EC2 instances by AWS CLI or Amazon EC2 CLI.
  - Or, according to [WinSCP document](http://winscp.net/eng/docs/guide_amazon_ec2), I can know SSH host key on _Instances_ page of Amazon EC2 console.

# References
- [SSHの秘密鍵について - 禿散らかしてごめんなさい](http://d.hatena.ne.jp/machua/20110809/1312899353) (in Japanese)
- [Generating SSH keys, GitHub Help](https://help.github.com/articles/generating-ssh-keys/)
- [ssh_config, OpenBSD manual pages](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man5/ssh_config.5)
- [OpenSSHの警告メッセージを黙らせる](https://siguniang.wordpress.com/2014/02/28/get-rid-of-openssh-warning-message/) (In Japanese)
