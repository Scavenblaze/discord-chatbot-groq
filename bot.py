import os
import discord
from groq import Groq

token = os.getenv('BOT_TOKEN')
groq_key = os.getenv('GROQ_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

groq_client = Groq(api_key=groq_key)

#configure bot
system_prompt = {
    "role":
    "system",
    "content":
    "You are a passive aggressive but helpful assistant. You reply with medium answers."
}

#initialize the chat history
chat_history = [system_prompt]


#discord code
class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!'):  #prefix for the bot

            prompt = message.content[1:]  #ignores the prefix

            chat_history.append({"role": "user", "content": prompt})

            response = groq_client.chat.completions.create(
                model="llama3-70b-8192",
                messages=chat_history,
                max_tokens=100,
                temperature=1.2)

            #append the response to the chat history
            chat_history.append({
                "role": "assistant",
                "content": response.choices[0].message.content
            })

            #sends message in discord
            await message.channel.send(response.choices[0].message.content)


client = MyClient(intents=intents)
client.run(token)
