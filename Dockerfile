# Pythonのイメージ
FROM python:3.10

# # 作業ディレクトリを設定する
# WORKDIR ../app

# 必要なパッケージをインストールする
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

