# Set up AWS CLI on Windows
## Environment
* Windows 10
* Python 3.6.3

## Install
Launch command prompt and install the latest aws-cli via pip based on [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#awscli-install-windows-pip).

```
$> python --version
Python 3.6.3

$> pip install awscli --user
Collecting awscli
  Downloading https://files.pythonhosted.org/packages/c8/1b/9263b91935816412dec18bd0dd5c690b5d69a4429639faa127ddc3e12f9f/awscli-1.16.73-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 2.2MB/s
Collecting rsa<=3.5.0,>=3.1.2 (from awscli)
  Downloading https://files.pythonhosted.org/packages/e1/ae/baedc9cb175552e95f3395c43055a6a5e125ae4d48a1d7a924baca83e92e/rsa-3.4.2-py2.py3-none-any.whl (46kB)
    100% |████████████████████████████████| 51kB 1.6MB/s
Collecting PyYAML<=3.13,>=3.10 (from awscli)
  Downloading https://files.pythonhosted.org/packages/fb/51/0c49c6caafe8d9a27ad9b0ca9f91adda5a5072b9efbbe7585fb97a4c71c4/PyYAML-3.13-cp36-cp36m-win32.whl (188kB)
    100% |████████████████████████████████| 194kB 2.2MB/s
Collecting botocore==1.12.63 (from awscli)
  Downloading https://files.pythonhosted.org/packages/2f/63/fa7652b2477726451d70c8ee2b4e795a9fa5e200b2426e2a2d08437e5880/botocore-1.12.63-py2.py3-none-any.whl (5.1MB)
    100% |████████████████████████████████| 5.1MB 1.3MB/s
Collecting s3transfer<0.2.0,>=0.1.12 (from awscli)
  Downloading https://files.pythonhosted.org/packages/d7/14/2a0004d487464d120c9fb85313a75cd3d71a7506955be458eebfe19a6b1d/s3transfer-0.1.13-py2.py3-none-any.whl (59kB)
    100% |████████████████████████████████| 61kB 2.0MB/s
Collecting docutils>=0.10 (from awscli)
  Downloading https://files.pythonhosted.org/packages/36/fa/08e9e6e0e3cbd1d362c3bbee8d01d0aedb2155c4ac112b19ef3cae8eed8d/docutils-0.14-py3-none-any.whl (543kB)
    100% |████████████████████████████████| 552kB 2.2MB/s
Collecting colorama<=0.3.9,>=0.2.5 (from awscli)
  Downloading https://files.pythonhosted.org/packages/db/c8/7dcf9dbcb22429512708fe3a547f8b6101c0d02137acbd892505aee57adf/colorama-0.3.9-py2.py3-none-any.whl
Requirement already satisfied: pyasn1>=0.1.3 in c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages (from rsa<=3.5.0,>=3.1.2->awscli) (0.3.7)
Collecting urllib3<1.25,>=1.20; python_version >= "3.4" (from botocore==1.12.63->awscli)
  Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 122kB 2.2MB/s
Collecting jmespath<1.0.0,>=0.7.1 (from botocore==1.12.63->awscli)
  Downloading https://files.pythonhosted.org/packages/b7/31/05c8d001f7f87f0f07289a5fc0fc3832e9a57f2dbd4d3b0fee70e0d51365/jmespath-0.9.3-py2.py3-none-any.whl
Collecting python-dateutil<3.0.0,>=2.1; python_version >= "2.7" (from botocore==1.12.63->awscli)
  Downloading https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl (225kB)
    100% |████████████████████████████████| 235kB 3.3MB/s
Requirement already satisfied: six>=1.5 in c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages (from python-dateutil<3.0.0,>=2.1; python_version >= "2.7"->botocore==1.12.63->awscli) (1.10.0)
Installing collected packages: rsa, PyYAML, urllib3, jmespath, python-dateutil, docutils, botocore, s3transfer, colorama, awscli
  The scripts pyrsa-decrypt-bigfile.exe, pyrsa-decrypt.exe, pyrsa-encrypt-bigfile.exe, pyrsa-encrypt.exe, pyrsa-keygen.exe, pyrsa-priv2pub.exe, pyrsa-sign.exe and pyrsa-verify.exe are installed in 'C:\Users\kaito\AppData\Roaming\Python\Python36\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyYAML-3.13 awscli-1.16.73 botocore-1.12.63 colorama-0.3.9 docutils-0.14 jmespath-0.9.3 python-dateutil-2.7.5 rsa-3.4.2 s3transfer-0.1.13 urllib3-1.24.1
```

Close command prompt. After that, you add `%APPDATA%\Python\Python36\Scripts` to
PATH environment variable. Then, launch command prompt again.

NOTE:
Command path on [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#awscli-install-windows-path)
isn't correct as of Dec. 13, 2018. Please check [issue #3181 on aws-cli GitHub repogitory](https://github.com/aws/aws-cli/issues/3181).
```
$> aws --version
拡張子 .py のファイルの関連付けが見つかりません
aws-cli/1.16.73 Python/3.6.3 Windows/10 botocore/1.12.63
```
