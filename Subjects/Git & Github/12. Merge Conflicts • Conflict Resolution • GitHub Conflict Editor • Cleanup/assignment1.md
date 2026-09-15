### Assignment 1 – Create and Resolve a Merge Conflict on GitHub (Mandatory)

**Goal:** Create a real conflict with two feature branches and resolve it using the GitHub browser editor.

1. Create/clone a repository and on `main` create `tasks.txt`:

```text
My Tasks
1. Study Git
2. Complete assignment
3. Review notes
```

2. Commit and push to `main`.
3. Create branch `feature/tasks-A` → change line 3 to `Practice merge conflicts` → commit → push → open PR (do **not** merge yet).
4. Switch back to `main`, create branch `feature/tasks-B` → change line 3 to `Watch Git tutorial` → commit → push → open second PR.
5. Merge the first PR successfully.
6. Merge the second PR → conflict appears.
7. Resolve the conflict on GitHub:
   - Understand Current vs Incoming
   - Decide final text (keep one, both, or write your own)
   - Remove all conflict markers
   - Mark as resolved → Commit merge → Merge the PR
8. Delete both remote feature branches.
9. Update local main and delete local branches:
   ```bash
   git checkout main
   git pull origin main
   git branch -D feature/tasks-A
   git branch -D feature/tasks-B
   ```

**Submit:**
- Repository link
- Screenshot of the conflict editor (showing markers)
- Screenshot of the successfully merged second PR
- Screenshot of `git log --oneline` after pull

**Answers:**

**Github Repo Link**

https://github.com/adityakatariya-a/day-12-assignment-1.git


**Screeshots**

<img width="1438" height="898" alt="Screenshot 2026-09-10 215406" src="https://github.com/user-attachments/assets/b6e47c93-75cc-42c8-a177-a93383013334" />

<img width="1438" height="898" alt="Screenshot 2026-09-10 215513" src="https://github.com/user-attachments/assets/99ec0e64-8bb3-4a58-ba47-5a7e634d3f9f" />

<img width="1535" height="862" alt="Screenshot 2026-09-10 215924" src="https://github.com/user-attachments/assets/bfd9fb18-8662-4e6c-ae64-58b32df39601" />
