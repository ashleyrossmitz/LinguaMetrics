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
5. Shows the total time per activity for a chosen period (today, the last week, or all time)
6. Formats durations as readable hours, minutes, and seconds
7. Displays the last three sessions that match the selected period

## ⚠️ Current limitations

- **The statistics table can break on long time values.** Large duration strings may make the columns uneven.
- **The language is hardcoded.** Every session is saved with the language `English`; there is no way to choose a language yet.
- **Error handling is partial.** Errors while creating the database and saving a session are handled, but errors while reading statistics are not handled yet. An error while closing a connection may also hide the original error.
- **Invalid periods are not checked inside the database functions.** The menus restrict the user's choice, but `load_period_totals()` and `load_latest_sessions()` do not explicitly handle an unexpected period value.
- **The week filter uses a date cutoff.** Sessions store the date as `YYYY-MM-DD`, without the time of day, so the filter does not represent an exact rolling seven-day period.
- **No migration for old databases.** The `language` column was added after the initial table was created. If you have a `statistics.db` from an earlier version, delete it only if you do not need its data; otherwise, a schema migration is needed.
- **Console only.** No GUI or web interface yet.
- **No automated tests yet.** The main scenarios are not covered by a `pytest` test suite.

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
- [x] Format durations for readable statistics output
- [x] Show the three most recent sessions for the selected period
- [ ] Fix table alignment for long time values
- [ ] Handle errors while reading statistics and closing database connections
- [ ] Validate period values inside the statistics functions
- [ ] Remove duplicated period-filter logic
- [ ] Add language selection
- [ ] Add a migration for existing databases
- [ ] Add tests (`pytest`)
- [ ] Further polish the console prototype (formatting and input validation)
- [ ] Build a website

## 📄 License

MIT
