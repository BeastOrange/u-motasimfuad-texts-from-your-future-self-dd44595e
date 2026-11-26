import os
import sys
from pathlib import Path

ENTRY_TEXT: str = (
    "Do NOT agree to watch your sister's ferret for 'just the weekend.' "
    "It is 2031, he has power of attorney, and I am not allowed on the good sofa."
)


def main() -> None:
    # Print the line to stdout
    print(ENTRY_TEXT)

    # Write to local output/entry.txt
    local_path = Path("output/entry.txt")
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text(f"{ENTRY_TEXT}\n", encoding="utf-8")

    # Attempt to write to /output/entry.txt if that path exists or parent exists
    try:
        root_path = Path("/output/entry.txt")
        if root_path.parent.is_dir():
            root_path.write_text(f"{ENTRY_TEXT}\n", encoding="utf-8")
    except Exception:
        pass

    # Support optional custom output destination if ENTRY_OUTPUT is provided
    custom_target = os.environ.get("ENTRY_OUTPUT")
    if custom_target:
        try:
            target_path = Path(custom_target)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(f"{ENTRY_TEXT}\n", encoding="utf-8")
        except Exception:
            pass


if __name__ == "__main__":
    main()
