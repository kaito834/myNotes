## Environments
- Windows 8.1
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 5.0.2
- [Vagrant](https://www.vagrantup.com/downloads.html) 1.7.4
- [Git for Windows(msysgit)](https://msysgit.github.io/) 1.9.5.msysgit.1

## Setup CentOS 6.5.3 by Vagrant
Download box files for CentOS 6.5.3. The url is linked on http://www.vagrantbox.es/.
```
$> vagrant box add CentOS65 https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'CentOS65' (v0) for provider:
    box: Downloading: https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box
    box: Progress: 100% (Rate: 812k/s, Estimated time remaining: --:--:--)
==> box: Successfully added box 'CentOS65' (v0) for 'virtualbox'!

$> tree /F %USERPROFILE%\.vagrant.d
(snip)
C:\USERS\KAITO\.VAGRANT.D
│  insecure_private_key
│  setup_version
│
├─boxes
│  └─CentOS65
│      └─0
│          └─virtualbox
│                  box-disk1.vmdk
│                  box-disk2.vmdk
│                  box.ovf
│                  metadata.json
│                  Vagrantfile
│
├─data
│  │  checkpoint_cache
│  │  checkpoint_signature
│  │
│  └─machine-index
│          index.lock
│
├─gems
│  └─ruby
│      └─2.0.0
├─rgloader
│      loader.rb
│
└─tmp
```

Initialize the box files on %USERPROFILE%\vagrant\CentOS65. I don't edit Vagrantfile in this tutorial.
```
$> vagrant init CentOS65
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
```

Boot CentOS 6.5.3 on Virtualbox by Vagrant.
```
$> vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'CentOS65'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: CentOS65_default_1439733848457_30266
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 => 2222 (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection timeout. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installedon
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 4.3.6
    default: VirtualBox Version: 5.0
==> default: Mounting shared folders...
    default: /vagrant => C:/Users/kaito/vagrant/CentOS65

$> vagrant status
Current machine states:

default                   running (virtualbox)

The VM is running. To stop this VM, you can run `vagrant halt` to
shut it down forcefully, or you can run `vagrant suspend` to simply
suspend the virtual machine. In either case, to restart it again,
simply run `vagrant up`.

$> tree /F
(snip)
C:.
│  Vagrantfile
│
└─.vagrant
    └─machines
        └─default
            └─virtualbox
                    action_provision
                    action_set_name
                    creator_uid
                    id
                    index_uuid
                    private_key
                    synced_folders

$> tree /F "%USERPROFILE%\VirtualBox VMs"
(snip)
C:\USERS\KAITO\VIRTUALBOX VMS
└─CentOS65_default_1439733848457_30266
    │  box-disk1.vmdk
    │  box-disk2.vmdk
    │  CentOS65_default_1439733848457_30266.vbox
    │  CentOS65_default_1439733848457_30266.vbox-prev
    │
    └─Logs
            VBox.log
            VBoxStartup.log
```

I can log in CentOS 6.5.3 via ssh. Then, I use ssh which is installed with msysgit in this tutorial;
```
$ ssh -i .vagrant/machines/default/virtualbox/private_key -p 2222 vagrant@127.0.0.1
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
RSA key fingerprint is 38:8b:ec:e7:14:fc:fc:ce:73:c1:94:b2:c6:3c:cf:59.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[127.0.0.1]:2222' (RSA) to the list of known hosts.
Last login: Sun Aug 16 14:20:47 2015 from 10.0.2.2
[vagrant@vagrant-centos65 ~]$ cat /etc/centos-release
CentOS release 6.5 (Final)
```

Halt the CentOS by Vagrant.
```
$> vagrant halt default
==> default: Attempting graceful shutdown of VM...

$> vagrant status
Current machine states:

default                   poweroff (virtualbox)

The VM is powered off. To restart the VM, simply run `vagrant up`
```

I can destory the CentOS on Virtualbox if it is not necessary.
```
$> vagrant destroy default
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Destroying VM and associated drives...

$> tree /F
(snip)
C:.
│  Vagrantfile
│
└─.vagrant
    └─machines
        └─default
            └─virtualbox

$> tree /F "%USERPROFILE%\VirtualBox VMs"
(snip)
C:\USERS\KAITO\VIRTUALBOX VMS
サブフォルダーは存在しません
```

## The Options of vagrant up
'vagrant up' has some options. The options are below;
```
$> vagrant up -h
Usage: vagrant up [options] [name]

Options:

        --[no-]provision             Enable or disable provisioning
        --provision-with x,y,z       Enable only certain provisioners, by type.
        --[no-]destroy-on-error      Destroy machine if any fatal error happens(default to true)
        --[no-]parallel              Enable or disable parallelism if provider supports it
        --provider PROVIDER          Back the machine with a specific provider
    -h, --help                       Print this help
```

Vagrant doesn't do provisioning if 'vagrant up' with --no-provision option would be executed.
```
$> vagrant up --no-provision

Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'CentOS65'...
(snip)
==> default: Machine not provisioned because `--no-provision` is specified.
```

## References
- [Windows上でVirtualBox+Vagrant+CentOSによる仮想環境構築 - Qiita](http://qiita.com/hiroyasu55/items/11a4c996b0c62450940f) (in Japanese)
