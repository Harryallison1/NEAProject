from django.test import TestCase
from .models import Question
from .utils import get_questions_by_topic
import csv
import os

class QuestionModelTest(TestCase):

    def setUp(self):
        """
        Method runs before every test.Used to load the test data from the CSV file into the  test database.
        """
        csv_file_path = '/home/harry/projects/newone/mynewone/questions.cv' 
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                Question.objects.create(
                    question_text=row[0],
                    correct_answer=row[1],
                    wrong_answer1=row[2],
                    wrong_answer2=row[3],
                    wrong_answer3=row[4],
                    topic=row[5]
                )

    def test_get_questions_by_topic(self):
        """
        Testing the `get_questions_by_topic` function using the data from the CSV.
        """
        #Tests the 'Structure and Function of the Processor' topic
        processor_questions = get_questions_by_topic('Structure and Function of the Processor')

        #Checks questions are returned for the 'Structure and Function of the Processor' topic
        self.assertGreater(processor_questions.count(), 0, "No questions found for 'Structure and Function of the Processor' topic")

        

        
