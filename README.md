# discord-chatbot-groq
This discord bot utilises the llama3-70b-8192 model to generate responses for user's messages sent on discord.  

Current features of this bot is:
- <b>Custom Bot Emotion:</b> Set custom response emotion of the bot using the command `!setmood [mood]`, for example: `!setmood cheerful` generates cheerful responses or `!setmood sad` generates sad responses.



## How to set up:

- Install Discord, Groq and dotenv libraries `pip install discord groq dotenv`
- Create a bot on discord developer portal and copy the secet key.
- Create an account on Groq and copy the API key.
- Paste the Bot's and Groq's api key as `BOT_TOKEN` and `GROQ_API_KEY` respectively.
- Run the bot and let it connect
- Invite the bot in your discord server.
- Start chatting with your bot using the command `![message]`
- Set custom mood using `!setmood [mood_name]`