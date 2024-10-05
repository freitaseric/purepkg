from lib import repo_list


class Repository:
    def __init__(self, codename: str, region: str, url: str, description=None) -> None:
        self.codename = codename
        self.description = description
        self.region = region
        self.url = url

    def __str__(self) -> str:
        return f"Repository({self.codename}): {self.url}\nRegion: {self.region}  Description: {self.description}  Domain: {self.get_domain()}"

    def get_domain(self) -> str:
        domain = self.url.split("https://")[1]
        domain = domain.replace("www.", "")
        domain = domain.split("/")[0]

        return domain
