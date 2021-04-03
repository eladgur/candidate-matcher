import unittest
from django.test import TestCase
from matcher.models import Skill, Candidate, Job
from matcher.util import candidateFinder


def create_candidate(name, title, skill_names):
    skills = Skill.objects.filter(name__in=skill_names)
    candidate = Candidate(title=title, name=name)
    candidate.save()
    candidate.skills.set(skills)
    candidate.save()


def create_job(title, skill_name):
    skill = Skill.objects.get(name=skill_name)
    Job.objects.create(title=title, skill=skill)


class CandidateFinderTests(TestCase):
    skill_names = ['C', 'C++', 'java', 'clojure', 'TS', 'JS', 'python', 'TJS']
    sw_eng_title = 'Software Engineer'
    sw_dev = 'Software Developer'
    wboy_title = 'Water Boy'

    def setUp(self):
        for skill_name in self.skill_names:
            Skill.objects.create(name=skill_name)
        create_candidate('Avi Kababi', self.sw_eng_title, ['python', 'clojure', 'java'])
        create_candidate('Avi Kababian', self.sw_eng_title, ['clojure', 'java'])
        create_candidate('Ali Kopter', self.sw_dev, ['TS', 'JS'])
        create_job(self.sw_eng_title, 'python')
        create_job(self.wboy_title, 'TS')
        create_job(self.sw_dev, 'TJS')

    def run_test(self, job, expected_candidate):
        candidate = candidateFinder(job)
        self.assertEqual(candidate, expected_candidate)

    def test_with_best_title_and_skills(self):
        job = Job.objects.get(title=self.sw_eng_title)
        expected_candidate = Candidate.objects.get(name='Avi Kababi')
        self.run_test(job, expected_candidate)

    def test_with_skill_no_title(self):
        job = Job.objects.get(title=self.wboy_title)
        expected_candidate = Candidate.objects.get(name='Ali Kopter')
        self.run_test(job, expected_candidate)

    def test_title_no_skill(self):
        job = Job.objects.get(title=self.sw_dev)
        expected_candidate = Candidate.objects.get(title=self.sw_dev)
        self.run_test(job, expected_candidate)
