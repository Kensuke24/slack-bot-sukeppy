"""
@respond_to('hoge')デコレータを付けた関数は、botに向けた投稿で、引数の文字列が含まれるときに反応する。
@listen_to('hoge')デコレータを付けた関数は、参加しているチャンネルで、botに向けた投稿以外で、引数の文字列が含まれるときに反応する。
反応する文字列は完全一致ではなく、含まれていればよい。
https://qiita.com/sukesuke/items/1ac92251def87357fdf6 より。sukesukeさんありがとうございます。
"""
from slackbot.bot import listen_to
import random

serif = ['おはよう', 'Good morning！！英語でも言えるよ！','今日も元気にいってみよー！！', 'ごきげんよう',
         'ダーリンおはようだっちゃ！','おはー','今日も輝いてるね！','おはようござんす','ピヨピヨ']

'''
serif_file = "plugins/serif_good_working.txt"
with open(serif_file, 'r') as f:
    serif = [l.strip() for 1 in f.readlines()]
'''

# prefix = ['おはよう！', 'おはようマスター。']
# message.send(random.choice(prefix) + random.choice(serif))    prefixをランダムで送る

@listen_to('おは')
def listen_func(message):
    message.reply(random.choice(serif))
