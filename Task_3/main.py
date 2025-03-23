from pathlib import Path
from typing import Generator
from collections import defaultdict


def load_logs(file_path: str) -> Generator[str]:
    try:
        absolute_path = Path(file_path).absolute()
        with open(absolute_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                parse_line = parse_log_line(line.strip())
                yield parse_line
    except Exception as e:
        print(e)


def parse_log_line(line: str) -> dict:
    list_pars = defaultdict(list)
    parse_line = line.split(" ")

    # parse_line = line.split(" ")
    # a = Counter(parse_line)
    # print(f" Counter ", a)
    # return parse_line


# print(load_logs("./goit-pycore-hw-05/Task_3/error.txt"))

for log_entry in load_logs("./goit-pycore-hw-05/Task_3/error.txt"):
    print(f"         ", log_entry)


# def filter_logs_by_level(logs: list, level: str) -> list:
#     pass


# def count_logs_by_level(logs: list) -> dict:
#     pass


# def display_log_counts(counts: dict):
#     pass
