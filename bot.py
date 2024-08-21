import os

import discord
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

token = os.getenv('BOT_TOKEN')
groq_key = os.getenv('GROQ_API_KEY')


intents = discord.Intents.default()
intents.message_content = True

groq_client = Groq(api_key=groq_key)

mood = 'helpful' #default mood


#discord code
class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user}!')


    async def on_message(self, message):
        try:
            
            #prevents the bot from replying to itself
            if message.author == self.user:
                return
            
            #sets bot's mood
            if message.content.startswith('!moodset '):
                mood = message.content[9:]
                await message.channel.send(f"bot's mood has been set to {mood}")
                

            if message.content.startswith('!'):  #prefix for the bot

                prompt = message.content[1:]  #ignores the prefix and takes user's message as prompt
                
                #configure bot
                system_prompt = {
                    "role":
                    "system",
                    "content":
                    f"You are a {mood} assistant. You reply with medium answers." #dynamically sets mood
                }
                
                #initialize the chat history
                chat_history = [system_prompt]

                chat_history.append({"role": "user", "content": prompt})

                #model
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
 
        #error catching
        except Exception as e:
            print(f"An error occurred {e}")
            await message.channel.send("There was some dumb error and I'll try to fix it until then watch a yt video")





client = MyClient(intents=intents)
client.run(token)
