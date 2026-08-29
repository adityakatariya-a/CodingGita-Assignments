### Assignment 1 
**Conflict during `git pull`**

**Goal:** Face and resolve a conflict that appears when you run `git pull origin main`.

1. On GitHub (remote `main`), create a file `welcome.txt` with the content:  
   `Welcome to Git class`
2. Commit it directly on GitHub.
3. On your **local main**, create the same file `welcome.txt` with different content:  
   `Welcome to Day 13`
4. Run:
   ```bash
   git add welcome.txt
   git commit -m "Add welcome.txt locally"
   git pull origin main
   ```
5. A conflict will appear. Resolve it by keeping **both** lines (or any final version you prefer).
6. Remove all conflict markers, then:
   ```bash
   git add welcome.txt
   git commit -m "Resolve pull conflict in welcome.txt"
   git push origin main
   ```

**Submit:**
- Screenshot of the conflict markers
- Screenshot of the final resolved file on GitHub
- Repository link

**Answers:**

**Repo link**

https://github.com/adityakatariya-a/day-13-assignment-1.git

**Screenshots**

<img width="1532" height="862" alt="Screenshot 2026-08-29 171409" src="https://github.com/user-attachments/assets/5c1eb09a-572b-488f-a5bb-3aa894ba1c5e" />

<img width="1438" height="898" alt="Screenshot 2026-08-29 171630" src="https://github.com/user-attachments/assets/d5961506-5272-430b-9a18-27c4169f3ca3" />






