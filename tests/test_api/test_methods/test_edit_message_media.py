from typing import Union

import pytest

from aiogram.methods import EditMessageMedia, Request
from aiogram.types import BufferedInputFile, InputMediaPhoto, Message
from tests.mocked_bot import MockedBot

pytestmark = pytest.mark.asyncio


class TestEditMessageMedia:
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(EditMessageMedia, ok=True, result=True)

        response: Union[Message, bool] = await EditMessageMedia(
            media=InputMediaPhoto(media=BufferedInputFile(b"", "photo.png"))
        )
        request: Request = bot.get_request()
        assert request.method == "editMessageMedia"
        assert response == prepare_result.result

    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(EditMessageMedia, ok=True, result=True)

        response: Union[Message, bool] = await bot.edit_message_media(
            media=InputMediaPhoto(media=BufferedInputFile(b"", "photo.png"))
        )
        request: Request = bot.get_request()
        assert request.method == "editMessageMedia"
        assert response == prepare_result.result
