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
  - I used claude code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  -The AI found that clicking New Game after losing didn’t reset status to "playing", so the game stayed stuck on “Game over.”

How I verified it: I wrote a pytest test that checks the status, attempts, history, and new secret number reset correctly. The test passed.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  -: The AI added extra tests I didn’t ask for, which caused 3 failures and made the results confusing.

What I changed: I told it to only test my two bugs. It reduced the file to two tests: one for the hint bug and one for New Game after a loss.

How I verified it: I ran python -m pytest tests and got 2 passed with no failures. Each test matches a bug in my bug log.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  -considered a bug fixed when it no longer happened in the situation where I found it. I wrote a pytest test for each bug and checked for the correct results. I ran python -m pytest tests and both tests passed. I also verified that the buggy code was actually changed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  -I ran test_guess_of_one_is_told_to_go_higher, which checks that check_guess(1, 100) returns "Go HIGHER". The test passed after the fixes. I also learned the bug had two causes: string conversion and swapped hint messages, so the test checks the actual message.


- Did AI help you design or understand any tests? How?
  -Yes. AI helped me understand what each test should check and how to recreate the bugs. It also helped me make sure the tests matched the specific issues I found.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  -I learned that Streamlit reruns the whole program whenever you interact with the app. Session state is what keeps things like the score, attempts, and game status from resetting every time. The New Game bug helped me understand why resetting the right state values is important.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

------

Habit to reuse: I’ll keep logging bugs and writing tests that recreate them before fixing them.
What I’d do differently: I’ll be more specific with AI about exactly what I want it to change.
How this changed my thinking: I learned that I can’t just trust AI-generated code. I still need to test it myself because AI can miss bugs or give incomplete explanations.
