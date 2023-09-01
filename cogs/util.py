import discord
from discord.ext import commands
import asyncio

# cogs let you put related commands and functions together under a class
class Util(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	@commands.command(name = 'timer',
		   # brief and description are what show up in the help menu
		   brief = 'Get pinged after given number of seconds elapses',
		   description = 'Get pinged after given number of seconds elapses',
		   # aliases give shorthands for the command
		   aliases = ['remind'])
	async def timer(self,
		  		     ctx : commands.Context,
					 time: int):
		"""
		Make a random choice between the arguments given
		:param ctx: provides context for command call (who called it, which channel was it called in, etc)
		:param time: the number of seconds to count down from 
		"""
		await asyncio.sleep(time)
		await ctx.send(f'{ctx.author.mention} your timer ran out! {time} seconds have passed.')
	
# add this cog to the client
async def setup(client):
	await client.add_cog(Util(client))