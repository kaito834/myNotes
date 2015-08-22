## Environments
- CentOS 6.5.3 on VirtualBox
  - Created by Vagrant; Box file is [here](https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box)

## Steps for Setup Python 3.4.3
```sh
$ python -V
Python 2.6.6
$ sudo yum install zlib-devel openssl-devel readline-devel ncurses-devel sqlite-devel expat-devel bzip2-devel tcl-devel tk-devel gdbm-devel
$ cd ~
$ curl -O https://www.python.org/static/files/pubkeys.txt
$ gpg --import pubkeys.txt
$ curl -O https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
$ curl -O https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz.asc
$ gpg --verify Python-3.4.3.tgz.asc
$ md5sum Python-3.4.3.tgz
$ tar zxvf Python-3.4.3.tgz
$ cd Python-3.4.3
$ ./configure --prefix=/usr/local/python34
$ make
$ sudo make altinstall
$ echo 'export PATH=/usr/local/python34/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
$ python3.4 -V
Python 3.4.3
$ sudo /usr/local/python3.4/bin/pip3.4 install --upgrade pip
```

### (Optional) Steps for Setup some libraries from PyPI(Python Package Index)
```sh
$ sudo /usr/local/python3.4/bin/pip3.4 install pycrypto
$ sudo /usr/local/python3.4/bin/pip3.4 install websocket-client
$ python3.4
>>> import websocket
>>> websocket.__file__
'/usr/local/python3.4/lib/python3.4/site-packages/websocket/__init__.py'
>>> quit()
```

## ToDo
- Provisioning Python 3.4.3 when CentOS 6.5.3 will be up on VirtualBox by Vagrant.
  - https://docs.vagrantup.com/v2/provisioning/index.html

## References
- [2. Using Python on Unix platforms, Python 3.4.3 documentation](https://docs.python.org/3/using/unix.html)
- [OpenPGP Public Keys, Download Python | Python.org](https://www.python.org/downloads/)
- [CentOS 7.0 - Python 3.4.1 インストール（ソースビルド）！ - mk-mode BLOG](http://www.mk-mode.com/octopress/2014/08/31/centos-7-0-installation-of-python-by-src/) (in Japanese)
