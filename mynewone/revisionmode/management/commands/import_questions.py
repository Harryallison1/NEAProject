import csv  # imports module for reading and writing CSV files
from django.core.management.base import BaseCommand  # class which allows creating custom management commands
from revisionmode.models import Question  # imports my Question model

class Command(BaseCommand):  # defines a custom Django command by inheriting from BaseCommand
    help = 'Import questions from a CSV file into the database'  # Help attribute provides description of command

    def add_arguments(self, parser):  # method allows me to specify a csv file as an argument when running the command
        parser.add_argument('csv_file', type=str, help='mynewone/questions.csv')

    def handle(self, *args, **kwargs):  # main function which is ran when the command is executed
        csv_file_path = kwargs['csv_file']  # retrieves the file path provided in the command line argument

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:  # opens csv for reading
            reader = csv.reader(csvfile)  # creates a csv reader object to process the file line by line
            next(reader)  # skips the first row of the csv file 
            
            for row in reader:  # loops through each row in the csv file
                print(row)  # Print each row to debug

                # Skip rows that don't have exactly 6 values
                if len(row) != 6:
                    print(f"Skipping row due to incorrect number of values: {row}")  # Print skipped rows for debugging
                    continue

                question_text, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3, topic = row
                
                # Create the Question object and save to the database
                Question.objects.create(
                    question_text=question_text,
                    correct_answer=correct_answer,
                    wrong_answer1=wrong_answer1,
                    wrong_answer2=wrong_answer2,
                    wrong_answer3=wrong_answer3,
                    topic=topic
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported questions from {csv_file_path}'))
        # This just displays a success message in green after importing all questions

        print(Question.objects.all())  # Print all the questions in the database after import





