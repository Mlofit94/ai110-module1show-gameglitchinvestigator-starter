# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Bugs I found:

Guessing 1 gave the wrong hint because the secret number was converted to text.
New Game didn't work after losing because the status wasn't reset.
The secret number could be outside the selected difficulty range.
The higher/lower hints were swapped.

Fixes I applied:

Fixed number comparisons and hint messages.
New Game now resets the game correctly and uses the proper difficulty range.
Moved game logic into logic_utils.py.
Added two pytest tests for my logged bugs. Both pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start Normal mode with secret 55.
2. Guess 40 - “Go HIGHER,” score -5.
3. Guess 70 - “Go LOWER,” score -10.
4. Guess 55 - Win, final score 40.
5. Try guessing again - game says you already won.
6. Click New Game - everything resets and a new secret number is chosen.
 
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
