import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    print("========================================================")
    print("봇 정보") 
    print(client.user.name)
    print(client.user.id)
    print("========================================================")

@client.event
async def on_message(message):
    if message.content == ('!test'):
        await message.channel.send("test")

@client.event
async def on_member_join(member):
    await member.guild.get_channel(687834516345454663).send(member.mention + """ HEAVYgiant( 헵자 )님 팬서버에 오신 걸 환영합니다! 메시지 하단에 있는 채널을 읽어주시고 활동을 시작해주세요! ( 공지, 밈 채널 제외 )
규칙 : #💌│to-follow 
채널 설명 : #💌│info-chn 
역할 설명 & 역할 선택 : #💌│info-role 
공지 : #🔔│notice 
해당 서버 밈 : #📁│memes""")

client.run(os.environ['token'])