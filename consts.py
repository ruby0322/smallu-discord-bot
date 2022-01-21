from discord.embeds import Embed


TOKEN = 'ODYzMDMwNjY1MDIzOTc5NTMy.YOg98A.YzhsQnyODZz5m3cP7LZWkA1Kgls'

command_prefix = '#'

welcome_channel_id = 863039310630486036
leave_channel_id = 863039330066104391
task_channel_id = 863095974620168202
news_channel_id = 865168900864868362


cle_des = '你好😄我是小幽👻\n\"()\"代表必要參數\n\"[]\" 代表選擇性參數\n🆕可以加空白 ex小幽 在嗎\n'

if True:
    cle = Embed(title='小幽指令集', descrption=cle_des) 
    cle.set_thumbnail(url='https://i.imgur.com/65rKSh9.png')
    cle.add_field(name='➖➖➖小幽公告📬➖➖➖', value='置頂指令', inline=False)
    cle.add_field(name='💬 小幽公告', value='▶ 時有可賺小幽幣的問卷\n▶ 小幽的公告會放在這裡\n▶ 不定期頻繁更新', inline=True)
    cle.add_field(name='➖➖➖關於小幽👻➖➖➖', value='關於小幽的指令', inline=False)
    cle.add_field(name='💬 小幽指令集', value='▶ 查看所有小幽看得懂的指令', inline=True)
    cle.add_field(name='💬 小幽回報', value='▶ 回報問題或想法給小幽的主人', inline=True)
    cle.add_field(name='💬 小幽在嗎', value='▶ 確認小幽是否正常運作', inline=True)
    cle.add_field(name='➖➖➖線上資料💻➖➖➖', value='關於小幽的指令', inline=False)
    cle.add_field(name='💬 小幽疫情', value='▶ 小幽給你及時疫情資訊\n▶ 資料來源: 衛福部疾管署\n▶ 請放心信任資訊', inline=True)
    cle.add_field(name='💬 小幽抽圖(關鍵字)', value='▶ 抽取1張相關圖片\n▶ 資料來源: Unsplash\n▶ 關鍵字以英文為佳', inline=True)
    cle.add_field(name='💬 小幽天氣(縣市)', value='▶ 小幽告訴你給定地區的天氣\n▶ 資料來源: 中央氣象局api\n▶ 請放心信任資訊', inline=True)
    cle.add_field(name='💬 小幽查(要查的東西)', value='▶ 小幽幫你估狗', inline=True)
    cle.add_field(name='💬 小幽科普', value='▶ 小幽隨機科普一個知識\n來源: 維基百科\n▶ 題庫上百萬', inline=True)
    cle.add_field(name='➖➖➖紓壓小品🕹➖➖➖', value='讓你放鬆心情的小功能', inline=False)
    cle.add_field(name='💬 小幽說(想說的話)', value='▶ 讓小幽學你說話', inline=True)
    cle.add_field(name='➖➖➖實用功能📋➖➖➖', value='幫你省時省力的小功能', inline=False)
    cle.add_field(name='💬 小幽算 (算式) [取整數/取到小數第()位]', value='▶ 讓小幽幫你解決數學吧', inline=True)
    cle.add_field(name='➖➖➖⚠施工中⚠➖➖➖', value='正在研發新功能', inline=False)

if True:
    be = Embed(title='小幽公告', description='近期公告')
    be.add_field(name='[功能]',  value='目前Discord開放的指令數目\n約為LINE的50%，還請見諒')
    be.add_field(name='[表單]',  value='暫無')