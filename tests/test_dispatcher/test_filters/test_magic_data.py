import pytest
from magic_filter import AttrDict

from aiogram import F
from aiogram.dispatcher.filters import MagicData
from aiogram.types import Update


class TestMagicDataFilter:
    @pytest.mark.asyncio
    async def test_call(self):
        called = False

        def check(value):
            nonlocal called
            called = True

            assert isinstance(value, AttrDict)
            assert value[0] == "foo"
            assert value[1] == "bar"
            assert value["spam"] is True
            assert value.spam is True
            return value

        f = MagicData(magic_data=F.func(check).as_("test"))
        result = await f(Update(update_id=123), "foo", "bar", spam=True)

        assert called
        assert isinstance(result, dict)
        assert result["test"]
