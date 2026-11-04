
from datetime import datetime, timezone
from pathlib import Path
import re

now = datetime.now(timezone.utc)
year = now.year

start = datetime(year, 1, 1, tzinfo=timezone.utc)
end = datetime(year + 1, 1, 1, tzinfo=timezone.utc)

percent = (now - start).total_seconds() / (end - start).total_seconds() * 100

length = 30
filled = round(length * percent / 100)
bar = "█" * filled + "░" * (length - filled)

section = f"`{bar}` **{percent:.2f}%**"

path = Path("README.md")
content = path.read_text(encoding="utf-8")

pattern = r"(<!-- YEAR_PROGRESS_START -->).*?(<!-- YEAR_PROGRESS_END -->)"

updated, count = re.subn(
    pattern,
    lambda m: f"{m.group(1)}\n  {section}\n  {m.group(2)}",
    content,
    flags=re.DOTALL
)

if count != 1:
    raise RuntimeError(f"Expected 1 marker pair, found {count}")

path.write_text(updated, encoding="utf-8")

print(f"Updated: {year} is {percent:.2f}% over.")
print(f"Progress bar: [{bar}]")
