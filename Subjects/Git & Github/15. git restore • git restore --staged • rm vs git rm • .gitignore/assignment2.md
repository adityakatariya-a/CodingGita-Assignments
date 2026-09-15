## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

**Answers**


**screenshot of git status after rm and git rm**

<img width="1535" height="862" alt="Screenshot 2026-09-13 154905" src="https://github.com/user-attachments/assets/c14403b5-856b-470e-880f-dcbc50e91736" />

**difference between rm and git rm**

<img width="1535" height="862" alt="Screenshot 2026-09-13 155932" src="https://github.com/user-attachments/assets/9046f5c5-ed0e-436d-801a-929ab667ef09" />


**github repo link**

https://github.com/adityakatariya-a/day-15-assignment-1.git
