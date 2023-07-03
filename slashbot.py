# This example requires the 'message_content' intent.

import discord

from typing import Optional
from discord import app_commands

MY_GUILD = discord.Object(id = 498310331563507724)  # replace with your guild id

class MyClient(discord.Client):
	def __init__(self, *, intents: discord.Intents):
		super().__init__(intents=intents)
		# A CommandTree is a special type that holds all the application command
		# state required to make it work. This is a separate class because it
		# allows all the extra state to be opt-in.
		# Whenever you want to work with application commands, your tree is used
		# to store and work with them.
		# Note: When using commands.Bot instead of discord.Client, the bot will
		# maintain its own tree instead.
		self.tree = app_commands.CommandTree(self)

	# In this basic example, we just synchronize the app commands to one guild.
	# Instead of specifying a guild to every command, we copy over our global commands instead.
	# By doing so, we don't have to wait up to an hour until they are shown to the end-user.
	# async def setup_hook(self):
	# 	# This copies the global commands over to your guild.
	# 	self.tree.copy_global_to(guild=MY_GUILD)
	# 	await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.tree.command()
@app_commands.describe(
	member = 'The member you want to challenge',
	rounds = 'The number of rounds you want to play, defaults to 1'
)
async def challenge(interaction: discord.Interaction, member: discord.Member, rounds: Optional[int] = None):
	rounds = rounds or 1
	wins = 0
	await interaction.response.send_message(f'{interaction.user.mention} challenged {member.mention} to a game of Rock, Paper, Scissors! {rounds} game(s) will be played.')
	for round in range(rounds):
		print("Hello")
		await (f'It is currently round {round + 1}. {interaction.user.mention} has won {wins} game(s) so far. {member.mention} has won {round - wins} game(s) so far.')
		await interaction.response.send_message(f'{interaction.user.mention} and {member.mention} need to DM me their responses!')
	 

client.run('MTExNjQ3MTc1NTE5Njg3NDc1Mg.Gmgf40.McSC1qL-r1QIFUEL4XqB2kYUiOn8wAx-ralnXs')
