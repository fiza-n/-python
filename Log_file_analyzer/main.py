# main.py
from pathlib import Path
from parser import parse_lines, read_file
from analyzer import count_error_log, get_Timestamps, get_message
from summarizer import summarize

base_dir = Path(__file__).resolve().parent

with read_file(base_dir / "log_file.txt") as f:
    entries = list(parse_lines(f))

stats = {
    "error_count": count_error_log(entries),
    "error_timestamps": get_Timestamps(entries),
    "error_messages": get_message(entries),
}

print(f"Total ERROR logs: {stats['error_count']}")
print(summarize(stats))
print("end")