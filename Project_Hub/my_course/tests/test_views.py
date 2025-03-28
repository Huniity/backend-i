import pytest
from django.test import Client
from my_course.forms import CourseForm
from my_course.models import Course
from django.contrib.auth.models import User


#---------------------- HOME PAGE TEST --------------------#

@pytest.mark.django_db
def test_homepage(client):
    response = client.get("/")
    assert response
    assert response.status_code == 200

@pytest.mark.django_db
def test_course_not_logged_in(client):
    response = client.get("/course")
    assert response
    assert response.status_code != 200

#---------------------- ADMIN TEST --------------------#

@pytest.mark.django_db
def test_admin_page(client, django_user_model):
    django_user_model.objects.create_superuser(username="admin", password="admin") 
    client.login(username="admin", password="admin")
    response = client.get("/admin/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_failure_admin_page(client, django_user_model):
    django_user_model.objects.create_superuser(username="admin", password="admin") 
    client.login(username="admin", password="")
    response = client.get("/admin/")
    assert response.status_code != 200

#---------------------- OBJECT CREATION TEST --------------------#

import pytest
from django.contrib.auth import get_user_model
from my_course.models import Course
from my_course.forms import CourseForm
from datetime import date

User = get_user_model()

@pytest.mark.django_db
@pytest.fixture
def course():
    """Fixture to create and return a Course instance"""
    user = User.objects.create_user(username="james", password="password")  # Create a test user
    
    course = Course.objects.create(
        course_title="Python Basics",
        category="Programming",
        school_name="Online Academy",
        description="Learn Python from scratch.",
        price=49.99,
        available_until=date(2025, 12, 31),  # A future date
        author="John Doe",
        user=user,  # Assign user
    )

    return course


@pytest.mark.django_db
def test_course_form_with_data(course):
    """Test that the CourseForm is valid with correct data"""
    data = {
        'course_title': course.course_title,
        'category': course.category,
        'school_name': course.school_name,
        'description': course.description,
        'price': course.price,
        'available_until': course.available_until,
        'author': course.author,
        'user': course.user.pk,  # Use primary key for foreign key
    }

    form = CourseForm(data=data)
    
    assert form.is_valid(), form.errors  # Check if form is valid and show errors if not
