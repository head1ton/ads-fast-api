from pathlib import Path

from pydantic import BaseConfig


class ENV(BaseConfig):
    LOCAL: str = "local"
    DEV: str = "dev"
    BETA: str = "beta"
    LIVE: str = "live"


BASE_DIR: str = Path(__file__).resolve().parent.parent


_env = ENV()
