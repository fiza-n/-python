from pathlib import Path
from contextlib import contextmanager
from log_entry import LogEntry


@contextmanager
def read_file(destination):
    f = open(destination, "r")
    try: 
        yield f
    finally:
        f.close()

base_dir = Path(__file__).resolve().parent
with read_file(base_dir / "log_file.txt") as f:
    for line in f:
        print(line)


def parse_lines(lines):
    for line in lines:
        parts = line.split(" ", 3)
        if len(parts) == 4:
            date,time,  message, log_level = parts
            timestamps = f"{date} { time}"
            yield LogEntry(timestamps.strip(), message.strip(), log_level.strip())
        else:
            print(f"Skipped malformed line: {line!r}")

parser = parse_lines(open(base_dir / "log_file.txt"))
