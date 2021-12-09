# discordpy-role-list-example

<img width="496" alt="command example" src="https://user-images.githubusercontent.com/42476527/145411793-9c3bed3e-0e2a-4448-ad69-6f94d0efa136.png">

これは、role一覧をcsv出力するコマンド（`??rolecsv`）の実装例を提示するためのリポジトリです。

## csvの形式

```
id,name,create_instant_invite,kick_members,ban_members,administrator,manage_channels,manage_guild,add_reactions,view_audit_log,priority_speaker,stream,read_messages,send_messages,send_tts_messages,manage_messages,embed_links,attach_files,read_message_history,mention_everyone,external_emojis,view_guild_insights,connect,speak,mute_members,deafen_members,move_members,use_voice_activation,change_nickname,manage_nicknames,manage_roles,manage_webhooks,manage_emojis,use_slash_commands,request_to_speak
0,@everyone,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True
```
- id：Discordのroleの並び順です。0が一番下に相当します。
- name：roleの名前です。
- その他：roleが持つ権限です。True/Falseで表します。

## Usage

### Heroku
```
heroku create {your-bot-name}
heroku config:set DISCORD_BOT_TOKEN={your_bot_token}
git push heroku master
```

### Local
```
touch .env
echo "DISCORD_BOT_TOKEN={your_bot_token}" >> .env
pipenv install
pipenv run bot
```
