import discord
from discord.ext import commands

discord_token = 'fake token for git hub upload'


client1 = commands.Bot(command_prefix="$", case_insensitive=True, intents = discord.Intents.all())

@client1.event
async def on_ready():
    print('We have loggend in as {0.user}'.format(client1))


@client1.command()
async def move(ctx, member: discord.Member = None, VoiceChannel=None):
    try:
        channel = discord.utils.get(ctx.guild.channels, id=int(VoiceChannel))
        if member == None:
            await ctx.message.author.move_to(channel)
        else:
            await member.move_to(channel)
    except Exception as e:
        embed = discord.Embed(
            title='**ERROR**',
            description=e,
            color=discord.Color.red()
        )
        await  ctx.send(embed=embed)

@client1.event
async def on_message(message):
    ctx = await client1.get_context(message)
    if ctx.valid:
        await client1.invoke(ctx)


# 위에서 설정한 client class를 token으로 인증하여 실행합니다.

client1.run(discord_token)

'''
-- Result
We have logged in as <discord.client.Client object at 0x7f82642aad90>
Bot name: Cake
Bot ID: 123456789123456789123456789
'''
