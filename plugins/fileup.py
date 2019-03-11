from slacker import Slacker

from slackbot.bot import listen_to
from slackbot.bot import respond_to
import slackbot_settings

tiku=['ちく', 'チク','蓄']   # リストをlisten_toに入力してanyで反応させたい（今はできてない）


@listen_to('ちく')
@listen_to('チク')
@listen_to('蓄')
def todoist_today_list(message):
    slacker = Slacker(slackbot_settings.API_TOKEN)
    channel = 'CC1LDH4BH'
    file = 'plugins/respond_text/tikuryoku.txt'     # ここまでの相対パス

    slacker.files.upload(file_=file, channels=channel)
    message.send('ファイルをアップロードしました')
