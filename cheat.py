"""
Github Commit Cheater
2015
"""

import sys
from datetime import date, timedelta
import os


def print_usage(scriptname):
    print("USAGE:")
    print("$ python3 " + scriptname + " <num_of_past_days>")
    print()


def cheat(num):
    today = date.today()
    for n in range(num):
        cheatday = today - timedelta(days=n)
        cheatday = str(cheatday) + " 0:0:0"
        os.system(change_date(cheatday) +
                  commit('cheating'))
    os.system(push())


def change_date(cheatday):
    export_author_date = "export GIT_AUTHOR_DATE='" + cheatday + "'; "
    export_commit_date = "export GIT_COMMITTER_DATE='" + cheatday + "'; "
    return export_author_date + export_commit_date


def commit(msg):
    return "git commit -m '" + msg + "' --allow-empty; "


def push():
    return "git push origin master; "


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage(sys.argv[0])
        sys.exit()
    try:
        cheat(int(sys.argv[1]))
    except ValueError:
        print("Wrong Argument!")
        print_usage(sys.argv[0])
        sys.exit()
