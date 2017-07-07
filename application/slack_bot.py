# -*- coding: utf-8 -*-
from slackbot.bot import Bot


def main():
    bot = Bot()
    print(bot)
    bot.run()

if __name__ == "__main__":
    main()