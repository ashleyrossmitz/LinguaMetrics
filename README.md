div align="center">

# LinguaMetrics

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Under%20active%20development-red.svg)

</div>

> LinguaMetrics is a timer application that counts how much time the user spends on a particular activity while learning a language.

## 📖 About the project

LinguaMetrics is a tool for people who want to learn a language through immersion. It measures how much time the user spends on various activities (e.g., listening, reading, viewing) and is intended to eventually save this data into statistics where you can track your progress.

At the moment, LinguaMetrics is the **first console prototype** in active development. It currently:

1. Asks the user for the type of activity (listening, reading, or viewing)
2. Waits for the user to press **any key** to start the timer and **any key** again to stop it
3. Calculates how much time the user spent on the activity
4. Prints the session data (date, duration, activity type) to the console

## ⚠️ Current limitations

- **Saving is not implemented yet.** `save_stats()` and `load_stats()` are stubs, and the statistics menu is empty. Session data is only printed to the console and is lost when the program exits.
- **Windows only.** The program uses `msvcrt.getch()`, which is only available on Windows. It will fail on Linux/macOS.
- No input validation yet — entering a non-numeric value in the menu will raise a `ValueError`.

## 🚀 Launch

```bash
python linguametrics.py
```

## Requirements

- Python 3.10+
- Windows OS (due to the use of msvcrt)


## 📁 Project structure

```
LibguaMetrics/
├── linguametrics.py       # main code
├── .gitignore             # what not to push to Git
├── README.md              # this file
└── LICENSE
```

## 🗺 Plans

□ Improve the console prototype
    □ Add input validation
    □ Implement save_stats() and load_stats()
    □ Implement the statistics menu
    □ Make input cross-platform (drop msvcrt)
    □ Move statistics storage to SQLite
□ Build a website

## 📄 License

MIT