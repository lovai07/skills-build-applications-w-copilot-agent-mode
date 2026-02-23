from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections using pymongo to avoid Djongo PK unhashable error
        from django.conf import settings
        import pymongo
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['octofit_db']
        db['leaderboard'].drop()
        db['activities'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='captainamerica@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium'),
            Workout.objects.create(name='Swimming', description='Swim 1km', difficulty='Hard'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Pushups', duration=10, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Swimming', duration=40, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[3], score=80, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
