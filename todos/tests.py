from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title="Test Todo", body="Do some basic testing")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "Do some basic testing")
        self.assertEqual(str(self.todo), self.todo.title)
        
    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Test Todo")
    
    def test_api_detailview(self): # new
        response = self.client.get(
        reverse("todo_detail", kwargs={"pk": self.todo.id}),
        format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Test Todo")