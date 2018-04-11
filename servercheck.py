import discord
from discord.ext import commands

class Mycog:
	"""IllusiveTea's Custom cog that checks if a server is up!"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def status public(self):
		"""Checks if a server is up"""

		import socket;
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(("158.69.250.106", 30120-30120 is default for FiveM ))
		if result == 0:
			await self.bot.say("Server is Currently: __**Online!**__")
		else:
			await self.bot.say("Server is Currently: __**Offline**__ :frowning:.")
			
	@commands.command()
	async def status developement(self):
		"""Checks if a server is up"""

		import socket;
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(("158.69.250.106", 30120-30120 is default for FiveM ))
		if result == 0:
			await self.bot.say("Server is Currently: __**Online!**__")
		else:
			await self.bot.say("Server is Currently: __**Offline**__ :frowning:.")


def setup(bot):
	bot.add_cog(Mycog(bot))
