import csv
import os


def main():
    homeworks_completed = HomeworkResult.objects.all()
    with open("report.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
        writer.writerow(homeworks_completed)


if __name__ == "__main__":
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_orm.settings")

    django.setup()
    from my_project.models import HomeworkResult

    main()
