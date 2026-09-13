## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

**Answers:**

<img width="1535" height="862" alt="Screenshot 2026-09-13 162742" src="https://github.com/user-attachments/assets/003d259b-b5a2-4aa3-b013-6ea2e3583ca0" />


<img width="1535" height="862" alt="Screenshot 2026-09-13 162805" src="https://github.com/user-attachments/assets/9044e2b2-d302-4680-8198-3b5a4631e8df" />

<img width="1535" height="862" alt="Screenshot 2026-09-13 162820" src="https://github.com/user-attachments/assets/24333392-c855-4c57-ba5f-0ad5e7190018" />

<img width="1535" height="862" alt="image" src="https://github.com/user-attachments/assets/07721be0-ffe6-4784-90fd-596d92561dbf" />

**repo link**

https://github.com/adityakatariya-a/day-15-assignment-3.git
