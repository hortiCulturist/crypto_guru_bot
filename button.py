from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def im_ready():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton("🤑Yes, I'm ready!"))
    return m


def make_money():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton("👌Let's make some money!💲"))
    return m


def user_menu():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton('🚨What will I get with VIP'))
    m.add(KeyboardButton('💲Prices'))
    m.insert(KeyboardButton('💳Payment details'))
    m.add(KeyboardButton('❓How does it work?'))
    m.add(KeyboardButton('📊VIP signal statistics'))
    m.insert(KeyboardButton('🥇Feedbacks'))
    m.add(KeyboardButton('👨‍💻Support'))
    m.insert(KeyboardButton('↪️ Channel link'))
    return m


def admin_menu():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.insert(KeyboardButton('📝Меню отзывов'))
    m.add(KeyboardButton('📧Менеджер рассылки'))
    return m


def pattern_button():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton('🔄Обновить отзыв'))
    m.add(KeyboardButton('✍️Изменить название шаблона отзыва'))
    m.insert(KeyboardButton('🔍Просмотр всех отзывов'))
    m.add(KeyboardButton('Назад'))
    return m


def send_manager_button():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton('✅Добавить шаблон рассылки'))
    m.insert(KeyboardButton('🗑Удалить шаблон рассылки'))
    m.add(KeyboardButton('📨Рассылка'))
    m.add(KeyboardButton('Назад'))
    return m


def review():
    m = InlineKeyboardMarkup(resize_keyboard=True)
    m.insert(InlineKeyboardButton('One more comment👍', callback_data='onmrcnt'))
    return m