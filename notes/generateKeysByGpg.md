# Generate openPGP public/private keys by GPG

### An Environment for this procedure
- [GnuPG(GPG)](https://www.gnupg.org/) 2.0.x on Windows 8.1
  - We should latest gpg if no specific reasons.
  - I have used one [Gpg4win](http://www.gpg4win.org/) contains 

### Procedure to generate keys
1. Define parameters
2. Generate public/private keys
3. Generate revocation certificate

#### 1. Define parameters
Before generating public/private keys, I will define some parameters. The parameters are following:
- Cryptographic algorithems
  - Usually, asymmetric key algorithms; RSA, DSA or others
  - Sometimes, cryptographic hash alogrithms; SHA-256 or others
- Size of key for cryptographic algorithm above
- Expiration date of the key

Firstly, I will select asymmetric algorithm that have not been compromised yet. We can know the alogrithms by some guidelines; for examples, [NIST SP 800-57](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57_part1_rev3_general.pdf) or [CRYPTREC暗号リスト](http://www.cryptrec.go.jp/images/cryptrec_ciphers_list_2013.pdf) (in Japanese). Secondly, I will define expiration date of the key. I usually define a year later as expiration date. Finally, I will define the size of key. I should define the size of which attackers would not be able to compromise a key. A web site provided by BlueKrypt, "[Cryptographic Key Length Recommendation](http://www.keylength.com/en/compare/)," is useful to define the size.

#### 2. Generate public/private keys
I generated public/private keys by gpg command. Then, cryptographic algorithem was **_RSA_**, size of the was **_2048 bits_** and expiration date was **_one year later_**; RSA 2048 bits has been default on gpg 2.0.27. Sorry, the result of gpg command has been in Japanase in this text:(

```
C:\Program Files (x86)\GNU\GnuPG> gpg --gen-key
gpg (GnuPG) 2.0.27; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

ご希望の鍵の種類を選択してください:
   (1) RSA と RSA (デフォルト)
   (2) DSA と Elgamal
   (3) DSA (署名のみ)
   (4) RSA (署名のみ)
あなたの選択は? 1
RSA 鍵は 1024 から 4096 ビットの長さで可能です。
鍵長は? (2048) 2048
要求された鍵長は2048ビット
鍵の有効期限を指定してください。
         0 = 鍵は無期限
      <n>  = 鍵は n 日間で期限切れ
      <n>w = 鍵は n 週間で期限切れ
      <n>m = 鍵は n か月間で期限切れ
      <n>y = 鍵は n 年間で期限切れ
鍵の有効期間は? (0)1y
鍵は04/11/16 18:48:54 東京 (標準時)で期限切れとなります
これで正しいですか? (y/N)y

GnuPGはあなたの鍵を識別するためにユーザIDを構成する必要があります。

本名: kaito
電子メール・アドレス: kaito834@gmail.com
コメント:
次のユーザIDを選択しました:
    "kaito <kaito834@gmail.com>"

名前(N)、コメント(C)、電子メール(E)の変更、またはOK(O)か終了(Q)?O
秘密鍵を保護するためにパスフレーズがいります。
(comment: Input window was pop-up by gpg that was cotained in Gpg4win)

gpg: AllowSetForegroundWindow(2284) failed: アクセスが拒否されました。

たくさんのランダム・バイトの生成が必要です。キーボードを打つ、マウスを動かす、
ディスクにアクセスするなどの他の操作を素数生成の間に行うことで、乱数生成器に
十分なエントロピーを供給する機会を与えることができます。
たくさんのランダム・バイトの生成が必要です。キーボードを打つ、マウスを動かす、
ディスクにアクセスするなどの他の操作を素数生成の間に行うことで、乱数生成器に
十分なエントロピーを供給する機会を与えることができます。
gpg: 鍵ABCDABCDを絶対的に信用するよう記録しました
(comment: I replaced original key-id to ABCDABCD)
公開鍵と秘密鍵を作成し、署名しました。

gpg: 信用データベースの検査
gpg: 「まぁまぁの信用」3、「全面的信用」1、PGP信用モデル
gpg: 深さ: 0  有効性:   7  署名:   0  信用: 0-, 0q, 0n, 0m, 0f, 7u
gpg: 次回の信用データベース検査は、2016-04-11です
pub   2048R/ABCDABCD 2015-04-12 [有効期限: 2016-04-11]
   フィンガー・プリント = XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX
uid       [  究極  ] kaito <kaito834@gmail.com>
sub   2048R/DCBADCBA 2015-04-12 [有効期限: 2016-04-11]
(comment: I replaced original key-id and fingerprint)
```

#### 3. Generate revocation certificate
After generating public/private keys, I generated revocation certificate for the keys too. I will use this certificate to revoke the keys if the private key is stolen or I lose the privete key or I forget passphrase; some documents have recommeneded to generate revocation certificate (See Reference). Sorry, the result of gpg command has been in Japanase in this text:(

```
C:\Program Files (x86)\GNU\GnuPG>gpg --gen-revoke ABCDABCD > revoke.asc

sec  2048R/ABCDABCD 2015-04-12 kaito <kaito834@gmail.com>
(comment: I replaced original key-id to "ABCDABCD")

この鍵にたいする失効証明書を作成しますか? (y/N) y
失効の理由を選択してください:
  0 = 理由は指定されていません
  1 = 鍵(の信頼性)が損なわれています
  2 = 鍵がとりかわっています
  3 = 鍵はもはや使われていません
  Q = キャンセル
(ここではたぶん1を選びたいでしょう)
あなたの決定は? 0
予備の説明を入力。空行で終了:
>
失効理由: 理由は指定されていません
(説明はありません)
よろしいですか? (y/N) y

次のユーザの秘密鍵のロックを解除するには
パスフレーズがいります:"kaito <kaito834@gmail.com>"
2048ビットRSA鍵, ID ABCDABCD作成日付は2015-04-12

ASCII外装出力を強制します。
失効証明書を作成しました。

みつからないように隠せるような媒体に移してください。もし_悪者_がこの証明書への
アクセスを得ると、あなたの鍵を使えなくすることができます。
媒体が読出し不能になった場合に備えて、この証明書を印刷して保管するのが賢明です。

しかし、ご注意ください。あなたのマシンの印字システムは、他の人がアクセスできる
場所にデータをおくことがあります!
```

### References
- [Key size, Wikipedia](http://en.wikipedia.org/wiki/Key_size)
- [PGP Key Management Guide for NetBSD developers](http://www.netbsd.org/developers/pgp.html#manage-recommendations)
- [Creating GPG Keys, Fedora Project](https://fedoraproject.org/wiki/Creating_GPG_Keys#GPG_Key_Revocation)