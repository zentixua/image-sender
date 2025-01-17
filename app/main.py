import asyncio
import io
import logging
import time

import win32clipboard

from .dependencies import bing_images
from .utils import utils, async_keyboard
from .utils.utils import send_to_clipboard

WAIT_TIME = 5


async def send():
    images = await bing_images.get_images(query, amount)
    async for image in images:
        try:
            image = await utils.prepare_image(io.BytesIO(image))
        except OSError as e:
            logging.warning(str(e), exc_info=e)
        await send_to_clipboard(win32clipboard.CF_DIB, image)
        await async_keyboard.press_and_release('ctrl+v, enter')
        await asyncio.sleep(1)


if __name__ == '__main__':
    query = input('Enter your search query: ')
    amount = int(input('Enter the maximum number of images: '))
    print(f'After {WAIT_TIME} seconds the sending of pictures will start. '
          f'Click on the input field in the desired application!')
    time.sleep(WAIT_TIME)
    asyncio.run(send())

    print('Great! Images have been sent successfully!')
