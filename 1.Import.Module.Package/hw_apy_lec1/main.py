import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == "__main__":
    print(datetime.date.today())
    print(get_employees())
    print(calculate_salary(40, 10))
