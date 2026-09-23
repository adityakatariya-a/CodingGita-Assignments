## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Photos of written answers.
- Repository link

**Answers:**

**Github Repo Link:**

https://github.com/adityakatariya-a/day-16-assignments-2.git

**Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)**

<img width="1535" height="862" alt="Screenshot 2026-09-23 205614" src="https://github.com/user-attachments/assets/a2c9cae2-08a8-4685-ae0d-6d31f3842ba1" />

<img width="1526" height="862" alt="Screenshot 2026-09-23 205856" src="https://github.com/user-attachments/assets/68d48a66-cb2c-4024-bdc1-97f643c985eb" />

<img width="1535" height="862" alt="Screenshot 2026-09-23 210029" src="https://github.com/user-attachments/assets/1464765a-d2b0-4b44-a786-ec789f3ee185" />

**Photos of written answers**

<img width="720" height="1280" alt="WhatsApp Image 2026-09-23 at 9 29 43 PM" src="https://github.com/user-attachments/assets/7b42561e-bd05-47c8-bb81-d09b027f356c" />
