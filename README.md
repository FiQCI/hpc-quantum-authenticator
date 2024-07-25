# About this site

This is the repository showing the proposed authentication for Quantum computers on HPCs

## Getting Started

To get a copy of this project up and running on your local machine for testing and development, you would need to have a minimum of the listed prerequisites installed on your local machine.

### Prerequisites

You must have

1. Python3 and pip. Run `python -v` in your terminal to confirm that you have them installed

2. GIT and Bash

### Installation

To get started, clone this repository on your local machine using the following steps:

```bash

git clone <repository-url>
```

Open your terminal and navigate to the repository folder and and create a virtual environment. A simple way to do this using pip is:

```bash

python3 -m venv .venv
```

```bash

. .venv/bin/activate
```
After creating the environment, the next step is to install packages that the project will use:

```bash

python3 -m venv .venv
```

## Starting the dev server

```bash
flask run
```

## Documentation 

The api is documented with postman and the documentation can be found here [Documentation](https://documenter.getpostman.com/view/14860523/2sA3kXFgkB)