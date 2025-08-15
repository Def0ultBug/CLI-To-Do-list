import json
import os
import click

__all__ = ["create", "read","update","delete","search"]


@click.command()
@click.argument("title")
@click.option("--content",prompt=True,help="Content of the title")
@click.option("--tags", help="Comma-separated list of tags")
@click.pass_context
def create(ctx : click.Context,title:str, content:str, tags:str)->None:
    todo_dir = ctx.obj["todo_dir"]
    todo_name = f"{title}.json"
    if (todo_dir / todo_name).exists():
        click.echo(f"Note {todo_name} already exists")
        exit(1)
    note_data = {
        "content": content,
        "tags" : tags.split(",") if tags else [],
    }
    with open(todo_dir / todo_name, "w") as f:
        json.dump(note_data, f)
    click.echo(f"Note '{title}' created.")

@click.command()
@click.argument("title")
@click.pass_context
def read(ctx:click.Context,title:str):
    todo_dir = ctx.obj["todo_dir"]
    todo_name = f"{title}.json"
    if not (todo_dir / todo_name).exists():
        click.echo(f"Note '{title}' does not exist")
        exit(1)
    with open(todo_dir / todo_name, "r") as f:
        todo_data = json.load(f)
        click.echo(f"Note '{title}' read.")
    click.echo(f"Tags : {todo_data['tags']}.")
    click.echo(f"content : {todo_data['content']}.")

@click.command()
@click.argument("title")
@click.option("--content", help="New content of the todo")
@click.option("--tags", help="Comma-separated list of new tags")
@click.pass_context
def update(ctx:click.Context,title:str, content:str, tags:str)->None:
    todo_name = f"{title}.json"
    todo_dir = ctx.obj["todo_dir"]
    if not todo_dir/todo_name.exists():
        raise click.ClickException(f"Note '{title}' does not exist")
    with open(todo_dir/todo_name, "r") as f:
        todo_data = json.load(f)
    if tags:
        todo_data["tags"] = tags.split(",") if tags else []
    if content:
        todo_data["content"] = content
    with open(todo_dir/todo_name, "w") as f:
        json.dump(todo_data, f)
        click.echo(f"Note '{title}' updated.")


@click.command()
@click.argument("title")
@click.pass_context
def delete(ctx:click.Context,title:str)->None:
    todo_dir = ctx.obj["todo_dir"]
    todo_name = f"{title}.json"
    if not (todo_dir / todo_name).exists():
        raise click.ClickException(f"Note '{title}' does not exist")
    os.remove(todo_dir / todo_name)
    click.echo(f"Note '{title}' deleted.")


@click.command()
@click.option("--tag", help="Filter notes by tag")
@click.option("--keyword", help="Search notes by keyword")
@click.pass_context
def search(ctx:click.Context,tag:str, keyword:str)->None:
    todo_dir = ctx.obj["todo_dir"]
    todos = [ todo for todo in os.listdir(todo_dir) if todo.endswith(".json")]
    res :list[str] = []
    for name in todos:
        with open(todo_dir / name, "r") as f:
            todo_data = json.load(f)
        tags = [t.lower() for t in todo_data.get("tags", [])]
        content = todo_data.get("content", "").lower()
        tag_match = tag.lower() in tags if tag else True
        keyword_match = keyword.lower() in content if keyword else True
        if tag_match and keyword_match:
            res.append(name.replace(".json", ""))
    click.echo(f"{len(res)} notes found.")
    for r in res:
        click.echo(f"- {r}")


