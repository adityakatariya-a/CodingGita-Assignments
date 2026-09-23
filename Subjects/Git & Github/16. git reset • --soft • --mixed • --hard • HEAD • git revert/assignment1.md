## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

**Answers:**

**Github Repo Link**

https://github.com/adityakatariya-a/day-16-assignment-1.git



**Screenshot of `git log --oneline` **before** reset**

<img width="1535" height="862" alt="Screenshot 2026-09-23 184435" src="https://github.com/user-attachments/assets/0154f8e5-34c8-4d89-b07b-f3289faa2a28" />

**Screenshot of `git log --oneline` and `git status` **after** reset**

<img width="1535" height="862" alt="Screenshot 2026-09-23 184721" src="https://github.com/user-attachments/assets/a6461ef0-1440-4fe1-b7a3-6ab084cc0c8d" />
