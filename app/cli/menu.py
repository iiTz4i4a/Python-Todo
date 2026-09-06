import questionary
def run_menu():
    return questionary.select("Select Action: ",choices=["Add Task","Remove Task","Change Title","Change Description","Complete Task","Exit"]).ask()


