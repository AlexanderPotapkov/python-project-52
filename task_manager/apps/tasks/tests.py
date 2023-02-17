from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.core.exceptions import ObjectDoesNotExist

from .views import TasksView, ShowTask, CreateTask, UpdateTask, DeleteTask
from ..users.models import User
from ..tasks.models import Task


class TestTasksUrls(SimpleTestCase):

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


class TestTasksViews(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.login_url = reverse('login')
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.tasks_url = reverse('tasks')
        self.task1 = Task.objects.get(pk=1)
        self.create_url = reverse('create_task')
        self.show_task_url = reverse('show_task', args=[1])
        self.update_url = reverse('update_task', args=[1])
        self.delete_url = reverse('delete_task', args=[1])
        self.form1 = {'name': 'New task',
                      'status': 1,
                      'description': 'description',
                      'author': 1,
                      'executor': 1,
                      'label': [1, 2, 3]}

    def test_tasks_view_GET(self):
        self.client.force_login(self.user1)
        self.task2 = Task.objects.get(pk=2)
        response = self.client.get(self.tasks_url)
        response_tasks = list(response.context['tasks'])
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response_tasks, [self.task1, self.task2])
        self.assertTemplateUsed(response, 'tasks/tasks.html')

    def test_show_task(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.show_task_url)
        descriptions = response.context['task']
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_view.html')
        self.assertQuerysetEqual([descriptions.name, descriptions.author,
                                  descriptions.executor,
                                  descriptions.description,
                                  descriptions.status,
                                  descriptions.date_create],
                                 [self.task1.name, self.task1.author,
                                  self.task1.executor, self.task1.description,
                                  self.task1.status, self.task1.date_create])

    def test_create_task_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_create_task_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.create_url, self.form1)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)
        self.assertTrue(Task.objects.get(pk=3))

    def test_update_task_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_update_task_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.update_url, self.form1)
        self.task = Task.objects.get(pk=1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.task.name, self.form1['name'])
        self.assertRedirects(response, self.tasks_url)

    def test_delete_self_task_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/delete.html')

    def test_delete_self_task_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)
        self.assertEqual(len(Task.objects.all()), 1)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=3)

    def delete_not_self_task_GET(self):
        self.client.force_login(self.user2)
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.tasks_url)

    def delete_not_self_task_POST(self):
        self.client.force_login(self.user2)
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.tasks_url)
        self.assertEqual(len(Task.objects.all()), 2)

    def test_filter(self):
        self.client.force_login(self.user1)
        content_form_1 = f'{self.tasks_url}' \
                         '?status=1&executor=1&label='
        response = self.client.get(content_form_1)
        tasks_list = response.context['tasks']
        self.assertEqual(len(tasks_list), 1)
        task = tasks_list[0]
        self.assertEqual(task.name, 'task_1')
        self.assertEqual(task.executor.id, 1)
        self.assertEqual(task.status.id, 1)
        self.assertEqual(task.author.id, 1)

    def test_filter_self_tasks(self):
        self.client.force_login(self.user1)
        content_form_2 = f'{self.tasks_url}' \
                         '?self_task=on'
        response_2 = self.client.get(content_form_2)
        tasks_list = response_2.context['tasks']
        self.assertEqual(len(tasks_list), 1)
        task = tasks_list[0]
        self.assertEqual(task.name, 'task_1')
        self.assertEqual(task.author.id, 1)
