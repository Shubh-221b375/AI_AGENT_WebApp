from ai_api import get_plan  # Only import get_plan
from executor import execute_commands
from rich import print
from rich.console import Console
from rich.markdown import Markdown

console = Console()

class AIAgent:
    def start(self):
        console.print("\n[bold green]🤖 What task would you like the agent to perform?[/bold green]")
        task = input("> ")

        console.print("\n[bold cyan]🧠 Generating a plan using AI...[/bold cyan]")
        plan = get_plan(task)

        console.print("\n[bold magenta]📋 Here's the generated plan:[/bold magenta]")
        console.print(Markdown(plan))

        approve = input("\n[bold yellow]✅ Approve this plan? (y/n): [/bold yellow]").strip().lower()
        if approve == 'y':
            success = execute_commands(plan)
            if success:
                console.print("\n[bold green]🎉 Task completed successfully![/bold green]")
            else:
                feedback = input("\n[bold red]❌ Task failed. What went wrong?[/bold red]\n> ")
                console.print("\n[bold cyan]🔁 Unable to refine the plan. Task failed.[/bold cyan]")
        else:
            console.print("[bold red]🚫 Task cancelled by user.[/bold red]")
