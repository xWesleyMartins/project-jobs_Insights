from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    try:
        result_data_file = read(path)
        salaries_list = [
            int(row["max_salary"])
            for row in result_data_file
            if row["max_salary"].isdigit()
        ]
        if not salaries_list:
            raise ValueError("No valid salaries found.")
        return max(salaries_list)
    except ValueError as err:
        print(str(err))
    except FileNotFoundError:
        print(f"file {path} Not found")


def get_min_salary(path: str) -> int:
    try:
        result_data_file = read(path)
        salaries_list = [
            int(row["min_salary"])
            for row in result_data_file
            if row["min_salary"].isdigit()
        ]
        if not salaries_list:
            raise ValueError("No valid salaries found.")
        return min(salaries_list)
    except ValueError as err:
        print(str(err))
    except FileNotFoundError:
        print(f"file {path} Not found")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        salary = int(salary)
        min_salary, max_salary = map(
            int, (job["min_salary"], job["max_salary"])
        )
        if min_salary > max_salary:
            raise ValueError("min_salary cannot be greater than max_salary")
    except (KeyError, TypeError):
        raise ValueError("informed value is invalid")
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
