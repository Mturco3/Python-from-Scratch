# Python Learning Journal

**Michele Turco**

My collection of notes, notebooks, exercises, and small experiments as I learn Python. Topics range from language basics to data analysis, visualization, APIs, databases, and machine learning. I update this repository as I explore new concepts and revisit older ones.

## Theory

Concept notes with code examples, organized by topic.

| Topic | What is here |
| --- | --- |
| [Basics](Theory/Basics/) | Regular expressions, checking library availability, and the `if __name__ == "__main__"` pattern |
| [Iterators and generators](Theory/Iterators_Generators/iterators_and_generators.ipynb) | `iter()`, `next()`, exhaustion, `yield`, and lazy processing; no external packages or datasets |
| [Comprehensions](Theory/Comprehensions/comprehensions.ipynb) | List, set, and dictionary comprehensions, filtering, conditional expressions, nesting, and lazy generator expressions |
| [Pandas](Theory/Pandas/) | DataFrames, indexing, filtering, updating data, grouping, and survey analysis |
| [Visualization](Theory/Visualization/) | Matplotlib and Seaborn examples using Iris data |
| [API requests](Theory/API_Requests/) | HTTP requests, query parameters, JSON responses, and weather data |
| [Databases](Theory/Databases/) | SQL queries with SQLite, MySQL connections, and data exploration |
| [Embeddings](Theory/Embeddings/) | Sentence embeddings and text similarity with Sentence Transformers and cosine similarity |

## Exercises

- [Python](Exercises/Python/): general Python practice notebooks.
- [Pandas](Exercises/Pandas/): data manipulation exercises.
- [Scikit-learn](Exercises/Scikit/): machine learning exercises.
- [Interview practice](Exercises/Interviews/): small programming challenges and solutions.

These are learning materials at different stages of completion. Some notebooks contain unfinished exercises or depend on local files and services.

## Running the examples

Use Python 3. From the repository root, a basic script can be run directly:

```sh
python Theory/Basics/if_name_main/script1.py
```

For notebooks, create an environment:

```sh
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in PowerShell, or `source .venv/bin/activate` on macOS/Linux, then install and start JupyterLab:

```sh
python -m pip install jupyterlab
python -m jupyterlab
```

The [iterators and generators notes](Theory/Iterators_Generators/iterators_and_generators.ipynb) contain examples that run entirely offline once Jupyter is installed.

Install additional packages for the specific topics:

| Topic | Install command |
| --- | --- |
| Data analysis, visualization, and Scikit-learn exercises | `python -m pip install numpy pandas matplotlib seaborn scikit-learn` |
| API requests | `python -m pip install requests` |
| MySQL | `python -m pip install mysql-connector-python pandas` |
| Text embeddings | `python -m pip install sentence-transformers scikit-learn` |

SQLite support comes with Python; the SQLite notebook also imports Pandas. The MySQL examples require a configured server. API examples need internet access, and the embeddings example downloads a model on its first run.
