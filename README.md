# 💸 Expense Tracker CLI App

A simple command-line **Expense Tracker** built in Python using **SQLite3**. This app lets you add, view, and summarize your personal expenses by category and date. Lightweight, fast, and perfect for practicing real-world Python with persistent data storage.

---

## 📦 Features

- Add new expenses with:
  - Amount
  - Predefined category
  - Optional note
  - Custom or current date
- View all expenses
- Filter expenses by:
  - Category
  - Date range
- Summarize total spending:
  - Overall
  - By category
  - By date range
- Data stored locally using SQLite database (`expenses.db`)

---

## 📁 Project Structure

```
.
├── main.py          # Main application file
├── expenses.db      # (auto-created) SQLite database
└── README.md
```

---

## 🛠️ Requirements

- Python 3.x  
- No external dependencies required (uses built-in `sqlite3` and `datetime`)

---

## ▶️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker-cli.git
   cd expense-tracker-cli
   ```

2. **Run the app**:
   ```bash
   python main.py
   ```

3. **Follow the prompts** to:
   - Add new expenses
   - View history
   - Get summaries

---

## 📊 Categories

Predefined categories include:
- Food
- Transport
- Rent
- Utilities
- Entertainment
- Health
- Shopping
- Other

You can expand these in `CATEGORIES` in the source code.

---

## 📌 TODO (Future Enhancements)

- [ ] Export to CSV
- [ ] Monthly trend graphs
- [ ] Edit/delete expense entries
- [ ] Switch to Tkinter or Flask for GUI/web interface
- [ ] Add budget limits and warnings

---

## 🧠 Learning Goals

This project was created to practice:
- SQL database handling in Python
- Clean command-line UX
- Structured data input/validation
- Grouping, filtering, and summarizing real data

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Thanks to the Python open-source community and all learners building alongside me. Feel free to fork and improve!
