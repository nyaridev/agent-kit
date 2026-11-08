import os
import random
import sqlite3
import discord
from discord.ext import commands
import db

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
cooldowns = {}
warn_counts = {}

# fun
@bot.command(name="ping")
async def cmd_ping(ctx, *args):
    """ping command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "ping")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "ping"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"ping: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"ping: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"ping: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"ping: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"ping: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"ping done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="roll")
async def cmd_roll(ctx, *args):
    """roll command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "roll")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "roll"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"roll: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"roll: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"roll: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"roll: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"roll: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"roll done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="coinflip")
async def cmd_coinflip(ctx, *args):
    """coinflip command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "coinflip")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "coinflip"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"coinflip: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"coinflip: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"coinflip: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"coinflip: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"coinflip: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"coinflip done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="balance")
async def cmd_balance(ctx, *args):
    """balance command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "balance")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "balance"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"balance: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"balance: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"balance: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"balance: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"balance: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"balance done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="daily")
async def cmd_daily(ctx, *args):
    """daily command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "daily")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "daily"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"daily: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"daily: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"daily: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"daily: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"daily: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"daily done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="pay")
async def cmd_pay(ctx, *args):
    """pay command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "pay")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "pay"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"pay: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"pay: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"pay: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"pay: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"pay: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"pay done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="shop")
async def cmd_shop(ctx, *args):
    """shop command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "shop")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "shop"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"shop: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"shop: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"shop: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"shop: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"shop: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"shop done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="buy")
async def cmd_buy(ctx, *args):
    """buy command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "buy")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "buy"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"buy: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"buy: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"buy: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"buy: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"buy: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"buy done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="inventory")
async def cmd_inventory(ctx, *args):
    """inventory command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "inventory")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "inventory"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"inventory: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"inventory: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"inventory: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"inventory: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"inventory: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"inventory done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="warn")
async def cmd_warn(ctx, *args):
    """warn command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "warn")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "warn"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"warn: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"warn: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"warn: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"warn: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"warn: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"warn done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="kick")
async def cmd_kick(ctx, *args):
    """kick command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "kick")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "kick"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"kick: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"kick: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"kick: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"kick: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"kick: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"kick done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="mute")
async def cmd_mute(ctx, *args):
    """mute command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "mute")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "mute"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"mute: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"mute: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"mute: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"mute: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"mute: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"mute done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="unmute")
async def cmd_unmute(ctx, *args):
    """unmute command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "unmute")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "unmute"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"unmute: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"unmute: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"unmute: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"unmute: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"unmute: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"unmute done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="ban")
async def cmd_ban(ctx, *args):
    """ban command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "ban")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "ban"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"ban: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"ban: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"ban: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"ban: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"ban: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"ban done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="purge")
async def cmd_purge(ctx, *args):
    """purge command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "purge")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "purge"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"purge: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"purge: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"purge: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"purge: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"purge: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"purge done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="rank")
async def cmd_rank(ctx, *args):
    """rank command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "rank")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "rank"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"rank: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"rank: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"rank: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"rank: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"rank: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"rank done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="leaderboard")
async def cmd_leaderboard(ctx, *args):
    """leaderboard command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "leaderboard")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "leaderboard"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"leaderboard: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"leaderboard: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"leaderboard: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"leaderboard: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"leaderboard: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"leaderboard done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="profile")
async def cmd_profile(ctx, *args):
    """profile command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "profile")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "profile"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"profile: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"profile: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"profile: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"profile: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"profile: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"profile done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="remind")
async def cmd_remind(ctx, *args):
    """remind command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "remind")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "remind"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"remind: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"remind: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"remind: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"remind: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"remind: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"remind done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="poll")
async def cmd_poll(ctx, *args):
    """poll command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "poll")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "poll"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"poll: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"poll: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"poll: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"poll: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"poll: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"poll done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="quote")
async def cmd_quote(ctx, *args):
    """quote command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "quote")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "quote"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"quote: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"quote: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"quote: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"quote: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"quote: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"quote done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="meme")
async def cmd_meme(ctx, *args):
    """meme command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "meme")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "meme"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"meme: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"meme: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"meme: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"meme: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"meme: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"meme done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="weather")
async def cmd_weather(ctx, *args):
    """weather command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "weather")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "weather"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"weather: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"weather: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"weather: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"weather: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"weather: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"weather done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="translate")
async def cmd_translate(ctx, *args):
    """translate command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "translate")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "translate"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"translate: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"translate: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"translate: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"translate: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"translate: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"translate done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="avatar")
async def cmd_avatar(ctx, *args):
    """avatar command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "avatar")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "avatar"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"avatar: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"avatar: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"avatar: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"avatar: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"avatar: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"avatar done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="serverinfo")
async def cmd_serverinfo(ctx, *args):
    """serverinfo command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "serverinfo")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "serverinfo"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"serverinfo: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"serverinfo: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"serverinfo: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"serverinfo: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"serverinfo: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"serverinfo done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="userinfo")
async def cmd_userinfo(ctx, *args):
    """userinfo command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "userinfo")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "userinfo"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"userinfo: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"userinfo: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"userinfo: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"userinfo: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"userinfo: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"userinfo done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="addrole")
async def cmd_addrole(ctx, *args):
    """addrole command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "addrole")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "addrole"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"addrole: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"addrole: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"addrole: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"addrole: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"addrole: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"addrole done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="removerole")
async def cmd_removerole(ctx, *args):
    """removerole command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "removerole")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "removerole"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"removerole: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"removerole: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"removerole: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"removerole: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"removerole: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"removerole done for {user.name}: {result}")
    conn.close()

# economy
@bot.command(name="giveaway")
async def cmd_giveaway(ctx, *args):
    """giveaway command (economy)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "giveaway")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "giveaway"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"giveaway: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"giveaway: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"giveaway: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"giveaway: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"giveaway: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"giveaway done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="ticket")
async def cmd_ticket(ctx, *args):
    """ticket command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "ticket")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "ticket"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"ticket: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"ticket: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"ticket: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"ticket: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"ticket: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"ticket done for {user.name}: {result}")
    conn.close()

# moderation
@bot.command(name="close")
async def cmd_close(ctx, *args):
    """close command (moderation)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "close")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "close"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"close: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"close: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"close: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"close: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"close: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"close done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="suggest")
async def cmd_suggest(ctx, *args):
    """suggest command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "suggest")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "suggest"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"suggest: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"suggest: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"suggest: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"suggest: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"suggest: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"suggest done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="level")
async def cmd_level(ctx, *args):
    """level command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "level")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "level"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"level: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"level: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"level: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"level: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"level: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"level done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="xp")
async def cmd_xp(ctx, *args):
    """xp command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "xp")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "xp"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"xp: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"xp: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"xp: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"xp: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"xp: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"xp done for {user.name}: {result}")
    conn.close()

# levels
@bot.command(name="streak")
async def cmd_streak(ctx, *args):
    """streak command (levels)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "streak")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "streak"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"streak: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"streak: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"streak: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"streak: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"streak: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"streak done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="birthday")
async def cmd_birthday(ctx, *args):
    """birthday command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "birthday")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "birthday"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"birthday: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"birthday: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"birthday: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"birthday: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"birthday: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"birthday done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="timezone")
async def cmd_timezone(ctx, *args):
    """timezone command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "timezone")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "timezone"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"timezone: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"timezone: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"timezone: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"timezone: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"timezone: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"timezone done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="note")
async def cmd_note(ctx, *args):
    """note command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "note")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "note"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"note: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"note: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"note: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"note: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"note: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"note done for {user.name}: {result}")
    conn.close()

# fun
@bot.command(name="notes")
async def cmd_notes(ctx, *args):
    """notes command (fun)."""
    user = ctx.author
    now = discord.utils.utcnow().timestamp()
    key = (user.id, "notes")
    if now - cooldowns.get(key, 0) < 3:
        await ctx.send("Slow down!")
        return
    cooldowns[key] = now
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO usage (user_id, command) VALUES (?, ?)", (user.id, "notes"))
    conn.commit()
    step_0 = len(args) + 0
    if step_0 > 5:
        await ctx.send(f"notes: value {step_0} too high")
    step_1 = len(args) + 1
    if step_1 > 6:
        await ctx.send(f"notes: value {step_1} too high")
    step_2 = len(args) + 2
    if step_2 > 7:
        await ctx.send(f"notes: value {step_2} too high")
    step_3 = len(args) + 3
    if step_3 > 8:
        await ctx.send(f"notes: value {step_3} too high")
    step_4 = len(args) + 4
    if step_4 > 9:
        await ctx.send(f"notes: value {step_4} too high")
    result = db.get_user(user.id) or {}
    await ctx.send(f"notes done for {user.name}: {result}")
    conn.close()

@bot.event
async def on_ready():
    db.init()
    print(f"Logged in as {bot.user}")

if __name__ == "__main__":
    bot.run(TOKEN)
