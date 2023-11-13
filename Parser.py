import json
import random

import sqlite3
import time
import traceback
import uuid
from threading import Thread

import requests
import asyncio

import time
import pyperclip
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

parser_db_path = r'parser.db'


def make_request(mode):

    time.sleep(random.randint(100,450)/100)

    header1_main = {
        'authorization': ''
    }

    header2_main = {
        'authorization': ''
    }

    header = {
        'authorization': ''
    }

    if mode == 0:
        urls = [['🔳short-term', 'https://discord.com/api/v9/channels/1008457658543636590/messages',
         'https://discord.com/api/v9/channels/1042838923174477945/messages']]

    if mode == 1:
        urls = [
            ['🧧gds-call', 'https://discord.com/api/v9/channels/1041769170817273937/messages',
             'https://discord.com/api/v9/channels/1071081635614826567/messages'],
            ['🧧president-call', 'https://discord.com/api/v9/channels/1050272713253593088/messages',
             'https://discord.com/api/v9/channels/1071081876548222976/messages'],
            ['🧧皇帝肝-call', 'https://discord.com/api/v9/channels/1043171690605199401/messages',
             'https://discord.com/api/v9/channels/1071082009914519642/messages'],
            ['🧧boun-call', 'https://discord.com/api/v9/channels/1050763080923099227/messages',
             'https://discord.com/api/v9/channels/1071082271081242634/messages'],
            ['🧧hip-call', 'https://discord.com/api/v9/channels/1057938517319229483/messages',
             'https://discord.com/api/v9/channels/1071083019777093642/messages'],
            ['🧧moment-call', 'https://discord.com/api/v9/channels/1062357713318858802/messages',
             'https://discord.com/api/v9/channels/1071083453006753923/messages'],
            ['🧧bigh-call', 'https://discord.com/api/v9/channels/1063697668922167388/messages',
             'https://discord.com/api/v9/channels/1071083704178446336/messages'],
            ['🧧udon-call', 'https://discord.com/api/v9/channels/995397783739695124/messages',
             'https://discord.com/api/v9/channels/1071085654705983559/messages'],
            ['🧧luisun', 'https://discord.com/api/v9/channels/1043445505620975616/messages',
             'https://discord.com/api/v9/channels/1071086012979236935/messages'],
            ['🧧shingboi', 'https://discord.com/api/v9/channels/1067321233244442704/messages',
             'https://discord.com/api/v9/channels/1071086210635792505/messages'],
            ['🧧ericyin', 'https://discord.com/api/v9/channels/1029826651237908480/messages',
             'https://discord.com/api/v9/channels/1071086632956072019/messages'],

            ['🤖🟦eth-flip-bot', 'https://discord.com/api/v9/channels/969280818566561872/messages',
             'https://discord.com/api/v9/channels/1068869148689575946/messages'],

            ['🟦eth-calls-swanny', 'https://discord.com/api/v9/channels/1011217316794613822/messages',
             'https://discord.com/api/v9/channels/1042841179487752283/messages'],
            ['🟦eth-calls-shawns', 'https://discord.com/api/v9/channels/1018824014732476437/messages',
             'https://discord.com/api/v9/channels/1042841271267504279/messages'],
            ['🟦eth-calls-lv', 'https://discord.com/api/v9/channels/958945278872928256/messages',
             'https://discord.com/api/v9/channels/1042841359557611642/messages']]

        header_ = header11

    elif mode == 2:

        urls = [['⬛️alpha-info', 'https://discord.com/api/v9/channels/958945385408266330/messages',
         'https://discord.com/api/v9/channels/1042841527325573150/messages'],
        ['🟪sol-calls-lv', 'https://discord.com/api/v9/channels/1023181417309536317/messages',
         'https://discord.com/api/v9/channels/1042841527631761409/messages'],
        ['⬜️zoo-alpha', 'https://discord.com/api/v9/channels/1003400309533593680/messages',
         'https://discord.com/api/v9/channels/1042841527862435920/messages'],
        ['⬜️zoo-crypto', 'https://discord.com/api/v9/channels/1004988674070564965/messages',
         'https://discord.com/api/v9/channels/1042842668566331393/messages'],
        ['⬜️searchfi', 'https://discord.com/api/v9/channels/1034696173975507024/messages',
         'https://discord.com/api/v9/channels/1042842512043282452/messages'],

        ['🟦eth-calls-gianny', 'https://discord.com/api/v9/channels/1022213582412324905/messages',
         'https://discord.com/api/v9/channels/1042836994046300200/messages'],
        ['🟦eth-calls-cook', 'https://discord.com/api/v9/channels/1014259693474033684/messages',
         'https://discord.com/api/v9/channels/1042837048547082250/messages'],
        ['🟦eth-calls-youngb', 'https://discord.com/api/v9/channels/1075865614431813643/messages',
         'https://discord.com/api/v9/channels/1042837143204155412/messages'],
        ['🟦eth-calls-breezy', 'https://discord.com/api/v9/channels/1017487072531058728/messages',
         'https://discord.com/api/v9/channels/1042837193489666078/messages'],
        ['🟦eth-calls-swew', 'https://discord.com/api/v9/channels/1034511698800955522/messages',
         'https://discord.com/api/v9/channels/1042837276037763114/messages'],
        ['🟩guides', 'https://discord.com/api/v9/channels/966813430046670928/messages',
         'https://discord.com/api/v9/channels/1042837615340175411/messages'],
        ['🟧chaley-calls', 'https://discord.com/api/v9/channels/1035632117356429332/messages',
         'https://discord.com/api/v9/channels/1042837844730847272/messages'],
        ['🟧seb-calls', 'https://discord.com/api/v9/channels/1042145886043648132/messages',
         'https://discord.com/api/v9/channels/1042837884643852319/messages'],
        ['⬛️market-update', 'https://discord.com/api/v9/channels/1008457573709647963/messages',
         'https://discord.com/api/v9/channels/1042838192098902037/messages'],
        ['🟧trades-and-analysis', 'https://discord.com/api/v9/channels/1008457574963757217/messages',
         'https://discord.com/api/v9/channels/1042838566922879046/messages']]

        header_ = header12

    elif mode == 3:
        urls = [['🟩educational-content', 'https://discord.com/api/v9/channels/1008457578008813637/messages',
         'https://discord.com/api/v9/channels/1042838664469823598/messages'],
        ['⬜️important', 'https://discord.com/api/v9/channels/1008457649546858526/messages',
         'https://discord.com/api/v9/channels/1042838788885458985/messages'],
        ['🔳short-term', 'https://discord.com/api/v9/channels/1008457658543636590/messages',
         'https://discord.com/api/v9/channels/1042838923174477945/messages'],
        ['⬛️news-and-recaps', 'https://discord.com/api/v9/channels/1008457656056422450/messages',
         'https://discord.com/api/v9/channels/1042839147506827356/messages'],
        ['⬜️whitelist', 'https://discord.com/api/v9/channels/1008457667720781834/messages',
         'https://discord.com/api/v9/channels/1042839343628296243/messages'],
        ['🟨airdrops-gp', 'https://discord.com/api/v9/channels/1008457665179029504/messages',
         'https://discord.com/api/v9/channels/1042839534565601320/messages'],
        ['🟩educational-gp', 'https://discord.com/api/v9/channels/1008457662796664837/messages',
         'https://discord.com/api/v9/channels/1042839631214952478/messages'],
        ['mint-alerts', 'https://discord.com/api/v9/channels/966573323863613460/messages',
         'https://discord.com/api/v9/channels/1060526811773153371/messages'],
        ['premint-подборка', 'https://discord.com/api/v9/channels/971920936330752110/messages',
         'https://discord.com/api/v9/channels/1060528299102707713/messages'],

        ['🟪sol-calls-daniel', 'https://discord.com/api/v9/channels/1023158869612048395/messages',
         'https://discord.com/api/v9/channels/1065576458422071306/messages'],
        ['🟪sol-calls-james', 'https://discord.com/api/v9/channels/1023158889484648468/messages',
         'https://discord.com/api/v9/channels/1065585552621064202/messages'],
        ['🟪sol-calls-sd', 'https://discord.com/api/v9/channels/1023158869612048395/messages',
         'https://discord.com/api/v9/channels/1065589548454772786/messages'],
        ['🟪sol-calls-lev', 'https://discord.com/api/v9/channels/1031651714195001364/messages',
         'https://discord.com/api/v9/channels/1065591260036993045/messages'],
        ['🟪sol-calls-pd', 'https://discord.com/api/v9/channels/1034201693325369345/messages',
         'https://discord.com/api/v9/channels/1065591449581785138/messages'],
        ['🟪sol-calls-ls', 'https://discord.com/api/v9/channels/1004164219656216656/messages',
         'https://discord.com/api/v9/channels/1065600016498049134/messages']]

        header_ = header13

    elif mode == 4:

        urls = [['🟦eth-calls-hang', 'https://discord.com/api/v9/channels/1020422998907437096/messages',
         'https://discord.com/api/v9/channels/1065608583116488784/messages'],
        ['🟦eth-calls-rio', 'https://discord.com/api/v9/channels/1026138074725486692/messages',
         'https://discord.com/api/v9/channels/1065623945623117895/messages'],
        ['🟦eth-calls-mount', 'https://discord.com/api/v9/channels/1051249380155457659/messages',
         'https://discord.com/api/v9/channels/1065652206117867560/messages'],
        ['🟦eth-calls-flipd', 'https://discord.com/api/v9/channels/1051249399004663849/messages',
         'https://discord.com/api/v9/channels/1065652481255800982/messages'],

        ['🟧trading-hang', 'https://discord.com/api/v9/channels/1020423311123021824/messages',
         'https://discord.com/api/v9/channels/1065613397804191785/messages'],

        ['⬜️rap-calls', 'https://discord.com/api/v9/channels/1020423054859452426/messages',
         'https://discord.com/api/v9/channels/1065604497973448764/messages'],
        ['⬜️nos-calls', 'https://discord.com/api/v9/channels/1015623967312191548/messages',
         'https://discord.com/api/v9/channels/1065612427015757825/messages'],
        ['⬜️early-nft', 'https://discord.com/api/v9/channels/1026138002830934026/messages',
         'https://discord.com/api/v9/channels/1065623563282960435/messages'],
        ['⬜️wo-calls', 'https://discord.com/api/v9/channels/1026138097034985604/messages',
         'https://discord.com/api/v9/channels/1065624177631039538/messages'],
        ['⬜️degen-calls', 'https://discord.com/api/v9/channels/1026139047434928219/messages',
         'https://discord.com/api/v9/channels/1065624526513262662/messages'],
        ['⬜️hub-calls', 'https://discord.com/api/v9/channels/1051249360589033583/messages',
         'https://discord.com/api/v9/channels/1065651971375243415/messages'],
        ['⬜️wl-collector', 'https://discord.com/api/v9/channels/1051249466558119946/messages',
         'https://discord.com/api/v9/channels/1065653149949493249/messages'],

        ['🟩education-f', 'https://discord.com/api/v9/channels/1051249430826864741/messages',
         'https://discord.com/api/v9/channels/1065652815516672140/messages'],

        ['twitter-tracer', 'https://discord.com/api/v9/channels/1021152920361779282/messages',
         'https://discord.com/api/v9/channels/1065623151452626964/messages'],

        ['⬜️nft-ha', 'https://discord.com/api/v9/channels/1067087104577900624/messages',
         'https://discord.com/api/v9/channels/1068868479173804052/messages']]

        header_ = header14

    elif mode == 5:

        header

        urls = [['🟪sol-calls-alpha', 'https://discord.com/api/v9/channels/1023569058584612926/messages',
         'https://discord.com/api/v9/channels/1068869476101144656/messages'],
        ['🤖🟦eth-buy-infl', 'https://discord.com/api/v9/channels/958396122727075880/messages',
         'https://discord.com/api/v9/channels/1068916886932312124/messages'],

        ['🟦eth-gard', 'https://discord.com/api/v9/channels/1076098351122092103/messages',
         'https://discord.com/api/v9/channels/1080498322722271232/messages'],
        ['🟦eth-gard-2', 'https://discord.com/api/v9/channels/996268037701386271/messages',
         'https://discord.com/api/v9/channels/1080498449872584754/messages'],
        ['🤖🟦-eth-infl-buy', 'https://discord.com/api/v9/channels/958396122727075880/messages',
         'https://discord.com/api/v9/channels/1080498033755684884/messages'],
        ['🤖🟦-eth-flip-bot', 'https://discord.com/api/v9/channels/969280818566561872/messages',
         'https://discord.com/api/v9/channels/1080498144070082560/messages'],

        ['🤖🟦eth-monitor-infl', 'https://discord.com/api/v9/channels/983631558751682580/messages',
         'https://discord.com/api/v9/channels/1068916886932312124/messages'],
        ['🤖🟦eth-mint-infl', 'https://discord.com/api/v9/channels/958046743625367555/messages',
         'https://discord.com/api/v9/channels/1068869148689575946/messages'],
        ['📈new-contracts', 'https://discord.com/api/v9/channels/1065363461892214835/messages',
         'https://discord.com/api/v9/channels/1068911009001111613/messages'],
        ['📈trading-open', 'https://discord.com/api/v9/channels/1056904471441047663/messages',
         'https://discord.com/api/v9/channels/1068911764776947722/messages'],
        ['📈launch-stretch', 'https://discord.com/api/v9/channels/1077630959274430527/messages',
         'https://discord.com/api/v9/channels/1068868345199333498/messages'],
        ['📈bullish-deployer', 'https://discord.com/api/v9/channels/1070242691465613384/messages',
         'https://discord.com/api/v9/channels/1068868803578052710/messages'],
        ['📈locked-pairs', 'https://discord.com/api/v9/channels/1034845036430508172/messages',
         'https://discord.com/api/v9/channels/1080502036069630054/messages'],
        ['📈recall-pairs', 'https://discord.com/api/v9/channels/1074445472648921270/messages',
         'https://discord.com/api/v9/channels/1080502315028590652/messages'],
        ['📈coin-infl-buy', 'https://discord.com/api/v9/channels/1080830828558426132/messages',
         'https://discord.com/api/v9/channels/1082603147391930480/messages'],

        ['arb-new-pairs', 'https://discord.com/api/v9/channels/1076514749367472208/messages',
         'https://discord.com/api/v9/channels/1100385749771239494/messages'],
        ['arb-liqudity-added', 'https://discord.com/api/v9/channels/1076516151523287102/messages',
         'https://discord.com/api/v9/channels/1100386041044676608/messages'],
        ['arb-bullish-deployer', 'https://discord.com/api/v9/channels/1076516183571959859/messages',
         'https://discord.com/api/v9/channels/1100386367185358868/messages']]



        header_ = header15


    # first_time = True

    while True:
        time.sleep(random.randint(1, 6))

        print(1)

        for urll in urls:

            time.sleep(random.randint(1,6))

            try:

                gardens_list = ['📈coin-infl-buy', '🟦eth-gard', '🟦eth-gard-2', '🤖🟦-eth-infl-buy', '🤖🟦-eth-flip-bot',
                                '🤖🟦eth-monitor-infl', '🤖🟦eth-mint-infl', '📈new-contracts', '📈trading-open',
                                '📈launch-stretch', '📈bullish-deployer', '📈locked-pairs', '📈recall-pairs',
                                'arb-new-pairs','arb-liqudity-added','arb-bullish-deployer']

                if urll[0] not in gardens_list:
                    header1 = header1_main
                else:
                    header1 = header2_main

                with requests.get(urll[1], headers=header1) as resp:
                    # print(resp)
                    # print('1')
                    time.sleep(5)

                    if resp.status_code == 200:
                        dd = json.loads(resp.text)
                        print(urll[0])

                        hh = []
                        k = [0]
                        for i in k:

                            if i in hh:
                                continue

                            # time.sleep(5)

                            try:
                                if 'syntax' in dd[i]['content'] or 'fuck' in dd[i]['content']:
                                    continue
                            except:
                                pass

                            sql.execute(f'''SELECT ID FROM messages WHERE ID = {int(dd[i]['id'])}''')

                            # print(i)

                            if sql.fetchone() == None:
                                if dd[i]['id'] != '1105381838094073897':
                                    continue
                                print(dd[i])

                                payload = {'content': dd[i]['content'],
                                           'embeds': []}

                                files = {'file': ''}

                                tag = 0
                                try:
                                    if payload['content'][0] == '(':
                                        payload['content'] = '(reply to the message' + payload['content'][
                                                                                       payload['content'].find(':'):]
                                except:
                                    pass

                                sql.execute(f'''INSERT INTO messages VALUES ({dd[i]['id']})''')
                                database.commit()

                                try:
                                    if '(reply to the message:*' in payload['content']:
                                        reply_embed = payload['content'].replace('(reply to the message:*', '')[:-1]

                                        message = dd[i - 1]['content']
                                        sql.execute(f'''INSERT INTO messages VALUES ({dd[i - 1]['id']})''')
                                        database.commit()

                                        channel_id = urll[2].split('/')[6]

                                        hh.append(i - 1)

                                        Session = sessionmaker(bind=engine)
                                        session = Session()

                                        new_post = Post(id = str(uuid.uuid4()),
                                                        type = 'REPLY',
                                                        messageText_reply = reply_embed,
                                                        messageText = json.dumps(message),
                                                        channel_id_RA = channel_id,
                                                        channel_id_other = urll[0],
                                                        header_number = mode)

                                        session.add(new_post)
                                        session.commit()
                                        session.close()

                                        # generate_and_send_reply_embed(reply_embed, message, channel_id, urll[0], header_)

                                        continue



                                except:
                                    pass

                                while payload['content'].count('<@&') != 0:

                                    if payload['content'].count(':arrow_up:') == 2:
                                        payload['content'] = payload['content'].replace(':arrow_up:', '')

                                    payload['content'] = (payload['content'][:payload['content'].find('<@&')] + payload[
                                                                                                                    'content'][
                                                                                                                payload[
                                                                                                                    'content'].find(
                                                                                                                    '>',
                                                                                                                    payload[
                                                                                                                        'content'].find(
                                                                                                                        '<@&')) + 1:])
                                    tag = 1
                                print((dd[i]['embeds']))
                                # if payload['content'] == '':
                                #     payload['content'] = 'File'

                                if len(dd[i]['attachments']) != 0:
                                    # print(i['attachments'])
                                    for attachment in dd[i]['attachments']:
                                        photo_link = attachment['url']

                                        p = requests.get(photo_link)
                                        out = open("img.jpg", "wb")
                                        out.write(p.content)
                                        out.close()

                                        files['file'] = ("img.jpg", open("img.jpg", "rb"))

                                        break



                                elif len(dd[i]['embeds']) != 0:
                                    print('embed')

                                    for embed in dd[i]['embeds']:
                                        print('embed')

                                        if embed['type'] == 'rich':
                                            print('embed')

                                            payload_1 = {'content': ''}

                                            try:

                                                print(urll[2].split('/'))


                                                true1 = True
                                                try:
                                                    if embed['title'] in dd[i - 1]['content']:
                                                        true1 = False
                                                        sql.execute(
                                                            f'''INSERT INTO messages VALUES ({dd[i - 1]['id']})''')
                                                        database.commit()
                                                except:
                                                    pass

                                                try:
                                                    if embed['title'] in dd[i + 1]['content']:
                                                        true1 = False
                                                        sql.execute(
                                                            f'''INSERT INTO messages VALUES ({dd[i + 1]['id']})''')
                                                        database.commit()
                                                except:
                                                    pass

                                                if true1 == True:
                                                    Session = sessionmaker(bind=engine)
                                                    session = Session()

                                                    new_post = Post(id=str(uuid.uuid4()),
                                                                    type='EMBED',
                                                                    # messageText_reply=reply_embed,
                                                                    messageText=json.dumps(embed),
                                                                    channel_id_RA=urll[2].split('/')[6],
                                                                    # channel_id_other=urll[0],
                                                                    header_number=mode)

                                                    session.add(new_post)
                                                    session.commit()
                                                    session.close()

                                                    # await generate_and_send_embed(embed, urll[2].split('/')[6])




                                            except:

                                                payload_1['content'] += embed['description']

                                                if urll[0] in ['🧧gds-call', '🧧president-call', '🧧皇帝肝-call',
                                                               '🧧boun-call', '🧧hip-call', '🧧moment-call', '🧧bigh-call',
                                                               '🧧udon-call', '🧧luisun', '🧧shingboi', '🧧ericyin']:

                                                    Session = sessionmaker(bind=engine)
                                                    session = Session()

                                                    new_post = Post(id=str(uuid.uuid4()),
                                                                    type='ASIAN_MSG',
                                                                    # messageText_reply=reply_embed,
                                                                    messageText=payload_1['content'],
                                                                    channel_id_RA=urll[2].split('/')[6],
                                                                    channel_id_other=urll[0],
                                                                    image=False,
                                                                    header_number=mode)

                                                    session.add(new_post)
                                                    session.commit()
                                                    session.close()

                                                    # await generate_and_send_asian_message(payload_1['content'],
                                                    #                                       urll[2].split('/')[6], False,
                                                    #                                       urll[0], header_)

                                                else:

                                                    Session = sessionmaker(bind=engine)
                                                    session = Session()

                                                    new_post = Post(id=str(uuid.uuid4()),
                                                                    type='MSG',
                                                                    # messageText_reply=reply_embed,
                                                                    messageText=payload_1['content'],
                                                                    channel_id_RA=urll[2].split('/')[6],
                                                                    channel_id_other=urll[0],
                                                                    image=False,
                                                                    header_number=mode)

                                                    session.add(new_post)
                                                    session.commit()
                                                    session.close()

                                                    # await generate_and_send_message(payload_1['content'],
                                                    #                                 urll[2].split('/')[6], False,
                                                    #                                 urll[0], header_)

                                                # print(r.text)
                                        elif embed['type'] == 'image':

                                            photo_link = embed['url']

                                            p = requests.get(photo_link)
                                            out = open("img.jpg", "wb")
                                            out.write(p.content)
                                            out.close()

                                            files['file'] = ("img.jpg", open("img.jpg", "rb"))

                                            break

                                if files['file'] == '':
                                    print('FIle')

                                    if urll[0] in ['🧧gds-call', '🧧president-call', '🧧皇帝肝-call', '🧧boun-call',
                                                   '🧧hip-call', '🧧moment-call', '🧧bigh-call', '🧧udon-call', '🧧luisun',
                                                   '🧧shingboi', '🧧ericyin']:

                                        Session = sessionmaker(bind=engine)
                                        session = Session()

                                        new_post = Post(id=str(uuid.uuid4()),
                                                        type='ASIAN_MSG',
                                                        # messageText_reply=reply_embed,
                                                        messageText=payload['content'],
                                                        channel_id_RA=urll[2].split('/')[6],
                                                        channel_id_other=urll[0],
                                                        image=False,
                                                        header_number=mode)

                                        session.add(new_post)
                                        session.commit()
                                        session.close()

                                        # await generate_and_send_asian_message(payload['content'], urll[2].split('/')[6],
                                        #                                       False, urll[0], header_)

                                    else:

                                        Session = sessionmaker(bind=engine)
                                        session = Session()

                                        new_post = Post(id=str(uuid.uuid4()),
                                                        type='MSG',
                                                        # messageText_reply=reply_embed,
                                                        messageText=payload['content'],
                                                        channel_id_RA=urll[2].split('/')[6],
                                                        channel_id_other=urll[0],
                                                        image=False,
                                                        header_number=mode)

                                        session.add(new_post)
                                        session.commit()
                                        session.close()

                                        # await generate_and_send_message(payload['content'], urll[2].split('/')[6],
                                        #                                 False, urll[0], header_)

                                    print(f'\n\n{payload["content"]}\n\n')



                                else:

                                    if urll[0] in ['🧧gds-call', '🧧president-call', '🧧皇帝肝-call', '🧧boun-call',
                                                   '🧧hip-call', '🧧moment-call', '🧧bigh-call', '🧧udon-call', '🧧luisun',
                                                   '🧧shingboi', '🧧ericyin']:

                                        Session = sessionmaker(bind=engine)
                                        session = Session()

                                        new_post = Post(id=str(uuid.uuid4()),
                                                        type='ASIAN_MSG',
                                                        # messageText_reply=reply_embed,
                                                        messageText=payload['content'],
                                                        channel_id_RA=urll[2].split('/')[6],
                                                        channel_id_other=urll[0],
                                                        image=True,
                                                        header_number=mode)

                                        session.add(new_post)
                                        session.commit()
                                        session.close()

                                        # await generate_and_send_asian_message(payload['content'], urll[2].split('/')[6],
                                        #                                       True, urll[0], header_)

                                    else:

                                        Session = sessionmaker(bind=engine)
                                        session = Session()

                                        new_post = Post(id=str(uuid.uuid4()),
                                                        type='MSG',
                                                        # messageText_reply=reply_embed,
                                                        messageText=payload['content'],
                                                        channel_id_RA=urll[2].split('/')[6],
                                                        channel_id_other=urll[0],
                                                        image=True,
                                                        header_number=mode)

                                        session.add(new_post)
                                        session.commit()
                                        session.close()

                                        # await generate_and_send_message(payload['content'], urll[2].split('/')[6], True,
                                        #                                 urll[0], header_)

                                # print(r.text)
                                # await asyncio.sleep(100000)
            except Exception as e:
                traceback.print_exc()
                print(e)
                print('Global error')
                pass

        time.sleep(5)



def print_numbers():



    thread = Thread(target=make_request, args=(0,))
    thread.start()

    # await make_request()
    time.sleep(6)



if __name__ == '__main__':
    print_numbers()



