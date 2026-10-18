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
5. Shows the total time per activity for a chosen period (today, the last seven calendar days, or all time)
6. Formats durations as readable hours, minutes, and seconds
7. Displays the last three sessions that match the selected period

## ⚠️ Current limitations

- **The statistics table can break on long time values.** Large duration strings may make the columns uneven.
- **The language is hardcoded.** Every session is saved with the language `English`; there is no way to choose a language yet.
- **Error handling is partial.** Errors while creating the database and saving a session are handled. Errors while reading statistics are caught by `show_statistics()`, but the message is generic. An error while closing a connection may also hide the original error.
- **Invalid periods are not checked inside the database functions.** The menus restrict the user's choice, but `load_period_totals()` and `load_latest_sessions()` do not explicitly handle an unexpected period value.
- **The week filter uses calendar dates.** It includes today and the previous six calendar days; it is not an exact rolling 168-hour period because sessions store only the date in `YYYY-MM-DD` format.
- **No migration for old databases.** The `language` column was added after the initial table was created. If you have a `statistics.db` from an earlier version, delete it only if you do not need its data; otherwise, a schema migration is needed.
- **Test coverage is limited.** The current `pytest` tests cover `prompt_int_in_range()`; session creation and database operations are not covered yet.
- **Console only.** No GUI or web interface yet.

## 🚀 Launch

```bash
python linguametrics.py
```

A `statistics.db` file will be created automatically in the current directory on first launch.

## Requirements

- Python 3.10+ (uses the `match` statement)
- SQLite is bundled with Python via the standard `sqlite3` module — no installation needed
- `pytest` is needed to run the tests

## 🧪 Tests

Install `pytest` if it is not already installed:

```bash
python -m pip install pytest
```

Run the test suite from the project directory:

```bash
python -m pytest
```

The current tests cover valid input, boundary values, non-integer input, and out-of-range input for `prompt_int_in_range()`.

## 📁 Project structure

```
LinguaMetrics/
├── linguametrics.py       # main code
├── test_linguametrics.py  # pytest tests
├── statistics.db          # SQLite database (created at runtime)
├── .gitignore             # what not to push to Git
├── README.md              # this file
└── LICENSE
```

## 🗺 Plans

- [x] Add the `language` column to the database
- [x] Add error handling for saving sessions and creating the database
- [x] Show totals per activity for today, the last seven calendar days, and all time
- [x] Format durations for readable statistics output
- [x] Show the three most recent sessions for the selected period
- [x] Handle SQLite errors while loading statistics
- [x] Correct the weekly filter to cover seven calendar dates
- [x] Add initial tests for `prompt_int_in_range()`
- [ ] Fix table alignment for long time values
- [ ] Handle errors while closing database connections without masking the original error
- [ ] Validate period values inside the statistics functions
- [ ] Remove duplicated period-filter logic
- [ ] Add tests for session creation and database operations using a temporary database
- [ ] Add language selection
- [ ] Add a migration for existing databases
- [ ] Further polish the console prototype (formatting and input validation)
- [ ] Build a website

## 📄 License

MIT
