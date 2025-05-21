from django.test import TestCase
from recipe.models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation_and_iteration(self):
        cat = Category.objects.create(name="Desserts")
        self.assertEqual(cat.name, "Desserts")
        self.assertIn("Desserts", list(cat))

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Dishes")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Spaghetti",
            description="Delicious spaghetti",
            instructions="Boil water, cook pasta",
            ingredients="Pasta, water, salt",
            category=self.category
        )
        self.assertEqual(recipe.title, "Spaghetti")
        self.assertEqual(recipe.category.name, "Main Dishes")
