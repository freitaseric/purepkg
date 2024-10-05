import argparse

from repository_manager import RepositoryManager


def install_subcommand(args):
    print(f"Subcommand: {args.subcommand}\nAll args: {args}")


def run(repository_manager: RepositoryManager):
    print(f"{repository_manager}")

    parser = argparse.ArgumentParser(
        description="A simple and fast universal package manager."
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    install_subcommand_parser = subparsers.add_parser(
        "install", help="Install or update a package."
    )
    install_subcommand_parser.set_defaults(func=install_subcommand)

    args = parser.parse_args()

    if args.subcommand:
        args.func(args)
    else:
        parser.print_usage()
