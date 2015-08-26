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
