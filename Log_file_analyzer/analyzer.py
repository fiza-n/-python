from parser import parse_lines, read_file
from pathlib import Path

base_dir = Path(__file__).resolve().parent

with read_file(base_dir / "log_file.txt") as f:
    entries = list(parse_lines(f))


def count_error_log():
   
    return sum(1 for entry in entries if entry.log_level == "ERROR")

def get_Timestamps():
    return [entry.timestamps for entry in entries if entry.log_level == "ERROR"]

def get_message():
    return [entry.message for entry in entries if entry.log_level == "ERROR"]

error_count = count_error_log()
timestamps = get_Timestamps()
message = get_message()

print(f"Total number of ERROR logs: {error_count}")
print(f"Timestamps of ERROR logs: {timestamps}")
print(f"Message of ERROR logs: {message}")
