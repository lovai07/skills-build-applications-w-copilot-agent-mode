from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'test@example.com')
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2024-01-01')
        self.assertEqual(str(activity), 'test@example.com - run')
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        lb = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(lb), 'test@example.com - 1')
