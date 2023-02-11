from django.test import TestCase
from ..models import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='mehdi@gmail.com',
            phone_number='09182251753',
            full_name='mehdi mirzaie',
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'mehdi@gmail.com')
        self.assertEqual(self.user.phone_number, '09182251753')
        self.assertEqual(self.user.full_name, 'mehdi mirzaie')
    
    def test_user_str(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_user_has_perm(self):
        self.assertTrue(self.user.has_perm('perm'))
    
    def test_user_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('app'))
    
    def test_user_is_staff(self):
        self.assertFalse(self.user.is_staff)