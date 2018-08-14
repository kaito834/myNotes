I noted/quoted helpful information or links about SQL(Structured Query Language) based on books.

# SQL 第2版 ゼロからはじめるデータベース操作
https://www.amazon.co.jp/dp/B01HD5VWWO/

This book give readers to learn SQL(Structured Query Language) syntax based on [SQL:2003 standard](https://en.wikipedia.org/wiki/SQL:2003).
Please see "標準SQL", 1-3 SQLの概要, 第1章 データベースとSQL.

## 第1章 データベースとSQL
- 1-3 SQLの概要
  * DDL(Data Definition Language)
    + CREATE, DROP, ALTER
  * DML(Data Manipulation Language)
    + SELECT, INSERT, UPDATE, DELETE
  * DCL(Data Control Language)
    + COMMIT, ROLLBACK, GRANT, REVOKE
  * SQLの基本的な記述ルール
  * COLUMN: 標準SQLと方言
- 1-4 テーブルの作成
  * CREATE DATABASE
  * CREATE TABLE
- 1-5 テーブルの削除と変更
  * DROP TABLE
  * ALTER TABLE

## 第2章 検索の基本
- 2-1 SELECT文の基本
- 2-2 算術演算子と比較演算子
  * 文字列に不等号を使うときの注意
  * NULLに比較演算子は使えない
- 2-3 論理演算子
  * NULLを含む場合の真理値
    + 2値論理 / 3値論理

## 第3章 集約と並べ替え
- 3-1 テーブルを集約して検索する
  * 集約関数(集合関数)
    + COUNT, SUM, AVG, MAX, MIN
  * NULLを除外して行数を数える
  * 重複値を除外して集約関数を使う(DISTINCTキーワード)
- 3-2 テーブルをグループに切り分ける
  * GROUP BY 句
  * 集約キーにNULLが含まれた場合
  * WHERE句を使った場合のGROUP BYの動作
  * 集約関数とGROUP BY句にまつわるよくある間違い
- 3-3 集約した結果に条件を指定する
  * HAVING句
    + HAVING句を使用するときのSELECT文の記述順序
  * COLUMN: WHERE句とHAVING句の実行速度
- 3-4 検索結果を並べ替える
  * ORDER BY句
    + 句の記述順序
  * 列番号は使ってはいけない

## 第4章 データの更新
- 4-1 データの登録(INSERT文の使い方)
  * COLUMN: 複数行INSERT
  * ほかのテーブルからのデータをコピーする
    + INSERT ... SELECT 文
- 4-2 データの削除(DELETE文の使い方)
  * DROP TABLE文とDELETE文
  * COLUMN: 削除と切り捨て
    + TRUNCATE コマンド
- 4-3 データの更新(UPDATE文の使い方)
  * NULLで更新するには
    + NULLクリア
  * 複数行の更新
- 4-4 トランザクション
  * トランザクションを作るには
  * COMMIT / ROLLBACK
  * COLUMN: トランザクションはいつはじまるのか
  * ACID特性

## 第5章 複雑な問い合わせ
- 5-1 ビュー
  * ビューとテーブル
  * ビューの作り方
    + CREATE VIEW
    + ビューの制限事項
  * ビューを削除する
    + DROP VIEW
- 5-2 サブクエリ
  * サブクエリとビュー
  * サブクエリの名前
  * スカラ・サブクエリ
- 5-3 相関サブクエリ
  * 普通のサブクエリと相関サブクエリの違い
  * 相関サブクエリも、結局は集合のカットをしている
  * 結合条件は必ずサブクエリの中に書く

## 第6章 関数、述語、CASE文
あとで整理する

## 第7章 集合演算
- 7-1 テーブルの足し算と引き算
  * テーブルの足し算 - UNION
    + 集合演算の注意事項
    + 重複行を残す集合関数 - ALLオプション
  * テーブルの共通部分の選択 - INTERSECT
  * レコードの引き算 - EXCEPT
- 7-2 結合(テーブルの列方向に連結する)
  * 結合とは
    + 結合(JOIN)
  * 内部結合 - INNER JOIN
    + 内部結合のポイント1 - FROM句
    + 内部結合のポイント2 - ON句
    + 内部結合のポイント3 - SELECT句
  * 外部結合 - OUTER JOIN
    + 外部結合のポイント1 - 片ほうのテーブルの情報がすべて出力される
    + 外部結合のポイント2 - どちらのテーブルをマスタにするか
  * 3つ以上のテーブルを使った結合
  * クロス結合 - CROSS JOIN
    + CROSS JOIN(直積)
  * 結合の方言と古い構文
