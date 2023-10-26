from rest_framework.test import APIRequestFactory, APIClient,APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Define a test case for the Employee model
class EmployeeTest(APITestCase):
    last_employee = 0  # Keep track of the last employee created
    createNew= False  # Flag to indicate whether a new employee was created

    # Set up the test case
    def setUp(self):

        # Create a test user and authenticate
        self.user = User.objects.create(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a department for the employee
        response = self.client.post('/api/v1/departments', {
            "name": "Tester"
        }, format='json')

        # Create an employee for testing
        self.test_employee_create()

    # Tear down the test case
    def tearDown(self):
        self.client.logout()

    # Test deleting an employee
    def test_employee_delete(self):
        response = self.client.delete(f'/api/v1/employees/{self.last_employee}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test deleting an employee that doesn't exist
    def test_employee_delete_fail(self):
        response = self.client.delete('/api/v1/employees/10')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test updating an employee
    def test_employee_update(self):
        response = self.client.put(f'/api/v1/employees/{self.last_employee}', {
            "name": "test",
            "email": "teste_new@gmail.com",
            "department": 1
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test listing all employees
    def test_employee_list(self):
        response = self.client.get('/api/v1/employees')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data.get('results')
        self.assertEqual(len(results), 2 if self.createNew else 1)

    # Test getting a single employee
    def test_employee_get(self):
        response = self.client.get(f'/api/v1/employees/{self.last_employee}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        name = response.data.get('name')
        self.assertEqual(name, 'test')

        email = response.data.get('email')
        self.assertNotEqual(email, "test@gmail.com")

        department = response.data.get('department')
        self.assertEqual(department, "Tester")

    # Test creating an employee
    def test_employee_create(self):
        response = self.client.post('/api/v1/employees', {
            "name": "test",
            "email": "teste@gmail.com",
            "department": 1
        })
        
        self.last_employee = response.data.get('id')
        assert self.last_employee is not None

        if self.last_employee!=1:
            self.createNew=True 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
