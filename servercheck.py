import discord
from discord.ext import commands

class Mycog:
	"""Server Checker ~wew~"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def status public(self):
		"""Checks if a server is up"""

		import socket;
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(("77.73.70.126", 30120-30120 is default for FiveM ))
		if result == 0:
			await self.bot.say("Development Server is Currently: __**Online!**__ :partyingface:")
		else:
			await self.bot.say("Development Server is Currently: __**Offline**__ :loudlycryingface:")
			
	@commands.command()
	async def status developement(self):
		"""Checks if a server is up"""

		import socket;
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(("77.73.70.126", 30120-30120 is default for FiveM ))
		if result == 0:
			await self.bot.say("Server is Currently: __**Online!**__ :partyingface:")
		else:
			await self.bot.say("Server is Currently: __**Offline**__ :loudlycryingface:")


def setup(bot):
	bot.add_cog(Mycog(bot))
