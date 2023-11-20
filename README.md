# Hightest Automation

## Table of Contents

- [Overview](#overview)
- [Scenario](#scenario)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Files](#files)
- [License](#license)

## Overview

The project involves the automation of a testing scenario to verify that a correctly filled ISTQB quiz on the [HighTest website](https://hightest.nc) results in an email indicating 100% correct answers.

## Scenario

1. Navigate to the HighTest website.
2. Click on the "Toolbox" link.
3. Access the ISTQB Foundation quiz in French.
4. Complete the quiz by selecting the correct answers and submit the test.
5. Enter a Yopmail email address on the next page and submit the form.
6. Go to Yopmail, check the emails, and verify that the received email indicates 100% correct answers.

## Installation

### Installing dependencies

Include any dependencies that need to be installed.

```bash
pip3 install -r requirements.txt
```

For get the list of your current dependencies.

```bash
pip3 freeze
```

### Installing Jupyter Notebook

If you don't have Jupyter Notebook installed, you can follow the installation guide:

- [Jupyter Notebook Installation Guide](https://jupyter.org/install)

## Usage

To execute the automated quiz script, run the `automate_quiz_ISTQB_FR.ipynb` Jupyter Notebook file. Make sure you have Jupyter Notebook installed on your system.

### Quick Start

Open `automate_quiz_ISTQB_FR.ipynb` with [Visual Studio Code](https://code.visualstudio.com)

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command:

```bash
jupyter notebook automate_quiz_ISTQB_FR.ipynb
```

## Dependencies

- Python 3.11.6
- selenium
- webdriver

## Files

- `automate_quiz_ISTQB_FR.ipynb`: Jupyter script for automating the ISTQB quiz.
- `report_quiz_ISTQB_FR.json`: Contains the results of the quiz execution.
- `reporting.py`: Module for generating success and error messages.
- `requirements.txt`: Contains the list of modules needed for the project.
- `yopmail.py`: Module for creating random email addresses and access to is mailbox.

## License

MIT License

Copyright (c) [2023] [Gauthier Rammault]

## To do list / Comment 

 * Attention les guidelines mentionnaient Selenium Java
 * ~~Les xPath pourrait être optimisés~~
 * Pareil pour la gestion des jeux de données (ici le couple question/réponse)
 * ~~En revue statique, je n'ai pas trouvé l'endroit où la vérification finale a lieu (résultats = 100%)~~