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
    filter_industry_list = list(
        industries for industries in jobs if industries["industry"] == industry
    )
    return filter_industry_list
