#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix = '?', intents = discord.Intents.all())
client.remove_command('help')



@client.event
async def on_ready():
	print('Connected!')
	await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game('Game Over'))


#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx,member: discord.Member,*,reason = None):
	emb = discord.Embed(title = 'Пользователь кикнут!', colour = discord.Color.red())
	await member.kick(reason = reason)
	emb.set_author(name=member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Информация', value = 'Кикнутый пользователь: {}'.format(member.mention))
	await ctx.send(embed = emb)

#ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx,member: discord.Member,*,reason = None):
	emb = discord.Embed(title = 'Пользователь забанен!', colour = discord.Color.red())
	await member.ban(reason = reason)
	emb.set_author(name=member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Информация', value = 'Забаненный пользователь: {}'.format(member.mention))
	await ctx.send(embed = emb)

#Авто-выдача роли
@client.event
async def on_member_join(member):
	channel = client.get_channel(747820695014080512)
	role = discord.utils.get(member.guild.roles, id = 747711684214259744)
	await member.add_roles(role)
	await channel.send(embed = discord.Embed(description = f':wave: Привет,  **{member.mention}**\n:heart_eyes: Сервер **Game Over** приветстввует тебя!\nGame Over 2.0  - это необычный сервер!\nНа нём есть множество каналов!\nОгромное количество ролей, игр и много чего другого!\nРекомендуем для прочтения:• Правила нащего дискорд сервера: <#747712287795707944>\n:question: • Условия получения ролей - <#787640939145330708>\n • Розыгрыши и многое другое - <#773273340734865451>\n Приятного общения на сервере! ', color = 10ff48))

#Авто-выдача роли
@client.event
async def on_member_remove(member):
	channel = client.get_channel(747820695014080512)
	await channel.send(embed = discord.Embed(description = f'**{member.name}**, покинул сервер!', color = 0xFFA500))

client.run(str(os.environ.get("TOKEN")))
