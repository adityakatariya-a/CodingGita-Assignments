## Assignment 3 – Practice git revert (Medium)

**Goal:** Safely undo a commit using `git revert` instead of reset.

1. Make sure you have at least 2–3 commits on `main`.
2. Choose the latest commit and revert it:
   ```bash
   git revert HEAD
   ```
   (Save the commit message that Git opens)
3. Run:
   ```bash
   git log --oneline
   ```
4. Observe that a **new commit** was created (the history was not deleted).
5. write the short answers in your own words in your notebook:
   - What does `git revert` do?
   - How is it different from `git reset`?
   - When is `git revert` safer than `git reset`?

**Submit:**
- Screenshot of `git log --oneline` showing the revert commit
- Photos of written answers.
- Repository link