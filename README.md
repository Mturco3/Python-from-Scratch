# Python Learning Journal

**Michele Turco**

My collection of notes, notebooks, exercises, and small experiments as I learn Python. Topics range from language basics to data analysis, visualization, APIs, databases, and machine learning. I update this repository as I explore new concepts and revisit older ones.

## Theory

Concept notes with code examples, organized by topic.

### Basics

| Topic | What is here |
| --- | --- |
| [Objects, expressions, variables](Theory/Basics/01_objects_expressions_variables.ipynb) | Python fundamentals |
| [Strings and I/O](Theory/Basics/02_strings_and_io.ipynb) | String operations and input/output |
| [Branching](Theory/Basics/03_branching.ipynb) | Conditionals and control flow |
| [Loops](Theory/Basics/04_loops.ipynb) | For and while loops |
| [Functions, scope, modules](Theory/Basics/05_functions_scope_modules.ipynb) | Defining functions, scope rules, imports |
| [Lists](Theory/Basics/06_lists.ipynb) | List operations and methods |
| [Comprehensions](Theory/Basics/07_comprehensions.ipynb) | List, set, dictionary comprehensions, filtering, and generator expressions |
| [Iterators and generators](Theory/Basics/08_iterators_and_generators.ipynb) | `iter()`, `next()`, exhaustion, `yield`, and lazy processing |
| [if \_\_name\_\_ == "\_\_main\_\_"](Theory/Basics/if_name_main/) | Module execution pattern |
| [Check library](Theory/Basics/check_library.py) | Check whether a Python library is installed |

### Libraries

| Topic | What is here |
| --- | --- |
| [Regex](Theory/Libraries/Regex/regex.ipynb) | Patterns, quantifiers, groups, and methods using the `re` module |
| [Pandas](Theory/Libraries/Pandas/) | DataFrames, indexing, filtering, updating data, grouping, and survey analysis |
| [Visualization](Theory/Libraries/Visualization/) | Matplotlib and Seaborn examples using Iris data |

### Topics

| Topic | What is here |
| --- | --- |
| [API requests](Theory/API_Requests/) | HTTP requests, query parameters, JSON responses, and weather data |
| [Databases](Theory/Databases/) | SQL queries with SQLite, MySQL connections, and data exploration |
| [Embeddings](Theory/Embeddings/) | Sentence embeddings and text similarity with Sentence Transformers and cosine similarity |

## Exercises

- [Python](Exercises/Python/): general Python practice notebooks.
- [Pandas](Exercises/Pandas/): data manipulation exercises.
- [Scikit-learn](Exercises/Scikit_Learn/): machine learning exercises.
- [Interview practice](Exercises/Interviews/): small programming challenges and solutions.

These are learning materials at different stages of completion. Some notebooks contain unfinished exercises or depend on local files and services.

## Running the examples

Use Python 3. From the repository root, a basic script can be run directly:

```sh
python Theory/Basics/if_name_main/script1.py
```

For notebooks, create an environment and install dependencies:

```sh
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in PowerShell, or `source .venv/bin/activate` on macOS/Linux, then install:

```sh
pip install -r requirements.txt
pip install jupyterlab
jupyter lab
```

SQLite support comes with Python; the SQLite notebook also imports Pandas. The MySQL examples require a configured server. API examples need internet access, and the embeddings example downloads a model on its first run.
