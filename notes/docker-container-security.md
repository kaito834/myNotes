Docker における User Namespace Remapping 実装のセキュリティ観点からの利点をきちんと理解する必要が出てきたため、
References を読み直して、Docker コンテナにおける Host/Container におけるシステム的な隔離実装を整理しておきます。
なお、このテキストでは Kubernetes(k8s) を対象外とします。

# Docker Host/Container Isolation
* Docker におけるソフトウェアスタック
  - Container Runtime (runC)
  - containerd
  - Docker daemon
  - Host OS
  - ※p.14 1.1.1 Docker を構成するコンポーネント群, Docker/Kubernetes開発・運用のためのセキュリティ実践ガイドに基づく
* Docker daemon は、下記のように Container Runtime を Host OS からシステム的に隔離した上で起動できる
  - [ネームスペース(名前空間)](https://man7.org/linux/man-pages/man7/namespaces.7.html)の分離
    + Mount Namespace
    + PID(Process ID) Namespace
    + Network Namespace
    + IPC(Inter-Process Communication) Namespace
    + UTS(UNIX Time-sharing System) Namespace
    + User Namespace
    + Cgroup Namespace
  - Container Runtime における root ユーザの[特権(Capabilities, ケイパビリティ)](https://man7.org/linux/man-pages/man7/capabilities.7.html)のはく奪
    + [Docker の初期設定では、すべてのケイパビリティを落としてから必要なものだけ付与する実装となっている](https://docs.docker.jp/engine/security/security.html#linux)
  - Container Runtime におけるシステムコールの制限 ([Secure Computing mode (seccomp)](https://docs.docker.com/engine/security/seccomp/))
    + Docker の初期設定では、seccomp が有効になっており、コンテナ内のプロセスが呼び出せシステムコールが厳しく制限されている
      * Refer to p.31 seccomp, 1.1.3 Docker の仕組み, Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド
  - Container Runtime における LSM (Linux Security Module の有効化): AppArmor, SELinux など
    + ファイルアクセス制御の厳格化
* また、Docker daemon および Container Runtime を root 以外のユーザでも起動できます
  - Docker daemon の場合、[Rootless モード](https://docs.docker.jp/engine/security/rootless.html)と呼ばれる
* セキュリティの観点では、Container Runtime が侵害されたときに、これらの隔離実装が他の Container および Host に被害が拡大することを防ぐ効果がある
  - 他の Container および Host に被害が拡大する要因
    + 下記の脆弱性に起因する「container breakout」
      * runC における脆弱性
      * Host OS: Linux kernel における脆弱性
    + container breakout: コンテナ内のプロセスがホスト上のリソースへのアクセス権限を奪取できてしまう問題
      * Refer to p.15 1.1.1 Docker を構成するコンポーネント群, Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド
* 強い権限のコンテナ（特権コンテナ）を動作させるなどの目的で隔離実装の一部を無効にしたい場合、下記の 3 点をもとに最終的にどうするか判断すべきと考える
  - 隔離実装の一部を無効にする目的のメリット
  - 対象の隔離実装の一部を無効化したときのセキュリティ観点からのリスク
  - 無効にする以外の他の方法論の有無（例えば、コンテナではなく Host OS でツールを動作させる）

## Docker における実行ユーザと特権のアクセス制御
セキュリティ観点から望ましい実行ユーザと特権のアクセス制御実装を優先度順にまとめてみます。
ただ、実運用上許容できない場合があるかもしれないこと、コミット時点の整理であることに留意してください。

1. Docker: [Rootless モード](https://docs.docker.jp/engine/security/rootless.html)で動作させる
  - dockerd/containerd/container runtime すべて root ユーザ以外のユーザで動作する
  - だが、一部の隔離実装が機能しないなど、実運用上許容できない見込みが非常に高い
  - Refer to pp.89-94 3.2.4 ランタイム自体を非 root で動かす(Rootless モード), Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド
2. Container Runtime: [User Namespace 機能](https://docs.docker.jp/engine/security/userns-remap.html)を有効にして、root 以外のユーザで動作させる
  - dockerd にて、User Namespace 機能を有効にして、Container runtime を動作させる
  - Container 上では root 権限に見えるため、root ユーザ以外でどういったユーザで動作させるべきかと検討せずに運用しやすい
  - User Namespace 機能が有効な状態で動作しないアプリケーションがある場合、[そのコンテナだけ User Namespace 機能を無効](https://docs.docker.jp/engine/security/userns-remap.html#disable-namespace-remapping-for-a-container)にして試してみたい
    + そのコンテナだけ User Namespace を無効にしても、既知の制限があるため期待通りに動作しない可能性がある
    + そうなってしまった場合、特権(Capabilities) や Seccomp のチューニングで動作するか検討する
  - Refer to pp.86-89 3.2.3 非 root ユーザを root に見せかける (User Namespace), Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド
3. Container Runtime: コンテナの用途ごとに適切な実行ユーザを指定する
  - コンテナの用途に応じて、適切な権限を持つ実行ユーザを指定する
    + 一般ユーザ権限で十分動作する場合には一般ユーザ権限を指定する
      * また可能ならば、no_new_privs ビットを有効にしておきたい
      * Refer to 3.5.2 権限昇格を防止する (no_new_privs ビット), Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド
    + どうしても (Host の) root 権限を必要とする場合、必要性およびメリットとリスクをふまえた上で判断する
  - 1, 2 に比べると、コンテナごとに判断が入るために運用コストが高く、運用上適切なユーザ権限が設定されないリスクも残る
  - Refer to pp.80-84 3.2.1 ユーザを指定する, Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド

# References
* [Docker/Kubernetes開発・運用のためのセキュリティ実践ガイド](https://book.mynavi.jp/ec/products/detail/id=114099) (2020年2月27日発売)
* [docker-docs-ja 19.03: Docker セキュリティ](https://docs.docker.jp/engine/security/toc.html#) (2020年10月4日閲覧)
* [Infra Study Meetup #6「インフラとセキュリティのこれから」](https://forkwell.connpass.com/event/187694/) (2020年9月25日)
  - [インフラとセキュリティとこれから @mrtc0](https://speakerdeck.com/mrtc0/inhuraji-pan-ji-shu-falsesekiyuriteitokorekara)
* [CloudNative Days Tokyo 2020](https://event.cloudnativedays.jp/cndt2020/talks) (2020年9月8, 9日 オンライン開催)
  - [Embedded Container Runtime using Linux capabilities, seccomp, cgroups](https://speakerdeck.com/kentatada/embedded-container-runtime-using-linux-capabilities-seccomp-cgroups)
* [Tokyo OpenStack Summit 2015: Unraveling Docker Security](https://www.slideshare.net/PhilEstes/tokyo-openstack-summit-2015-unraveling-docker-security) (Published on Nov 30, 2015)
  - via https://integratedcode.us/2016/02/05/docker-1-10-security-userns/
* [Trend Micro: Why A Privileged Container in Docker Is a Bad Idea](https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html) (2019年12月)
