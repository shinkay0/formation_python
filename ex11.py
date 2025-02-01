import os
import discord
from discord.ext import commands
from discord.ui import Button, View
from groq import Groq

TOKEN = os.environ.get("DISCORD_TOKEN")
client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def clear(ctx):
    await ctx.channel.purge()


@bot.event
async def on_ready():
    print("ok")

    questions = [
        "Qu'est-ce qu'une assurance vie et comment fonctionne-t-elle?",
        "Quels sont les avantages fiscaux d'une assurance vie?",
        "Comment choisir le bon contrat d'assurance vie?",
    ]

    @bot.command()
    async def gpt(ctx):
        view = View()

        def add_buttons_to_view(view, questions):
            for i, question in enumerate(questions):
                button = Button(label=question,
                                style=discord.ButtonStyle.green)

                async def callback(interaction, index=i):
                    q = questions[index]

                    chat_completion = client.chat.completions.create(
                        messages=[{
                            "role": "user",
                            "content": q,
                        }],
                        model="llama-3.3-70b-versatile",
                        max_completion_tokens=200)
                    await interaction.response.send_message(
                        chat_completion.choices[0].message.content)

                button.callback = callback
                view.add_item(button)

        add_buttons_to_view(view, questions)

        await ctx.send("Choisir une question", view=view)


bot.run(TOKEN)
