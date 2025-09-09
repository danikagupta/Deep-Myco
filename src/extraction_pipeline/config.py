import os
from dataclasses import dataclass

@dataclass
class Settings:
    data_dir: str = os.getenv("MYCO_DATA_DIR", "./data")
    openai_key: str | None = os.getenv("OPENAI_API_KEY")
    serpstack_key: str | None = os.getenv("SERPSTACK_API_KEY")
    model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    max_input_tokens: int = int(os.getenv("MAX_INPUT_TOKENS", "100000"))

settings = Settings()

def require(name: str, value: str | None):
    if not value:
        raise RuntimeError(f"Missing required setting: {name}")
    return value
