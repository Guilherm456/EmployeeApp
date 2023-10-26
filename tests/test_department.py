from rest_framework.test import APIRequestFactory, APIClient,APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Define a test case for the Department model
class DepartmentTest(APITestCase):
    departmentID = 0  # Keep track of the last department created
    createNew= False  # Flag to indicate whether a new department was created

    # Set up the test case
    def setUp(self):

        # Create a test user and authenticate

        # The database of tests is different from the database of the application
        # So we need to create a user in the test database
        self.user = User.objects.create(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a department for testing
        self.test_department_create()

    # Tear down the test case
    def tearDown(self):
        self.client.logout()

    # Test deleting a department
    def test_department_delete(self):
        response = self.client.delete(f'/api/v1/departments/{self.departmentID}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test deleting a department that doesn't exist
    def test_department_delete_fail(self):
        response = self.client.delete('/api/v1/departments/10')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test updating a department
    def test_department_update(self):
        response = self.client.put(f'/api/v1/departments/{self.departmentID}', {
            "name": "Tester",
            "description": "Tester department"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Test getting a single department
    def test_department_get(self):
        response = self.client.get(f'/api/v1/departments/{self.departmentID}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        name = response.data.get('name')
        self.assertEqual(name, 'Tester')

        description = response.data.get('description')
        self.assertNotEqual(description, 'Tester department')
    
    # Test listing all departments
    def test_department_list(self):
        response = self.client.get('/api/v1/departments')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data.get('results')
        # If a new department was created, there should be two results
        self.assertEqual(len(results), 2 if self.createNew else 1)

    # Test creating a department
    def test_department_create(self):
        response = self.client.post('/api/v1/departments', {
            "name": "Tester",
            "description": "123"
        }, format='json')
        
        # Store the ID of the last created department
        self.departmentID = response.data.get('id')
        
        assert self.departmentID is not None

        if self.departmentID!=1:
            self.createNew=True

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
