from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import TasksView, ShowTask, CreateTask, UpdateTask, DeleteTask


class TestTagsUrls(SimpleTestCase):

    def test_task_view(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func.view_class, TasksView)

    def test_task_show(self):
        url = reverse('show_task', args='1')
        self.assertEquals(resolve(url).func.view_class, ShowTask)

    def test_task_create(self):
        url = reverse('create_task')
        self.assertEquals(resolve(url).func.view_class, CreateTask)

    def test_task_update(self):
        url = reverse('update_task', args='1')
        self.assertEquals(resolve(url).func.view_class, UpdateTask)

    def test_task_delete(self):
        url = reverse('delete_task', args='1')
        self.assertEquals(resolve(url).func.view_class, DeleteTask)


class TestTasksViewsWithoutAuth(TestCase):

    def setUp(self):
        self.login = reverse('login')
        self.urls = [reverse('tasks'),
                     reverse('create_task'),
                     reverse('delete_task', args='1'),
                     reverse('update_task', args='1'),
                     reverse('show_task', args='1')]

    def test_no_auth(self):
        for url in self.urls:
            response = self.client.get(url)
            self.assertRedirects(response, self.login)
