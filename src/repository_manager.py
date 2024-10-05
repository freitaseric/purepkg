from lib import repo_list


class RepositoryManager:
    def __init__(self) -> None:
        self.repositories = repo_list.parse()

    def __str__(self) -> str:
        for repo in self.repositories:
            print(f"{repo}")

        return ""
