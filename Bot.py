import discord
from discord.ext import commands
from discord import app_commands
import os
from keep_alive import keep_alive

TOKEN=os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

UnicodeEmoji = "\N{HEAVY LARGE CIRCLE}"
UnicodeEmoji2 = "\N{Cross Mark}"

list_yesno = [UnicodeEmoji, UnicodeEmoji2]
list_1 = ['1️⃣', '2️⃣', '3️⃣']
list_2 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
list_3 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']

@bot.event
async def on_ready ():
    print("起動")

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期")
    except Exception as e:
        print(e)

@bot.tree.command(name="yes-no")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="⭕   "+q1,value="",inline=False)
    embed.add_field(name="❌   "+q2,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_yesno)):
     await message.add_reaction(list_yesno[i])
    return

@bot.tree.command(name="question3")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_1)):
     await message.add_reaction(list_1[i])
    return

@bot.tree.command(name="question4")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_2)):
     await message.add_reaction(list_2[i])
    return

@bot.tree.command(name="question5")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str, q5:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    embed.add_field(name="5   "+q5,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_3)):
     await message.add_reaction(list_3[i])
    return

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
   embed = discord.Embed(description="## [__エラー__](https://forms.gle/gDPMPrvWxKdESqTZA)が発生した場合")
   embed.add_field(name="/yes-noで投票を開始をできます。                                                                                    /questionで複数投票を開始することができます。",value="",inline=False)
   embed.add_field(name="**title**",value="投票のタイトルを入力してください",inline=False)
   embed.add_field(name="q1",value="1つ目の回答を作成",inline=True)
   embed.add_field(name="q2",value="2つ目の回答を作成",inline=True)
   embed.add_field(name="q3",value="3つ目の回答を作成",inline=True)
   embed.set_author(name="py",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg")
   await interaction.response.send_message(embed=embed,ephemeral=True)

ID_ROLE_MEMBER = 1222196302780301335
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(ID_ROLE_MEMBER)
    await member.add_roles(role)
keep_alive()

bot.run(TOKEN)