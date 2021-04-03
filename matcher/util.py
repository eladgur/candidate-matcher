from matcher.models import Job, Candidate
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def to_title(candidate):
    candidate.title.lower()


def add_title_score_single(candidate, title_to_score):
    candidate.title_score = title_to_score[candidate.title]
    return candidate


def add_title_score(job_title, candidates):
    titles = [c.title for c in candidates]
    titles = list(dict.fromkeys(titles))
    title_to_score = dict(process.extract(job_title, titles))
    return list(map(lambda c: add_title_score_single(c, title_to_score), candidates))


def add_skill_score(skill_name, candidate):
    skills = list(candidate.skills.all())
    skill_names = list(dict.fromkeys([s.name for s in skills]))
    p = process.extract(skill_name, skill_names)
    scores = map(lambda a: a[1], p)
    candidate.skill_score = sum(scores)


def add_score(job, candidates):
    with_title_scores = add_title_score(job.title, candidates)
    for candidate in with_title_scores:
        add_skill_score(job.skill.name, candidate)
        candidate.score = candidate.title_score + candidate.skill_score
    return with_title_scores

def candidateFinder(job):
    candidates = list(Candidate.objects.all())
    scored_candidates = add_score(job, candidates)
    scored_candidates.sort(key=lambda c: c.score, reverse=True)
    return scored_candidates[0]
