from rich.console import Console
from rich.table import Table

def show_tasks(tasks):
    table = Table(title="Todo-List")

    table.add_column("Task ID", justify="center", style="blue", no_wrap=True)
    table.add_column("Task Title", style="magenta")
    table.add_column("Task Description", style="magenta")
    table.add_column("Created At", justify="center", style="cyan", no_wrap=True)
    table.add_column("Status", justify="right", style="green")
    
    for task in tasks:
        # table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
        table.add_row(f"{task.id}",f"{task.title}",f"{task.description}",f"{task.created_at.strftime("%Y-%m-%d %H:%M")}",f"{'✓ done' if task.completed else '✗ pending'}")

    console = Console()
    console.print(table)

