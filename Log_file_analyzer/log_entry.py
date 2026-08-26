from dataclasses import dataclass
import time

@dataclass
class LogEntry():
    timestamps: str
    log_level : str
    message: str

