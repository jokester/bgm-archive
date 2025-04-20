import click
from .validate_archive import validate_archive


@click.group()
def cli():
    """Bangumi Archive CLI tools."""
    pass


# Register commands
cli.add_command(validate_archive)


if __name__ == "__main__":
    cli()
