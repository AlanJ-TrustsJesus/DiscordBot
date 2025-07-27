import discord #make sure to install discord.py
import random
from discord.ext import commands #simply import what's needed
from webserver import keep_alive #for it to run , with out webserver file
intents=discord.Intents.default() #new discord makes this necessary 
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents) #this means the commands are identified using prefix !
@bot.event #Event listener 
async def on_ready():
    print(f"{bot.user}has connected to server") #sends a message to terminal that bot is working
@bot.command() #identifies the message as command , necessary or command wont work
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention},how are you?!") #hello , how are you
@bot.command()
async def add(ctx,*nums:float): 
    num=0
    for i in nums:
        num=num+i
    await ctx.send(f"The sum is {num:.2f}") #2f for 2 point floating
@bot.command()
async def sub(ctx,num1:float,*nums:float):
    for i in nums:
        num1=num1-i
    await ctx.send(f"The difference is {num1:.2f}")
@bot.command()
async def mul(ctx,num1:float,*nums:int): #simply multiply 
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
        await ctx.send(f"The quotient is {int(num1)} and remainder is {int(num2)}") #remainder only if two vars , otherwise its not really a remainder is it
@bot.event
async def on_message(message): #for simply reading messages without a prefix
    if message.author ==bot.user:
        return
    elif message.content.lower().startswith(('hi','hai','hola','howdy','hallo','hey','hello')):
        reply=random.choice([f'Hello {message.author}!', 'Hi', 'Hey', 'Hai', 'Hiya', 'Greetings', 'Yo', "How you doing?"])
        await message.channel.send(reply)
    elif message.content.lower().startswith(('bye','goodbye','cya','see you later','see ya')):
        reply=random.choice([f'Goodbye {message.author}!',"Goodbye!","See ya!","Have a nice day","later then!","Byee!"])
        await message.channel.send(reply)
    await bot.process_commands(message)           #without this , the bot.command() stuff won't work
keep_alive()
bot.run("token here")   #Enter your discord bot token from dev site
