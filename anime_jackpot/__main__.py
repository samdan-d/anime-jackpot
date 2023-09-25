import typer

from anime_jackpot import cli, __app_name__


def main():
    typer.run(cli.options)
    cli.app()


if __name__ == '__main__':
    main()

# import typer
#
# app = typer.Typer()
#
#
# @app.command()
# def hello(name: str):
#     print(f"Hello {name}")
#
# e
# @app.command()
# def goodbye(name: str, formal: bool = False):
#     if formal:
#         print(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         print(f"Bye {name}!")
#
#
# if __name__ == "__main__":
#     app()
