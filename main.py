#!/usr/bin/env python

"""
Main cli or app entry point
"""

from mylib.calculator import add
import click


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers together

    Example:
        ./main.py add 1 2
    """

    click.echo(click.style(str(add(a, b)), fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
