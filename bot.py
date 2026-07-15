import os
import discord
from discord.ext import commands

# Configuration des permissions (Intents) pour que le bot puisse lire les messages
intents = discord.Intents.default()
intents.message_content = True  # Indispensable pour lire le contenu des messages !

# On crée le bot avec le préfixe "!"
bot = commands.Bot(command_type=None, command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté avec succès en tant que {bot.user.name} !")

@bot.command()
async def dis(ctx, *, message: str):
    """Commande !dis qui fait répéter le bot"""
    await ctx.send(message)

# Récupération sécurisée du Token de ton bot (configuré dans les variables d'environnement sur Render)
token = os.getenv("DISCORD_TOKEN")

if token:
    bot.run(token)
else:
    print("Erreur : Le token de connexion (DISCORD_TOKEN) est introuvable. Ajoute-le dans les variables d'environnement de Render.")
