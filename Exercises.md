# Python Revival Skill  
This list is designed to progressively reactivate Python knowledge, moving from core syntax to concepts crucial for a professional environment.

Here is a curated list of exercises, from basic to advanced.

---

### Level 1: Syntax & Core Concepts Refresh
*Goal: Get the muscle memory for Python syntax back.*

1.  **Hello, Again!**
    *   Write a program that asks for the user's name and greets them. (e.g., "Hello, Alice!").

2.  **Basic Calculator**
    *   Write a script that takes two numbers and an operator (+, -, *, /) from the user and performs the calculation. Handle division by zero gracefully.

3.  **String Manipulation**
    *   Write a function that takes a string and returns:
        *   The string reversed.
        *   The string in all uppercase.
        *   The number of vowels in the string.

4.  **List Operations**
    *   Create a list of numbers. Write code to:
        *   Find the sum and average.
        *   Find the largest and smallest number.
        *   Create a new list with only the even numbers.

5.  **FizzBuzz (The Classic)**
    *   Print numbers from 1 to 100.
        *   For multiples of 3, print "Fizz".
        *   For multiples of 5, print "Buzz".
        *   For multiples of both 3 and 5, print "FizzBuzz".

---

### Level 2: Data Structures & Algorithms
*Goal: Practice problem-solving with common data structures.*

6.  **Word Counter**
    *   Write a function that counts the frequency of each word in a given string. Return a dictionary where keys are words and values are counts. Ignore case and punctuation.

7.  **List Overlap**
    *   Write a function that takes two lists and returns a new list that contains only the elements that are common between them (without duplicates).

8.  **Fibonacci Sequence**
    *   Write a function to generate the first N numbers in the Fibonacci sequence using both iterative and recursive approaches. Discuss the trade-offs.

9.  **Prime Checker**
    *   Write a function to check if a number is prime. Then, write a function to generate all prime numbers up to a number N (using the Sieve of Eratosthenes for a challenge).

10. **Palindrome Checker**
    *   Write a function that checks if a given string is a palindrome (ignoring spaces, punctuation, and case). (e.g., "A man, a plan, a canal, Panama!" returns True).

---

### Level 3: Object-Oriented Programming (OOP)
*Goal: Re-familiarize yourself with structuring code using classes, crucial for large projects.*

11. **Bank Account Class**
    *   Create a `BankAccount` class with attributes `owner` and `balance`.
    *   Implement methods `deposit(amount)` and `withdraw(amount)`. The `withdraw` method should not allow withdrawals that exceed the balance.
    *   Add a `__str__` method to print a user-friendly summary.

12. **Inheritance: Shapes**
    *   Create a base class `Shape` with a method `area()`.
    *   Derive classes `Rectangle` and `Circle` that inherit from `Shape` and implement their own `area()` methods.

13. **Library System**
    *   Create classes `Book`, `Author`, and `Library`.
    *   A `Book` belongs to an `Author` (use composition).
    *   The `Library` class should manage a collection of books with methods to `add_book(book)`, `remove_book(book)`, and `search_books(title="", author_name="")`.

---

### Level 4: Intermediate & Job-Readiness Concepts
*Goal: Practice with concepts you'll see daily in a professional setting.*

14. **File I/O & CSV Processing**
    *   Read a CSV file (e.g., `data.csv` with columns `Name`, `Age`, `City`).
    *   Calculate the average age.
    *   Find all people from a specific city.
    *   Write the results to a new text file. Use the `csv` module.

15. **API Consumption (Requests Library)**
    *   Use the `requests` library to fetch data from a public API (e.g., JSONPlaceholder: `https://jsonplaceholder.typicode.com/posts`).
    *   Print the titles of all posts.
    *   Handle potential errors (e.g., no internet, API not responding).

16. **List Comprehensions & Generators**
    *   Take the exercises from Level 1 (e.g., finding even numbers, squaring numbers) and rewrite them using list comprehensions.
    *   For a large range of numbers, create a generator expression to find even numbers instead of a list comprehension. Explain the memory difference.

17. **Error Handling & Logging**
    *   Take your "Basic Calculator" or "API Consumption" code.
    *   Wrap the risky parts in `try...except` blocks to handle specific exceptions (e.g., `ValueError`, `ZeroDivisionError`, `requests.exceptions.RequestException`).
    *   Use the `logging` module to log informative messages (debug, info, error) instead of just printing.

18. **Decorators**
    *   Write a decorator `timer` that measures the time a function takes to execute and prints it.
    *   Write a decorator `logger` that logs the arguments a function was called with and its return value.

---

### Level 5: Advanced & Real-World Simulation
*Goal: Tackle more complex problems that integrate multiple concepts.*

19. **Simple Web Scraper (BeautifulSoup)**
    *   Use `requests` and `BeautifulSoup` to scrape the headlines from a news website (please check the site's `robots.txt` first!).
    *   Store the headlines and their links in a structured format (e.g., a list of dictionaries, a CSV file).

20. **CLI Tool with `argparse`**
    *   Create a command-line tool that takes a word and a URL.
    *   The tool should fetch the web page and count how many times the word appears on it.
    *   Use the `argparse` module to handle command-line arguments cleanly.

21. **Context Managers**
    *   Create a custom context manager (using a class with `__enter__` and `__exit__`) that temporarily changes the current working directory, runs a block of code, and then changes back to the original directory.

22. **Data Analysis Basics (Pandas)**
    *   Install `pandas`.
    *   Read a CSV dataset (e.g., from Kaggle, like Titanic or Iris).
    *   Perform basic analysis: show head/tail, check for missing values, calculate mean/max/min of a column, filter data based on a condition (e.g., all passengers in 1st class).

23. **Mini-Project: To-Do List Manager**
    *   **Integrate multiple concepts:** Create a console-based to-do list manager.
    *   Use a class to represent a `Task`.
    *   Store tasks in a file (JSON or CSV) so they persist between runs.
    *   Implement functions to `add`, `view`, `complete`, and `delete` tasks.
    *   Use the `argparse` module to create a command-line interface for it (e.g., `todo.py add "Buy milk"`).

### Tips for Your Journey:

*   **Don't Just Code, Refactor:** After you get something working, go back. Can you make it more efficient? More readable? Can you use a more Pythonic feature (e.g., a list comprehension, a built-in function like `enumerate()`)?
*   **Version Control:** Use Git from the start. Make a repository for your exercises, commit your code after each exercise, and write good commit messages. This is a non-negotiable job skill.
*   **Read the Docs:** Get used to reading the official Python documentation to understand the tools you're using (`argparse`, `csv`, `requests`, etc.).
*   **Virtual Environments:** Use a virtual environment (e.g., `venv`) for exercises that require external libraries (Level 4+). This is a critical best practice.

Good luck with your practice! You'll be back up to speed in no time.