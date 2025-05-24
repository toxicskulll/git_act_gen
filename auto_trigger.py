import random
import subprocess
import os

# Chance to run the .bat file: 40% chance
if random.random() < 0.4:
    print("🎯 Running bat file...")
    subprocess.run(["run_commits.bat"], shell=True)
else:
    print("🛑 Skipping this round.")
