This text is my notes to use Linux tool chain on Windows 10.

# Tools to use Linux tool chain on Windows 10
- Git Bash, which is included on [Git for Windows](https://gitforwindows.org/)
  * *Git for Windows provides a BASH emulation used to run Git from the command line.*
  * According to [this Qiita post](https://qiita.com/Ted-HM/items/9a60f6fcf74bbd79a904), Git Bash is based on MSYS2
- [MSYS2](https://www.msys2.org/)
  * *MSYS2 is a collection of tools and libraries providing you with an easy-to-use environment for building, installing and running native Windows software.*
  * *To provide easy installation of packages and a way to keep them updated it features a package management system called Pacman, which should be familiar to Arch Linux users.*
- [WSL: Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/)
  * *The Windows Subsystem for Linux lets developers run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.*
  * As of Sep. 2020, there are 2 versions on WSL: WSL 1 and 2
  * You can find [Windows Subsystem for Linux Overview on Microsoft Blog (WSL 1)](https://docs.microsoft.com/ja-jp/archive/blogs/wsl/windows-subsystem-for-linux-overview)
    + Via https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux
- [Cygwin](https://www.cygwin.com/)

# Links
- [Qiita: Windowsのコマンドライン開発環境](https://qiita.com/ymdymd/items/2fe0235e8126f06e74ca) (in Japanese / Last update: Apr. 3, 2020)
- [Qiita: Windowsで使えるターミナルとシェルのまとめ](https://qiita.com/Ted-HM/items/9a60f6fcf74bbd79a904) (in Japanese / Last update: Sep. 25, 2019)
- [Wikipedia: MinGW](https://ja.wikipedia.org/wiki/MinGW) (in Japanese / Read on Sep. 5, 2020)
  * Help me to understand difference between MinGW and MSYS
- [GnuWin](http://gnuwin32.sourceforge.net/)
  * Last update: 27-12-2010 10:15:32
- [Microsoft Docs: Linux 用 Windows サブシステム (WSL) ディストリビューションを手動でダウンロードする](https://docs.microsoft.com/ja-jp/windows/wsl/install-manual) (in Japanese / May 28, 2020)
- [Qiita: WSL (Windows Subsystem for Linux) をコマンドラインでインストールする](https://qiita.com/moriai/items/850ee91d60edc91e7b7e) (in Japanese / Last Update: Jun. 29, 2020)
  * 下記の環境において、管理者権限における PowerShell: Add-AppxPackage コマンドレットで Kali をインストールしたところ、Kali を起動できない状況に陥った
    + Windows 10 1809
    + ローカル Administrator 権限を持たないユーザでログイン
    + Administrator 権限が必要な場合、別のローカル Administrator ユーザで認証して権限昇格
