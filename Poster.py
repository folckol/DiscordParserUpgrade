import json
import random

import sqlite3

import asyncio

import requests

import discord
from discord.ext import commands
from discord.errors import HTTPException
import contextlib

from sqlalchemy.orm import sessionmaker
from DB_Models import *

token1 = ''
token2 = ''
token3 = ''
token4 = ''
token5 = ''

token_asian = ''

header11 = {'Authorization': f'DeepL-Auth-Key {token1}'}
header12 = {'Authorization': f'DeepL-Auth-Key {token2}'}
header13 = {'Authorization': f'DeepL-Auth-Key {token3}'}
header14 = {'Authorization': f'DeepL-Auth-Key {token4}'}
header15 = {'Authorization': f'DeepL-Auth-Key {token5}'}

header22 = {'Authorization': f'DeepL-Auth-Key {token_asian}'}

payload11 = {'text': '',
             'target_lang': 'RU'}

payload22 = {'text': '',
             'target_lang': 'EN'}

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

database = sqlite3.connect('database.db', check_same_thread=False)
sql = database.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS messages
                (ID INTEGER)''')
database.commit()

sql.execute('''CREATE TABLE IF NOT EXISTS messages_for_trans
                (ID INTEGER,
                text TEXT,
                trans TEXT)''')
database.commit()

parser_db_path = r'C:\Users\Администратор\PycharmProjects\pythonProject\Rescue_PASS_system\Telegram\ü«Γ ñ½∩ óδñáτ¿ æ«ΣΓá\parser.db'

'button[dl-test="cookie-banner-strict-accept-all"]'


# async def generate_and_send_reply_embed(embed11, message, channel_id):
#
#     channel = bot.get_channel(int(channel_id))
#
#     embed = discord.Embed(title='Пришел ответ на это сообщение', description=embed11, color=discord.Colour.from_rgb(173, 138, 47))
#
#     await channel.send(content = message,embed=embed)

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.button(label="Перевод", style=discord.ButtonStyle.green)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # await interaction.response.edit_message(content=f"This is an edited button response!")

        id = interaction.message.id

        sql.execute(f"""SELECT trans FROM messages_for_trans WHERE ID = {id}""")

        await interaction.response.send_message(sql.fetchone()[0], ephemeral=True)


async def generate_and_send_reply_embed(embed11, message, channel_id, channel_name, header):
    channel = bot.get_channel(int(channel_id))

    embed = discord.Embed(
        description='**📌 Пришел ответ на это сообщение:**\n\n' + embed11 + '\n\n\n**✉️ Ответ:**\n\n' + message,
        color=discord.Colour.from_rgb(173, 138, 47))

    payload11['text'] = message
    r = requests.post('https://api-free.deepl.com/v2/translate',
                      data=payload11, headers=header)
    trans_text = json.loads(r.text)['translations'][0]['text']

    msg = await channel.send(embed=embed, view=Buttons())

    sql.execute(f"""INSERT INTO messages_for_trans VALUES (?,?,?)""", (msg.id, message, trans_text))
    database.commit()

    try:
        with contextlib.closing(
                sqlite3.connect(parser_db_path, check_same_thread=False)) as conn:
            with conn as cursor:
                cursor.execute(f"""INSERT INTO posts_translate VALUES (?,?,?)""",
                               (f'{msg.id}', f'Канал {channel_name}\n\n' + message,
                                f'Канал {channel_name}\n\n' + trans_text))
                conn.commit()

                cursor.execute(f"""INSERT INTO posts VALUES (?,?,?,?)""",
                               (channel_name, message, False, f'{msg.id}'))
                conn.commit()
    except:
        pass


async def generate_and_send_message(message, channel_id, file, channel_name, header):
    channel = bot.get_channel(int(channel_id))

    embed = discord.Embed(description=message, color=discord.Colour.from_rgb(173, 138, 47))

    payload11['text'] = message
    r = requests.post('https://api-free.deepl.com/v2/translate',
                      data=payload11, headers=header)
    trans_text = json.loads(r.text)['translations'][0]['text']

    if file == True:
        with open("img.jpg", "rb") as f:
            file = discord.File(f)
            embed.set_image(url="attachment://img.jpg")

            msg = await channel.send(file=file, embed=embed, view=Buttons())

            try:
                with contextlib.closing(
                        sqlite3.connect(parser_db_path, check_same_thread=False)) as conn:
                    with conn as cursor:
                        cursor.execute(f"""INSERT INTO posts_translate VALUES (?,?,?)""",
                                       (f'{msg.id}', f'Канал {channel_name}\n\n' + message,
                                        f'Канал {channel_name}\n\n' + trans_text))
                        conn.commit()

                        cursor.execute(f"""INSERT INTO posts VALUES (?,?,?,?)""",
                                       (channel_name, message, True, f'{msg.id}'))
                        conn.commit()
            except:
                pass

    else:
        try:
            msg = await channel.send(embed=embed, view=Buttons())
        except HTTPException:
            embed.add_field(name='Parsed', value='by Rescue Alpha')
            msg = await channel.send(embed=embed, view=Buttons())

        except:
            asyncio.sleep(6)
            msg = await channel.send(embed=embed, view=Buttons())

        try:
            with contextlib.closing(
                    sqlite3.connect(parser_db_path, check_same_thread=False)) as conn:
                with conn as cursor:
                    cursor.execute(f"""INSERT INTO posts_translate VALUES (?,?,?)""",
                                   (f'{msg.id}', f'Канал {channel_name}\n\n' + message,
                                    f'Канал {channel_name}\n\n' + trans_text))
                    conn.commit()

                    cursor.execute(f"""INSERT INTO posts VALUES (?,?,?,?)""",
                                   (channel_name, message, False, f'{msg.id}'))
                    conn.commit()
        except:
            pass

    sql.execute(f"""INSERT INTO messages_for_trans VALUES (?,?,?)""", (msg.id, message, trans_text))
    database.commit()


async def generate_and_send_asian_message(message, channel_id, file, channel_name, header):
    channel = bot.get_channel(int(channel_id))

    payload22['text'] = message
    r = requests.post('https://api-free.deepl.com/v2/translate',
                      data=payload22, headers=header22)
    text = json.loads(r.text)['translations'][0]['text']

    payload11['text'] = text
    r = requests.post('https://api-free.deepl.com/v2/translate',
                      data=payload11, headers=header)
    trans_text = json.loads(r.text)['translations'][0]['text']

    print(text)

    embed = discord.Embed(description=text, color=discord.Colour.from_rgb(173, 138, 47))

    if file == True:
        with open("img.jpg", "rb") as f:
            file = discord.File(f)
            embed.set_image(url="attachment://img.jpg")

            msg = await channel.send(file=file, embed=embed, view=Buttons())

            try:
                with contextlib.closing(
                        sqlite3.connect(parser_db_path, check_same_thread=False)) as conn:
                    with conn as cursor:
                        cursor.execute(f"""INSERT INTO posts_translate VALUES (?,?,?)""",
                                       (f'{msg.id}', f'Канал {channel_name}\n\n' + message,
                                        f'Канал {channel_name}\n\n' + trans_text))
                        conn.commit()

                        cursor.execute(f"""INSERT INTO posts VALUES (?,?,?,?)""",
                                       (channel_name, message, True, f'{msg.id}'))
                        conn.commit()
            except:
                pass
    else:
        msg = await channel.send(embed=embed, view=Buttons())

        try:
            with contextlib.closing(
                    sqlite3.connect(parser_db_path, check_same_thread=False)) as conn:
                with conn as cursor:
                    cursor.execute(f"""INSERT INTO posts_translate VALUES (?,?,?)""",
                                   (f'{msg.id}', f'Канал {channel_name}\n\n' + message,
                                    f'Канал {channel_name}\n\n' + trans_text))
                    conn.commit()

                    cursor.execute(f"""INSERT INTO posts VALUES (?,?,?,?)""",
                                   (channel_name, message, False, f'{msg.id}'))
                    conn.commit()
        except:
            pass

    sql.execute(f"""INSERT INTO messages_for_trans VALUES (?,?,?)""", (msg.id, message, trans_text))
    database.commit()


async def generate_and_send_embed(embed11, channel_id):
    print(embed11, channel_id)


    try:
        embed = discord.Embed(title=embed11['title'], description=embed11['description'],
                              color=discord.Colour.from_rgb(173, 138, 47))
    except:
        try:
            embed = discord.Embed(title=embed11['url'], description=embed11['description'],
                                  color=discord.Colour.from_rgb(173, 138, 47))
        except:
            try:
                embed = discord.Embed(title=embed11['title'], description='',
                                      color=discord.Colour.from_rgb(173, 138, 47))
            except:
                try:
                    embed = discord.Embed(title=embed11['url'], description='',
                                          color=discord.Colour.from_rgb(173, 138, 47))
                except:
                    embed = discord.Embed(title='', description=embed11['description'],
                                          color=discord.Colour.from_rgb(173, 138, 47))

    try:
        fields = embed11['fields']
        for field in fields:
            embed.add_field(name=field['name'], value=field['value'], inline=field['inline'])
    except:
        pass

    embed.set_footer(text='Parsed by Rescue Alpha')



    channel = bot.get_channel(int(channel_id))

    await channel.send(embed=embed)


async def make_request():

    Session = sessionmaker(bind=engine)
    session = Session()

    posts = session.query(Post).all()

    for i in posts:

        if i.messageText == '':
            session.query(Post).filter(Post.id == i.id).delete()
            continue

        # print(i.type, i.messageText)

        if i.header_number == 1:
            header_ = header11
        elif i.header_number == 2:
            header_ = header12
        elif i.header_number == 3:
            header_ = header13
        elif i.header_number == 4:
            header_ = header14
        else:
            header_ = header15


        if i.type == 'REPLY':
            await generate_and_send_reply_embed(i.messageText_reply, json.loads(i.messageText), i.channel_id_RA, i.channel_id_other, header_)
        elif i.type == 'EMBED':
            await generate_and_send_embed(json.loads(i.messageText), i.channel_id_RA)
        elif i.type == 'ASIAN_MSG':
            if i.image:
                await generate_and_send_asian_message(i.messageText, i.channel_id_RA, True, i.channel_id_other, header_)
            else:
                await generate_and_send_asian_message(i.messageText, i.channel_id_RA, False, i.channel_id_other, header_)

        elif i.type == 'MSG':
            if i.image:
                await generate_and_send_message(i.messageText, i.channel_id_RA, True, i.channel_id_other, header_)
            else:
                await generate_and_send_message(i.messageText, i.channel_id_RA, False, i.channel_id_other,header_)

        session.query(Post).filter(Post.id == i.id).delete()

    session.commit()
    session.close()



@bot.event
async def on_ready():
    print(f'Bot is ready, running as {bot.user}.')
    asyncio.create_task(print_numbers())


async def print_numbers():
    while True:
        try:

            await make_request()

            await asyncio.sleep(1)

        except Exception as e:
            print(e)
            print('ОШИБКА')

            await asyncio.sleep(5)


if __name__ == '__main__':
    token = 'MTA2OTE3NjM1OTYxMzY0ODg5Ng.GdCxHf.QF4NYkDu_bCZ6L1avxJuOVYvI-FIg8dar-uzHY'

    bot.run(token, log_handler=None)
