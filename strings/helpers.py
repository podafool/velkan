#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """▶️ Normal Commands 

/play or /vplay - Bot will start playing your given query on voice chat

/playforce - Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/pause  - Pause the playing music.
/resume - Resume the paused music.
/mute - Mute the playing music.
/unmute - Unmute the muted music.
/skip - Skip the current playing music.
/stop - Stop the playing music.
/shuffle - Randomly shuffles the queued playlist.
/seek  - Forward Seek the music to your duration
/seekback  - Backward Seek the music to your duration

/queue- Check Queue List of Music

/skip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

 /loop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times."""


HELP_2 = """🗯 For channels

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.

/cplay  - Bot will start playing your given query on Stream live links on voice chats.
/cplayforce -  Similar to /playforce but use for channel
/cpause - Pause the playing music.

/cresume- Resume the paused music.
/cmute- Mute the playing music.
/cunmute- Unmute the muted music.
/cskip- Skip the current playing music.
/cstop- Stop the playing music.
/cshuffle- Randomly shuffles the queued playlist.
/cseek - Forward Seek the music to your duration
/cseekback - Backward Seek the music to your duration

/cqueue- Check Queue List of Music.

/cskip [Number(example: 3)] - Skips music to a the specified queued number.
 /cloop [enable/disable] or [Numbers between 1-10] - Bot loops the current playing music to 1-10 times on voice chat. Default to 10 times."""


HELP_3 = """🎛 Other commands

/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/restart - Restart bot for your chat

Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

/player -  Get a interactive Playing Panel."""

HELP_4 = """⚙️ Settings commands

/settings - Get a complete group's settings with inline buttons

  **Options in Settings:**
1️. Set Audio Quality.
2️. Set Video Quality.
3️. Auth Users:- You can change admin commands (like /skip, /stop etc) mode from here to everyone or admins only.
4️. Clean Mode: When enabled deletes the bot's messages after 5 mins from your group.
5. Command Clean : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.
6️. Play Settings:
/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 
  Options in playmode:
  1️. Search Mode [Direct or Inline] - Changes your search mode while you give /play mode. 
  2️. Admin Commands [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)
  3️. Play Type [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""
