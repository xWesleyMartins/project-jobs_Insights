from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    try:
        result_data_file = read(path)
        all_industries = set()
        for row in result_data_file:
            if row.get("industry"):
                all_industries.add(row["industry"])
        return list(all_industries)
    except FileNotFoundError:
        print(f"file {path} Not found")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
