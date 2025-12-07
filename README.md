# Todo In-Memory Python Console App

## Project Overview
This project implements a simple command-line todo application that stores tasks in memory. It demonstrates basic CRUD (Create, Read, Update, Delete) operations and the ability to mark tasks as complete or incomplete.

## Features
- Add tasks with a title and an optional description.
- List all tasks with their status and details.
- Update the title and/or description of an existing task.
- Mark tasks as complete or pending.
- Delete tasks by their ID.

## Technology Stack
- Python 3.13+

## Setup and Run

### Prerequisites
- Python 3.13 or higher installed on your system.

### Installation
1. Clone the repository (if applicable):
   ```bash
   git clone <repository_url>
   cd In_Memory_Python_Console_App
   ```
2. Navigate to the project directory:
   ```bash
   cd In_Memory_Python_Console_App
   ```
3. Install dependencies (if any - for this phase, there are none):
   ```bash
   pip install -r requirements.txt
   ```

### How to Run
Execute the `main.py` file from the root of the project:
```bash
python main.py
```

### Usage
Once the application is running, you will see a `>` prompt. Type `help` to see the available commands.

#### Commands:
- `add`: Add a new todo. You will be prompted for a title and an optional description.
- `list`: List all current todos with their IDs, titles, descriptions, and statuses.
- `update`: Update an existing todo. You will be prompted for the todo ID and then for new title and description (leave blank to keep current).
- `complete`: Mark a todo as complete. You will be prompted for the todo ID.
- `pending`: Mark a todo as pending. You will be prompted for the todo ID.
- `delete`: Delete a todo. You will be prompted for the todo ID.
- `exit`: Exit the application.
- `help`: Display the list of available commands.

## Example Workflow

```
Welcome to the In-Memory Todo CLI!
Type 'help' for commands.
> add
Enter todo title: Buy groceries
Enter todo description (optional): Milk, eggs, bread
Added:
[ ] ID: <some-uuid> | Title: Buy groceries | Status: pending | Created: <timestamp>
    Description: Milk, eggs, bread
> add
Enter todo title: Finish report
Enter todo description (optional): Finalize Q3 earnings report
Added:
[ ] ID: <some-uuid> | Title: Finish report | Status: pending | Created: <timestamp>
    Description: Finalize Q3 earnings report
> list
[ ] ID: <some-uuid-1> | Title: Buy groceries | Status: pending | Created: <timestamp>
    Description: Milk, eggs, bread
[ ] ID: <some-uuid-2> | Title: Finish report | Status: pending | Created: <timestamp>
    Description: Finalize Q3 earnings report
> complete <some-uuid-1>
Marked complete:
[✓] ID: <some-uuid-1> | Title: Buy groceries | Status: completed | Created: <timestamp>
    Description: Milk, eggs, bread
> list
[✓] ID: <some-uuid-1> | Title: Buy groceries | Status: completed | Created: <timestamp>
    Description: Milk, eggs, bread
[ ] ID: <some-uuid-2> | Title: Finish report | Status: pending | Created: <timestamp>
    Description: Finalize Q3 earnings report
> delete <some-uuid-2>
Todo deleted.
> list
[✓] ID: <some-uuid-1> | Title: Buy groceries | Status: completed | Created: <timestamp>
    Description: Milk, eggs, bread
> exit
Exiting Todo CLI. Goodbye!
```

## Windows Users: WSL 2 Setup

If you are on Windows, it is highly recommended to use [WSL 2 (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) for development.

### Installation Steps:
1. **Install WSL 2:**
   ```bash
   wsl --install
   ```
2. **Set WSL 2 as default:**
   ```bash
   wsl --set-default-version 2
   ```
3. **Install Ubuntu (e.g., Ubuntu 22.04 LTS):**
   ```bash
   wsl --install -d Ubuntu-22.04
   ```
   After installation, you can open Ubuntu from your Start Menu and run your Python application within the Linux environment.
