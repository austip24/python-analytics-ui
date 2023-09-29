# Getting Started

You will need Python 3.11 get started. I am using pipenv to install python-based dependencies. You will also need Node.js to make use of Tailwind. The latest supported (v18+) version will work just fine. There will NOT be a Node.js server hosting the app. Node.js is used solely for development purposes with styling. To get started, clone this repository to the device/machine you want to run the application on.

## Installation

### Languages / Tools

1. Install [Python 3.11](https://www.python.org/downloads/). Make sure that Python has been added to your system path so that you can make use of the `pip` executable. If you are installing Python from the link, there will be an option to include Python in your system path early on in the installation process.
2. Install [Node.js](https://nodejs.org/en). The latest version will work just fine.
3. To check that you have everything set up properly, open a terminal of your choice and run the following commands. The result of each command should be a version number. If you get an error indicating that the command is not found, then you need to add the respective executable to your system path.

```bash
# these are included by installing Python
pip --version
python --version

# these are included by installing Node
node --version
npm --version
```

### Environment Setup

If you are familiar with Python already, you can set up a virtual environment however you want. If not, here are the steps needed to set up an environment with [pipenv](https://pypi.org/project/pipenv/).

1. Install pipenv with the following command:

```bash
pip install --user pipenv
```

2. Navigate to your project's directory (see Directory Structure 'Root'). You should see Pipfile and Pipfile.lock files. These files list out the dependencies for the app.
3. Run the following command to create a new virtual environment with the dependencies installed:

```bash
pipenv install
```

4. Now, you are ready to run the application.

### Running the Application

To run the application, you will need two terminals open. One for the python script, and one for the node script (this is used in development to create a real-time stylesheet of TailwindCSS' output).

1. Navigate to the 'Root' directory (see Directory Structure) below in BOTH terminals.
2. In one terminal, run the following command to start the Dash app. This assumes you have already set up a virtual environment using pipenv. If not, you will have to run the script using whatever way is required with the method you used to create a virtual environment.

```bash
pipenv run python app.py
```

3. In the other terminal, run the following command to execute the Tailwind script.

```bash
npm run tailwind-watch
```

4. Your application should now be running with hot-reloading available for both Dash and Tailwind. Navigate to the URL specified in the terminal used to execute the Python/Dash script.

## Directory Structure

Have a look at the app's directory structure below to understand the purpose of each file.

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
├─ 📄requirements.txt
├─ 📄README.md
└─ 📄tailwind.config.js   # tailwind configuration. you can add/extend utility classes here
```
