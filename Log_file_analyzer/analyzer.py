from parser import parse_lines, read_file
from pathlib import Path

base_dir = Path(__file__).resolve().parent

def count_error_log(entries):
    return sum(1 for entry in entries if entry.log_level == "ERROR")

def get_Timestamps(entries):
    return [entry.timestamps for entry in entries if entry.log_level == "ERROR"]

def get_message(entries):
    return [entry.message for entry in entries if entry.log_level == "ERROR"]

if __name__ == "__main__":
    with read_file(base_dir / "log_file.txt") as f:
        entries = list(parse_lines(f))
