I noted some useful references for me about "[Pythonプロフェッショナルプログラミング第2版](http://www.amazon.co.jp/Python-2-ebook/dp/B00XZTYMG6/)".

# Part1 Pythonで開発しよう
## 01-03-02 開発に便利なツール
- flake8(コーディングスタイル/シンタックスのチェック)
> この中でも、Pythonにおけるコーディングスタイルを提唱しているのがPEP 8で、
> そのコーディングスタイルに沿っているかどうかをチェックしてくれるのが「**[flake8](https://pypi.python.org/pypi/flake8)**」モ
> ジュールです。

I searched similar python libraries as flake8 on Google, then found a post on Qiita.
According to [the post](http://qiita.com/ynakayama/items/8616f4c0c6e372de9a42), I have known the following libraries below:
- [pep8](https://pypi.python.org/pypi/pep8)
- [pyflakes](https://pypi.python.org/pypi/pyflakes)
- [pytest](https://pypi.python.org/pypi/pytest)
  - py.test --pep8 ugly_sample.py

# Part2 チーム開発のサイクル
## 07-03-06 API リファレンスとプログラムを一体管理する仕組み(docstring、doctest、autodec)
> Pythonであれば、docstringをうまく利用することにより、この問題を解決できます。
> docstringは、Pythonのモジュールやクラス、関数の一番最初に書かれた文字列オブジェクト
> のことを指します。

- Other references
  - pp.195-196 6.1.4 ドキュメンテーション文字列, "[Python文法詳解](http://www.oreilly.co.jp/books/9784873116884/)"
  - pp.230-233 11.2 対話的な実行例をテストする, "[Pythonライブラリ厳選レシピ](http://www.amazon.co.jp/Python-ebook/dp/B017GT6PC4/)"
