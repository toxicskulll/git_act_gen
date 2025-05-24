import subprocess
import random
import time
import os

FILE = "hello.txt" #set file name
BRANCH = "main" #change only if not using main by default

commit_messages = [ 
    "Updated hello.txt", "Small tweak", "Minor changes", "Added content",
    "Routine update", "Another update", "More data", "Fixing file"
] #change commit message as required

num_commits = random.randint(0, 8)
print(f"Making {num_commits} commits...")

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
    else:
        if result.stdout:
            print(f"{result.stdout.strip()}")
        else:
            print("✅ Command executed.")

# ✅ Pull latest changes to avoid rejection
run_command(f"git pull origin {BRANCH} --rebase")

for i in range(num_commits):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"Update {i+1}: {random.randint(1000,9999)}\n")

    msg = random.choice(commit_messages)
    run_command("git add hello.txt")
    run_command(f'git commit -m "{msg} ({i+1}/{num_commits})"')
    time.sleep(0.9)

run_command(f"git push origin {BRANCH}")
print("All commits pushed!")
