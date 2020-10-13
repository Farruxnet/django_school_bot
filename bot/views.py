from django.shortcuts import render
import telebot
from telebot import types
from django.conf import settings
from django.http.response import HttpResponse
from . models import Teacher, Category, About
from botconfig.models import SiteConf
# 1329029511:AAEg6VIV5Ik0m-SPpOI8XgG36RnOi4WxFkw
bot = telebot.TeleBot(settings.BOT_TOKEN)

############################################################################

# def web_hook_view(request):

#     if request.method == 'POST':

#         bot.process_new_updates([telebot.types.Update.de_json(request.body.decode("utf-8"))])
#         bot.set_webhook(url="https://schoolonlineuz.pythonanywhere.com")
#         return HttpResponse(status=200)
#     return HttpResponse('<a href="https://farruxnet.uz">Farruxnet.uz</a>')

def web_hook_view(request):
    if request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode("utf-8"))])
        return HttpResponse(status=200)
    return HttpResponse('404 not found')


############################################################################

@bot.message_handler(regexp='🔙 Orqaga')
def back_bot(message):
    start_message(message)

############################################################################

@bot.message_handler(commands=['start'])
def start_message(message):
    if SiteConf.objects.all().order_by('-id')[:1]:
        starttext = SiteConf.objects.all().order_by('-id')[:1]
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        button = ['🏫 Maktab haqida', '👨‍🏫 O\'qituvchilar', '📕 Kurslar', '📕 Kurslar haqida', '❕ Qoidalar', '☎️ Aloqa',]
        home_keyboard.add(*button)
        for txt in starttext:
            bot.send_message(message.chat.id, txt.starttext, reply_markup=home_keyboard, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Assalomu alaykum!\nBotimiz to\'liq ishga tushgani yo\'q!')
############################################################################
        
@bot.message_handler(regexp='📕 Kurslar haqida')
def about_course(message):
    home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    button = ['🔙 Orqaga']
    home_keyboard.add(*button)
    about = About.objects.all()
    if about:
        bot.send_message(message.chat.id, 'Kurslar haqida:', reply_markup=home_keyboard) 
        for i in about:
            bot.send_message(message.chat.id, f'<a href="{settings.SITE_URL}{i.img.url}"><b><i>{i.name} kursi haqida</i></b></a>\n{i.text}', parse_mode="HTML", disable_web_page_preview=False)
    else:
        bot.send_message(message.chat.id, 'Malumot yoq', reply_markup=home_keyboard) 

############################################################################
   
@bot.message_handler(regexp='🏫 Maktab haqida')
def school_about(message):
    starttext = SiteConf.objects.all().order_by('-id')[:1]
    home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    button = ['🔙 Orqaga']
    home_keyboard.add(*button)
    for txt in starttext:
        bot.send_message(message.chat.id, txt.aboutschool, reply_markup=home_keyboard)
        
############################################################################

@bot.message_handler(regexp='☎️ Aloqa')
def contact(message):
    contact_text = SiteConf.objects.all().order_by('-id')[:1]
    home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    button = ['🔙 Orqaga']
    home_keyboard.add(*button)
    for txt in contact_text:
        bot.send_message(message.chat.id, f'<b>Biz bilan bog\'lanish</b>\n\nE-mail: {txt.email}\nTel: {txt.tel}\nManzil: {txt.address}', parse_mode='HTML', reply_markup=home_keyboard)

############################################################################

@bot.message_handler(regexp='📕 Kurslar')
def school_fan(message):
    def get_fan(msg):
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        button = ['🔙 Orqaga']
        home_keyboard.add(*button)

        if msg.text == '🔙 Orqaga':
            start_message(message)
        elif About.objects.filter(name__name=msg.text):
            bot.send_message(message.chat.id, f'Kurs: {msg.text}', reply_markup=home_keyboard)
            get_about_fan = About.objects.filter(name__name=msg.text)
            for i in get_about_fan:
                bot.send_message(message.chat.id, f'<a href="{settings.SITE_URL}{i.img.url}"><b><i>{i.name} kursi haqida</i></b></a>\n{i.text}', parse_mode="HTML", disable_web_page_preview=False)
        else:
            bot.send_message(message.chat.id, 'Ma\'lumot topilmadi!', reply_markup=home_keyboard)

    starttext = Category.objects.all()
    if starttext:
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        button = []
        for but in starttext:
            button.append(but.name)
        home_keyboard.add(*button)
        home_keyboard.row('🔙 Orqaga')
        bot.send_message(message.chat.id, "Kurslar:", reply_markup=home_keyboard)
        bot.register_next_step_handler(message, get_fan)
    else:
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        home_keyboard.row('🔙 Orqaga')
        bot.send_message(message.chat.id, "Kurslar topilmadi", reply_markup=home_keyboard)
############################################################################

@bot.message_handler(regexp='❕ Qoidalar')
def qoidalar(message):
    qoida = SiteConf.objects.all().order_by('-id')[:1]
    
    back_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    back_btn.row('🔙 Orqaga')
    for i in qoida:
        bot.send_message(message.chat.id, f'<b>Qoidalar</b>\n\n{i.qoida}', parse_mode='HTML', reply_markup=back_btn)
 
############################################################################

@bot.message_handler(regexp='👨‍🏫 O\'qituvchilar')
def school_about(message):
    if Teacher.objects.all():
        teacher_obj = Teacher.objects.all()
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        button = ['🔙 Orqaga']
        home_keyboard.add(*button)
        text = ''
        bot.send_message(message.chat.id, 'O\'qituvchilar:', reply_markup=home_keyboard)
        for txt in teacher_obj:
            orde_teacher_button = types.InlineKeyboardMarkup(row_width=1)
            orde_teacher_button.add(types.InlineKeyboardButton(text='🖌 O\'qituvchiga yozilish', callback_data=txt.id))
            text = f'Ismi: {txt.name} \nKurs: {txt.category}\nO\'qituvchi haqida: {txt.about}'
            bot.send_photo(message.chat.id, txt.img, caption=text, reply_markup=orde_teacher_button)
        
        @bot.callback_query_handler(func=lambda call:True)
        def call_teacher_add(call):
            send_teacher = Teacher.objects.filter(id=call.data)
            def send_teacher_func(message):
                if message.text == '🔙 Orqaga':
                    start_message(message)
                else:
                    for i in send_teacher:
                        te = f'Yangi o\'quvchi:\n\n#O\'qituvchi: {i.name}\n#Kurs: {i.category}\n\nO\'quvchi haqida: {message.text}'
                        bot.send_message(settings.GROUP_ID, te)
                        bot.send_message(message.chat.id, 'Ma\'muryatga yuborildi! Tez orada siz bilan bog\'lanamiz!😊')
            for i in send_teacher:
                bot.send_message(call.message.chat.id, f'O\'qituvchi: {i.name}\nKurs: {i.category}\nDarsga yozilish uchun to\'liq ismingiz va telefon raqamingizni yozing:')
                bot.register_next_step_handler(call.message, send_teacher_func)
    else:
        home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        button = ['🔙 Orqaga']
        home_keyboard.add(*button)
        bot.send_message(message.chat.id, 'O\'qituvchilar topilmadi!', reply_markup=home_keyboard)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     if TgUser.objects.filter(user_id=message.chat.id).exists():
#         starttext = SiteConf.objects.all().order_by('-id')[:1]
#         home_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
#         button = ['🏫 Maktab haqida', '👨‍🏫 O\'qituvchilar', '📕 Kurslar', '📕 Kurslar haqida', '❕ Qoidalar', '☎️ Aloqa',]
#         home_keyboard.add(*button)
#         for txt in starttext:
#             bot.send_message(message.chat.id, txt.starttext, reply_markup=home_keyboard)
#     else:
#         def get_name(message):
#             try:
#                 global getname
#                 getname = message.text
#                 button_tel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#                 button_tel.add(types.KeyboardButton('📞 Telefon raqamni yuborish', request_contact=True))
#                 text = 'Telefon raqamingizni yuboring'
#                 bot.send_message(message.chat.id, text, reply_markup=button_tel)
#                 bot.register_next_step_handler(message, get_tel)
#             except:
#                 bot.send_message(message.chat.id, "Xato! ism qabul qilishda")

#         def get_tel(message):
#             try:
#                 global tel
#                 tel = message.contact.phone_number
#                 try:
#                     TgUser.objects.create(user_id=message.chat.id, name=getname, tel=tel)
#                     start_message(message)
#                 except:
#                     pass
#             except:
#                 bot.send_message(message.chat.id, "Xato! telefon qabul qilishda")

#         text = 'Assalomu alaykum!\n'
#         text += 'Bot imkoniyatlaridan foydalanish uchun ro\'yxatdan o\'ting\nIsmingizni kiriting:'
#         bot.send_message(message.chat.id, text)
#         bot.register_next_step_handler(message, get_name)
