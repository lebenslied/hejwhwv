import discord

client = discord.Client()

global_chat_channel_name = "baumchat"


@client.event
async def on_message(message: discord.Message):
    if message.author.bot: return
    if message.channel.name.lower() == global_chat_channel_name.lower():
        # Nachicht wurde in einem GlobalChat geschrieben
        for guild in client.guilds:
            # Geht durch alle Server in denen der Bot ist
            for channel in guild.channels:
                # Geht durch alle Channels von den Servern
                if channel.name.lower() == global_chat_channel_name.lower():
                    # Checkt ob der channel GlobalChat heißt
                    if channel.type == discord.ChannelType.text and message.channel.id != channel.id:
                        # Checkt ob der channel ein TextChannel ist
                        # und ob es nicht der ist in den die nachicht geschrieben würde
                        embed = discord.Embed(title=str(message.author), description=str(message.content),
                                              color=0x99ccff)
                        embed.set_thumbnail(url=message.author.avatar_url)
                        await channel.send(embed=embed)
                        # sendet einen Embed mit Name, Nachicht und Profielbild

client.run("NzAxMTMwNjE0MzgzODM3MTk1.XptA6Q.O_NNMdA2_BO75QgewJTSj1L3NiA")
