# coding: utf-8
# APIをGithubに載せずに管理する方法を試行錯誤中
# Herokuを使用する。

import os

# botアカウントのトークンを指定
API_TOKEN = os.environ["BOT_API_TOKEN"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "ちょっと何言っているかわからないです。環境変数は連携できましたか？"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
