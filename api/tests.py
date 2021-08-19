from django.test import TestCase

# I should've written some tests instead of overcomplating :(.

def seed_currencies() {
    Currency = apps.get_model('api', 'Currency')
}