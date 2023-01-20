import testcount,reply

def nameregister(event):
    if testcount.name_count == 0:
        reply.reply_message(event,"名前を入力してください")
        testcount.name_count = 1
    elif testcount.name_count == 1:
        global user
        global name
        user = event.source.user_id
        name = event.message.text
        reply.reply_message(event,name + "\nこの名前で登録します\nこれからあなたの発言は、名前込みで当チャンネルフォロワーに発信されます\n使用が終わり次第、解除と送信してください")
        testcount.name_count = 2

