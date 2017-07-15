# -*- coding: utf-8 -*-

"""
from slackbot.bot import respond_to

@respond_to('こんにちは')
@respond_to('今日は')
def hello(message):
	message.reply('こんにちは!')
"""

"""
from slackbot.bot import respond_to, listen_to

@listen_to('私は(.*)です')
@listen_to('わたしは(.*)です')
def hello(message, something):
	message.reply('こんにちは!{0}さん。'.format(something))

@respond_to('(.*)')
def refrection(message, something):
	message.reply(something)
"""


from slackbot.bot import respond_to

from dialogue_system.bot import Bot

bots = {}


def create_or_read(user_id):
	return bots[user_id] if user_id in bots else Bot()


def save_bot(bot, user_id):
	bots[user_id] = bot


@respond_to('(.*)')
def food(message, something):
	body = message.body
	text, ts, user_id = body['text'], body['ts'], body['user']
	bot = create_or_read(user_id)
	reply_message = bot.reply(text)
	save_bot(bot, user_id)
	message.reply(reply_message)