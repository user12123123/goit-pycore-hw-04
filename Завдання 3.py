import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_tree(directory: Path, prefix: str = ""):
    """

    """
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda e: (e.is_file(), e.name.lower())
        )
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Немає доступу до {directory}]{Style.RESET_ALL}")
        return

    for entry in entries:
        if entry.is_dir():
            print(f"{prefix}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
            print_tree(entry, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: потрібно передати шлях до директорії.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії{Style.RESET_ALL}")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"{Fore.RED}Помилка: шлях '{target_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: '{target_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.BLUE}{Style.BRIGHT}{target_path.name}/{Style.RESET_ALL}")
    print_tree(target_path)


if __name__ == "__main__":
    main()