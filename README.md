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
4. Saves the session (date, duration, activity type, language) into `statistics.db`
5. Shows the total time per activity for a chosen period (today, last week, or all time) in the statistics menu

## ⚠️ Current limitations

- **The statistics output is raw.** Totals per activity are printed as a plain dictionary, in seconds. There is no formatting and no list of recent sessions yet.
- **The language is hardcoded.** Every session is saved with the language `English`; there is no way to choose a language yet.
- **Error handling is partial.** Errors while creating the database and saving a session are handled (the session data is shown on screen if it could not be saved). Errors while reading statistics are not handled yet, so the program may crash with an unhandled exception.
- **No migration for old databases.** The `language` column was added to the table recently. If you have a `statistics.db` from an earlier version, delete it so the app can create a new one.
- **Console only.** No GUI or web interface yet.

## 🚀 Launch

```bash
python linguametrics.py
```

A `statistics.db` file will be created automatically in the current directory on first launch.

## Requirements

- Python 3.10+ (uses the `match` statement)
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

- [x] Add the `language` column to the database
- [x] Add error handling for saving sessions and creating the database
- [x] Show totals per activity for today, the last week, and all time
- [ ] Format the statistics output (readable table, time in minutes/hours)
- [ ] Show the list of recent sessions
- [ ] Add error handling for reading statistics
- [ ] Add language selection
- [ ] Add tests (`pytest`)
- [ ] Improve the console prototype (clearer formatting, input validation polish)
- [ ] Build a website

## 📄 License

MIT