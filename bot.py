import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

API_TOKEN = '8922281842:AAEPl9hN4GaIRhPiHODyVZd5fbreOkn4yag'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def main_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🏢 О студии'), KeyboardButton(text='🎮 Об игре')],
            [KeyboardButton(text='📥 Скачать игру'), KeyboardButton(text='📞 Контакты')],
            [KeyboardButton(text='❓ FAQ'), KeyboardButton(text='🔄 Главное меню')]
        ],
        resize_keyboard=True
    )
    return kb

def back_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='◀️ Назад в меню', callback_data='main_menu')]]
    )

def download_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚀 Перейти в канал', url='https://t.me/stayaliivve')],
            [InlineKeyboardButton(text='📁 Скачать с Google Диск', url='https://drive.google.com/file/d/1alghy0OElRUf0ZxgVnR1eDUmZM6mSNCW/view?usp=drive_link')],
            [InlineKeyboardButton(text='◀️ Назад в меню', callback_data='main_menu')]
        ]
    )

def contacts_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🌐 Сайт', url='https://ironbrak.samp.date')],
            [InlineKeyboardButton(text='📢 Канал студии', url='https://t.me/Ironbrakst')],
            [InlineKeyboardButton(text='🎮 Канал игры', url='https://t.me/stayaliivve')],
            [InlineKeyboardButton(text='📧 Написать нам', url='mailto:ironbrakentertainment@gmail.com')],
            [InlineKeyboardButton(text='◀️ Назад в меню', callback_data='main_menu')]
        ]
    )

WELCOME = """
<b>👋 Добро пожаловать в официального бота игровой студии <i>Iron Brak</i>!</b>

Мы — молодая команда, создающая атмосферные игры с душой. Здесь вы найдёте всё о нас, нашей игре и сможете связаться с нами.

<b>🔹 Что умеет бот:</b>
• Расскажет о студии и игре
• Покажет, где скачать наш проект
• Даст ответы на частые вопросы
• Предоставит контакты для связи

Выберите нужный раздел в меню ниже ⬇️
"""

ABOUT_STUDIO = """
<b>🏢 Iron Brak Studio</b>

Основана в <b>2025 году</b> небольшой командой энтузиастов, которых объединяет страсть к созданию запоминающихся игровых миров.

<b>🔹 Наша философия:</b>
• Мы не гонимся за трендами — мы ищем свой уникальный голос
• Каждая деталь важна, от сценария до звукового сопровождения
• Мы верим, что игра может быть искусством

<b>🔹 Текущий статус:</b>
Сейчас мы взяли паузу, чтобы переосмыслить накопленный опыт и набраться сил для нового рывка. Скоро мы вернёмся с чем-то по-настоящему особенным!

<b>🔹 Разработчик:</b> Iron Brak Studio
<b>🔹 Издатель:</b> Iron Brak Entertainment
"""

ABOUT_GAME = """
<b>🎮 Stay Alive: The Beginning of the Story</b>

Вы — обычный врач, который оказывается в эпицентре биологической катастрофы. Город охвачен хаосом, а вам предстоит бороться за выживание и искать ответы на вопросы: что произошло и как остановить это?

<b>🔹 Особенности игры:</b>
• <i>Атмосферный хоррор</i> с упором на историю
• <i>Сложный моральный выбор</i>, влияющий на сюжет
• <i>Реалистичная графика</i> и звук, погружающий в мир
• <i>Интерактивное окружение</i> — используйте предметы и окружение для выживания

<b>🔹 Статус разработки:</b>
Игра активно разрабатывается. Мы готовим для вас уникальный опыт, поэтому не торопимся с релизом. Следите за новостями — мы обязательно удивим вас!
"""

DOWNLOAD = """
<b>📥 Скачать игру</b>

Наш проект доступен для скачивания двумя способами:

1. В официальном Telegram-канале (кнопка ниже)
2. На Google Диске (вторая кнопка)

Выберите удобный вариант 👇
"""

CONTACTS = """
<b>📬 Наши контакты</b>

Мы всегда открыты для общения! Пишите нам по любым вопросам — от предложений по игре до сотрудничества.

<b>🔹 Сайт:</b> <a href='https://ironbrak.samp.date'>ironbrak.samp.date</a>
<b>🔹 Email:</b> ironbrakentertainment@gmail.com
<b>🔹 Telegram-канал студии:</b> <a href='https://t.me/Ironbrakst'>@Ironbrakst</a>
<b>🔹 Канал игры:</b> <a href='https://t.me/stayaliivve'>@stayaliivve</a>

Также подписывайтесь на наши соцсети (скоро запустим)!
"""

FAQ = """
<b>❓ Часто задаваемые вопросы</b>

<b>1. Когда выйдет игра?</b>
На данный момент точной даты нет — мы на этапе глубокой переработки концепции. Как только появится определённость, мы объявим дату в наших каналах.

<b>2. На каких платформах будет игра?</b>
Планируется выход на <b>PC (Windows)</b>, а затем, возможно, на консолях. Более точная информация появится позже.

<b>3. Можно ли присоединиться к вашей команде?</b>
Да! Если вы разделяете нашу страсть к атмосферным играм и обладаете навыками в программировании, 3D-моделировании, сценаристике или звукодизайне — напишите нам на email. Мы всегда рады талантливым людям.

<b>4. Будет ли демо-версия?</b>
Мы рассматриваем возможность выпуска демо, но пока не готовы дать обещаний. Следите за анонсами.

<b>5. Как я могу поддержать разработку?</b>
Мы ценим вашу поддержку! Вы можете рассказать о нас друзьям, подписаться на наши соцсети и делиться отзывами. Это лучшая помощь на текущем этапе.
"""

HELP = """
<b>🤖 Помощь по боту</b>

Используйте кнопки главного меню, чтобы получить информацию:
• <b>🏢 О студии</b> — история и философия Iron Brak
• <b>🎮 Об игре</b> — подробности о "Stay Alive"
• <b>📥 Скачать игру</b> — ссылка на канал с игрой
• <b>📞 Контакты</b> — все способы связи с нами
• <b>❓ FAQ</b> — ответы на популярные вопросы

Если у вас остались вопросы, пишите нам в личные сообщения или на почту. Всегда рады помочь!
"""

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name or "друг"
    await message.answer(
        f"<b>Привет, {user_name}!</b>\n\n" + WELCOME,
        reply_markup=main_keyboard(),
        parse_mode='HTML'
    )

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(HELP, parse_mode='HTML', reply_markup=main_keyboard())

@dp.message(Command('menu'))
async def cmd_menu(message: types.Message):
    await message.answer(
        "🔙 Вы вернулись в главное меню.",
        reply_markup=main_keyboard()
    )

@dp.message(F.text == '🔄 Главное меню')
async def back_to_menu(message: types.Message):
    await cmd_menu(message)

@dp.message(F.text == '🏢 О студии')
async def about_studio(message: types.Message):
    await message.answer(ABOUT_STUDIO, parse_mode='HTML', reply_markup=back_inline())

@dp.message(F.text == '🎮 Об игре')
async def about_game(message: types.Message):
    await message.answer(ABOUT_GAME, parse_mode='HTML', reply_markup=back_inline())

@dp.message(F.text == '📥 Скачать игру')
async def download_game(message: types.Message):
    await message.answer(DOWNLOAD, parse_mode='HTML', reply_markup=download_inline())

@dp.message(F.text == '📞 Контакты')
async def contacts(message: types.Message):
    await message.answer(CONTACTS, parse_mode='HTML', reply_markup=contacts_inline(), disable_web_page_preview=True)

@dp.message(F.text == '❓ FAQ')
async def faq(message: types.Message):
    await message.answer(FAQ, parse_mode='HTML', reply_markup=back_inline())

@dp.callback_query(F.data == 'main_menu')
async def callback_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "<b>🔙 Главное меню</b>\n\nВыберите интересующий вас раздел:",
        reply_markup=None,
        parse_mode='HTML'
    )
    await callback.message.answer(
        "Используйте кнопки под полем ввода.",
        reply_markup=main_keyboard()
    )
    await callback.answer()

@dp.message()
async def handle_unknown(message: types.Message):
    await message.answer(
        "😕 Извините, я не понимаю этот запрос.\n"
        "Пожалуйста, воспользуйтесь кнопками меню.",
        reply_markup=main_keyboard()
    )

async def main():
    logging.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())