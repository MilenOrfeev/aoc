import glob
import importlib


def run_all():
    task_files = glob.glob("task*")
    task_files.sort()

    for task_file in task_files:
        module_name = task_file[:-3]  # remove .py
        task_name = module_name.capitalize()
        task_name = task_name[0:-3] + " " + task_name[-3] + "." + task_name[-1]

        print('-' * 10 + task_name + '-' * 10)

        module = importlib.import_module(module_name)
        module.solve()
        print('-' * 28 + '\n\n')


if __name__ == "__main__":
    run_all()
