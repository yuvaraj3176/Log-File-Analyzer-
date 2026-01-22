import random
from datetime import datetime

def generate_log_file(path, lines=50000):
    methods = ["GET", "POST", "PUT"]
    errors = ["200", "404", "500", "403"]

    with open(path, "w") as f:
        for _ in range(lines):
            if random.random() < 0.02:
                f.write("INVALID LOG ENTRY\n")
                continue

            log = f"{datetime.now()} {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)} {random.choice(methods)} {random.choice(errors)}\n"
            f.write(log)
