import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def clear(ctx):
    await ctx.channel.purge()


@bot.command()
async def hello(ctx):
    await ctx.send('bonjour')


questions = [{
    "question": "Quel est la capitale de la France?",
    "answers": ["lyon", "paris", "france", "strasbourg"],
    "correct_answer": "B"
}, {
    "question": "En quelle année a été fondé Apple?",
    "answers": ["1976", "1980", "1990", "2000"],
    "correct_answer": "A"
}, {
    "question": "Quel est le nom de famille de l'acteur Will?",
    "answers": ["smith", "johnson", "jackson", "brown"],
    "correct_answer": "A"
}]

question_count = 0
correct = 0
quiz_active = False


@bot.command()
async def quiz(ctx):
    global question_count, correct, quiz_active

    if not quiz_active:
        question_count = 0
        correct = 0
        quiz_active = True

    if question_count < len(questions):
        await ctx.send(questions[question_count]["question"])
        for i, answer in enumerate(questions[question_count]["answers"]):
            await ctx.send(f"{chr(65 + i)}: {answer}")
    else:
        await ctx.send(
            f"Quiz terminé! Nombre de bonnes réponses : {correct}/{len(questions)}"
        )
        quiz_active = False


@bot.event
async def on_message(message):
    global question_count, correct, quiz_active

    if message.author == bot.user:
        return

    if quiz_active and message.content.upper() in ["A", "B", "C", "D"]:
        if message.content.upper(
        ) == questions[question_count]["correct_answer"]:
            await message.channel.send("Bonne réponse!")
            correct += 1
        else:
            await message.channel.send("Mauvaise réponse!")
        question_count += 1

        if question_count < len(questions):
            await message.channel.send(questions[question_count]["question"])
            for i, answer in enumerate(questions[question_count]["answers"]):
                await message.channel.send(f"{chr(65 + i)}: {answer}")
        else:
            await message.channel.send(
                f"Quiz terminé! Nombre de bonnes réponses : {correct}/{len(questions)}"
            )
            quiz_active = False

    await bot.process_commands(message)


bot.run(TOKEN)
