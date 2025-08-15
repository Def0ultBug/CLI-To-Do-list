import click
from config import TODO_DIR,CONFIG,load_config,save_config

@click.command()
def create():
    """Create a new config file"""
    config = load_config()
    save_config(config)
    click.echo(f"New config file created.")

@click.command()
def show():
    """show a config file"""
    if not  CONFIG.exists():
        click.echo("Config not found.")
        exit(1)
    config = load_config()
    click.echo(f"To-Do dir {config.get('todo_dir',TODO_DIR)}")

@click.command()
@click.option("--todo-dir","-n",type=click.Path(exists=True))
def update(todo_dir:str):
    """update The Path/location of the todo file on the Config file"""
    config = load_config()
    config["todo_dir"] = todo_dir
    save_config(config)
    click.echo(f"Config updated.")