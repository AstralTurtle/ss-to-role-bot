# This example requires the 'message_content' intent.

import discord
import pandas as pd

from settings import get_settings


settings = get_settings()

intents = discord.Intents.default()
intents.message_content = True

client: discord.Client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await set_role(client)


@client.event
async def on_message(message):
    pass


async def set_role(client: discord.Client):
    rsvp_form: pd.DataFrame = pd.read_excel("data")
    discord_names = rsvp_form["Discord Username"]

    guild: discord.Guild = await client.get_guild(settings.guild_id)
    role = await discord.utils.get(guild.roles, name=settings.role)

    for name in discord_names:
        member: discord.Member = await guild.get_member_named(name)
        await member.add_roles(role, "Assigned from Spreadsheet")


if __name__ == "__main__":
    client.run(settings.token)
