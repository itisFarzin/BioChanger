#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv


load_dotenv()


class Config:
	LOGGER = None
	DEBUG = False

	SESSION_NAME = os.environ.get("SESSION_NAME", "BioChanger")
	# The Telegram API things
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH", None)
	#
	IN_MEMORY = bool(os.environ.get("IN_MEMORY", False))
	OWNER_ID = int(os.environ.get("OWNER_ID", 1004490950))
	# Proxy things
	PROXY_SCHEME = os.environ.get("PROXY_SCHEME", None)
	PROXY_HOSTNAME = os.environ.get("PROXY_HOSTNAME", None)
	PROXY_PORT = int(os.environ.get("PROXY_PORT", 12345))
	PROXY_USERNAME = os.environ.get("PROXY_USERNAME", None)
	PROXY_PASSWORD = os.environ.get("PROXY_PASSWORD", None)
