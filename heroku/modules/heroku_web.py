# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

# ©️ Codrago, 2024-2025
# This file is a part of Heroku Userbot
# 🌐 https://github.com/coddrago/Heroku
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

import logging
import os
import random

import herokutl
from herokutl.tl.functions.messages import (
    GetDialogFiltersRequest,
    UpdateDialogFilterRequest,
)
from herokutl.tl.types import Message
from herokutl.utils import get_display_name

from .. import loader, log, main, utils
from .._internal import fw_protect, restart
from ..inline.types import InlineCall
from ..web import core

logger = logging.getLogger(__name__)


@loader.tds
class HerokuWebMod(loader.Module):
    """Web mode add account"""

    strings = {"name": "HerokuWeb"}


    @loader.command()
    async def weburl(self, message: Message, force: bool = False):
        url = "http://127.0.0.1:00"
        
        if force:
            form = message
            await form.edit(
                self.strings("tunnel_opened"),
                reply_markup={"text": self.strings("web_btn"), "url": url},
                photo="https://imgur.com/a/lgmzCpj.png",
            )
        else:
            form = await self.inline.form(
                self.strings("tunnel_opened"),
                message=message,
                reply_markup={"text": self.strings("web_btn"), "url": url},
                photo="https://imgur.com/a/lgmzCpj.png",
            )
