from django.test import TestCase #Django's built in testing framework for unit tests    
from .models import Question       #Django automatically provices an isolated test database for each test
from .utils import get_questions_by_topic, check_answer, get_question_feedback
import csv
import os

class QuestionModelTest(TestCase): #defines a test case class which inherits from TestCase

    def setUp(self): #called before every test method in the test class
        #This runs before every test it is used to load the test data from the CSV file into the  test database.
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
                )   #Previous lines just creates and saves a new Question object in the test database

    #Tests below are for get_questions_by_topic()

    def test_get_questions_by_topic(self):
        
        #Tests the Structure and Function of the Processor topic
        processor_questions = get_questions_by_topic('Structure and Function of the Processor')

        #Checks questions are returned for the Structure and Function of the Processor topic
        self.assertGreater(processor_questions.count(), 0, "No questions found for 'Structure and Function of the Processor' topic")

    def test_for_notexist_topic(self):
        #Calls function with a topic that does not exist
        non_exist_questions = get_questions_by_topic('Non existent topic')

        #Checks that the returned query set is empty
        self.assertEqual(non_exist_questions.count(), 0, "Expected an empty query set for a non existent topic")

    def test_questions_for_correct_topic(self):
        topic = 'Structure and Function of the Processor'
    
        #Gets the questions for Structure and Function of the Processor
        questions = get_questions_by_topic(topic)

        #This part ensures that all returned questions belong to the specified topic
        for question in questions:
            self.assertEqual(question.topic, topic, f"Question '{question}' is not in the topic '{topic}'")

    def test_get_questions_emptydatabase(self):
        #Deletes all Question objects
        Question.objects.all().delete()

        #Tries to extract questions from structure and f of processor
        questions = get_questions_by_topic('Structure and Function of the Processor')

        #question count should be 0 
        self.assertEqual(questions.count(), 0, "Empty QuerySet is expected")

    #Tests below are for check_answer()

    def test_correct_answer(self):
        #Creates a question object with "Performs arithmetic and logical operations" as the correct answer
        question = Question(correct_answer="Performs arithmetic and logical operations")

        #Sets the users answer as the same thing
        user_answer = "Performs arithmetic and logical operations"

        #Checks that the function correctly returns True
        self.assertTrue(check_answer(question, user_answer), "Should return True for the right answer")

    def test_incorrect_answer(self):
        question = Question(correct_answer="RAM") 
        user_answer = "ROM"  #Wrong anwer is entered as the user answer
        self.assertFalse(check_answer(question, user_answer), "Function should return False for an incorrect answer") 

    #Tests below are for get_question_feedback()

    def test_get_question_feedback_correct_answer(self):
        question = Question(correct_answer="CPU")  #Made up Question object
        user_answer = "CPU" 
        self.assertEqual(get_question_feedback(question, user_answer), "Correct! Well done.")

    def test_get_question_feedback_incorrect_answer(self):
        question = Question(correct_answer="RAM")
        user_answer = "Hard Drive"
        self.assertEqual(get_question_feedback(question, user_answer), "Incorrect. The correct answer was: RAM")

    #Test below are for get_remaining_questions()







        

        
