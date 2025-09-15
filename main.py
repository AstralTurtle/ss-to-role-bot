# This example requires the 'message_content' intent.

import discord
import pandas as pd

from settings import get_settings


settings = get_settings()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client: discord.Client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await set_role(client)
    await client.close()


@client.event
async def on_message(message):
    pass


async def set_role(client: discord.Client):
    rsvp_form: pd.DataFrame = pd.read_excel("data.xlsx")
    discord_names = rsvp_form["Discord Username"]

    guild: discord.Guild = client.get_guild(settings.guild_id)
    role: discord.Role = discord.utils.get(guild.roles, name=settings.role)
    print(guild, role.id)
    for name in discord_names:
        try:
            member: discord.Member = guild.get_member_named(name)
            # print(name, member)
            await member.add_roles(role, reason="Assigned from Spreadsheet")
        except:
            print(name)


if __name__ == "__main__":
    client.run(settings.token)
