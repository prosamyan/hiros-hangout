import discord


discord.Intents.default()


@bot.command(name='addrole', hidden=True)
@has_permissions(administrator=True)
async def add_beta_role(ctx, role='beta-test'):
    with open('./beta_list.csv', 'r+') as beta_role_file:
        for item in beta_role_file:
            print(f'{item}')

            guild = discord.utils.find(lambda g : g.id == ctx.guild, bot.guilds)
            member = discord.utils.find(lambda m : m.id == item, ctx.guild.members)

            if role is not None:
                if member is not None:
                    await member.add_roles()
                    print(f'{role} added to {member}')
                
                else:
                    print(f'Member not found.')
            else:
                print(f'Role not found.')
