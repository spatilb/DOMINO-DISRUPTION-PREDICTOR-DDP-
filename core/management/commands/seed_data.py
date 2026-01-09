from django.core.management.base import BaseCommand
from core.models import Tag, RootCauseRule

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds initial data for DDP'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Demo User
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user('demo', 'demo@example.com', 'demo123')
            self.stdout.write('Created Demo User (username: demo, password: demo123)')
        else:
            self.stdout.write('Demo User already exists')

        # Tags
        tags = ['Study', 'Work', 'Health', 'Tech Issue', 'Social', 'Commute']
        tag_objects = {}
        for t_name in tags:
            tag, created = Tag.objects.get_or_create(name=t_name)
            tag_objects[t_name] = tag
            if created:
                self.stdout.write(f'Created Tag: {t_name}')

        # Rules
        rules = [
            {
                'tag': 'Study',
                'keyword': 'tired',
                'label': 'Fatigue detected. Try the Pomodoro technique or take a 20-min power nap.'
            },
            {
                'tag': 'Study',
                'keyword': 'distracted',
                'label': 'High distraction. Put your phone in another room.'
            },
            {
                'tag': 'Tech Issue',
                'keyword': 'internet',
                'label': 'Network instability. Check router or switch to hotspot.'
            },
            {
                'tag': 'Health',
                'keyword': 'headache',
                'label': 'Dehydration likely. Drink water and take a screen break.'
            },
            {
                'tag': 'Work',
                'keyword': 'meeting',
                'label': 'Meeting overrun. Set a hard stop time for next meeting.'
            }
        ]

        for rule_data in rules:
            tag = tag_objects.get(rule_data['tag'])
            if tag:
                rule, created = RootCauseRule.objects.get_or_create(
                    tag=tag,
                    keyword=rule_data['keyword'],
                    defaults={'root_cause_label': rule_data['label']}
                )
                if created:
                    self.stdout.write(f"Created Rule: {rule}")

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
