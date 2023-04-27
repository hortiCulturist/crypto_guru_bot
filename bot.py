import asyncio

import aiogram
from aiogram import Bot
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile, InputMedia, InputMediaPhoto
from aiogram.utils import executor

import button
import config
import db

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    print('Bot is running')
    db.start_db()


class MassSend(StatesGroup):
    sendd1 = State()
    sendd2 = State()


class saveMessage(StatesGroup):
    sv_mess1 = State()
    sv_mess2 = State()
    sv_mess3 = State()


class updateFeedback(StatesGroup):
    updateFeedback1 = State()
    updateFeedback2 = State()


class editPattern(StatesGroup):
    editPattern1 = State()
    editPattern2 = State()


class deletePattern(StatesGroup):
    deletePattern1 = State()


@dp.message_handler(commands='start', user_id=config.ADMIN_ID)
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text="Добро пожаловать!", reply_markup=button.admin_menu())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text="Добро пожаловать!", reply_markup=button.user_menu())


@dp.message_handler(text='📝Меню отзывов', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    db.first_add_post()
    await bot.send_message(chat_id=message.chat.id, text=f'Меню отзывов', reply_markup=button.pattern_button())


@dp.message_handler(text='📧Менеджер рассылки', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Меню отзывов', reply_markup=button.send_manager_button())


@dp.message_handler(text='Назад', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Главное меню', reply_markup=button.admin_menu())


@dp.chat_join_request_handler()
async def chat_join_request_handler(chat_join_request: types.ChatJoinRequest):
    chat_member = await bot.get_chat_member(chat_join_request.chat.id, chat_join_request.from_user.id)
    user_id = chat_join_request.user_chat_id
    chat_id = chat_join_request.chat.id
    await chat_join_request.approve()
    db.add_user(user_id, chat_id)
    print(f'user_id - {user_id}')
    print(f'chat_id - {chat_id}')
    photo = InputFile("photo/photo_1.jpeg")
    await bot.send_photo(chat_id=user_id, photo=photo, caption=f'Hey! I am Alex - a crypto trader and author of the <a href="https://t.me/+y0mM3yr9A59iMWFk">Crypto Guru channel</a>. \n'
                                                               f'Here you can find all information about Crypto Guru VIP signals and contact our manager!\n\n'
                                                               f'🔥<b>Ready to start inceasing your deposit up to 12 times every month?</b>🔥', parse_mode='html',
                         reply_markup=button.im_ready())
    # await bot.copy_message(chat_id=chat_join_request.from_user.id, from_chat_id=data[0][0], message_id=data[0][1], reply_markup=button.im_ready())


@dp.message_handler(text="🤑Yes, I'm ready!")
async def welcome_post(message: types.Message):
    photo = InputFile("photo/photo_2.jpeg")
    await bot.send_message(chat_id=message.chat.id, text="Just over a <u>year ago I deposited $20,000</u> into my first crypto account.\n"
                                                         "<u>As of today It's now worth 1.7 million dollars.</u>\n\n"
                                                         "🤔This wasn't just some string of luck. If you don't know who I am - I was a professional day trader in the stock market for 17 years.\n\n", parse_mode="html")
    with open('voice/voice.ogg', 'rb') as voice:
        await bot.send_voice(message.from_user.id, voice)
    await bot.send_message(chat_id=message.chat.id, text="✔<b>I took all those skills that I learned and transferred them into my telegram group.</b>", parse_mode="html")
    await asyncio.sleep(2)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="💯<b>You can do the same</b> if you follow me and use my knowledge.\n"
                                                                       "Ready to start this journey together?🤝", parse_mode='html', reply_markup=button.make_money())


@dp.message_handler(text="👌Let's make some money!💲")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Fine! Now stay tuned and check updates on my channel. Don't miss your chance when I give <b>free signals</b> and you can <b>earn good profit!</b>\n\n"
                                                         "🔐https://t.me/+y0mM3yr9A59iMWFk\n\n"
                                                         "⚠️To start earnings 10-12x, you need to get a VIP signals subscription.\n"
                                                         "Click on the '💲Prices' button to choose the right offer and get additional info", parse_mode='html', reply_markup=button.user_menu())


@dp.message_handler(text="🚨What will I get with VIP")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="<b>What’s included for VIP subscription?</b>\n\n"
                                                         "👉VIP Signals subscription contains daily market updates of information that allow you to achieve a multiple increase in the profitability of your futures orders.\n"
                                                         "❗️ Namely:\n\n"
                                                         "1️⃣<b>Up to 8 VIP signals!</b>\nAbout 50 coins on analytics in a day, it comes 4-8 high quality VIP signals per day\n\n"
                                                         "2️⃣<b>More than 1000% profit from just one \n💎GEM signal</b>!\nAbout half of the VIP signals at a distance of 1-2 weeks can give more than 1000% profit\n\n"
                                                         "3️⃣<b>Accurate and low risky signals</b>!\nI give out Entry points / Profit targets / Stop Losses - this allows you not to worry about the analysis, you just need to open and close a deal\n\n"
                                                         "4️⃣<b>Ahead the market</b>\nYou can stay ahead of the market and receive VIP signals earlier than all other players - this is a strong advantage\n\n"
                                                         "5️⃣<b>Reliable strategy!</b>\nYou will work on my successful trading strategy that gives results! Some clients have already earned over $30,000 with me\n\n"
                                                         "6️⃣<b>Taining for beginners</b>\nBasic instructions and materials for beginners. Valuable knowledge and experience. We bring success to every client!\n\n"
                                                         "7️⃣<b>Personal support</b>\nHigh quality support 24/7 - no user will be left without help\n\n"
                                                         "🔥This is all you need so that you can start <b>increasing your funds up to 7-10 times</b> by simply copying orders and following my analytics.🔥\n\n"
                                                         "💳❗️<i>Message me to make a payment and get VIP access</i> <a href='https://t.me/alex_graysvip'>Alex Grayson</a>", parse_mode='html')


@dp.message_handler(text="💲Prices")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="<b>Subscription prices for Crypto Guru VIP-Signals Community</b>\n\n"
                                                         "🔐VIP-subscription <u>1 month\n<b>290$</b> (<i>Start earnings on futures</i>)</u>\n\n"
                                                         "🔐VIP-subscription <u>1 year\n<b>690$</b> (<i>Profitable</i>)</u>\n\n"
                                                         "🔐👑<b><u>Lifetime</u></b>👑 VIP-subscription\n<u><b>1190$</b>  - (<i>Best offer</i>)</u>\n\n"
                                                         "*<i>Payment method USDT TRC20</i>\n\n"
                                                         "💳❗️Message me to make a payment and get VIP access\n"
                                                         "<a href='https://t.me/alex_graysvip'>Alex Grayson</a>", parse_mode='html')


@dp.message_handler(text="💳Payment details")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="TVB83t7QGxKqjfMZbNP4cS7QAciYCPnf6y")
    await bot.send_message(chat_id=message.chat.id, text="☝️☝️☝️"
                                                         "<b>USDT TRC20 Address</b>\n\n"
                                                         "You can pay directly through BINANCE App\n"
                                                         "<i>Message me if there are any problems</i> <a href='https://t.me/alex_graysvip'>Alex Grayson</a>👨‍💻", parse_mode='html')


@dp.message_handler(text="❓How does it work?")
async def welcome_post(message: types.Message):
    photo1_path = "photo/photo_3.jpeg"
    photo2_path = "photo/photo_4.jpeg"
    photo1 = InputMediaPhoto(media=open(photo1_path, "rb"))
    photo2 = InputMediaPhoto(media=open(photo2_path, "rb"))
    await bot.send_media_group(chat_id=message.chat.id, media=[photo1, photo2])
    await bot.send_message(chat_id=message.chat.id, text="<b>How does it work?</b>\n\n"
                                                         "It works by subscription. You pay for the period and get access to the VIP channel for this time.\n\n"
                                                         "👑<b>VIP members</b> receive accurate signals, about 4-8 per day. Entry and exit zones, as well as targets notifications (look at the photos). Using these signals, you must open orders on your exchange (for example, Binance, Bybit)\n\n"
                                                         "👉🏻Following these recommendations, you will easily get your first profit! VIP also includes an acquaintance and support, teaching basic instructions and tutorials\n\n"
                                                         "💎<b>All of this will give you the opportunity to increase your deposit by 10-12 times in a first month!</b>\n\n"
                                                         "✅<b>Create your additional income with Crypto Guru VIP signals!</b>\n\n\n\n"
                                                         "💳<i>Payment for VIP access:</i>  <a href='https://t.me/alex_graysvip'>Alex Grayson</a> 👨‍💻", parse_mode='html')


@dp.message_handler(text="📊VIP signal statistics")
async def welcome_post(message: types.Message):
    photo1_path = "photo/photo_5.jpeg"
    photo2_path = "photo/photo_6.jpeg"
    photo1 = InputMediaPhoto(media=open(photo1_path, "rb"))
    photo2 = InputMediaPhoto(media=open(photo2_path, "rb"))
    await bot.send_media_group(chat_id=message.chat.id, media=[photo1, photo2])
    await bot.send_message(chat_id=message.chat.id, text="🔍Check my VIP signal statistics for last month - it's a great result that has led my VIP clients to success. <b>Join VIP Community to get the same result already in the first week!</b>\n\n"
                                                         "💳💳❗️<i>Message me to make a payment and get VIP access</i>  <a href='https://t.me/alex_graysvip'>Alex Grayson</a> 👨‍💻",
                           parse_mode='html')


@dp.message_handler(text="🥇Feedbacks")
async def welcome_post(message: types.Message):
    db.add_feedback(message.from_user.id)
    feed_list = db.get_all_post()
    print(feed_list)
    x = db.edit_feedback(message.from_user.id)[0]
    print(x)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id=feed_list[x][1],
                           message_id=feed_list[x][2],
                           reply_markup=button.review())


@dp.callback_query_handler(text="onmrcnt")
async def welcome_post(call: types.CallbackQuery):
    feed_list = db.get_all_post()
    print(feed_list)
    x = db.edit_feedback(call.from_user.id)[0]
    print(x)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=feed_list[x][1],
                           message_id=feed_list[x][2],
                           reply_markup=button.review())


@dp.message_handler(text="👨‍💻Support")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="📍24/7 support is only available for our VIP members. "
                                                         "Our experts will help you achieve trading success, we will be glad to meet you in our VIP Community. "
                                                         "👉Message me to pay for 👑VIP access <a href='https://t.me/alex_graysvip'>Alex Grayson</a>", parse_mode='html')


@dp.message_handler(text="↪️ Channel link")
async def welcome_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Invite for friends 👉🏻 https://t.me/+y0mM3yr9A59iMWFk")


@dp.message_handler(text='🔄Обновить отзыв', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Пришлите название нужного шаблона: \n'
                                                         f'(Все шаблоны ниже)')
    for posts in db.get_all_post():
        await bot.send_message(chat_id=message.chat.id, text=posts[0])
    await updateFeedback.updateFeedback1.set()


@dp.message_handler(state=updateFeedback.updateFeedback1)
async def save_sample_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await updateFeedback.next()
    await bot.send_message(message.chat.id, text='Пришлите пост:')


@dp.message_handler(state=updateFeedback.updateFeedback2, content_types=aiogram.types.ContentType.ANY)
async def save_sample(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        title = data.get('title')
    db.add_post(title, message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, text=f'Вы успешно добавили шаблон поста под названием "{title}"',
                           reply_markup=button.admin_menu())
    await state.finish()


@dp.message_handler(text='✍️Изменить название шаблона отзыва', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Пришлите название шаблона: ')
    await editPattern.editPattern1.set()


@dp.message_handler(state=editPattern.editPattern1)
async def save_sample_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['old_title'] = message.text
    await editPattern.next()
    await bot.send_message(message.chat.id, text='Введите новое название:')


@dp.message_handler(state=editPattern.editPattern2)
async def save_sample(message: types.Message, state: FSMContext):
    new_title = message.text
    async with state.proxy() as data:
        old_title = data.get('old_title')
    if db.update_posts_by_name(old_title, new_title):
        await bot.send_message(message.chat.id,
                               text=f'✅Вы успешно изменили имя шаблона "{old_title}" на "{new_title}"',
                               reply_markup=button.admin_menu())
        await state.finish()
    else:
        await bot.send_message(message.chat.id, text=f'❌Не удалось обновить имя шаблона, \n'
                                                     f'возможно при вводе была допущена ошибка!',
                               reply_markup=button.admin_menu())
        await state.finish()


@dp.message_handler(text='🔍Просмотр всех отзывов', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    for posts in db.get_all_post():
        await bot.send_message(message.chat.id, text=f'Название: {posts[0]} 👇')
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=posts[1], message_id=posts[2])



@dp.message_handler(text='✅Добавить шаблон рассылки', user_id=config.ADMIN_ID)
async def create_post(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Пришлите название шаблона: ')
    await saveMessage.sv_mess1.set()


@dp.message_handler(state=saveMessage.sv_mess1)
async def save_sample_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await saveMessage.next()
    await bot.send_message(message.chat.id, text='Пришлите пост:')


@dp.message_handler(state=saveMessage.sv_mess2, content_types=aiogram.types.ContentType.ANY)
async def save_sample(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        title = data.get('title')
    db.add_message(title, message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, text=f'Вы успешно добавили шаблон поста под названием "{title}"',
                           reply_markup=button.admin_menu())
    await state.finish()


@dp.message_handler(text='🗑Удалить шаблон рассылки', user_id=config.ADMIN_ID)
async def delete_pattern(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Пришлите название шаблона: ')
    for i in db.get_all_pattern():
        print(i)
        await bot.send_message(chat_id=message.chat.id, text=f"Имя шаблона: {i[1]}")
    await deletePattern.deletePattern1.set()


@dp.message_handler(state=deletePattern.deletePattern1)
async def save_sample(message: types.Message, state: FSMContext):
    pattern_name = message.text
    if db.delete_pattern(pattern_name):
        await bot.send_message(message.chat.id, text=f'✅Вы успешно удалили шаблон поста под названием "{pattern_name}"',
                               reply_markup=button.admin_menu())
        await state.finish()
    else:
        await bot.send_message(message.chat.id, text=f'❌Не удалось удалить шаблон под названием "{pattern_name}"\n'
                                                     f'Проверьте правильность ввода',
                               reply_markup=button.admin_menu())
        await state.finish()


@dp.message_handler(text='📨Рассылка', state=None, user_id=config.ADMIN_ID)
async def send_out(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f"Введите ID шаблона для отправки:")
    if db.get_message():
        for i in db.get_message():
            await bot.send_message(message.chat.id, text=f'ID: {i[0]}\n'
                                                         f'Имя шаблона: {i[1]}')
        await MassSend.sendd1.set()
    else:
        await state.finish()
        await bot.send_message(message.chat.id, text='❌Вы не добавили ни одного шаблона')


@dp.message_handler(state=MassSend.sendd1)
async def send(message: types.Message, state: FSMContext):
    sample_id = message.text
    chan_id = message.from_user.id
    await state.finish()
    if sample_id.isdigit():
        data = db.template_selection(int(sample_id))
        print(data)
        if data:
            good, bad = 0, 0
            await state.finish()
            errors_list = []
            for i in db.all_user():
                print(i)
                try:
                    await bot.copy_message(chat_id=i[1], from_chat_id=message.chat.id, message_id=data[0][3],
                                           reply_markup=button.admin_menu())
                    good += 1
                except Exception as e:
                    bad += 1
                    errors_list.append(e)
            await bot.send_message(message.from_user.id, 'Рассылка завершена успешно\n'
                                                         f'Доставлено: {good}\n'
                                                         f'Не доставлено: {bad}\n'
                                                         f'Ошибки {set(errors_list)}',
                                   reply_markup=button.admin_menu())
        else:
            await bot.send_message(message.chat.id, text='❌Шаблон указан не верно, рассылка невозможна',
                                   reply_markup=button.admin_menu())  # menu button
    else:
        await bot.send_message(message.chat.id, text='❌Вы ввели не цифру!', reply_markup=button.admin_menu())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
