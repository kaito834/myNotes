This is my tutorial for [Yubikey](https://www.yubico.com/products/yubikey-hardware/), multi protocol USB security keys developed by Yubico.

# What is YubiKey
Yubikey is a security key device, which is developed by [Yubico](https://www.yubico.com/products/yubikey-hardware/).
Yubikey consists of a few product series, and support [security functions below](https://www.yubico.com/products/yubikey-hardware/compare-yubikeys/).
Yubikey users can use Yubikey as 2 factor authentication device, secure key storage and other security purpose.
Also, [a lot of Web service](https://www.yubico.com/solutions/) have already integrated with Yubikey.

- Secure Static Passwords
- Yubico OTP
- OATH – HOTP (Event)
- OATH – TOTP (Time)
- Smart Card (PIV-Compatible)
- OpenPGP
- FIDO U2F (Universal Second Factor)
- Secure Element

# Use Yubikey at 2 Factor Authentication(2FA)
## My Environments
- [Yubikey 4](https://www.yubico.com/products/yubikey-hardware/yubikey4/)
  * Bought via [Amazon.co.jp](https://www.amazon.co.jp/gp/product/B018Y1Q71M/)
- Windows 10 Professional
- [Yubico Authenticator](https://www.yubico.com/support/knowledge-base/categories/articles/yubico-authenticator-download/)

## Procedures
1. Install Yubico Authenticator
2. Launch Yubico Authenticator and insert Yubikey in USB slot
3. Select File > Add Credential at the menu bar on Yubico Authenticator
4. Launch Web browser and open the 2FA registration page of each Web service
5. Confirm the secret or some parameters for 2FA at the page, and then go back to Yubico Authenticator
  * Usually, the secret and parameters are provided by QR code
  * Please see "Key URI format at QR code" section below
6. Input name and the secret, select some credential type and then click "Add credential" button
  * You can use to click "Scan a QR code" button instead of inputting parameters manually
7. Go back to the registration page on Web browser
8. Input one time password generated by Yubico Authenticator
9. Congratulation! Complete to enable 2FA authentication by YubiKey

**Note: You may want to enable not only Yubikey, but also other app like Google Authenticator. Then, you need to set the secret the other app at same time.**

### Key URI format at QR code
According to [Key Uri Format at google-authenticator repositry](https://github.com/google/google-authenticator/wiki/Key-Uri-Format), Key URI format may be as follows:
```
otpauth://TYPE/LABEL?PARAMETERS
```

For this procedures, input/select the values on Key URI into the fields at Yubico Authenticator.

| Parameter of Key URI | Target field on Yubico Authenticator | Note                                      |
| -------------------- | ------------------------------------ | ----------------------------------------- |
| Label                | Name                                 | Input url-decoded value into target field |
| Secret               | Secret key                           | The value is encoded by Base32            |
| Types                | Credential type - OATH Type          | TOTP / HOTP                               |
| Digits (Optional)    | Credential type - Number of digits   | 6 / 8                                     |
| Algorithm (Optional) | Credential type - Algorithm          | SHA-1 / SHA-256                           |

## Links for 2 Factor Authentication
- Google
  * [Turn on 2-Step Verification, Google Account Help](https://support.google.com/accounts/answer/185839?hl=en)
  * [Install Google Authenticator, Google Account Help](https://support.google.com/accounts/answer/1066447?hl=en)
    + Setting up Google Authenticator on multiple devices
- Amazon
  * [Amazon.co.jp ヘルプ: 2段階認証について](https://www.amazon.co.jp/gp/help/customer/display.html/?ie=UTF8&nodeId=202025410) (in Japanese)
  * [Amazon.co.jp ヘルプ: 2段階認証の設定を変更する](https://www.amazon.co.jp/gp/help/customer/display.html/?ie=UTF8&nodeId=202073720) (in Japanese)
- GitHub
  * [Configuring two-factor authentication via a TOTP mobile app, GitHub Help](https://help.github.com/articles/configuring-two-factor-authentication-via-a-totp-mobile-app/)
- Dropbox
  * [Enable two-step verification  – Dropbox](https://www.dropbox.com/help/security/enable-two-step-verification)
- Facebook
  * [What is two-factor authentication and how does it work? | Facebook Help Center](https://www.facebook.com/help/148233965247823)
- Amazon Web Service(AWS)
  * [Using Multi-Factor Authentication (MFA) in AWS - AWS Identity and Access Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- Tumblr
  * [Two-factor authentication - Help Center](https://tumblr.zendesk.com/hc/en-us/articles/226270148-Two-factor-authentication)

# SSH public key authentication by YubiKey
There are 2 ways for SSH public key authentication by YubiKey. The procedures of way 1. are explained in this document.

1. [Use certificate as SSH key stored in YubiKey with PIV](https://developers.yubico.com/PIV/)
2. [Use PGP key pair as SSH key stored in YubiKey](https://developers.yubico.com/PGP/SSH_authentication/)

## My Environment
- YubiKey 4
- Windows 10 Professional
- `openssl` included in Git for Windows
- [Yubico PIV Tool](https://developers.yubico.com/yubico-piv-tool/)
- [OpenSC](https://github.com/OpenSC/OpenSC/wiki)
- [putty-cac](https://github.com/NoMoreFood/putty-cac/releases)

## Procedures: Use certificate as SSH key stored in YubiKey
This procedures allow you to log in github.com via SSH public key authentication by YubiKey.

Also, this procedures are based on [dev.yubico: Using PIV for SSH through PKCS11](https://developers.yubico.com/PIV/Guides/SSH_with_PIV_and_PKCS11.html), and I noted something interesting and issue happened on my work at "Notes for the procedures" section below.

1. Download the latest Yubico PIV Tool and extract it
2. Insert YubiKey into USB slot
  - Change [PIN/PUK, Management Key(MGM)](https://developers.yubico.com/PIV/Introduction/Admin_access.html) if you don't change default value of PIN/PUK, MGM  
3. Generate RSA key pair by `openssl` command (Refer to [dev.yubico:Generating keys using OpenSSL](https://developers.yubico.com/PIV/Guides/Generating_keys_using_OpenSSL.html))
  - NOTE: My YubiKey 4 is vulnerable to [YSA-2017-01/CVE-2017-15361](https://www.yubico.com/support/security-advisories/ysa-2017-01/), so RSA key pair is generated at out of YubiKey
4. Import RSA private key into YubiKey slot 9a, and then delete the private key from your disk
5. Generate self-signed certificate
6. Import the self-signed certificate into YubiKey
7. Install OpenSC and confirm file path of `opensc-pkcs11.dll`
  - Default install path: `C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll`
8. Download putty-cac and run the putty-cac
9. Configure setting below on putty-cac window
  - Connection > SSH > Certificate: Click [Set PKCS Cert...] button and select `opensc-pkcs11.dll` at step 7
  - Select certificate for SSH authentication based on CN value defined at step 5.
  - Click [Copy to Clipboard] button and add copied SSH public key into your GitHub account (Refer to [GitHub document](https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account))
  - Confirm that checkbox:"Attempt certificate authentication" is enabled
10. Input `github.com` at Host name field and click [Open] button
11. Start SSH session, and then input `git` as log in user
12. Open putty authentication dialog and input your PIN code
13. Close SSH session silently if you succeeded to log in
  - NOTE: GitHub does not provide shell access (Refer to [GitHub document](https://help.github.com/en/articles/testing-your-ssh-connection))
14. Congratulation!

```
# Step 2.1. (Windows command prompt)
$> yubico-piv-tool.exe -a version
Application version 4.3.4 found.

$> yubico-piv-tool.exe -a change-pin
Enter pin: <input current PIN code>
Enter new pin: <input new PIN code>
Verifying - Enter new pin: <input new PIN code>
Successfully changed the pin code.

$> yubico-piv-tool.exe -a change-puk
Enter puk: <input current PUK code>
Enter new puk: <input new PUK code>
Verifying - Enter new puk: <input new PUK code>
Successfully changed the puk code.

$> yubico-piv-tool.exe -a set-mgm-key
Enter new management key: <input new management key>
Verifying - Enter new management key: <input new management key>
Successfully set new management key.

# Step 3. (Git Bash)
$ openssl version
OpenSSL 1.1.1a  20 Nov 2018
$ openssl genrsa -out key.pem 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
................+++++
.........+++++
e is 65537 (0x010001)
$ openssl rsa -in key.pem -outform PEM -pubout -out public.pem
writing RSA key

# Step 4. (Windows command prompt)
$> yubico-piv-tool.exe -s 9a -a import-key -i key.pem -k
Enter management key: <input your management key>
Successfully imported a new private key.
$> del key.pem

# Step 5. (Windows command prompt)
$> yubico-piv-tool.exe -a verify-pin -a selfsign-certificate -s 9a -S "/CN=SSH key/" -i public.pem -o cert.pem
Enter PIN: <input PIN code for YubiKey>
Successfully verified PIN.
Successfully generated a new self signed certificate.

# Step 6. (Windows command prompt)
$> yubico-piv-tool.exe -a import-certificate -s 9a -i cert.pem -k
Enter management key: <input your management key>
Successfully imported a new certificate.
```

### Notes for the Procedures
#### Error: Failed authentication with the application
"Failed authentication with the application" error may happen if you don't run yubico-piv-tool.exe without `-k` option.
You can find explanation about the error in [Yubico PIV Tool Command Line Guide](https://www.yubico.com/wp-content/uploads/2016/05/Yubico_PIV_Tool_Command_Line_Guide_en.pdf).

#### Failed CAPI cert approach at putty-cac
putty-cac allows you to authenticate public key stored in YubiKey via Windows native API; Setting of Connection > SSH > Certificate: [Set CAPI Cert...].
However, I didn't succeed the approach on my end, because putty authentication dialog at step 12. didn't open on the approach.
According to [a support thread on yubico](https://forum.yubico.com/viewtopica529.html?p=9865), it supposes that windows driver replaced by Windows Update causes this issue.

Therefore, `opensc-pkcs11.dll` in OpenSC is used in the procedures above as alternative approach.

#### GitHub doesn't allow their user to add vulnerable SSH public key at GitHub
If you try to add vulnerable SSH public key for YSA-2017-01/CVE-2017-15361 at GitHub, the action will be failed with error messages below.
According to [issue 127 on yubico-piv-tool](https://github.com/Yubico/yubico-piv-tool/issues/127), GitHub assumes to detect vulnerable SSH public key and block to add the key at GitHub.
> Key is weak. GitHub recommends using ssh-keygen to generate a RSA key of at least 2048 bits.

By the way, messages below will be outputted if you run `generate` action via yubico-piv-tool at vulnerable YubiKey for YSA-2017-01/CVE-2017-15361.
```
$> yubico-piv-tool.exe -s 9a -A RSA2048 -a generate -o public.pem
YubiKey serial number 5436356 is affected by vulnerability CVE-2017-15361 (ROCA) and should be replaced. On-chip key generation was permitted by default, but is not recommended.  The default behavior will change in a future Yubico release.  See YSA-2017-01 <https://www.yubico.com/support/security-advisories/ysa-2017-01/> for additional information on device replacement and mitigation assistance.
Successfully generated a new private key.
```

# References
- Yubico
  * [Downloads Archives](https://www.yubico.com/support/knowledge-base/categories/downloads/)
  * [Documentation Archives](https://www.yubico.com/support/knowledge-base/categories/guides/)
  * [OATH, dev.yubico](https://developers.yubico.com/OATH/)
    + Helpful figure in Use OATH with the YubiKey section
  * [How to Use Your YubiKey With Authenticator Codes | Yubico](https://www.yubico.com/support/knowledge-base/categories/articles/how-to-use-your-yubikey-with-authenticator-codes/)
  * [Flexible Modern Authentication with the Multi-Protocol YubiKey, Yubico Blog](https://www.yubico.com/2017/07/flexible-modern-authentication-with-multiprotocol-yubikey/)
    + One-Time Passwords(OTP), CCID(smart card) - PIV, OpenPGP and OATH, - and Universal 2nd Factor(U2F)
- [YubiKey製品一覧, CloudGate](https://www.cloudgate.jp/yubikey.html) (in Japanese)
- [秘密鍵、管理してますか? YubiKeyで鍵の一元管理とSSH接続、２段階認証の高速化を試す, Qiita](http://qiita.com/dseg/items/77d77467970b1b510285) (in Japanese)
- [yubikeyでセキュリティ筋力を鍛える](http://joemphilips.com/post/yubikey_setup/)
- [YubiKeyのPIVカードでSSHする](https://www.cuspy.org/diary/2015-08-11-yubikey-piv-ssh/) (in Japanese)
- [Putty CAC で SSH に YubiKey を使う(OpenSC編)](https://blog.haniyama.com/2018/02/02/yubikey-ssh-opensc/) (in Japanese)
- [PIV Usage Guides: Enable SSH](https://piv.idmanagement.gov/engineering/ssh/)
- [QR Code Editor (in Japanese)](http://www.psytec.co.jp/freesoft/01/)
