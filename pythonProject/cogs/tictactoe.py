import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@slash_command(description="Startet TicTacToe")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    print(f"{ctx.author.name} hat /tictactoe gemacht")
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Jetzt ist <@" + str(player1.id) + "> dran.")
        elif num == 2:
            turn = player2
            await ctx.send("Jetzt ist <@" + str(player2.id) + "> dran.")
    else:
        await ctx.send("Es wird greade gespielt warte bis das Spiel fertig ist!.")
    await ctx.respond(f"Es wurde erfolgreich TicTacToe gestartet", ephemeral=True)


@slash_command(description="Platziert ein Feld bei TicTacToe")
async def place(ctx, pos: int):
    print(f"{ctx.author.name} hat /place gemacht")
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Es ist gleichstand")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Bitte stelle sicher das du eine Zahl zwischen 1-9 eingibst.")
        else:
            await ctx.send("Du bist nicht am Zug.")
    else:
        await ctx.send("Starte mit ,tictactoe ein neues Spiel.")
    await ctx.respond(f'Zeichen wurde erfolgreich gesetzt')


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Trage bitte 2 Spieler ein (dich und deinen Gegner).")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(
            "Bitte gehe sicher das du die Person getaggt hast mit der du Spielen willst (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bitte gebe eine Position ein wo du dein x/o setzen willst.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bitte stelle sicher eine ganze Zahl einzugeben.")

def setup(bot):
    bot.add_cog(TicTacToe(bot))