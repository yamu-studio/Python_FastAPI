# やむぅのポートフォリオで使用するAPI(バックエンド)

### 今回使用した言語・フレームワーク等

<img src="https://skillicons.dev/icons?i=python,fastapi,mysql,git,github,vscode,docker" />

### 起動方法

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

2. API 環境の開始

```
uvicorn app.main:app --reload
```

3. API の状況確認・ドキュメント

```
http://127.0.0.1:8000/docs
```

4. コンテナの終了

```
docker compose stop
```

### DB構成や内容

[DBダンプ](https://github.com/yamu-studio/Python_FastAPI/blob/feature/youtube_api/db/ダンプ_yamuyamu.sql)をご確認ください。
