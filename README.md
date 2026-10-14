<div align="center">

# LinguaMetrics

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-embedded-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Under%20active%20development-red.svg)

</div>

> LinguaMetrics is a timer application that counts how much time the user spends on a particular activity while learning a language.

## 📖 About the project

LinguaMetrics is a tool for people who want to learn a language through immersion. It measures how much time the user spends on various activities (e.g., listening, reading, viewing) and saves each session into a local SQLite database so progress can be tracked over time.

At the moment, LinguaMetrics is a **console prototype** in active development. It currently:

1. Asks the user for the type of activity (listening, reading, or viewing)
2. Waits for the user to press **Enter** to start the timer and **Enter** again to stop it
3. Calculates how much time the user spent on the activity
4. Saves the session (date, duration, activity type) into `statistics.db`

## ⚠️ Current limitations

- **The statistics menu is empty.** Sessions are stored, but there is no way to view them from inside the app yet.
- **No error handling for database failures.** If `statistics.db` cannot be opened or written to, the program will crash with an unhandled exception.
- **Console only.** No GUI or web interface yet.

## 🚀 Launch

```bash
python linguametrics.py
```

A `statistics.db` file will be created automatically in the current directory on first launch.

## Requirements

- Python 3.10+ (uses dict | dict merge syntax)
- SQLite is bundled with Python via the standard sqlite3 module — no installation needed

## 📁 Project structure

```
LinguaMetrics/
├── linguametrics.py       # main code
├── statistics.db          # SQLite database (created at runtime)
├── .gitignore             # what not to push to Git
├── README.md              # this file
└── LICENSE
```

## 🗺 Plans

- [ ] Implement the statistics menu (totals per activity, recent sessions)
- [ ] Add per-day and per-week breakdowns
- [ ] Add error handling for database failures
- [ ] Improve the console prototype (clearer formatting, input validation polish)
- [ ] Build a website

## 📄 License

MIT