import json


def load_candidates():
    """Loading the candidates from JSON-FILE"""
    with open("candidates.json", "r", encoding='utf-8') as f:
        content = json.load(f)
    return content


def get_all():
    """Printing all the candidates"""
    content = load_candidates()
    for user in content:
        print(user)


def get_by_pk(pk):
    """Showing candidates by PK"""
    content = load_candidates()
    for user in content:
        if pk == user.get("pk"):
            return user


def get_by_skill(skill_name):
    """Showing candidates by skills"""
    content = load_candidates()
    same_skills = []
    for skills in content:
        if skill_name in skills.get("skills"):
            same_skills.append(skills)
    return same_skills

