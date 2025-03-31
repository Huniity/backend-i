import typer
from session_9.bot import run_bot
import os

token = os.getenv('DISCORD_TOKEN', None)

app = typer.Typer()

@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run_bot(token)

if __name__ == "__main__":
    app(token)