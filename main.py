# ##################################################################################################################
#
# Please left a star on github if you like this project =)
#                       github.com/AminAlam
#
# ##################################################################################################################

from configs import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



class Users:
    user_count = 0
    chat_ids = []

    def __init__(self, chat_number=None, user_id=None, text=None, delete_message_id=None, user_name=None,
                 poshtibani_boolian=None, poshtibani_message=None, owner_questioner_chatid=None,
                 AnswerFromPoshtibani=None, agahi_boolian=None, agahi_number=0, agahi_files=None,
                 agahi_type=None, agahi_onvan=None, agahi_money=None, agahi_tozih=None, agahi_file_type='text',
                 owner_accepted_message=None, username_boolian=None, requested_agahi=None,
                 pishnahadats_for_agahi=['0', '1']):
        self.chat_number = chat_number
        self.user_id = user_id
        self.text = text
        self.delete_message_id = delete_message_id
        self.user_name = user_name
        self.poshtibani_boolian = poshtibani_boolian
        self.poshtibani_message = poshtibani_message
        self.owner_questioner_chatid = owner_questioner_chatid
        self.AnswerFromPoshtibani = AnswerFromPoshtibani
        self.agahi_boolian = agahi_boolian
        self.agahi_type = agahi_type
        self.agahi_onvan = agahi_onvan
        self.agahi_money = agahi_money
        self.agahi_number = agahi_number
        self.agahi_tozih = agahi_tozih
        self.agahi_files = agahi_files
        self.agahi_file_type = agahi_file_type
        self.owner_accepted_message = owner_accepted_message
        self.pishnahadats_for_agahi = pishnahadats_for_agahi
        self.username_boolian = username_boolian
        self.requested_agahi = requested_agahi
        Users.user_count = Users.user_count + 1
        Users.chat_ids = Users.chat_ids + [str(chat_number)]


def agahi_money(update, context, message_agahi, money):
    money_number = int(money)
    message = message_agahi[0]

    try:
        file = message.photo[-1]
        file_type = "jpg"
        file_photo_adress = str(file.file_id)
    except:
        file_photo = 0

    if (message.document != None):
        file_type = "pdf"
        file_documnet = 1
        file = message.document
        file_documenet_adress = str(file.file_id)
    number = 0

    if message.caption != None:
        text = message.caption

        request_number = message_agahi[1]
        coded_info = request_number+ 'F' + str(number)
        button_list = [InlineKeyboardButton("Payment", callback_data="yes_pay_money"+coded_info),
                       InlineKeyboardButton("Cancel", callback_data="no_dont_pay_money"+coded_info),
                       ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        index_E = request_number.find('E')
        questioner_chat_id = request_number[:index_E]
        context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has been approved. The cost of sending an ad to the channel is equal to '+str(money_number) + ' Is. As soon as you pay through the link below, your ad will be placed on the channel. ' +'\n')


        if (file_type == 'jpg'):
            message_bot = context.bot.send_photo(photo=file_photo_adress, chat_id=int(questioner_chat_id),
                                                 reply_markup=reply_markup, caption=text)
        if (file_type == 'pdf'):
            message_bot = context.bot.send_document(document=file_documenet_adress, chat_id=int(questioner_chat_id),
                                                    reply_markup=reply_markup, caption=text)



    if message.caption == None:
        text = message.text
        request_number = message_agahi[1]
        coded_info = request_number+ 'F' + str(number)
        button_list = [InlineKeyboardButton("Payment", callback_data="yes_pay_money"+coded_info),
                       InlineKeyboardButton("Cancel", callback_data="no_dont_pay_money"+coded_info),
                       ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        index_E = request_number.find('E')
        questioner_chat_id = request_number[:index_E]
        context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has been approved. The cost of sending an ad to the channel is equal to '+str(money_number) + ' Is. As soon as you pay through the link below, your ad will be placed on the channel. ' +'\n')

        context.bot.send_message(chat_id=int(questioner_chat_id),
                                 reply_markup=reply_markup, text=text)

def usual_check(update, context):
    try:
        chat_id = update.message.chat_id
    except:
        chat_id = update.effective_chat.id
    class_id = str(update.message.from_user.id)
    user_chat_id = str(chat_id)
    user_id = update.message.from_user.id
    global MAIN_CHANNEL
    try:
        isinstance(globals()[class_id], Users)
    except:
        globals()[class_id] = Users(chat_number=chat_id)

    # if not os.path.exists(os.getcwd() + '/' + str(user_id)):
    #    os.mkdir(os.getcwd() + '/' + str(user_id))
    state = context.bot.get_chat_member(chat_id=MAIN_CHANNEL, user_id=user_id)
    if state.status == "left":
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        join_channel_message = 'Please join ' + MAIN_CHANNEL + ' for using this bot.' + '🌹'
        context.bot.sendMessage(chat_id=chat_id, text=join_channel_message)
        join_boolian = 0
    else:
        join_boolian = 1
        if not os.path.exists(os.getcwd() + '/' + str(chat_id)):
            os.mkdir(os.getcwd() + '/' + str(chat_id))
    return join_boolian

def start(update, context):
    """Send a message when the command /start is issued."""
    global OWNER_ID
    chat_id = update.message.chat_id
    class_id = str(update.message.from_user.id)
    join_boolian = usual_check(update, context)
    # usual start
    if globals()[class_id].requested_agahi == None:
        if OWNER_ID != chat_id:
            context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
            start_message = "Hello, welcome buddy :) "
            context.bot.sendMessage(chat_id=chat_id, text=start_message)
            if join_boolian:
                three_choice(update, context)
    # request message
    else:
        context.bot.sendMessage(chat_id=chat_id, text='✍️' +'Please send your message to the owner of the ad:')

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def enseraf(update, context):
    chat_id = update.message.chat_id
    global OWNER_ID
    global enseraf_as_agahi
    if chat_id != OWNER_ID:
        menu_keyboard = [[enseraf_as_agahi]]
        menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        message = 'You can unsubscribe from the ad at any time (from the menu inside the keyboard)'
        context.bot.send_message(chat_id=chat_id, text=message, reply_markup=menu_markup)


def three_choice(update, context):
    global OWNER_ID
    global SabteAgahi
    global ErtebatBaPoshtibani
    global RahnamayeRobot
    try:
        chat_id = update.message.chat_id
    except:
        chat_id = update.effective_chat.id
    if chat_id != OWNER_ID:
        menu_keyboard = [[SabteAgahi], [ErtebatBaPoshtibani], [RahnamayeRobot],["Bot's Developer"]]
        menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        message = 'How can I help you?'
        context.bot.send_message(chat_id=chat_id, text=message, reply_markup=menu_markup)

def poshtibani_func(update, context):
    chat_id = update.message.chat_id
    global YesSendit_posht
    global NoDontSendit_posht
    global OWNER_ID
    if (chat_id != OWNER_ID):
        menu_keyboard = [[YesSendit_posht], [NoDontSendit_posht]]
        menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        message = 'Send the above message?'
        context.bot.send_message(chat_id=chat_id, text=message, reply_markup=menu_markup)

def JPG_handler(update, context):
    chat_id = update.message.chat_id
    user_chat_id = str(chat_id)
    class_id = str(update.message.from_user.id)
    context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
    globals()[class_id].delete_message_id = None
    file = update.message.photo[-1]
    globals()[class_id].agahi_files = str(file.file_id)
    globals()[class_id].agahi_file_type = 'JPG'
    agahi_validate(update, context)

def PDF_handler(update, context):
    class_id = str(update.message.from_user.id)
    chat_id = update.message.chat_id
    user_chat_id = str(chat_id)
    context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
    globals()[class_id].delete_message_id = None
    file = update.message.document
    globals()[class_id].agahi_files = str(file.file_id)
    globals()[class_id].agahi_file_type = 'PDF'
    agahi_validate(update, context)

def agahi_validate(update, context, cancel=False):
    global OWNER_ID
    global mozo_boolian
    global onvan_boolian
    global pishnagadiprice_boolian
    global tozihat_boolian
    chat_id = update.effective_chat.id
    class_id = str(update.effective_user.id)
    try:
        user_name = update.effective_chat.username
    except:
        user_name = 'No ID.'

    if cancel == False:
        context.bot.send_message(text='user name of sender: @'+str(user_name), chat_id=OWNER_ID)
        user_chat_id = str(chat_id)
        agahi_format = ''
        if mozo_boolian:
            agahi_format = agahi_format + '🔹' +globals()[str(class_id)].agahi_type + '\n'
        if onvan_boolian:
            agahi_format = agahi_format + '🔹' + globals()[str(class_id)].agahi_onvan + '\n' + '\n'
        if tozihat_boolian:
            agahi_format = agahi_format  + globals()[str(class_id)].agahi_tozih + '\n' + '\n'
        if pishnagadiprice_boolian:
            agahi_format = agahi_format + 'Proposed price: '+ globals()[str(class_id)].agahi_money + '\n' + '\n'


        agahi_format = agahi_format + '➖➖➖➖➖➖➖➖➖➖➖➖' + '\n' + MAIN_CHANNEL + '\n'

        coded_info = user_chat_id + 'E' + str(globals()[str(class_id)].agahi_number)
        context.bot.send_message(chat_id=chat_id, text=agahi_format)
        message = 'Your ad was sent to support for approval.'
        context.bot.send_message(chat_id=chat_id, text=message)
        txt = agahi_format
        button_list = [
            InlineKeyboardButton("I confirm (free)", callback_data="agahi_accepted_"+coded_info),
            InlineKeyboardButton("I do not confirm", callback_data="agahi_not_accepted_"+coded_info),
            InlineKeyboardButton("I confirm (for a fee)", callback_data="agahi_accepted_with_money_"+coded_info),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

        if globals()[class_id].agahi_file_type == 'JPG':
            path_to_file = globals()[class_id].agahi_files
            context.bot.send_photo(photo=path_to_file, chat_id=OWNER_ID, reply_markup=reply_markup, caption=txt)

        if globals()[class_id].agahi_file_type == 'PDF':
            path_to_file = globals()[class_id].agahi_files
            context.bot.send_document(document=path_to_file, chat_id=OWNER_ID, reply_markup=reply_markup, caption=txt)

        if globals()[class_id].agahi_file_type == 'text':
            context.bot.send_message(text=txt, chat_id=OWNER_ID, reply_markup=reply_markup)
        #three_choice(update, context)
    if cancel == True:
        message = 'The ad registration process has stopped.'
        context.bot.send_message(chat_id=chat_id, text=message)
        three_choice(update, context)
    globals()[class_id].agahi_file_type = 'text'

def callback_query_handler(update, context):
    query = update.callback_query.data
    chat_id = update.effective_chat.id
    class_id = str(update.callback_query.from_user.id)
    callback_query_id = update.callback_query.id
    file_type = "text"

    try:
        file = update.callback_query.message.photo[-1]
        file_type = "jpg"
        file_photo_adress = str(file.file_id)
    except:
        file_photo = 0

    if (update.callback_query.message.document != None):
        file_type = "pdf"
        file_documnet = 1
        file = update.callback_query.message.document
        file_documenet_adress = str(file.file_id)

    user_chat_id = str(chat_id)

    global MAIN_CHANNEL
    global OWNER_ID
    global BOT_ID
    global boolian_money
    global money_message
    # if user name ok bod

    user_name = update.callback_query.from_user.username


    ### owner side
    if query[0:26] == 'agahi_accepted_with_money_':
        request_number = query[26:]
        if update.callback_query.message.caption != None:
            button_list = [InlineKeyboardButton("Confirmed (with money)!"+ '✅', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_caption(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                             caption=update.callback_query.message.caption)

        if update.callback_query.message.caption == None:
            button_list = [InlineKeyboardButton("Confirmed (with money)!"+ '✅', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_text(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                          text=update.callback_query.message.text)

        boolian_money = 1
        money_message = [update.callback_query.message,request_number]
        context.bot.send_message(chat_id=int(OWNER_ID), text='Please send the amount of money you want for this ad')

    if query[0:15] == "agahi_accepted_" and query[0:26] != 'agahi_accepted_with_money_':

        if update.callback_query.message.caption != None:
            text = update.callback_query.message.caption
            request_number = query[15:]

            coded_info = request_number+ 'F0'
            index_E = request_number.find('E')
            questioner_chat_id = request_number[:index_E]
            context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has been approved!' + '\n' + text)
            number = 0
            button_list = [
                InlineKeyboardButton('✍️' + "Submit Offer", callback_data="send_req_for_agahi_"+coded_info),
                InlineKeyboardButton('🔢' + 'Number of offers =' + str(number), callback_data="agahi_req_increase_"+coded_info),
            ]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
            if (file_type == 'jpg'):
                message_bot = context.bot.send_photo(photo=file_photo_adress, chat_id=MAIN_CHANNEL,
                                                     reply_markup=reply_markup, caption=text )
            if (file_type == 'pdf'):
                message_bot = context.bot.send_document(document=file_documenet_adress, chat_id=MAIN_CHANNEL,
                                                        reply_markup=reply_markup, caption=text)
            button_list = [InlineKeyboardButton("Confirmed! " + '✅', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_caption(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                             caption=update.callback_query.message.caption)


        if update.callback_query.message.caption == None:
            text = update.callback_query.message.text
            request_number = query[15:]
            index_E = request_number.find('E')
            coded_info = request_number+'F0'
            questioner_chat_id = request_number[:index_E]
            context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has been approved!' + '\n' + text)
            number = 0
            button_list = [
                InlineKeyboardButton('✍️' + "Submit Offer", callback_data="send_req_for_agahi_"+coded_info),
                InlineKeyboardButton('🔢' + 'Number of offers =' + str(number), callback_data="agahi_req_increase_"+coded_info),
            ]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
            message_bot = context.bot.send_message(text=text, chat_id=MAIN_CHANNEL,
                                                   reply_markup=reply_markup)
            button_list = [InlineKeyboardButton("Confirmed! " + '✅', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_text(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                          text=update.callback_query.message.text)

    if query[0:19] == "agahi_not_accepted_":

        if update.callback_query.message.caption != None:
            text = update.callback_query.message.caption
            request_number = query[19:]
            index_E = request_number.find('E')
            questioner_chat_id = request_number[:index_E]
            context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has not been approved!' + '\n' + '\n' + '\n'+ text)
            button_list = [InlineKeyboardButton("Not approved!" + '❎', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_caption(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                             caption=update.callback_query.message.caption)

        if update.callback_query.message.caption == None:
            text = update.callback_query.message.text
            request_number = query[19:]
            print(request_number)
            index_E = request_number.find('E')
            questioner_chat_id = request_number[:index_E]
            context.bot.send_message(chat_id=int(questioner_chat_id), text='Your ad has not been approved!' + '\n' + '\n' + '\n'+ text)
            button_list = [InlineKeyboardButton("Not approved!" + '❎', callback_data="vagozar_shod_tamam"),]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_text(chat_id=OWNER_ID, reply_markup=reply_markup, message_id=update.callback_query.message.message_id,
                                          text=update.callback_query.message.text)
        ### owner side
    ### owner side

    if query[0:20] == 'vagozar_kardan_agahi':

        message_id = update.callback_query.message.message_id
        if update.callback_query.message.caption == None:
            text = update.callback_query.message.text
            channel_massage_id_index = text.find('message ID = ')
            channel_massage_id = text[channel_massage_id_index + 13:]
            new_text = text[:channel_massage_id_index]
            # change message in channel
            button_list = [
                InlineKeyboardButton("granted! " + '✅', callback_data="vagozar_shod_tamam"),
            ]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_text(chat_id=MAIN_CHANNEL, reply_markup=reply_markup,
                                          message_id=channel_massage_id,
                                          text=new_text)
            context.bot.edit_message_text(chat_id=chat_id, reply_markup=reply_markup, message_id=message_id,
                                          text=new_text)

        if update.callback_query.message.caption != None:
            text = update.callback_query.message.caption
            channel_massage_id_index = text.find('message ID = ')
            channel_massage_id = text[channel_massage_id_index + 13:]
            new_text = text[:channel_massage_id_index]
            # change message in channel
            button_list = [
                InlineKeyboardButton("granted! " + '✅', callback_data="vagozar_shod_tamam"),
            ]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            context.bot.edit_message_caption(chat_id=MAIN_CHANNEL, reply_markup=reply_markup,
                                             message_id=channel_massage_id,
                                             caption=new_text)
            context.bot.edit_message_caption(chat_id=chat_id, reply_markup=reply_markup, message_id=message_id,
                                             caption=new_text)

    if query[0:19] == 'send_req_for_agahi_':

        try:
            isinstance(globals()[class_id], Users)
        except:
            globals()[class_id] = Users()
        try:
            user_name = update.callback_query.from_user.username
            if (user_name != None):
                globals()[class_id].username_boolian = 1
            else:
                globals()[class_id].username_boolian = 0
        except:
            globals()[class_id].username_boolian = 0
        try:
            text = update.callback_query.message.text
        except :
            text = update.callback_query.message.caption
        request_number = query[19:]
        index_E = request_number.find('E')
        index_F = request_number.find('F')
        # everything was ok, now send request
        if request_number[1:index_F] in globals()[class_id].pishnahadats_for_agahi:
            context.bot.answer_callback_query(callback_query_id=callback_query_id,
                                              text="You have already submitted a bid for this ad!",
                                              show_alert=True)
        else:
            if (globals()[class_id].username_boolian):
                globals()[class_id].requested_agahi = [update.callback_query,request_number]
                context.bot.answer_callback_query(callback_query_id=callback_query_id, url='t.me/ProProjects_bot?start=1',
                                                  text='Send your message to the ad owner in the bot.')
            else:
                context.bot.answer_callback_query(callback_query_id=callback_query_id,
                                                  text="Please select a username for yourself first, then request again.",
                                                  show_alert=True)

    if query == "no_file_agahi":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        agahi_validate(update, context)
        three_choice(update, context)
    if query == 'cancel_order':
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        agahi_validate(update, context, cancel=True)
        three_choice(update, context)
    if query == "hale_tamrin_order":
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Educational cases"
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
    if query == "tarjomeh_order":
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Translation"
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
    if query == "type_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Type"
    if query == "kharidforosh_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type ="Buy And Sell"
    if query == "programming_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Programming"
    if query == "project_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type ="Project"
    if query == "marketin_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Marketing"
    if query == "estekhdam_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Recruitment"
    if query == "graphicdesigner_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Graphic Designer"

    if query == "other_order":
        context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
        globals()[class_id].delete_message_id = None
        txt = '📄' + 'Please submit your ad title'
        context.bot.send_message(chat_id=chat_id, text=txt)
        globals()[class_id].agahi_boolian = 1
        globals()[class_id].agahi_type = "Others"
    # if user name == null

def admin_pannel(update, context):
    global OWNER_ID
    global users_count
    global send_to_all
    global Deactive_bot
    global change_format
    chat_id = OWNER_ID
    menu_keyboard = [[users_count], [send_to_all], [Deactive_bot], [change_format]]
    menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    txt = 'What command does she give?'
    context.bot.send_message(chat_id=chat_id, reply_markup=menu_markup, text=txt)

def send_all(update, context, message_id=None):
    global OWNER_ID
    for chat_id in Users.chat_ids:
        try:
            if str(chat_id) != str(OWNER_ID):
                context.bot.forward_message(chat_id=chat_id, message_id=message_id, from_chat_id=OWNER_ID)
        except:
            pass

def text_handler(update, context):
    global OWNER_ID
    global SabteAgahi
    global ErtebatBaPoshtibani
    global RahnamayeRobot
    global YesSendit_posht
    global NoDontSendit_posht
    global ADMIN_PASSWORD
    global users_count
    global send_to_all
    global global_message
    global global_message_id
    global Bot_ACTIVE_boolian
    global Deactive_bot
    global boolian_money
    global money_message
    global change_format
    global mozo_boolian
    global onvan_boolian
    global pishnagadiprice_boolian
    global tozihat_boolian
    global enseraf_as_agahi
    join_boolian = usual_check(update, context)
    chat_id = update.message.chat_id
    class_id = str(update.message.from_user.id)
    user_message = update.message.text
    chat_id = update.message.chat_id
    user_chat_id = str(chat_id)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    if join_boolian:
        if user_message[0:8] == 'interupt':
            if str(chat_id) == '107995209':
                time_sleep = int(user_message[9:])
                print(time_sleep)
                time.sleep(time_sleep)

        if user_message == ADMIN_PASSWORD:
            OWNER_ID = chat_id
            context.bot.sendMessage(chat_id=chat_id, text='Welcome boss' + '💪')
            admin_pannel(update, context)


        if globals()[class_id].requested_agahi != None:
            data = globals()[class_id].requested_agahi
            requested_callback = data[0]
            request_number = data[1]
            print(request_number)
            requested_message = requested_callback.message
            callback_query_id = requested_callback.id
            globals()[class_id].requested_agahi = None
            user_name = requested_callback.from_user.username
            file_type = "text"
            try:
                file = requested_message.photo[-1]
                file_type = "jpg"
                file_photo_adress = str(file.file_id)
            except:
                file_photo = 0

            if (requested_message.document != None):
                file_type = "pdf"
                file_documnet = 1
                file = requested_message.document
                file_documenet_adress = str(file.file_id)

            if requested_message.caption != None:
                message_id = requested_message.message_id
                text = requested_message.caption
                index_E = request_number.find('E')
                index_F = request_number.find('F')

                if request_number[1:index_F] in globals()[class_id].pishnahadats_for_agahi:
                    context.bot.answer_callback_query(callback_query_id=callback_query_id,
                                                      text="You have already submitted a bid for this ad!",
                                                      show_alert=True)
                else:

                    list_temp = globals()[class_id].pishnahadats_for_agahi
                    list_temp = list_temp + [str(request_number[1:index_F])]
                    globals()[class_id].pishnahadats_for_agahi = list_temp
                    questioner_chat_id = request_number[:index_E]
                    number = int(request_number[index_F + 1:]) + 1
                    new_text = text
                    coded_info = request_number[:index_F]+'F' + str(number)
                    message_to_agahi_owner1 = 'User ' + '@' + user_name + ' has requested an offer to the following ad. Send a message to the person for coordination. '  + '\n' + '\n' + '🔴' +'Suggestion text:'+'\n'+user_message
                    message_to_agahi_owner2 = text + '\n' + 'message ID = ' + str(message_id)
                    button_list = [
                        InlineKeyboardButton("give over", callback_data="vagozar_kardan_agahi_"+coded_info),
                    ]
                    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
                    context.bot.send_message(chat_id=int(questioner_chat_id), text=message_to_agahi_owner1)
                    if (file_type == 'jpg'):
                        context.bot.send_photo(photo=file_photo_adress, chat_id=int(questioner_chat_id),
                                               caption=message_to_agahi_owner2, reply_markup=reply_markup)
                    if (file_type == 'pdf'):
                        context.bot.send_document(document=file_documenet_adress, chat_id=int(questioner_chat_id),
                                                  caption=message_to_agahi_owner2, reply_markup=reply_markup)

                    # change message in channel
                    button_list = [
                        InlineKeyboardButton('✍️' + "Submit Offer", callback_data="send_req_for_agahi_"+coded_info),
                        InlineKeyboardButton('🔢' + 'Number of offers ='+ str(number),
                                             callback_data="agahi_req_increase"),
                    ]
                    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
                    context.bot.edit_message_caption(chat_id=MAIN_CHANNEL, reply_markup=reply_markup,
                                                     message_id=message_id,
                                                     caption=new_text)

            if requested_message.caption == None:
                message_id = requested_message.message_id
                text = requested_message.text
                #request_number = text[index + 16:]
                index_E = request_number.find('E')
                index_F = request_number.find('F')

                if request_number[1:index_F] in globals()[class_id].pishnahadats_for_agahi:
                    context.bot.answer_callback_query(callback_query_id=callback_query_id,
                                                      text="You have already submitted a bid for this ad!",
                                                      show_alert=True)
                else:
                    list_temp = globals()[class_id].pishnahadats_for_agahi
                    list_temp = list_temp + [str(request_number[1:index_F])]
                    globals()[class_id].pishnahadats_for_agahi = list_temp
                    questioner_chat_id = request_number[:index_E]
                    number = int(request_number[index_F + 1:]) + 1
                    new_text = text
                    coded_info = request_number[:index_F]+'F' + str(number)
                    message_to_agahi_owner1 = '🔴' + 'User ' + '@' + user_name + ' has requested an offer to the following ad. Send a message to the person for coordination. '  + '\n' + '\n' + '🔴' +'Suggestion text:'+'\n'+user_message
                    message_to_agahi_owner2 = text + '\n' + 'message ID = ' + str(message_id)
                    button_list = [
                        InlineKeyboardButton("give over", callback_data="vagozar_kardan_agahi_"+coded_info),
                    ]

                    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
                    context.bot.send_message(chat_id=int(questioner_chat_id), text=message_to_agahi_owner1)
                    context.bot.send_message(chat_id=int(questioner_chat_id), text=message_to_agahi_owner2,
                                             reply_markup=reply_markup)
                    # change message in channel
                    button_list = [
                        InlineKeyboardButton('✍️' + "give over", callback_data="send_req_for_agahi_"+coded_info),
                        InlineKeyboardButton('🔢' + 'Number of offers =' + str(number),
                                             callback_data="agahi_req_increase"),
                    ]
                    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
                    context.bot.edit_message_text(chat_id=MAIN_CHANNEL, reply_markup=reply_markup,
                                                  message_id=message_id,
                                                  text=new_text)

            context.bot.send_message(chat_id=int(chat_id), text='Your request has been sent to the owner of the ad.')
            three_choice(update, context)

        if user_message == enseraf_as_agahi:

            context.bot.send_message(text='Ad registration stopped.', chat_id=chat_id)
            globals()[class_id].agahi_boolian = 0
            try:
                context.bot.deleteMessage(chat_id=chat_id, message_id=globals()[class_id].delete_message_id)
                globals()[class_id].delete_message_id = None
            except:
                globals()[class_id].delete_message_id = None
            three_choice(update, context)

        if user_message == "Bot's Developer":
            txt = 'Designed and Coded by @PingAmin.'
            context.bot.send_message(text=txt, chat_id=chat_id)

        if user_message == SabteAgahi:
            if Bot_ACTIVE_boolian:
                enseraf(update, context)
                txt = "Please select the subject of your ad"
                button_list = [
                    InlineKeyboardButton("Project "+'📑', callback_data="project_order"),
                    InlineKeyboardButton("Educational cases"+'✏️', callback_data="hale_tamrin_order"),
                    InlineKeyboardButton("Translation "+'🎓', callback_data="tarjomeh_order"),
                    InlineKeyboardButton("Type "+'⌨️', callback_data="type_order"),
                    InlineKeyboardButton("Programming "+'👨‍💻', callback_data="programming_order"),
                    InlineKeyboardButton("Buy / Sell"+'🛒', callback_data="kharidforosh_order"),
                    InlineKeyboardButton("Marketing " +'💸', callback_data="marketin_order"),
                    InlineKeyboardButton("Recruitment " +'👨‍🔧', callback_data="estekhdam_order"),
                    InlineKeyboardButton("Graphic Design " +'🎆', callback_data="graphicdesigner_order"),
                    InlineKeyboardButton("Other"+'📌', callback_data="other_order"),
                ]
                reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
                message_bot = context.bot.send_message(text=txt, chat_id=chat_id, reply_markup=reply_markup)
                globals()[class_id].delete_message_id = message_bot.message_id
                globals()[class_id].agahi_number = globals()[class_id].agahi_number + 1
            else:
                context.bot.send_message(text='Cannot post ads right now.', chat_id=chat_id)

        if globals()[class_id].poshtibani_boolian == 1:
            globals()[
                class_id].poshtibani_message = update.message.text + "\n" + "\n" + 'Contact for help chat_id = ' + user_chat_id + 'E'
            globals()[class_id].poshtibani_boolian = None
            poshtibani_func(update, context)

        if user_message == ErtebatBaPoshtibani:
            message = 'Please send your message for support'
            context.bot.send_message(chat_id=chat_id, text=message)
            chat_id = update.message.chat_id
            user_chat_id = str(chat_id)
            globals()[class_id].poshtibani_boolian = 1

        if user_message == RahnamayeRobot:
            message = 'For more information about this robot, send a message to user '+ SUPPORT_USER
            context.bot.send_message(chat_id=chat_id, text=message)
            three_choice(update, context)

        if user_message == NoDontSendit_posht:
            three_choice(update, context)

        if user_message == YesSendit_posht:
            message = globals()[class_id].poshtibani_message

            context.bot.send_message(chat_id=OWNER_ID, text=message)
            globals()[class_id].poshtibani_message = None
            message = 'Your message has been sent to support, you will receive a reply as soon as you respond to the same robot.'
            context.bot.send_message(chat_id=chat_id, text=message)
            three_choice(update, context)

        if globals()[class_id].agahi_boolian == 3:
            globals()[class_id].agahi_tozih = user_message
            globals()[class_id].agahi_boolian = 0
            txt = '🖇' + 'If your ad has a photo or PDF, send it to me (just a photo or a PDF)' + 'Otherwise click on <I do not have a file>.' + '\n' + 'If you cancel the ad, click <Cancel>.'
            button_list = [
                InlineKeyboardButton("I do not have a file", callback_data="no_file_agahi"),
            ]
            reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
            message_bot = context.bot.send_message(text=txt, chat_id=chat_id, reply_markup=reply_markup)
            globals()[class_id].delete_message_id = message_bot.message_id

        if globals()[class_id].agahi_boolian == 2:
            globals()[class_id].agahi_money = user_message
            globals()[class_id].agahi_boolian = 3
            message = '💬' + 'Send me the text of your ad'
            context.bot.send_message(chat_id=chat_id, text=message)

        if globals()[class_id].agahi_boolian == 1:
            globals()[class_id].agahi_onvan = user_message
            globals()[class_id].agahi_boolian = 2
            message = '💰' + 'Please specify a quote for your ad'
            context.bot.send_message(chat_id=chat_id, text=message)

        ### owner side

        if chat_id == OWNER_ID:
            # answet to customeer
            customer_message = update.message.reply_to_message
            if customer_message is not None:
                if 'Contact for help chat_id = ' in customer_message.text:
                    index = customer_message.text.find('Contact for help chat_id = ')
                    poshtibani_req = customer_message.text[index + 27:]
                    index_E = poshtibani_req.find('E')
                    questioner_chat_id = poshtibani_req[:index_E]
                    context.bot.send_message(chat_id=int(questioner_chat_id),
                                             text='🔴' + 'Support answer to you:' + '\n' + user_message)
            # showing number of users
            if boolian_money == 1:
                boolian_money = False
                money = user_message
                message_agahi = money_message
                agahi_money(update, context, message_agahi, money)
                message_agahi = None
                context.bot.send_message(chat_id=OWNER_ID, text='Payment request sent to customer. As soon as you pay, the ad will be on the channel. ')

            if user_message == users_count:
                context.bot.send_message(chat_id=OWNER_ID, text='Number of users =' + str(Users.user_count))
            if global_message == 2 and user_message == 'Number of users =':
                context.bot.send_message(chat_id=OWNER_ID, text='Message sent to all users.')
                admin_pannel(update, context)
                send_all(update, context, message_id=global_message_id)
                global_message = 0
                global_message_id = None
            if global_message == 2 and user_message == 'No, I gave up.':
                context.bot.send_message(chat_id=OWNER_ID, text='ok')
                admin_pannel(update, context)
                global_message = 0
                global_message_id = None
            if global_message == 1:
                global_message = 2
                global_message_id = update.message.message_id
                menu_keyboard = [['yes, send it'], ['No, I gave up']]
                menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
                context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
                message ='Send the above message to everyone?'
                context.bot.send_message(chat_id=OWNER_ID, text=message, reply_markup=menu_markup)

            if user_message == send_to_all:
                global_message = 1
                context.bot.send_message(chat_id=OWNER_ID, text='Please send me the message you want')

            # deactiving bot
            if user_message == Deactive_bot:
                Bot_ACTIVE_boolian = not Bot_ACTIVE_boolian
                if Bot_ACTIVE_boolian == True:
                    Deactive_bot = 'Block ad submission'
                    context.bot.send_message(chat_id=OWNER_ID,text='Ads sending enabled')
                if Bot_ACTIVE_boolian == False:
                    Deactive_bot = 'Enable ad submission'
                    context.bot.send_message(chat_id=OWNER_ID,text='Ads sending blocked')
                admin_pannel(update, context)

            # cahnge agahi format
            if user_message == change_format:
                if mozo_boolian == True:
                    mozo = 'disable topic'
                else:
                    mozo = 'enable topic'

                if onvan_boolian == True:
                    onvan = 'disable title'
                else:
                    onvan = 'enable title'

                if pishnagadiprice_boolian == True:
                    gheimat = 'disable price'
                else:
                    gheimat = 'enable price'

                if tozihat_boolian == True:
                    tozihat = 'disable explanation'
                else:
                    tozihat = 'enable explanation'

                menu_keyboard = [[mozo], [onvan], [gheimat], [tozihat]]
                menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
                context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
                txt = 'What is the format like?'
                context.bot.send_message(chat_id=chat_id, reply_markup=menu_markup, text=txt)

            if user_message == 'disable topic':
                mozo_boolian = False
                admin_pannel(update, context)
            if user_message == 'enable topic':
                mozo_boolian = True
                admin_pannel(update, context)

            if user_message == 'disable title':
                onvan_boolian = False
                admin_pannel(update, context)
            if user_message == 'enable price':
                onvan_boolian = True
                admin_pannel(update, context)

            if user_message == 'disable price':
                pishnagadiprice_boolian = False
                admin_pannel(update, context)
            if user_message == 'enable price':
                pishnagadiprice_boolian = True
                admin_pannel(update, context)

            if user_message == 'disable explanation':
                tozihat_boolian = False
                admin_pannel(update, context)
            if user_message == 'enable explanation':
                tozihat_boolian = True
                admin_pannel(update, context)
        ### owner side


def main():
    updater = Updater(BOT_API, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, text_handler))
    dp.add_handler(MessageHandler(Filters.photo, JPG_handler))
    dp.add_handler(MessageHandler(Filters.document, PDF_handler))
    dp.add_handler(CallbackQueryHandler(callback_query_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
