import re
import logging

LOG_PATTERN = re.compile(
    r"(?P<timestamp>.+?) (?P<ip>\d+\.\d+\.\d+\.\d+) (?P<method>\w+) (?P<status>\d+)"
)

def parse_logs(file_path):
    parsed_data = []
    total_requests = 0

    with open(file_path, "r") as file:
        for line in file:
            total_requests += 1
            match = LOG_PATTERN.match(line.strip())
            if match:
                parsed_data.append(match.groupdict())
            else:
                logging.warning(f"Malformed log skipped: {line.strip()}")

    return parsed_data, total_requests
