import os

import constants
from lib import repo_list


def init():
    if not os.path.exists(constants.PUREPKG_PATH):
        os.makedirs(constants.PUREPKG_PATH)

    if not os.path.exists(constants.PUREPKG_REPOLIST_PATH):
        with open(constants.PUREPKG_REPOLIST_PATH, "w") as f:
            f.write("\n")
            f.close()

        repo_list.init()
