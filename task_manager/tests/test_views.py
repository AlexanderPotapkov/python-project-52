from django.test import Client, TestCase
from django.urls import reverse


from task_manager.apps.users.models import User


class TaskManagerViewsTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user1 = User.objects.get(pk=1)
        self.form1 = {
            'username': 'user',
            'password': 'password'
        }

    def test_home_page_view_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_manager/index.html')

    def test_login_user_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_manager/login.html')

    def test_login_user_POST(self):
        response = self.client.post(self.login_url, self.form1)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user1.username, 'user1')
        self.assertEquals(self.user1.password, 'password1')

    def test_logout_user_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.index_url)
