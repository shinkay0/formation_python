import os
import discord
from discord.ext import commands
from discord.ui import Button, View

TOKEN = os.environ.get("DISCORD_TOKEN")

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
        {
            "question":
            "Qu'est-ce qu'une assurance vie et comment fonctionne-t-elle?",
            "reponse":
            "Une assurance vie est un contrat entre entre vous et un assureur. Vous payez des primes régulières"
        },
        {
            "question":
            "Quels sont les avantages fiscaux d'une assurance vie?",
            "reponse":
            "Les avantages fiscaux d'une assurance vie sont nombreux. Vous pouvez par exemple bénéficier d'une exonération d'impôt sur les plus-values"
        },
        {
            "question":
            "Comment choisir le bon contrat d'assurance vie?",
            "reponse":
            "Pour choisir le bon contrat d'assurance vie, il est important de prendre en compte plusieurs critères. Vous devez notamment tenir compte de votre situation personnelle, de vos objectifs financiers et de votre appétence au risque"
        },
    ]

    @bot.command()
    async def ui(ctx):
        view = View()

        def add_buttons_to_view(view, questions):
            for i, question in enumerate(questions):
                button = Button(label=question["question"],
                                style=discord.ButtonStyle.green)

                async def callback(interaction, index=i):
                    await interaction.response.send_message(
                        questions[index]["reponse"])

                button.callback = callback
                view.add_item(button)

        add_buttons_to_view(view, questions)

        await ctx.send("Choisir une question", view=view)


bot.run(TOKEN)
