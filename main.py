import discord
import random
from discord.ext import commands
from webserver import keep_alive
intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user}has connected to server")
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention},how are you?!")
@bot.command()
async def add(ctx,*nums:float):
    num=0
    for i in nums:
        num=num+i
    await ctx.send(f"The sum is {num:.2f}")
@bot.command()
async def sub(ctx,num1:float,*nums:float):
    for i in nums:
        num1=num1-i
    await ctx.send(f"The difference is {num1:.2f}")
@bot.command()
async def mul(ctx,num1:float,*nums:int):
    for i in nums:
        num1*=i
        await ctx.send(f"The product is {num1:.2f}")
@bot.command()
async def div(ctx,num1:float,*nums:int):
    if len(nums)>1:
        for i in nums:
            num1=num1/i
        await ctx.send(f"The quotient is {num1:.2f}")
    else:
        num2=num1%nums[0]
        num1=num1/nums[0]
        await ctx.send(f"The quotient is {int(num1)} and remainder is {int(num2)}")
@bot.event
async def on_message(message):
    if message.author ==bot.user:
        return
    elif message.content.lower().startswith(('hi','hai','hola','howdy','hallo','hey','hello')):
        reply=random.choice([f'Hello {message.author}!', 'Hi', 'Hey', 'Hai', 'Hiya', 'Greetings', 'Yo', "How you doing?"])
        await message.channel.send(reply)
    elif message.content.lower().startswith(('bye','goodbye','cya','see you later','see ya')):
        reply=random.choice([f'Goodbye {message.author}!',"Goodbye!","See ya!","Have a nice day","later then!","Byee!"])
        await message.channel.send(reply)
    await bot.process_commands(message)
keep_alive()
bot.run("token here")
