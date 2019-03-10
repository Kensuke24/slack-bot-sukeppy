# このbotはQiita内sukesukeさんの記事"https://qiita.com/sukesuke/items/1ac92251def87357fdf6"の写経です。

# coding: utf-8

from slackbot.bot import Bot
import slackbot_settings

API_TOKEN = slackbot_settings.API_TOKEN

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()
