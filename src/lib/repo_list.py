import constants
from repository import Repository


def init():
    with open(constants.PUREPKG_REPOLIST_PATH, "w") as f:
        f.write(constants.INITIAL_REPOLIST)


def parse():
    repositories = []

    with open(constants.PUREPKG_REPOLIST_PATH, "r") as f:
        data = f.read()

        for repo in data.split("\n"):
            repositories.append(Repository(codename="", region="Brazil", url=repo))

    return repositories
