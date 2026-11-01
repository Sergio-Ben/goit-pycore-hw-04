import sys
from pathlib import Path

from colorama import Fore, Style, init

INDENT = "    "


def print_directory(path: Path, level: int = 0):
    indent = INDENT * level
    print(f"{indent}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")

    try:
        items = sorted(path.iterdir(), key=lambda item: item.name.lower())
    except PermissionError:
        print(f"{indent}{INDENT}{Fore.RED}[немає доступу]{Style.RESET_ALL}")
        return

    for item in items:
        if item.is_dir():
            print_directory(item, level + 1)
        else:
            print(f"{indent}{INDENT}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python {sys.argv[0]} <шлях до директорії>{Style.RESET_ALL}")
        sys.exit(1)

    path = Path(sys.argv[1]).resolve()

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path}' не існує{Style.RESET_ALL}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією{Style.RESET_ALL}")
        sys.exit(1)

    print_directory(path)


if __name__ == "__main__":
    main()
