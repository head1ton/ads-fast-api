import time


def get_current_linux_timestamp() -> str:
    return str(int(time.time() * 1000))
