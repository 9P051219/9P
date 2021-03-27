app.run(token)
import asyncio
import discord

app = discord.Client()

token = "your_token"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("파이썬 봇 실행중") #새로운 코드
    await app.change_presence(status=discord.Status.online, activity=game) #바뀜

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "9P출력":
        await message.channel.send("Python Bot에 의해 출력됨.") #바뀜
    if message.content.startswith("9P1부터10"):
        for x in range(10):
            await message.channel.send(x+1) #바뀜
    if message.content.startswith("9P계산"):
        global calcResult
        if message.content[7:].startswith("더하기"):
            calcResult = int(message.content[11:12])+int(message.content[13:14])
            await message.channel.send("Result : "+str(calcResult)) #바뀜
        if message.content[7:].startswith("빼기"):
            calcResult = int(message.content[10:11])-int(message.content[12:13])
            await message.channel.send("Result : "+str(calcResult)) #바뀜
        if message.content[7:].startswith("곱하기"):
            calcResult = int(message.content[11:12])*int(message.content[13:14])
            await message.channel.send("Result : "+str(calcResult)) #바뀜
        if message.content[7:].startswith("나누기"):
            try:
                calcResult = int(message.content[11:12])/int(message.content[13:14])
                await message.channel.send("Result : "+str(calcResult)) #바뀜
            except ZeroDivisionError:
                await message.channel.send("You can't divide with 0.") #바뀜

<<<<<<< HEAD
app.run(token)
=======
client.run(os.environ['token'])
>>>>>>> 7ff88289ddf917facc5346ab66af777146f964a8
