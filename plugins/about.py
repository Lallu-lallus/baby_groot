await client.send_message(
            caption=presete.ABOUT_TXT.format(query.from_user.mention),
            chat_id=query.message.chat.id,
            reply_markup=reply_markup,
