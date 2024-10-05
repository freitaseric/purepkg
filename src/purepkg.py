import cli
from lib import app_setup
from repository_manager import RepositoryManager


def main():
    app_setup.init()

    repository_manager = RepositoryManager()

    cli.run(repository_manager)


if __name__ == "__main__":
    main()
