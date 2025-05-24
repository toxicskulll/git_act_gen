import random
import subprocess
import os

if random.random() < 0.4: #currently has 40% chance to make a commit on start
    print("🎯 Running bat file...")
    subprocess.run(["run_commits.bat"], shell=True)
else:
    print("🛑 Skipping this round.")
