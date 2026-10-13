<div align="center">

# LinguaMetrics

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Under%20active%20development-red.svg)

</div>

> LinguaMetrics is a timer application that counts how much time the user spends on a particular activity while learning a language.

## 📖 About the project

LinguaMetrics is a tool for people who want to learn a language through immersion. It measures how much time the user spends on various activities (e.g., listening, reading, viewing) and is intended to eventually save this data into statistics where you can track your progress.

At the moment, LinguaMetrics is the **first console prototype** in active development. It currently:

1. Asks the user for the type of activity (listening, reading, or viewing)
2. Waits for the user to press **Enter** to start the timer and **Enter** again to stop it
3. Calculates how much time the user spent on the activity
4. Prints the session data (date, duration, activity type) to the console

## ⚠️ Current limitations

- **Saving is not implemented yet.** `save_stats()` and `load_stats()` are stubs, and the statistics menu is empty. Session data is only printed to the console and is lost when the program exits.

## 🚀 Launch

```bash
python linguametrics.py
```

## Requirements

- Python 3.10+

## 📁 Project structure

```
LibguaMetrics/
├── linguametrics.py       # main code
├── .gitignore             # what not to push to Git
├── README.md              # this file
└── LICENSE
```

## 🗺 Plans

- [ ] Improve the console prototype
- [ ] Implement save_stats() and load_stats()
- [ ] Implement the statistics menu
- [ ] Move statistics storage to SQLite
- [ ] Build a website

## 📄 License

MIT