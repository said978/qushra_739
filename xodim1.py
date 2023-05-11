

import openpyxl
import pandas as pd
import telebot
from pushbullet import pushbullet
from telebot import types
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = telebot.TeleBot("5165263339:AAGoPdt4arFdOAwYuXeORPGYWRE091LzqOM")




workbook = openpyxl.load_workbook('data.xlsx')
sheet = workbook.active
@bot.message_handler(commands=['start'])
def send_welcome(message):
    stic = open('stic/welcome.webp', 'rb') #чтение файла в двоичном формате

    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("СМС QULANMA ")
    but2 = types.KeyboardButton("Xodimlar")
    markup.add(but1, but2)

    # Add phone number and timestamp to the spreadsheet
    row = [message.chat.id.user, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    sheet.append(row)
    workbook.save('data.xlsx')

    bot.reply_to(message, "Ассалому Алайкум ва Рахматуллахи ва Баракатух, {0.first_name}\nкредит карздорликни куриш мумкин".format(message.from_user)
    ,parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.id,stic)
@bot.message_handler(func=lambda message: message.text == "СМС QULANMA")
def send_video(message):
	video = open('stic/vid.mp4', 'rb')
	bot.send_video(message.chat.id, video,timeout=50)

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == "Xodimlar":
        inMurkup = types.InlineKeyboardMarkup(row_width=3)
        but1 = types.InlineKeyboardButton("A.Raxmonov", callback_data='book1')
        but2 = types.InlineKeyboardButton("A.Rustamov", callback_data='book2')
        but3 = types.InlineKeyboardButton("B.Dusiyarov", callback_data='book3')
        but4 = types.InlineKeyboardButton("V.Abdunazarov", callback_data='book4')
        but5 = types.InlineKeyboardButton("V.Begmanov", callback_data='book5')
        but6 = types.InlineKeyboardButton("G.Ziyaboev", callback_data='book6')
        but7 = types.InlineKeyboardButton("G.Ibodullaev", callback_data='book7')
        but8 = types.InlineKeyboardButton("G.Najmiddinova", callback_data='book8')
        but9 = types.InlineKeyboardButton("G.Nodirova", callback_data='book9')
        but10 = types.InlineKeyboardButton("J.Bobobekov", callback_data='book10')
        but11 = types.InlineKeyboardButton("J.Fayziev", callback_data='book11')
        but12 = types.InlineKeyboardButton("J.Sherkulov", callback_data='book12')
        but13 = types.InlineKeyboardButton("Z.Esanova", callback_data='book13')
        but14 = types.InlineKeyboardButton("I.Qorjabov", callback_data='book14')
        but15 = types.InlineKeyboardButton("K.Voxidov", callback_data='book15')
        but16 = types.InlineKeyboardButton("K.Ixtiyarov", callback_data='book16')
        but17 = types.InlineKeyboardButton("M.Tolliboeva", callback_data='book17')
        but18 = types.InlineKeyboardButton("N.Shirinov", callback_data='book18')
        but19 = types.InlineKeyboardButton("O.Jobborov", callback_data='book19')
        but20 = types.InlineKeyboardButton("O.Yalgashev", callback_data='book20')
        but21 = types.InlineKeyboardButton("Sardor", callback_data='book21')
        but22 = types.InlineKeyboardButton("S.Nodirov", callback_data='book22')
        but23 = types.InlineKeyboardButton("S.Tukliboev", callback_data='book23')
        but24 = types.InlineKeyboardButton("S.Ernazarova", callback_data='book24')
        but25 = types.InlineKeyboardButton("U.Abdiev", callback_data='book25')
        but26 = types.InlineKeyboardButton("U.Radjabov", callback_data='book26')
        but27 = types.InlineKeyboardButton("X.Abdum¢minov", callback_data='book27')
        but28 = types.InlineKeyboardButton("X.Chutboev", callback_data='book28')
        but29 = types.InlineKeyboardButton("XS.Pardaev", callback_data='book29')
        but30 = types.InlineKeyboardButton("Sh.Xamidov", callback_data='book30')
        but31 = types.InlineKeyboardButton("A.Jumanov", callback_data='book31')
        but32 = types.InlineKeyboardButton("E.Boliqulov", callback_data='book32')
        but33 = types.InlineKeyboardButton("E.Karshiev", callback_data='book33')
        but34 = types.InlineKeyboardButton("E.Temirov", callback_data='book34')
        but35 = types.InlineKeyboardButton("E.Eshboev", callback_data='book35')
        but36 = types.InlineKeyboardButton("Yuridik Bulm", callback_data='book36')
        inMurkup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12, but13, but14, but15,
                     but16, but17, but18, but19, but20, but21, but22, but23, but24, but25, but26, but27, but28, but29,
                     but30, but31, but32, but33, but34, but35, but36)

        bot.send_message(message.chat.id, "XODIMLAR RO'YXATI", reply_markup=inMurkup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'book1':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT'),
                     InlineKeyboardButton("NPL", callback_data='NPL'),
                     InlineKeyboardButton("SP", callback_data='SP'),
                     InlineKeyboardButton("SMS", callback_data='SMS')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig:", reply_markup=reply_markup)

    elif call.data in ['RUYXAT', 'NPL', 'SP', 'SMS']:
        # Extract the id from the callback data
        book_id = {'RUYXAT': 1, 'NPL': 2, 'SP': 3, 'SMS': 4}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)

            if call.data in ['SMS']:
                # Extract the id from the callback data
                book_id = {'SMS': 4}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.aqSQ0pxWKFFNQwUhLBRZ1H8TbI9pBBHL"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book2':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT1'),
                     InlineKeyboardButton("NPL", callback_data='NPL2'),
                     InlineKeyboardButton("SP", callback_data='SP3'),
                     InlineKeyboardButton("SMS", callback_data='SMS4')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)

    elif call.data in ['RUYXAT1', 'NPL2', 'SP3', 'SMS4']:
        # Extract the id from the callback data
        book2_id = {'RUYXAT1': 5, 'NPL2': 6, 'SP3': 7, 'SMS4': 8}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book2_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)

            if call.data in ['SMS4']:
                # Extract the id from the callback data
                book_id = {'SMS4': 8}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.f7ehE0HqTa8vt5lDYQUf4uCdYrJDy4zT"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book3':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT5'),
                     InlineKeyboardButton("NPL", callback_data='NPL6'),
                     InlineKeyboardButton("SP", callback_data='SP7'),
                     InlineKeyboardButton("SMS", callback_data='SMS8')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT5', 'NPL6', 'SP7', 'SMS8']:
        # Extract the id from the callback data
        book3_id = {'RUYXAT5': 9, 'NPL6': 10, 'SP7': 11, 'SMS8': 12}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book3_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS8']:
                # Extract the id from the callback data
                book_id = {'SMS8': 12}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.EzKY6Lrj2sse7wnNNAQ8yvMJhaegUz5L"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book4':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT9'),
                     InlineKeyboardButton("NPL", callback_data='NPL10'),
                     InlineKeyboardButton("SP", callback_data='SP11'),
                     InlineKeyboardButton("SMS", callback_data='SMS12')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT9', 'NPL10', 'SP11', 'SMS12']:
        # Extract the id from the callback data
        book4_id = {'RUYXAT9': 13, 'NPL10': 14, 'SP11': 15, 'SMS12': 16}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book4_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS12']:
                # Extract the id from the callback data
                book_id = {'SMS12': 16}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.GT4SwdyyxDfkxHibHh5pDRtfFXrgAWj0"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book5':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT13'),
                     InlineKeyboardButton("NPL", callback_data='NPL14'),
                     InlineKeyboardButton("SP", callback_data='SP15'),
                     InlineKeyboardButton("SMS", callback_data='SMS16')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT13', 'NPL14', 'SP15', 'SMS16']:
        # Extract the id from the callback data
        book5_id = {'RUYXAT13': 17, 'NPL14': 18, 'SP15': 19, 'SMS16': 20}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book5_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''


            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)

            if call.data in ['SMS16']:
                # Extract the id from the callback data
                book_id = {'SMS16': 20}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.0gRLPLJUDQKDxaJDpnScin7VFhiuY3OZ"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book6':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT17'),
                     InlineKeyboardButton("NPL", callback_data='NPL18'),
                     InlineKeyboardButton("SP", callback_data='SP19'),
                     InlineKeyboardButton("SMS", callback_data='SMS20')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT17', 'NPL18', 'SP19', 'SMS20']:
        # Extract the id from the callback data
        book6_id = {'RUYXAT17': 21, 'NPL18': 22, 'SP19': 23, 'SMS20': 24}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book6_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS20']:
                # Extract the id from the callback data
                book_id = {'SMS20': 24}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book7':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT21'),
                     InlineKeyboardButton("NPL", callback_data='NPL22'),
                     InlineKeyboardButton("SP", callback_data='SP23'),
                     InlineKeyboardButton("SMS", callback_data='SMS24')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT21', 'NPL22', 'SP23', 'SMS24']:
        # Extract the id from the callback data
        book7_id = {'RUYXAT21': 25, 'NPL22': 26, 'SP23': 27, 'SMS24': 28}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book7_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS24']:
                # Extract the id from the callback data
                book_id = {'SMS24': 28}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.HmZteYZtJvkhCbH5j1lUVUl64WSFajYr"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book8':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT25'),
                     InlineKeyboardButton("NPL", callback_data='NPL26'),
                     InlineKeyboardButton("SP", callback_data='SP27'),
                     InlineKeyboardButton("SMS", callback_data='SMS28')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT25', 'NPL226', 'SP27', 'SMS28']:
        # Extract the id from the callback data
        book8_id = {'RUYXAT25': 29, 'NPL26': 30, 'SP27': 31, 'SMS28': 32}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book8_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS28']:
                # Extract the id from the callback data
                book_id = {'SMS28': 32}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.LOVRpCxd6ZrLOjU9RNMQnzzniVfHbqzq"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book9':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT29'),
                     InlineKeyboardButton("NPL", callback_data='NPL30'),
                     InlineKeyboardButton("SP", callback_data='SP31'),
                     InlineKeyboardButton("SMS", callback_data='SMS32')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT29', 'NPL30', 'SP31', 'SMS32']:
        # Extract the id from the callback data
        book9_id = {'RUYXAT29': 33, 'NPL30': 34, 'SP31': 35, 'SMS32': 36}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book9_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS32']:
                # Extract the id from the callback data
                book_id = {'SMS32': 36}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book10':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT33'),
                     InlineKeyboardButton("NPL", callback_data='NPL34'),
                     InlineKeyboardButton("SP", callback_data='SP35'),
                     InlineKeyboardButton("SMS", callback_data='SMS36')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT33', 'NPL34', 'SP35', 'SMS36']:
        # Extract the id from the callback data
        book10_id = {'RUYXAT33': 37, 'NPL34': 38, 'SP35': 39, 'SMS36': 40}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book10_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS36']:
                # Extract the id from the callback data
                book_id = {'SMS36': 40}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book11':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT37'),
                     InlineKeyboardButton("NPL", callback_data='NPL38'),
                     InlineKeyboardButton("SP", callback_data='SP39'),
                     InlineKeyboardButton("SMS", callback_data='SMS40')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT37', 'NPL38', 'SP39', 'SMS40']:
        # Extract the id from the callback data
        book11_id = {'RUYXAT37': 41, 'NPL38': 42, 'SP39': 43, 'SMS40': 44}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book11_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS40']:
                # Extract the id from the callback data
                book_id = {'SMS40': 44}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.9qLOmY5hgmnQbOkUD2uGirEky4BFcivv"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book12':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT41'),
                     InlineKeyboardButton("NPL", callback_data='NPL42'),
                     InlineKeyboardButton("SP", callback_data='SP43'),
                     InlineKeyboardButton("SMS", callback_data='SMS44')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT41', 'NPL42', 'SP43', 'SMS44']:
        # Extract the id from the callback data
        book12_id = {'RUYXAT41': 45, 'NPL42': 46, 'SP43': 47, 'SMS44': 48}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book12_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''


            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS44']:
                # Extract the id from the callback data
                book_id = {'SMS44': 48}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.bpN3YJjg3SKhCwFvwnD2QphOGPlg7Sib"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book13':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT45'),
                     InlineKeyboardButton("NPL", callback_data='NPL46'),
                     InlineKeyboardButton("SP", callback_data='SP47'),
                     InlineKeyboardButton("SMS", callback_data='SMS48')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT45', 'NPL46', 'SP47', 'SMS48']:
        # Extract the id from the callback data
        book13_id = {'RUYXAT45': 49, 'NPL46': 50, 'SP47': 51, 'SMS48': 52}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book13_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS48']:
                # Extract the id from the callback data
                book_id = {'SMS48': 52}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.c0ySTty83zmlLSoooeGcIt6mh204Qg7x"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book14':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT49'),
                     InlineKeyboardButton("NPL", callback_data='NPL50'),
                     InlineKeyboardButton("SP", callback_data='SP51'),
                     InlineKeyboardButton("SMS", callback_data='SMS52')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT49', 'NPL50', 'SP51', 'SMS52']:
        # Extract the id from the callback data
        book14_id = {'RUYXAT49': 53, 'NPL50': 54, 'SP51': 55, 'SMS52': 56}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book14_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS52']:
                # Extract the id from the callback data
                book_id = {'SMS52': 56}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.eA0MsXOmltqMK7ywWMgEjSaQApuIGVtm"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book15':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT53'),
                     InlineKeyboardButton("NPL", callback_data='NPL54'),
                     InlineKeyboardButton("SP", callback_data='SP55'),
                     InlineKeyboardButton("SMS", callback_data='SMS56')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT53', 'NPL54', 'SP55', 'SMS56']:
        # Extract the id from the callback data
        book15_id = {'RUYXAT53': 57, 'NPL54': 58, 'SP55': 59, 'SMS56': 60}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book15_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''
            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS56']:
                # Extract the id from the callback data
                book_id = {'SMS56': 60}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.f5wGyXZ2QH3btzYYUg6TsvZMa7MbzoCj"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book16':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT57'),
                     InlineKeyboardButton("NPL", callback_data='NPL58'),
                     InlineKeyboardButton("SP", callback_data='SP59'),
                     InlineKeyboardButton("SMS", callback_data='SMS60')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT57', 'NPL58', 'SP59', 'SMS60']:
        # Extract the id from the callback data
        book16_id = {'RUYXAT57': 61, 'NPL58': 62, 'SP59': 63, 'SMS60': 64}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book16_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS60']:
                # Extract the id from the callback data
                book_id = {'SMS60': 64}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.tRAar6Brn7iREBVDhEORK3Gnm8iLX0WT"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book17':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT61'),
                     InlineKeyboardButton("NPL", callback_data='NPL62'),
                     InlineKeyboardButton("SP", callback_data='SP63'),
                     InlineKeyboardButton("SMS", callback_data='SMS64')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT61', 'NPL62', 'SP63', 'SMS64']:
        # Extract the id from the callback data
        book17_id = {'RUYXAT61': 65, 'NPL62': 66, 'SP63': 67, 'SMS64': 68}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book17_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS64']:
                # Extract the id from the callback data
                book_id = {'SMS64': 68}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.jUBFHhyXs0TlFOFTO0ziWnmnAvXhfsx5"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book18':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT65'),
                     InlineKeyboardButton("NPL", callback_data='NPL66'),
                     InlineKeyboardButton("SP", callback_data='SP67'),
                     InlineKeyboardButton("SMS", callback_data='SMS68')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT65', 'NPL66', 'SP67', 'SMS68']:
        # Extract the id from the callback data
        book18_id = {'RUYXAT65': 69, 'NPL66': 70, 'SP67': 71, 'SMS68': 72}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book18_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''
            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS68']:
                # Extract the id from the callback data
                book_id = {'SMS68': 72}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.tvtozL1VVNywHD3x83j1s3wG03VH4G55"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book19':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT69'),
                     InlineKeyboardButton("NPL", callback_data='NPL70'),
                     InlineKeyboardButton("SP", callback_data='SP71'),
                     InlineKeyboardButton("SMS", callback_data='SMS72')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT69', 'NPL70', 'SP71', 'SMS72']:
        # Extract the id from the callback data
        book19_id = {'RUYXAT69': 73, 'NPL70': 74, 'SP71': 75, 'SMS72': 76}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book19_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS72']:
                # Extract the id from the callback data
                book_id = {'SMS72': 76}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book20':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT73'),
                     InlineKeyboardButton("NPL", callback_data='NPL74'),
                     InlineKeyboardButton("SP", callback_data='SP75'),
                     InlineKeyboardButton("SMS", callback_data='SMS76')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT73', 'NPL74', 'SP75', 'SMS76']:
        # Extract the id from the callback data
        book20_id = {'RUYXAT73': 77, 'NPL74': 78, 'SP75': 79, 'SMS76': 80}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book20_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS76']:
                # Extract the id from the callback data
                book_id = {'SMS76': 80}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book21':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT77'),
                     InlineKeyboardButton("NPL", callback_data='NPL78'),
                     InlineKeyboardButton("SP", callback_data='SP79'),
                     InlineKeyboardButton("SMS", callback_data='SMS80')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT77', 'NPL78', 'SP79', 'SMS80']:
        # Extract the id from the callback data
        book21_id = {'RUYXAT77': 81, 'NPL78': 82, 'SP79': 83, 'SMS80': 84}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book21_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS80']:
                # Extract the id from the callback data
                book_id = {'SMS80': 84}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.n4DDQlzGRLn1kRfN2RMa8gUcJWtcBULS"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book22':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT81'),
                     InlineKeyboardButton("NPL", callback_data='NPL82'),
                     InlineKeyboardButton("SP", callback_data='SP83'),
                     InlineKeyboardButton("SMS", callback_data='SMS84')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT81', 'NPL82', 'SP83', 'SMS84']:
        # Extract the id from the callback data
        book22_id = {'RUYXAT81': 85, 'NPL82': 86, 'SP83': 87, 'SMS84': 88}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book22_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS84']:
                # Extract the id from the callback data
                book_id = {'SMS84': 88}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.nCM0koNI9oGCSkElF9zSjqt2Dvbv6soC"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book23':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT85'),
                     InlineKeyboardButton("NPL", callback_data='NPL86'),
                     InlineKeyboardButton("SP", callback_data='SP87'),
                     InlineKeyboardButton("SMS", callback_data='SMS88')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT85', 'NPL86', 'SP87', 'SMS88']:
        # Extract the id from the callback data
        book23_id = {'RUYXAT85': 89, 'NPL86': 90, 'SP87': 91, 'SMS88': 92}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book23_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS88']:
                # Extract the id from the callback data
                book_id = {'SMS88': 92}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.rbDks4xsWJVQ4omxJXE1b3rkxq3CX3tI"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book24':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT89'),
                     InlineKeyboardButton("NPL", callback_data='NPL90'),
                     InlineKeyboardButton("SP", callback_data='SP91'),
                     InlineKeyboardButton("SMS", callback_data='SMS92')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT89', 'NPL90', 'SP91', 'SMS92']:
        # Extract the id from the callback data
        book24_id = {'RUYXAT89': 93, 'NPL90': 94, 'SP91': 95, 'SMS92': 96}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book24_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS92']:
                # Extract the id from the callback data
                book_id = {'SMS92': 96}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.pBbnhIxfw5r74hlFGOxjvbNTfORgHFvJ"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book25':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT93'),
                     InlineKeyboardButton("NPL", callback_data='NPL94'),
                     InlineKeyboardButton("SP", callback_data='SP95'),
                     InlineKeyboardButton("SMS", callback_data='SMS96')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT93', 'NPL94', 'SP95', 'SMS96']:
        # Extract the id from the callback data
        book25_id = {'RUYXAT93': 97, 'NPL94': 98, 'SP95': 99, 'SMS96': 100}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book25_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS96']:
                # Extract the id from the callback data
                book_id = {'SMS96': 100}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.1QDzJ5V9ikBQBlkkUVL6kDS7titj6OES"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book26':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT97'),
                     InlineKeyboardButton("NPL", callback_data='NPL98'),
                     InlineKeyboardButton("SP", callback_data='SP99'),
                     InlineKeyboardButton("SMS", callback_data='SMS100')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT97', 'NPL98', 'SP99', 'SMS100']:
        # Extract the id from the callback data
        book26_id = {'RUYXAT97': 101, 'NPL98': 102, 'SP99': 103, 'SMS100': 104}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book26_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS100']:
                # Extract the id from the callback data
                book_id = {'SMS100': 104}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.C4z1e6CS7BkD3nGjJb6rW0OMNuCXGJOK"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")

    if call.data == 'book27':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT101'),
                     InlineKeyboardButton("NPL", callback_data='NPL102'),
                     InlineKeyboardButton("SP", callback_data='SP103'),
                     InlineKeyboardButton("SMS", callback_data='SMS104')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT101', 'NPL102', 'SP103', 'SMS104']:
        # Extract the id from the callback data
        book27_id = {'RUYXAT101': 105, 'NPL102': 106, 'SP103': 107, 'SMS104': 108}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book27_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS104']:
                # Extract the id from the callback data
                book_id = {'SMS104': 108}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book28':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT105'),
                     InlineKeyboardButton("NPL", callback_data='NPL106'),
                     InlineKeyboardButton("SP", callback_data='SP107'),
                     InlineKeyboardButton("SMS", callback_data='SMS108')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT105', 'NPL106', 'SP107', 'SMS108']:
        # Extract the id from the callback data
        book28_id = {'RUYXAT105': 109, 'NPL106': 110, 'SP107': 111, 'SMS108': 112}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book28_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS108']:
                # Extract the id from the callback data
                book_id = {'SMS108': 112}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book29':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT109'),
                     InlineKeyboardButton("NPL", callback_data='NPL110'),
                     InlineKeyboardButton("SP", callback_data='SP111'),
                     InlineKeyboardButton("SMS", callback_data='SMS112')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT109', 'NPL110', 'SP111', 'SMS112']:
        # Extract the id from the callback data
        book29_id = {'RUYXAT109': 113, 'NPL110': 114, 'SP111': 115, 'SMS112': 116}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book29_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS112']:
                # Extract the id from the callback data
                book_id = {'SMS112': 116}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.vEGNJXMOKS4Fg1biLyyRbdODWbv36IF8"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book30':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT113'),
                     InlineKeyboardButton("NPL", callback_data='NPL114'),
                     InlineKeyboardButton("SP", callback_data='SP115'),
                     InlineKeyboardButton("SMS", callback_data='SMS116')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT113', 'NPL114', 'SP115', 'SMS116']:
        # Extract the id from the callback data
        book30_id = {'RUYXAT113': 117, 'NPL114': 118, 'SP115': 119, 'SMS116': 120}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book30_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS116']:
                # Extract the id from the callback data
                book_id = {'SMS116': 120}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book31':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT117'),
                     InlineKeyboardButton("NPL", callback_data='NPL118'),
                     InlineKeyboardButton("SP", callback_data='SP119'),
                     InlineKeyboardButton("SMS", callback_data='SMS120')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT117', 'NPL118', 'SP119', 'SMS120']:
        # Extract the id from the callback data
        book31_id = {'RUYXAT117': 121, 'NPL118': 122, 'SP119': 123, 'SMS120': 124}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book31_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS120']:
                # Extract the id from the callback data
                book_id = {'SMS120': 124}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book32':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT121'),
                     InlineKeyboardButton("NPL", callback_data='NPL122'),
                     InlineKeyboardButton("SP", callback_data='SP123'),
                     InlineKeyboardButton("SMS", callback_data='SMS124')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT121', 'NPL122', 'SP123', 'SMS124']:
        # Extract the id from the callback data
        book32_id = {'RUYXAT121': 125, 'NPL122': 126, 'SP123': 127, 'SMS124': 128}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book32_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS124']:
                # Extract the id from the callback data
                book_id = {'SMS124': 128}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.0XFRCPVVhW365sTxjHztHkGRzoXqn2vn"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book33':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT125'),
                     InlineKeyboardButton("NPL", callback_data='NPL126'),
                     InlineKeyboardButton("SP", callback_data='SP127'),
                     InlineKeyboardButton("SMS", callback_data='SMS128')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT125', 'NPL126', 'SP127', 'SMS128']:
        # Extract the id from the callback data
        book33_id = {'RUYXAT125': 129, 'NPL126': 130, 'SP127': 131, 'SMS128': 132}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book33_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS128']:
                # Extract the id from the callback data
                book_id = {'SMS128': 132}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.Wl1muwtW2Sdn44vbBuMZKctykmPiZcCD"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book34':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT129'),
                     InlineKeyboardButton("NPL", callback_data='NPL130'),
                     InlineKeyboardButton("SP", callback_data='SP131'),
                     InlineKeyboardButton("SMS", callback_data='SMS132')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT129', 'NPL130', 'SP131', 'SMS132']:
        # Extract the id from the callback data
        book34_id = {'RUYXAT129': 133, 'NPL130': 134, 'SP131': 135, 'SMS132': 136}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book34_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS132']:
                # Extract the id from the callback data
                book_id = {'SMS132': 136}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.5wAPFpDURHSGTEiNobwI9USaR8Zg2aJj"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book35':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT133'),
                     InlineKeyboardButton("NPL", callback_data='NPL134'),
                     InlineKeyboardButton("SP", callback_data='SP135'),
                     InlineKeyboardButton("SMS", callback_data='SMS136')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT133', 'NPL134', 'SP135', 'SMS136']:
        # Extract the id from the callback data
        book35_id = {'RUYXAT133': 137, 'NPL134': 138, 'SP135': 139, 'SMS136': 140}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book35_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:
            message = ''
            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS136']:
                # Extract the id from the callback data
                book_id = {'SMS136': 140}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o.guR7UoAaxZPkKiG1Ia3AFXaiLFhMBQuG"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")
    if call.data == 'book36':
        keyboard = [[InlineKeyboardButton("RUYXAT", callback_data='RUYXAT137'),
                     InlineKeyboardButton("NPL", callback_data='NPL138'),
                     InlineKeyboardButton("SP", callback_data='SP139'),
                     InlineKeyboardButton("SMS", callback_data='SMS140')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "Ma'lumotlarni va SMS yuborish uchun tugamni bosig", reply_markup=reply_markup)
    elif call.data in ['RUYXAT137', 'NPL138', 'SP139', 'SMS140']:
        # Extract the id from the callback data
        book36_id = {'RUYXAT137': 141, 'NPL138': 142, 'SP139': 143, 'SMS140': 144}[call.data]

        # Read the data from the Excel file
        df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

        # Filter the data based on the id
        df_filtered = df[df['id'] == book36_id]

        # Check if there is data for the selected id
        if df_filtered.empty:
            bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
        else:

            if df_filtered.empty:
                bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
            else:
                # Select only the 'name' and 'Sum' columns
                df_filtered = df_filtered[['name', 'Sum']]

                # Define the filename based on the selected option
                filename = call.data + '.xlsx'

                # Save the file in the 'data' directory
                df_filtered.to_excel('data/' + filename, index=False)

                # Read the file and send it as a document
                with open('data/' + filename, 'rb') as file:
                    bot.send_document(call.message.chat.id, document=file)
            if call.data in ['SMS140']:
                # Extract the id from the callback data
                book_id = {'SMS140': 144}[call.data]

                # Read the data from the Excel file
                df = pd.read_excel('citat1.xlsx', sheet_name='Лист1')

                # Convert the "Sum" column to a numeric data type
                # df['Sum'] = pd.to_numeric(df['Sum'], errors='coerce')

                # Filter the data based on the id
                df_filtered = df[df['id'] == book_id]

                # Check if there is data for the selected id
                if df_filtered.empty:
                    bot.send_message(call.message.chat.id, "Bunday ma'lumot yo'q xozircha.")
                else:
                    # Get the Pushbullet API key
                    pb_api_key = "o00"

                    # Authenticate with the Pushbullet API
                    pb = pushbullet.Pushbullet(pb_api_key)

                    # Load the device that you want to send SMS to
                    device = pb.devices[0]  # Replace 0 with the index of your device

                    # Loop over the filtered data and send an SMS to each phone number
                    for index, row in df_filtered.iterrows():
                        phone_number = row['name']
                        name = row['Sum']
                        message = row['txt']
                        message_text = f"Hurmatli {name}, {message}"
                        print(f"Sending SMS to {phone_number}: {message_text}")

                        # Send the SMS using Pushbullet
                        push = pb.push_sms(device, phone_number, message_text)

                        if 'active' in push and push['active']:
                            print("SMS sent successfully!")
                        else:
                            print("Failed to send SMS.")


bot.polling(none_stop=True)