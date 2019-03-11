from slacker import Slacker

from slackbot.bot import respond_to
import slackbot_settings


@respond_to('^うぷ$')
def todoist_today_list(message):
    slacker = Slacker(slackbot_settings.API_TOKEN)
    channel = 'channel'
    file = 'C:\Users\msrel\OneDrive\デスクトップ\Git\slack-bot-sukeppy\plugins\respond_text\tikuryoku.txt'

    slacker.files.upload(file_=file, channels=channel)
    message.send('ファイルをアップロードしました')
