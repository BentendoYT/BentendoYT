
from datetime import datetime, timezone
from pathlib import Path

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

start_marker = "<!-- YEAR_PROGRESS_START -->"
end_marker = "<!-- YEAR_PROGRESS_END -->"

before, remainder = content.split(start_marker, 1)
_, after = remainder.split(end_marker, 1)

content = before + start_marker + "\n  " + section + "\n  " + end_marker + after

path.write_text(content, encoding="utf-8")
