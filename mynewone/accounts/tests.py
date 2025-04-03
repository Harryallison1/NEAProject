from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

class LoginTest(TestCase): 

    def test_login(self): #This is test 2 for login page testing
        long_username = "A" * 50000 #Username is A * 50000
        long_password = "A" * 50000 #Password is A * 50000

        response = self.client.post("/accounts/login/", {
            "username": long_username,
            "password": long_password
        })

        print(response.content)  
        print(response.wsgi_request.user)
        session = self.client.session
        print("User ID:", session.get('_auth_user_id')) 
        self.assertEqual(response.status_code, 200)  

class RegisterTest(TestCase):

    def test_long_username(self): #This is test 1 for sign up page testing
        long_username = "long_username" * 1000  #Very long username
        password = "Strange_Mouse82"
        email = "long_username@gmail.com"

        response = self.client.post("/accounts/register/", {
            "username": long_username,
            "email": email,
            "password1": password,
            "password2": password
        })

        self.assertEqual(response.status_code, 200) 
        
        user_exists = (User.objects.filter(username=long_username).exists()) #User should not be created
        print(f"User with username '{long_username}' exists: {user_exists}") 
        self.assertFalse(user_exists)


    def test_long_email(self): #This is test 3 for sign up page testing

        username = "test_user290"
        password = "Pencil_Case28"
        
        long_email_part = "thisisanextremelylongemailaddresswithwaytoomanycharactersanditisdefinitelytoolongforanynormalusecase"
        long_email = long_email_part * 10000 + "@example.com" 

        response = self.client.post("/accounts/register/", {
            "username": username,
            "email": long_email,
            "password1": password,
            "password2": password
        })

        self.assertEqual(response.status_code, 200)

        user_exists = User.objects.filter(username=username).exists()
    
        print(f"User with username '{username}' exists: {user_exists}")  
        self.assertFalse(user_exists)  #User shouldnt be created

    def test_long_password(self): #This is test 4 for sign up testing
        
        long_password = "P@sswor_d12" * 10000  #Very long password 

        response = self.client.post("/accounts/register/", {
            "username": "test_robustnessuser",
            "email": "test_robust@gmail.com",
            "password1": long_password,
            "password2": long_password
        })
        
        print("Start of long password test")

        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "Ensure this value has at most") 
        self.assertFalse(User.objects.filter(username="test_robustnessuser").exists())  #User shouldn't be created

        print("End of long password test")

