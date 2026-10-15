# akettunen copyright 2026

import argparse
import platform

import colorama
import psutil
import termcolor

colorama.init()

#change logo here
LOGO = [
    r" _______ ",
    r"|   |   |",
    r"|---|---|",
    r"|___|___|",
]

#logo size
LOGO_WIDTH = max(len(line) for line in LOGO) + 2

#check if windows
def is_win():
    return platform.system() == "Windows"

#host
def get_host():
    return platform.node()

#os
def get_os():
    if not is_win():
        return termcolor.colored("your os is not windows!", "yellow")
    return f"Windows {platform.release()} ({platform.version()})"

#memo
def get_memory():
    memory = psutil.virtual_memory()
    return f"{memory.total / (1024 ** 3):.2f} gb"

#disk
def get_disk():
    disk = psutil.disk_usage("/")
    return f"{disk.total / (1024 ** 3):.2f} gb"

#labels and results
def build_info():
    return [
        ("host:", get_host()),
        ("os:", get_os()),
        ("memory:", get_memory()),
        ("disk:", get_disk()),
    ]

#labels print cyan, results print as normal
def print_report(info):
    for i in range(max(len(LOGO), len(info))):
        left = LOGO[i] if i < len(LOGO) else ""
        label, value = info[i] if i < len(info) else ("", "")

        logo_part = termcolor.colored(f"{left:<{LOGO_WIDTH}}", "cyan")
        label_part = termcolor.colored(f"{label:<8}", "cyan")
        print(logo_part + label_part + value)

#commands
def main():
    parser = argparse.ArgumentParser(
        description=termcolor.colored(
            "mindows - a system information tool for windows.",
            "cyan",
            "on_black",
        )
    )
    parser.add_argument(
        "--issue",
        action="store_true",
        help="show how to contact the author about a problem",
    )
    args = parser.parse_args()

    if args.issue:
        print(termcolor.colored(
            "if you have an issue with mindows, contact me on discord or github:",
            "yellow",
        ))
        print(termcolor.colored("discord: @ak0101101", "magenta"))
        print(termcolor.colored(
            "github: https://github.com/akx25/mindows/issues",
            "black",
            "on_white",
        ))
        return

    print_report(build_info())


if __name__ == "__main__":
    main()
