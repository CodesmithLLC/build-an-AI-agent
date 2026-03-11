# Build An AI Agent 🤖

This repository is the contains the code used in the workshop so that, even if you haven't learned Python yet, you can code along and develop a high-level understanding of the process. We highly encourage you to take your time, pick the code apart, and unpack what's going on under the hood as well.

## Link to the workshop 🔗

👉 [**Code along with the workshop on YouTube**](https://www.youtube.com/watch?v=_dbXrBxq_SQ&t=5435s)

## How it all works ⚙️

Everything you need to run this workflow is already included.
Each file works as is but if you’d like to follow along step-by-step with Will Sentance during the workshop, you can:

Remove the code from each file.

Use the code_store.txt file as your guide.

Add code back in section by section as you go.

This approach helps you build a mental model of how each piece connects, even if you’re still getting comfortable with Python. 🚀

## API Key and URL 🔑

To make this project fully functional, you’ll need two pieces of information:

Your OpenAI API key (used in extract_event.py to describe screenshots).

Your Google Apps Script Web App URL (used in create_event.py to create Google Calendar events).

💡 Note: For security, never store sensitive keys directly in your code.
During the workshop, we hardcode them for simplicity — but in a real-world project, you should use environment variables (.env files or your system’s environment settings).

Before committing or pushing to GitHub, remove any hardcoded API keys or URLs! 🔒

## Folder structure 🗂️

```
build-an-AI-agent/
code_store.txt          # Contains code snippets to follow along with the workshop
screenshot_agent.py     # Watches for new screenshots and triggers the workflow
extract_event.py        # Sends screenshots to OpenAI to extract event details
create_event.py         # Sends extracted event data to Google Apps Script
screenshot_agent.log    # Records events, errors, and process updates
```

### Note on Python packages 🐍

If you encounter an error when running the project that looks like:

 ```text
ModuleNotFoundError: No module named 'requests'
```

it likely means the requests package is not installed in the Python environment that is running the script.

You can install it by running:

```bash
/usr/bin/python3 -m pip install requests
```

In essence, whichever Python interpreter is running your .py files needs to have the requests package installed on it. The command above installs requests for the system Python interpreter located at /usr/bin/python3.

This installs the package directly into your system’s Python environment for simplicity, so you can focus on understanding how the AI agent works rather than managing Python environments.

In larger or production projects, developers typically use virtual environments to isolate dependencies and avoid conflicts between projects.

If you’d like to remove the package later, you can uninstall it with:

```bash
/usr/bin/python3 -m pip uninstall requests
```

### VS Code Interpreter Note 📝

You may also encounter issues if VS Code is not using the same Python interpreter that you installed the package on.

Make sure you have the Python extension installed in VS Code.

#### Then:

```
Press Cmd + Shift + P to open the Command Palette (Ctrl + Shift + P on Windows)

Type Python: Select Interpreter

Select /usr/bin/python3
```
This ensures VS Code runs your scripts using the same interpreter where the requests package was installed.

Happy coding!
