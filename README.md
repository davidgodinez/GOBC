# Summarizer
"Project Overview: The Garden Oaks Baptist Church app facilitates automation of sermon summaries. It streamlines the process of condensing sermons into key messages, which are then distributed via mid-week emails to the congregation."

***

## Setup
To configure the summarizer, several steps are necessary.

### VSCode

Be sure to install VSCode. This is your code editor and will be place you interact with the codebase. 
Use the following [link](https://code.visualstudio.com/download) for download the software package. 

Be sure to install necessary extensions such as pylance, and other python suggestions. These will usually be suggested by VSCode.

```

You can run VS Code from the terminal by typing 'code' after adding it to the path: Launch VS Code. Open the Command Palette (Cmd+Shift+P) and type 'shell command' to find the Shell Command: Install 'code' command in PATH command.

```

### Poetry

On a system level, it's important to have poetry installed which can be done following the directions found in this [link](https://python-poetry.org/docs/#installing-with-the-official-installer).

Be sure to add poetry in your path. To do this you can access your `~./zshrc` and have the following:

`export PATH="$HOME/.poetry/bin:$PATH"`

After installing poetry, in the terminal you need to initialize a poetry shell, this is a virtual environment that will isolate the dependencies used for this program. This can be done with the command
`poetry shell`.

Once a shell has been initialized, you will need to install your dependencies, necessary external scripts for your program to run accurately. This can be done by running the command `poetry install`.

*** 

## Credentials

Be sure to create a file called `credentials.json` inside the root directory. This file will have the following content:

```
{
    "OPENAI_KEY": "<openai_api_key>"
}

```

## Installation / Running the Application

Once the setup is completed and all dependencies are installed, you can run the application by following these steps:

1. Place the Word file you want to summarize in the `files` directory.
2. Execute the `gui.py` script. You do this by running the following command: 
`poetry run python gui.py`

3. The application will open in a new window. Click on the "Summarize Message" button to generate a summary of the most recent file placed in the `files` directory.

4. The summarized text will be saved in a new file in the `summarized_files` directory.

***

## Project Structure

Here's a brief explanation of the project structure:

- `gui.py`: This script provides a graphical user interface for the summarizer application.
- `text_summarizer.py`: This script handles the summarization of Word files.
- `files`: This directory is where you should place the Word files you want to summarize.
- `summarized_files`: This directory is where the summarized text files are stored.
