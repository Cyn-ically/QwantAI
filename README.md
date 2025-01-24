# QwantAI

QwantAI is a Python library that provides an easy-to-use interface for interacting with the Qwant search engine. You can use it to perform searches and retrieve results either as a single text or streamed data in real time via WebSocket.

---

## Important information

- The AI feel like being French only, so if you are looking for something good (Already don't use this) and you have to put fr_FR (Default value)
- You can still try, but less result will work for any other language
## Features

- Perform searches on Qwant using a simple Python function.
- Retrieve results in your preferred language.
- Choose between streamed real-time output or a single consolidated response.
- Lightweight and easy to integrate into any project.

---

## Installation

Install QwantAI using `pip` (once packaged):

```bash
pip install QwantAI
```

If you're developing locally, clone the repository and install it directly:

```
git clone https://github.com/ramona-flower/QwantAI.git
cd QwantAI
pip install .
```

Usage
Import the package and start searching:

# Non-Streamed Example
- Retrieve all results as a single text response.

```py
import QwantAI

response = QwantAI.search("Python programming", language="en_US", streamed=False)
print(response)
```

# Streamed Example
- Retrieve results in real-time as they are generated.

```py
import QwantAI

QwantAI.search("Python programming", language="en_US", streamed=True)
```

# Parameters
search(query, language="en_US", streamed=False)

| Parameter | Type   | Description                                                   | Default  |
|-----------|--------|---------------------------------------------------------------|----------|
| query     | str    | The search query string.                                      | Required |
| language  | str    | The language for the search (e.g., en_US).                   | en_US    |
| streamed  | bool   | Whether to stream results or fetch them all at once.          | False    |

Requirements
```
Python 3.6+
requests (for HTTP requests)
websocket-client (for WebSocket communication)
```
Install dependencies with:

```
pip install -r requirements.txt
```

# Disclaimer
This project is provided for educational and informational purposes only. The creator of this package is not responsible for any misuse or damages caused by using this tool. Users are responsible for ensuring their usage complies with applicable laws and regulations.

# Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

Fork the repository.
Create a feature branch: ```git checkout -b feature-name```

Commit your changes: ```git commit -m 'Add new feature'```

Push to the branch: ```git push origin feature-name```
Open a pull request.

# License
This project is licensed under the Apache 2.0 License. See the LICENSE file for more information.

# Acknowledgments
Special thanks to the Qwant search engine for providing a robust API.
