# Fast Api でサーバ側実装

Docker でデータベース(MySQL)を構築して、
Python の Fast Api で CRUD 操作等を行う。

0. 初期設定
   ※コレをクローンした際にしてほしいこと

・コンテナの作成と開始(デタッチモード使ってる)

```
docker compose up -d
```

1. コンテナの開始(デタッチモード使ってる)

```
docker compose start -d
```

2. Api 環境の開始

```
conda activate yamu_portfolio_py12
uvicorn app.main:app --reload
```

3. API のド状況確認・ドキュメント

```
http://127.0.0.1:8000/docs
```

4. コンテナの終了

```
docker compose stop
```
