import asyncio
import discord
from discord.ext import commands
from pyVinted import Vinted
import requests
import json
import pytz

BOT_TOKEN = "MTExNTY5NTI3MDkxOTk1MDM1Ng.Gxs89v.9m5xzs210kQ-NZjhnuiGdgWbXH0SW4a1wF97dc"  # Remplacez par le token de votre bot
WEBHOOK = "https://discord.com/api/webhooks/1121491092051857549/L2JwMiCLb5NaDntrs0uucGVt-Jt0G64Z9JPn2xTD_cKiLe9H3M2EbhvbMWzS-YuAeHYY"  # Remplacez par l'URL de votre webhook Discord

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="!", intents=intents)
sent_items = set()  # Utilisez un ensemble pour stocker les IDs des articles déjà envoyés

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user.name} \n        -----------------------")

@bot.command()
async def snipe (ctx, link):
    vinted = Vinted()
    while True:
        items = vinted.items.search(link, 10, 1)

        if items:
            for item in items:
                if item.id not in sent_items:
                    sent_items.add(item.id)  # Ajoutez l'ID de l'article à l'ensemble des articles envoyés

                    # Obtenez les détails de l'article ici
                    title = item.title
                    # ... autres détails de l'article
                    if title != "":
                        title = title
                    else:
                        title = "Not found"

                    screen = item.photo
                    if screen != "":
                        screen = screen
                    else:
                        screen = "Not found"

                    brand = item.brand_title
                    if brand != "":
                        brand = brand
                    else:
                        brand = "Not found"

                    price = item.price
                    if price != "":
                        price = price
                    else:
                        price = "Not found"

                    url = item.url
                    if url != "":
                        url = url
                    else:
                        url = "Not found"

                    currency = item.currency
                    if currency != "":
                        currency = currency
                    else:
                        currency = "Not found"

                    create = item.created_at_ts
                    if create != "":
                        tz = pytz.timezone('Europe/Paris')  # Fuseau horaire UTC+2 (Europe/Paris)
                        create = create.astimezone(tz)
                        create = create.strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        create = "Not found"

                    if currency == "EUR":
                        price = f"{price}€"
                    else:
                        price = price
                        
                    
                     #Créez un embed pour le message Discord
                    embed = discord.Embed(title="Vinted Bot", description="The best Vinted Bot is here!", color=discord.Color.blue())
                    embed.set_thumbnail(url="https://www.presse-citron.net/app/uploads/2020/06/vinted-logo.jpg")
                    embed.set_image(url=screen)
                    embed.add_field(name=f"{title} : {url}", value=f"⌛ **Published **: `{create}`\n🔖 **Brand **: `{brand}`\n💰 **Price **: `{price}`\n")
                    embed.set_footer(text="Dev By KyroLast", icon_url="https://i.pinimg.com/originals/3c/c6/e7/3cc6e7226c2ab03619a012c9bcf12c17.gif")

                    # Envoyez l'embed au canal où la commande a été exécutée
                    await ctx.send(embed=embed)

                    print("[+] embed sent with succes")
                   
                    

        else:
            await ctx.send("Aucun article trouvé.")

        await asyncio.sleep(15)  # Attendre 60 secondes avant de refaire la recherche

loop = asyncio.get_event_loop()
loop.create_task(bot.start(BOT_TOKEN))
loop.run_forever()
