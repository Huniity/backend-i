import typer
import os

app = typer.Typer()

@app.command()
def createsuperuser(username: str, email: str, password: str):
    """
    Create a Django superuser via Typer CLI.
    """
    os.system(f'echo "from django.contrib.auth import get_user_model; '
              f'User = get_user_model(); '
              f'User.objects.create_superuser(\'{username}\', \'{email}\', \'{password}\')" | python manage.py shell')

if __name__ == "__main__":
    app()