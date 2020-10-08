import random
import os
import discord

# create discord client
client = discord.Client()

token = 'INSERT BOT TOKEN'

# bot is ready
@client.event
async def on_ready():
	try:
		# print bot information
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))
	
	except Exception as e:
		print(e)

@client.event
async def on_message(message):
	if message.content.startswith('!roll'):
		randroll = 0
		rolltotal = 0
		x,inputroll = message.content.split( )
		num,sides = inputroll.split("d")
		await message.channel.send('Rolling '+ num + ' ' + sides + ' sided dice for you.')
		for x in range (0,int(num)):
			randroll = random.randint(1, int(sides))
			await message.channel.send(randroll)
			rolltotal += randroll
		await message.channel.send('The total value of those rolls is ' + str(rolltotal) +'.')

client.run(token)
