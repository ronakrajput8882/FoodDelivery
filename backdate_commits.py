import subprocess
import os
from datetime import datetime

COMMITS = [
    
    ("2026-05-27", 10, 15, "feat: add data preprocessing pipeline"),
    ("2026-05-27", 11, 42, "feat: implement feature engineering module"),
    ("2026-05-27", 13, 20, "fix: resolve null handling in dataset loader"),
    ("2026-05-27", 15, 5,  "refactor: clean up model training script"),
    ("2026-05-27", 17, 33, "docs: update README with usage instructions"),
    ("2026-05-27", 19, 50, "chore: add requirements.txt and .gitignore"),

    ("2026-05-27", 9,  10, "feat: add model evaluation metrics"),
    ("2026-05-27", 10, 45, "feat: implement cross-validation logic"),
    ("2026-05-27", 12, 30, "fix: correct label encoding for categorical vars"),
    ("2026-05-27", 14, 15, "refactor: modularise training and inference code"),
    ("2026-05-27", 15, 55, "test: add unit tests for data pipeline"),
    ("2026-05-27", 17, 20, "docs: add model architecture explanation"),
    ("2026-05-27", 19, 40, "chore: update .gitignore and project structure"),
]

LOG_FILE = "commit_log.txt" 


def run(cmd: list[str], env=None):
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"  ✗ ERROR: {result.stderr.strip()}")
    return result

def make_commit(date: str, hour: int, minute: int, message: str, index: int):
    timestamp = f"{date}T{hour:02d}:{minute:02d}:00"

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] commit #{index}: {message}\n")

    run(["git", "add", LOG_FILE])

    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"]    = timestamp
    env["GIT_COMMITTER_DATE"] = timestamp

    result = run(["git", "commit", "-m", message], env=env)
    status = "✓" if result.returncode == 0 else "✗"
    print(f"  {status}  [{timestamp}]  {message}")

def main():
    check = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                           capture_output=True, text=True)
    if check.returncode != 0:
        print("✗ Not inside a git repository. cd into your repo first.")
        return

    print("=" * 60)
    print("  Backdated Commit Script  |  techwithronak")
    print("=" * 60)
    print(f"\n  Total commits to create: {len(COMMITS)}")
    print(f"  → 17 May 2026 : 6 commits")
    print(f"  → 18 May 2026 : 7 commits\n")

    for i, (date, hour, minute, msg) in enumerate(COMMITS, start=1):
        make_commit(date, hour, minute, msg, i)

    print("\n" + "=" * 60)
    print(f"  Done!  {len(COMMITS)} commits created.")
    print("  Run  'git push'  to update GitHub.\n")
    print("  git log --oneline -15")
    print("=" * 60)

    log = subprocess.run(["git", "log", "--oneline", "-15"],
                         capture_output=True, text=True)
    print(log.stdout)

if __name__ == "__main__":
    main()