import sys
from pathlib import Path
from collections import defaultdict
from typing import List, Dict


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    try:
        absolute_path = Path(file_path).resolve()
        print(f"Absolute way for the current file: {absolute_path}")

        with open(absolute_path, "r", encoding="utf-8") as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Помилка: файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка під час зчитування файлу: {e}")
        sys.exit(1)
    return logs


def parse_log_line(line: str) -> Dict[str, str]:
    try:
        parts = line.split(" ", 3)
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3] if len(parts) > 3 else "",
        }
    except IndexError:
        print(f"Помилка розбору рядка: {line}")
        return {}


def filter_logs_by_level(
    logs: List[Dict[str, str]], level: str
) -> List[Dict[str, str]]:

    return [log for log in logs if log.get("level") == level.upper()]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:

    counts = defaultdict(int)
    for log in logs:
        if "level" in log:
            counts[log["level"]] += 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    print(f"{'Рівень логування':<15} | {'Кількість':<10}")
    print("-" * 27)
    for level, count in counts.items():
        print(f"{level:<15} | {count:<10}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу_логів> [<рівень_логування>]")
        sys.exit(1)

    # Зчитуємо аргументи командного рядка
    file_path = sys.argv[1]
    filter_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Завантажуємо логи
    logs = load_logs(file_path)

    # Підраховуємо кількість записів за рівнями
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо задано рівень логування, виводимо відповідні записи
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nДеталі логів для рівня '{filter_level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()


# python main.py ./error.txt
# python main.py ./error.txt error
