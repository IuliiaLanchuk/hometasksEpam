import csv
import os

import django


def main():
    homeworks_completed = HomeworkResult.objects.all()
    with open("report.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
        writer.writerow(homeworks_completed)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_orm.project_orm.settings")

    django.setup()
    from project_orm.my_project.models import HomeworkResult

    main()
