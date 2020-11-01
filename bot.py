import discord
from random import choice
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("token")

bot = Bot("!")
# client = discord.Client()

with open("./compliments.txt", "r") as file:
    complimentList = list(file)


def getCompliment():
    return choice(complimentList)


# decorator
@bot.event
async def on_ready():
    print("We have logged in")


@bot.event
async def on_message(message):
    print(message.author, message.content, message.channel)
    if message.content[0] != "!":
        if message.author != bot.user:
            await message.channel.send("HI" + " " + str(message.author.mention))
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def compliment(ctx, member: discord.Member):
    memberList = ctx.message.guild.members
    print(memberList)
    complimentToSend = getCompliment()
    await ctx.send(complimentToSend + " " + str(member.mention))


# runs bot
bot.run(key)
