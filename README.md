# ボイスチャンネル入室通知アプリ
## 概要
Discordのボイスチャンネルに入室した際、自動でLINEグループに通知を送るアプリです。
## サンプル
準備中です。
## 技術
- Python
  - discord.py
- LINE Notify API
- Heroku
## 使い方
1. コードをダウンロードしてHerokuにデプロイ  
   もしくはFolkしてHerokuのDeployment methodでGitHubと連携、デプロイ
2. 以下の環境変数を適切に設定
   - DISCORD_BOT_ACCESS_TOKEN
   - VOICE_CHANNEL_ID
   - LINE_NOTIFY_ACCESS_TOKEN

## 開発動機
共通のメンバーを持つLINEグループとDiscordサーバがあるが、メンバーの一部はDiscordには不慣れで  
かつアクティブ率が低いため、ボイスチャンネルで雑談をしていても気づかないことが多く、  
利用されにくいという状況になっています。

そこで、気楽にボイスチャンネルを活用してもらうために、ボイスチャンネル入室時にLINEに通知を飛ばし、  
ボイスチャンネルにメンバーがいることに気づいてもらおうと思い、このアプリケーションを開発しました。

## TODO
- :running: 使い方の2が不親切すぎるので解説ブログを書く
- :walking: 通知の際、サムネイル画像かStickerを表示する(LINE Notify API)