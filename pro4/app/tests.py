from django.test import TestCase

# Create your tests here.
from app.models import user_profile

print(user_profile.objects.all())
