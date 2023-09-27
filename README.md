# Getting Started

You will need Python 3.11 get started. I am using pipenv to install python-based dependencies. You will also need Node.js to make use of Tailwind. The latest supported (v18+) version will work just fine. There will NOT be a Node.js server hosting the app. Node.js is used solely for development purposes with styling.

## Directory Structure

Have a look at the app's directory structure below to understand the purpose of .

```
Root
├─ 📁src   # contains application code
│  ├─ 📁assets  # contains styles and any static files/images
│  │  ├─ 📁css
│  │  │  ├─ 📁dist  # this only exists if you execute the Tailwind script
│  │  │  └─ 📁src
│  │  │     └─ 📄input.css   # Tailwind input
│  │  └─ 📁static
│  ├─ 📁components  # contains components of the app (sidebar, graphs, etc.)
│  ├─ 📁pages   # contains the pages/routes of the app
│  └─ 📁utils   # utilities used throughout the app
│     ├─ 📄constants.py
│     ├─ 📄funcs.py
├─ 📄.gitignore
├─ 📄app.py           # main executable for script
├─ 📄package-lock.json
├─ 📄package.json
├─ 📄Pipfile
├─ 📄Pipfile.lock
├─ 📄README.md
└─ 📄tailwind.config.js
```

## Installation

TODO

## Running the App

TODO
