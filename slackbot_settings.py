# coding: utf-8
# APIをGithubに載せずに管理する方法を試行錯誤中
# Herokuを使用する。

import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# botアカウントのトークンを指定
API_TOKEN = os.environ["BOT_API_TOKEN"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "ちょっと何言っているかわからないです。"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

