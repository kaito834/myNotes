#!/bin/sh
# A shell script for provisioning Python 3.4.3 on CentOS 6.5.x
#
# http://docs.vagrantup.com/v2/provisioning/shell.html
# config.vm.provision "shell", path: "setupPython3.4.3.sh"
#
# Ref. https://github.com/kaito834/myNotes/blob/master/notes/setupPython3OnCentOS.md

# Exit this shell script if Python 3.4.3 has already installed
if [ -d /usr/local/python34 ]; then
  echo "[!] Python 3.4.3 has already installed on /usr/local/python34 ."
  exit 1
fi

# Install rpm packages
echo "yum -q -y install ..."
sudo yum -q -y install zlib-devel openssl-devel readline-devel ncurses-devel sqlite-devel expat-devel bzip2-devel tcl-devel tk-devel gdbm-devel
echo "yum -q -y install ... [Done]"

# Install Python 3.4.3
# ToDo: Verify .tgz.asc by gpg
mkdir /tmp/python34; cd /tmp/python34
echo "curl --silent -O Python-3.4.3.tgz ..."
curl --silent -O https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
echo "curl --silent -O Python-3.4.3.tgz ... [Done]"
echo "Install Python 3.4.3 ..."
tar zxvf Python-3.4.3.tgz
cd ./Python-3.4.3
./configure --prefix=/usr/local/python34
make
sudo make altinstall
# echo 'export PATH=/usr/local/python34/bin:$PATH' >> ~/.bashrc
# source ~/.bashrc
echo "Install Python 3.4.3 ... [Done]"

# Update pip and install Python packages
echo "Upgrade pip ..."
sudo /usr/local/python34/bin/pip3.4 install -q --upgrade pip
echo "Upgrade pip ... [Done]"
echo "Install Python packages ..."
sudo /usr/local/python34/bin/pip3.4 install -q pycrypto
sudo /usr/local/python34/bin/pip3.4 install -q websocket-client
sudo /usr/local/python34/bin/pip3.4 freeze
echo "Install Python packages ... [Done]"

exit 0
