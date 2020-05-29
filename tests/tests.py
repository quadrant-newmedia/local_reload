from django.test import TestCase, override_settings

class MyTestCase(TestCase):
    def test_template_renders(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)