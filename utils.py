import json
from config import DATA_PATH


# Загрузка файла json
def open_json(path=DATA_PATH):
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


# возвращает список всех кандидатов
def load_candidates_from_json():
    candidates = open_json()
    return candidates


# возвращает одного кандидата по его id
def get_candidate(candidate_id):
    candidates = open_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


# возвращает кандидатов по имени
def get_candidates_by_name(candidate_name):
    name_candidates = []
    candidate_name_lower = candidate_name.lower()
    candidates_name = open_json()

    for candidate in candidates_name:
        names = candidate["name"].lower().strip().split(" ")
        if candidate_name_lower in names:
            name_candidates.append(candidate)
            continue
    return name_candidates


# возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name):
    skilled_candidates = []
    skill_name_lower = skill_name.lower()
    candidates_skill = open_json()

    for candidate in candidates_skill:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue
    return skilled_candidates
