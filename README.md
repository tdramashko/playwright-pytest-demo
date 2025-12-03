# Python QA Unit Test Demo (Calculator Class)

This repository contains a simple, working example of Python unit testing using the standard `unittest` framework. It is designed to demonstrate proficiency in core Python programming, test structure, and exception handling for a QA role.
The project contains two main files:
* `app.py`: The application logic (a `Calculator` class) that contains methods to be tested.
* `test_app.py`: The unit test suite utilizing `unittest.TestCase` to verify the logic.
  ## ⚙️ Setup and Execution

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd python-qa-project
   ```
2. **Run Tests:** Use the Python `unittest` module runner:
   ```bash
   python -m unittest test_app.py
   ```
The execution should confirm **4 tests ran successfully**.
## ✨ Technical Highlights (What is being tested)

* **Unit Test Structure:** Proper use of the `unittest.TestCase` class.
* **Setup/Teardown:** Utilization of `setUp()` and `tearDown()` methods to ensure test isolation.
* **Positive Assertions:** Verification of correct output using `self.assertEqual()`.
* **Negative Testing:** Asserting that the correct exception is raised using **`self.assertRaises(ValueError)`** when dividing by zero.
