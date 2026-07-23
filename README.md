# Password Strength Checker 🔒

A simple Python script designed to evaluate the strength of a user-provided password based on security best practices (length, digits, uppercase letters, and special characters).

---

## 🚀 Features

- **Length Check:** Ensures the password has at least 8 characters.
- **Digit Detection:** Verifies the presence of numbers using `isdigit()`.
- **Uppercase Detection:** Checks for uppercase letters using `isupper()`.
- **Symbol Detection:** Scans for special characters using `string.punctuation`.
- **Scoring System:** Evaluates total criteria met (0-4) and classifies the password as **Weak**, **Medium**, or **Strong**.

---

## 🛠️ Concepts & Technologies Used

- **Python 3**
- `string.punctuation` for symbol validation
- List comprehensions with `any()` for efficient character checks
- Basic scoring and conditional logic (`if` / `elif` / `else`)

---

## ⚙️ How to Run

1. Make sure you have Python installed.
2. Clone or download this repository.
3. Open your terminal or IDE (e.g., Pydroid 3, VS Code).
4. Run the script:

```bash
python main.py
