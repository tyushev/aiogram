import pytest

from aiogram.methods import Request, SetChatStickerSet
from tests.mocked_bot import MockedBot

pytestmark = pytest.mark.asyncio


class TestSetChatStickerSet:
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatStickerSet, ok=True, result=True)

        response: bool = await SetChatStickerSet(chat_id=-42, sticker_set_name="test")
        request: Request = bot.get_request()
        assert request.method == "setChatStickerSet"
        assert response == prepare_result.result

    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatStickerSet, ok=True, result=True)

        response: bool = await bot.set_chat_sticker_set(chat_id=-42, sticker_set_name="test")
        request: Request = bot.get_request()
        assert request.method == "setChatStickerSet"
        assert response == prepare_result.result
