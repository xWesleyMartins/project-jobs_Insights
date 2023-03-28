from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path) as csv_file:
            return list(csv.DictReader(csv_file))
    except FileNotFoundError:
        print(f"file {path} Not found")


def get_unique_job_types(path: str) -> List[str]:
    try:
        result_data_file = read(path)
        return {result_data["job_type"] for result_data in result_data_file}
    except FileNotFoundError:
        print(f"file {path} Not found")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job = list(job for job in jobs if job["job_type"] == job_type)
    return filter_job
