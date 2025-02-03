import csv
from django.core.management.base import BaseCommand
from revisionmode.models import Question

class Command(BaseCommand):
    help = 'Import questions from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='mynewone/questions.cv')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            
            for row in reader:
                question_text, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3, topic = row
                Question.objects.create(
                    question_text=question_text,
                    correct_answer=correct_answer,
                    wrong_answer1=wrong_answer1,
                    wrong_answer2=wrong_answer2,
                    wrong_answer3=wrong_answer3,
                    topic=topic
                )
       

        self.stdout.write(self.style.SUCCESS(f'Successfully imported questions from {csv_file_path}'))




