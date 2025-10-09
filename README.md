# Build An AI Agent 🤖

## Welcome to the source code for Codesmith's workshop on Building an AI Agent!

This repository is the contains the code used in the workshop so that, even if you haven't learned Python yet, you can code along and develop a high-level understanding of the process. We highly encourage you to take your time, pick the code apart, and unpack what's going on under the hood as well.

## Link to the workshop 🔗

👉 [**Code along with the workshop on YouTube**](https://www.youtube.com/watch?v=_dbXrBxq_SQ&t=5435s)

## How it all works ⚙️

Everything you need to run this workflow is already included.
Each file works as is but if you’d like to follow along step-by-step with Will Sentence during the workshop, you can:

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

workshop-build-ai-agent/
code_store.txt          # Contains code snippets to follow along with the workshop
screenshot_agent.py     # Watches for new screenshots and triggers the workflow
extract_event.py        # Sends screenshots to OpenAI to extract event details
create_event.py         # Sends extracted event data to Google Apps Script
screenshot_agent.log    # Records events, errors, and process updates

Happy coding! 