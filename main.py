import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import os
from dotenv import load_dotenv

import parser as pr
from request_to_ai import sum_text

load_dotenv()

CHANNEL = os.getenv('TELEGRAM_CHANNEL')
bot = Bot(os.getenv('TOKEN'))
USER_ID = os.getenv('USER_ID')
dp = Dispatcher()

async def main():
    if os.environ.get('IS_WORKER') == '1':
        asyncio.create_task(start())
    await dp.start_polling(bot)
    

async def start():
    while True:
        try:
            await bot.send_message(USER_ID, 'Подготавливаю пост...')
            html_content = await pr.get_html_text('https://www.rbc.ru/economics/')
            soup = pr.get_soup(html_content)
            title = pr.get_post_title(soup)
            post_url = pr.get_post_url(soup)
            post_content = await pr.get_post_content(post_url)
            post_text = pr.get_post_text(pr.get_soup(post_content))
            picture = pr.get_picture(pr.get_soup(post_content))
            
            await bot.send_message(USER_ID, 'Передаю пост нейросети...')
            post_text = sum_text(post_text)
            
            await bot.send_photo(chat_id=CHANNEL, photo=picture, caption=f'<b>{title}</b>\n\n{post_text}', parse_mode='html')
            await bot.send_message(USER_ID, 'Выложил пост!')
            await asyncio.sleep(10800)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())