# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | suspected area
|-------|-------------------|-----------------|------------------------|---------------|

1. | guess of 1| "go higher"|"go lower"| NA  |app.py, Bug: On even-numbered attempts, app.py:158-161 converts the secret number to a string. This makes guess > secret in check_guess() (app.py:37) raise a TypeError (int vs str), which falls into the except block (app.py:41-47) that compares the guess and secret as strings instead of numbers.

Effect: String comparison is lexicographic, not numeric — so "1" > "100" is False in Python. Guessing 1 gets told "Go LOWER" even though 1 is the minimum, because the code is comparing text, not values.|


2. |After attemps is run dry, New game does nothing | new game started | Nothing happens |app.py:134-138 — the new_game block resets attempts and secret but never resets status, combined with app.py:140-145 which checks status and calls st.stop() before a new game can begin.  |


3. |Diffulty range to easy |secret # between 1 and 20 |Secret is outside of range|app.py:136, This hardcodes the range to 1–100, ignoring the selected difficulty. So if you're on "Easy" (sidebar says range 1–20) or "Hard" (range 1–50), clicking New Game can still pick a secret number outside that displayed range — making the game unwinnable within the shown bounds. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
