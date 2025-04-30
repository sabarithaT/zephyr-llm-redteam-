# Zephyr LLM Redteam

This project is a basic red teaming test setup for a simulated LLM-based app, using Python.

## Files Included

- **helpers.py**: Contains the `ZephyrApp` class with mock methods to simulate a chatbot (`chat()` and `reset()`).
- **zephyr_redteam_test.py**: A script that runs red team-style prompts against the `ZephyrApp` to test its responses.

## How to Run

1. Clone the repo or download the files.
2. Open a terminal in the project directory.
3. Run the test script using:

```bash
python zephyr_redteam_test.py
