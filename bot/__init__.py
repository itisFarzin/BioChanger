#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from bot.config import Config

logging.basicConfig(
	level=logging.DEBUG if Config.DEBUG else logging.WARNING,
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = Config.LOGGER or logging.getLogger(__name__)
SESSION_NAME = Config.SESSION_NAME
API_ID = Config.API_ID
API_HASH = Config.API_HASH
IN_MEMORY = Config.IN_MEMORY

PROXY_SCHEME = Config.PROXY_SCHEME
PROXY_HOSTNAME = Config.PROXY_HOSTNAME
PROXY_PORT = Config.PROXY_PORT
PROXY_USERNAME = Config.PROXY_USERNAME
PROXY_PASSWORD = Config.PROXY_PASSWORD
