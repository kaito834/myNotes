I noted useful references for me in this text. These references relate to Web API.

### Encrypted String as access token instead of OAuth

アクセストークンとリフレッシュトークンの両方が必要な理由,"[OAuth 2.0をはじめよう](http://www.oreilly.co.jp/books/9784873115580/)", O'Reilly Japan
```
しかし、これによってAPIリクエストに対する遅延が生じる可能性があります。そのためAPIプロバイダの中には、OAuthの代わりにアクセストークンとして署名付き文字列や暗号化文字列を使うプロバイダもあります。このようなトークンであればより低コストで検証できるからです。
```

### Custom Headers

ブラウザからのアクセスを想定しないAPIの場合, "[Web API: The Good Parts](http://www.oreilly.co.jp/books/9784873116860/)", O'Reilly Japan
```
したがってブラウザからのアクセスの必要がなければ、セッションには異なるセッション管理の方法を使ったり、独自のHTTPヘッダを使ってクライアントを識別する、次の節で述べるようなチェックサムを使うなど、ブラウザからのSCRIPT要素を使ったアクセスを防ぐようにする必要があります。
```

### Cross Origin Request Sharing(CORS)
実際のAPIの対応状況を見てみる, "[Web API: The Good Parts](http://www.oreilly.co.jp/books/9784873116860/)", O'Reilly Japan

- Foursquare API
  - https://api.foursquare.com/v2/users/self?oauth_token=(snip)&v=20140422
  - Access-Control-Allow-Origin: *
- GitHub API
  - https://api.github.com/users/takaaki-mizuno
  - Access-Control-Allow-Origin: *

### List of Security Headers
"[List of useful HTTP headers(OWASP)](https://www.owasp.org/index.php/List_of_useful_HTTP_headers)" lists following HTTP headers from the security perspective.
- Public-Key-Pins
- Strict-Transport-Security
- X-Frame-Options
- X-XSS-Protection
- X-Content-Type-Options
- Content-Security-Policy
- Content-Security-Policy-Report-Only

"[REST Security Cheat Sheet(OWASP)](https://www.owasp.org/index.php/RE,ST_Security_Cheat_Sheet#Send_security_headers)" recommends to output X-Content-Type-Options header and X-Frame-Options one.

> To make sure the content of a given resources is interpreted correctly by the browser,
> the server should always send the Content-Type header with the correct Content-Type,
> and preferably the Content-Type header should include a charset. The server should
> also send an __X-Content-Type-Options: nosniff__ to make sure the browser does not
> try to detect a different Content-Type than what is actually sent (can lead to XSS).
>
> Additionally the client should send an __X-Frame-Options: deny__ to protect against
> drag'n drop clickjacking attacks in older browsers.

#### X-Content-Type-Options: nosniff
6.3.1 XSS, "[Web API: The Good Parts](http://www.oreilly.co.jp/books/9784873116860/)", O'Reilly Japan

> また最新の Firefox や Chrome、および IE9 以降ではこのヘッダを付けることで、JavaScript として
> 実行可能なメディアタイプを限定することが可能になり、後述する JSON インジェクションの危険性を減らす
> ことができるため、このヘッダは JSON でデータを返す際には必ず付けるべきです。

6.5.1 X-Content-Type-Options, "[Web API: The Good Parts](http://www.oreilly.co.jp/books/9784873116860/)", O'Reilly Japan

> このヘッダは JSON を JSON 以外として解釈することを防いでくれます。JSON は配信側としては JSON
> 以外として解釈される必要はありませんから、JSON で API を配信する場合はもはや絶対に付けておいた
> ほうが良いヘッダといえるでしょう。
> また IE9 以降や Chrome では、SCRIPT 要素で指定されたファイルにこのヘッダを設定してあり、
> さらにスクリプト(JavaScript や IE の場合は VBScript)を表すメディアタイプでなかった場合には、
> 実行を行わずにエラーになります。たとえば JavaScript ファイルを配信したいけれど実行はされたくない、
> といった場合にも(ブラウザが限定されるものの)このヘッダは有効です。たとえば GitHub ではリポジトリで
> 管理されている JavaScript ファイルを直接 SCRIPT 要素として読み込まれないために、メディアタイプを
> text/plain にしたうえで、このヘッダを付けています。
