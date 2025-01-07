from django.db import models
from django.utils import timezone
from hashlib import sha256


class UserProfile(models.Model):
    # User fields
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    first_name = models.CharField(max_length=150, null=True, blank=True)  # Allow nulls temporarily
    last_name = models.CharField(max_length=150, null=True, blank=True)  # Allow nulls temporarily
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def set_password(self, raw_password):
        # Hashing the password using SHA256 for simplicity
        self.password = sha256(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        return self.password == sha256(raw_password.encode()).hexdigest()

    def __str__(self):
        return self.username







from django.db import models

class CareerForm(models.Model):
    # Stage 1: Personal Information
    highest_degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    gpa_or_grade = models.CharField(max_length=50)
    
    # Stage 2: Current Occupation
    current_occupation = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    internship_experience = models.TextField()
    skills_acquired = models.TextField()
    top_skills_known = models.TextField()

    # Stage 3: Career Goals
    current_career_goal = models.CharField(max_length=255)
    is_employed = models.BooleanField(default=False)
    preferred_industry = models.CharField(max_length=255)
    desired_job_role = models.CharField(max_length=255)
    preferred_work_environment = models.CharField(max_length=255)

    # Stage 4: Passion & Tools
    top_3_skills = models.TextField()
    passionate_areas = models.TextField()
    tools_and_technologies = models.TextField()
    certifications = models.TextField()

    # Stage 5: Future Vision
    future_goals = models.TextField()
    challenges = models.TextField()
    open_to_training = models.BooleanField(default=False)
    identified_mentor = models.BooleanField(default=False)
    support_needed = models.TextField()
    interested_in_internships = models.BooleanField(default=False)
    personalized_recommendations = models.BooleanField(default=False)

    # Additional field for resume or portfolio
    resume_or_portfolio = models.FileField(upload_to='uploads/', null=True, blank=True)

    # User related information
    user_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Career Form for {self.user_id} - {self.highest_degree}"




from django.db import models
from django.contrib.auth.models import User

class Widget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    elfsight_embed_code = models.TextField(blank=True, null=True)  # Field to store embed code
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class WidgetLayout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    layout_data = models.JSONField(default=dict)  # Store layout as JSON