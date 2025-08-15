import tools
import click
from config import TODO_DIR,load_config
from pathlib import Path
import config_commands

@click.version_option()
@click.group()
@click.pass_context
def todo(ctx:click.Context)->None:
    config = load_config()
    todo_dir = config.get("todo_dir", TODO_DIR)
    ctx.ensure_object(dict)
    ctx.obj["config"] = config
    ctx.obj["todo_dir"] = Path(todo_dir)

@todo.group()
def tool():
    pass
'''
tool.add_command(tools.create) # use it like this : python myapp.py tools create "title" "content" "tags"
tool.add_command(tools.read) # use it like this : python myapp.py tools read "title"
tool.add_command(tools.update)
tool.add_command(tools.delete) # use it like this : python myapp.py tools delete "title"
tool.add_command(tools.search)
'''

for name in tools.__all__:
    cmd = getattr(tools,name)
    tool.add_command(cmd)


@todo.group()
def config():
    pass

config.add_command(config_commands.create) # use it like this : python myapp.py config create
config.add_command(config_commands.show) # use it like this : python myapp.py config read "todo_dir"
config.add_command(config_commands.update)

if __name__ == "__main__":
    todo()









