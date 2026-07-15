import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# 1. Création d'un mini serveur Web pour Render
app = Flask('')

@app.route('/')
def home():
    return "Le bot est en ligne et fonctionnel !"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# On lance le serveur web dans un thread séparé
Thread(target=run_web_server).start()

# 2. Configuration et démarrage du bot Discord
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_type=None, command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté avec succès en tant que {bot.user.name} !")

@bot.command()
async def dis(ctx, *, message: str):
    """Commande !dis qui fait répéter le bot"""
    await ctx.send(message)

token = os.getenv("DISCORD_TOKEN")

if token:
    bot.run(token)
else:
    print("Erreur : Le token de connexion (DISCORD_TOKEN) est introuvable.")
