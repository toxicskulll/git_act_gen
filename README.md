# 🌀 Virtual Commit Generator (Windows Automation)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)](https://www.microsoft.com/windows/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Automation](https://img.shields.io/badge/Task-Scheduler%20Active-success)](#)

Automates **random commits** to a **private GitHub repo** using Python + Windows Task Scheduler. Useful for streak keeping, testing CI triggers, or learning automation workflows.

---

## 📸 Demo Screenshot

> 📅 Auto-trigger runs randomly through Windows Task Scheduler  
> 💻 Commits are pushed with messages like:
> `Updated hello.txt (2/5)` or `Routine update (4/7)`

![Task Scheduler Setup Screenshot](https://via.placeholder.com/800x400?text=Task+Scheduler+Setup)  
*You can replace this with your own screenshot for clarity.*

---

## 🔧 Features

- 📝 Randomized edits to a dummy file
- 🔀 Random number and message of commits
- ⏱️ 40% chance of triggering on each scheduled run
- 🔄 Git commit + push automation

---

## 🧰 File Breakdown

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `auto_committer.py` | Makes random commits and pushes to GitHub    |
| `auto_trigger.py`   | 40% chance to run the commit generator       |
| `run_commits.bat`   | Executes the Python committer script         |
| `hello.txt`         | Target file for dummy updates                |

---

## ⚙️ Setup Instructions

### 1. ✅ Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Git for Windows](https://git-scm.com/)
- Private GitHub repo already cloned locally
- Git is authenticated (via GitHub CLI, Credential Manager, or SSH)

---

### 2. 🛠 Initial Setup

```bash
git clone https://github.com/your-username/your-private-repo.git
cd your-private-repo

Update variables in auto_committer.py:
