# BioChanger (Pyrogram)

A Telegram Client bot for adding time to your bio (WIP)

> in future im going to add new features to this bot

I don't have ANY WARRANTY if telegram ban your account or something
# Environment Variables

### Required Variables
* `APP_ID` and `API_HASH`: Get these two variable from [my.telegram.org/apps](https://my.telegram.org/apps).

### Optional Variables
* `IN_MEMORY`: if you want to use bot and not having a session file, set this variable to true so bot runs in memory
* `OWNER_ID` not useful for now
### Proxy (if you're not using proxy, ignore it)
* `PROXY_SCHEME`, `PROXY_HOSTNAME` and `PROXY_PORT`: set your proxy settings
* `PROXY_USERNAME` and `PROXY_PASSWORD`: if your proxy require authorization, set this variables

## .env file examples:
### example 1:
>API_ID = 1234<br>
API_HASH = abcd1234
### example 2:
>API_ID = 1234<br>
API_HASH = abcd1234<br><br>
PROXY_SCHEME = https<br>
PROXY_HOSTNAME = localhost<br>
PROXY_PORT = 1234