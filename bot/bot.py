#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyrogram

from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot import (
	LOGGER,
	SESSION_NAME,
	API_ID,
	API_HASH,
	IN_MEMORY,
	PROXY_SCHEME,
	PROXY_HOSTNAME,
	PROXY_PORT,
	PROXY_USERNAME,
	PROXY_PASSWORD
)


class Bot(pyrogram.Client):
	def __init__(self):
		proxy = dict()
		if PROXY_SCHEME and PROXY_HOSTNAME and PROXY_PORT:
			if PROXY_USERNAME and PROXY_PASSWORD:
				proxy["username"] = PROXY_USERNAME
				proxy["password"] = PROXY_PASSWORD
			proxy["scheme"] = PROXY_SCHEME
			proxy["hostname"] = PROXY_HOSTNAME
			proxy["port"] = PROXY_PORT

		super().__init__(name="data/"+SESSION_NAME,
						 api_id=API_ID,
						 api_hash=API_HASH,
						 proxy=proxy,
						 in_memory=IN_MEMORY)

		self.bio = None

		self.scheduler = AsyncIOScheduler()

	async def start(self):
		await super().start()

		try:
			self.bio = (
				await self.invoke(
					pyrogram.raw.functions.users.GetFullUser(id=pyrogram.raw.types.InputUserSelf())
				)
			).full_user.about
		except Exception as e:
			LOGGER.exception(e)
			raise

		self.scheduler.start()
		self.scheduler.add_job(self.change_bio, trigger="cron", minute="*/1")
		LOGGER.info("BioChanger started")

	async def stop(self, *arg):
		self.scheduler.shutdown()
		await self.update_profile(bio=self.bio)
		await super().stop()
		LOGGER.info("BioChanger stopped. cya.")

	async def change_bio(self):
		await self.update_profile(bio=f"{self.bio} {datetime.now().strftime('%H:%M')}")
