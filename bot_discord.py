# bot_discord.py

import discord
import asyncio
from chatbot_atencion import obtener_respuesta


# Intents necesarios para recibir mensajes
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Creamos el cliente de Discord
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f' El bot se ha conectado como {client.user}')

@client.event
async def on_message(message):
    # Evita que el bot se responda a sí mismo
    if message.author == client.user:
        return

    # Obtenemos el contenido del mensaje
    contenido = message.content

    # Simula que el bot "está escribiendo"
    async with message.channel.typing():
        await asyncio.sleep(1.5)  # tiempo de espera

        # Obtenemos la respuesta del chatbot
        respuesta = obtener_respuesta(contenido)

        # Respondemos al usuario
        await message.channel.send(respuesta)

# Iniciamos el bot
client.run(TOKEN)
