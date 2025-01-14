# Generated by Django 5.0.7 on 2024-12-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_degree', models.CharField(max_length=255)),
                ('field_of_study', models.CharField(max_length=255)),
                ('university_name', models.CharField(max_length=255)),
                ('graduation_year', models.IntegerField()),
                ('gpa_or_grade', models.CharField(max_length=50)),
                ('current_occupation', models.CharField(max_length=255)),
                ('organization_name', models.CharField(max_length=255)),
                ('years_of_experience', models.IntegerField()),
                ('internship_experience', models.TextField()),
                ('skills_acquired', models.TextField()),
                ('top_skills_known', models.TextField()),
                ('current_career_goal', models.CharField(max_length=255)),
                ('is_employed', models.BooleanField(default=False)),
                ('preferred_industry', models.CharField(max_length=255)),
                ('desired_job_role', models.CharField(max_length=255)),
                ('preferred_work_environment', models.CharField(max_length=255)),
                ('top_3_skills', models.TextField()),
                ('passionate_areas', models.TextField()),
                ('tools_and_technologies', models.TextField()),
                ('certifications', models.TextField()),
                ('future_goals', models.TextField()),
                ('challenges', models.TextField()),
                ('open_to_training', models.BooleanField(default=False)),
                ('identified_mentor', models.BooleanField(default=False)),
                ('support_needed', models.TextField()),
                ('interested_in_internships', models.BooleanField(default=False)),
                ('personalized_recommendations', models.BooleanField(default=False)),
                ('resume_or_portfolio', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
