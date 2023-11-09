# 基本となるイメージを指定
FROM python:3.8

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# 環境変数の設定（Pythonがpycファイルとディスクキャッシュを書き込まないようにする）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 依存関係のインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトコードのコピー
COPY . .

# コンテナがリッスンするポート番号を指定
EXPOSE 8000

# サーバを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

