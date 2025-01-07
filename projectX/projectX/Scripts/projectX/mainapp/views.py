from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import RegistrationForm, LoginForm, CareerFormModel
from django.http import HttpResponse


def landing_page(request):
    """Render landing page."""
    return render(request, 'home.html')


def register_view(request):
    """Handle user registration."""
    if request.method == "POST":
        # Extract fields from the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        nationality = request.POST.get('nationality')

        # Password validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        else:
            # Check if email already exists
            if UserProfile.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
            else:
                # Create and save the new user
                user = UserProfile(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    address=address,
                    date_of_birth=date_of_birth,
                    city=city,
                    nationality=nationality,
                )
                # Hash and set the password using the defined model method
                user.set_password(password1)
                user.save()
                messages.success(request, "Registration successful. Please fill out the career form.")
                # Save user id in session and redirect to career form
                request.session['user_id'] = user.id
                return redirect('login')

    return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CareerForm
from django.core.files.storage import FileSystemStorage

def career_form_view(request):
    """Handle career form submission."""
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "You must log in first.")
        return redirect('login')

    user = UserProfile.objects.get(id=user_id)

    if request.method == "POST":
        try:
            # Gather form data
            data = {
                "user_id": user,
                "highest_degree": request.POST.get("highest_degree"),
                "field_of_study": request.POST.get("field_of_study"),
                "university_name": request.POST.get("university_name"),
                "graduation_year": int(request.POST.get("graduation_year")),
                "gpa_or_grade": request.POST.get("gpa_or_grade"),
                "current_occupation": request.POST.get("current_occupation"),
                "organization_name": request.POST.get("organization_name"),
                "years_of_experience": int(request.POST.get("years_of_experience")),
                "internship_experience": request.POST.get("internship_experience"),
                "skills_acquired": request.POST.get("skills_acquired"),
                "top_skills_known": request.POST.get("top_skills_known"),
                "current_career_goal": request.POST.get("current_career_goal"),
                "is_employed": request.POST.get("is_employed") == "True",
                "preferred_industry": request.POST.get("preferred_industry"),
                "desired_job_role": request.POST.get("desired_job_role"),
                "preferred_work_environment": request.POST.get("preferred_work_environment"),
                "top_3_skills": request.POST.get("top_3_skills"),
                "passionate_areas": request.POST.get("passionate_areas"),
                "certifications": request.POST.get("certifications"),
                "future_goals": request.POST.get("future_goals"),
                "challenges": request.POST.get("challenges"),
                "open_to_training": request.POST.get("open_to_training") == "True",
                "identified_mentor": request.POST.get("identified_mentor") == "True",
                "support_needed": request.POST.get("support_needed"),
                "interested_in_internships": request.POST.get("interested_in_internships") == "True",
                "personalized_recommendations": request.POST.get("personalized_recommendations") == "True",
            }

            # Handle file upload
            if "resume_or_portfolio" in request.FILES:
                resume_file = request.FILES["resume_or_portfolio"]
                fs = FileSystemStorage()
                data["resume_or_portfolio"] = fs.save(resume_file.name, resume_file)

            # Save career form data
            CareerForm.objects.create(**data)

            messages.success(request, "Form submitted successfully!")
            return redirect("dashboard")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect("career_form")

    return render(request, "career_form.html")



def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserProfile.objects.get(email=email)
                if user.check_password(password):
                    # Set user session
                    request.session['user_id'] = user.id
                    messages.success(request, "Login successful.")
                    
                    # Check if the user has already submitted the career form
                    if CareerForm.objects.filter(user_id=user).exists():
                        return redirect('dashboard')  # Redirect to dashboard if career form is submitted
                    else:
                        return redirect('career_form')  # Redirect to career form if not submitted
                else:
                    messages.error(request, "Invalid credentials.")
            except UserProfile.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    """User dashboard after successful login."""
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "You must log in first.")
        return redirect('login')
    try:
        user = UserProfile.objects.get(id=user_id)
        return render(request, 'dashboard.html', {'user': user})
    except UserProfile.DoesNotExist:
        messages.error(request, "Session error. Please log in again.")
        return redirect('login')


def logout_view(request):
    """Logout user securely."""
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have logged out.")
    return redirect('/')


def course_view(request):
    return render(request,"course.html")

def course_grid_view(request):
    return render(request,"coursegrid.html")

def course_content_page_view(request):
    return render(request,"coursecontent.html")




def work_listing_view(request):
    return render(request,"worklisting.html")



def work_search_view(request):
    search_query = request.GET.get('query', '')
    # Mocked result. Replace with database search logic.
    results = [
        {"name": "Graphic Designer", "location": "United States", "hourly_rate": 70},
        {"name": "Web Developer", "location": "India", "hourly_rate": 50},
    ]
    # Filter results based on search query
    filtered_results = [result for result in results if search_query.lower() in result['name'].lower()]

    context = {
        "search_query": search_query,
        "results": filtered_results,
    }
    return render(request, "worksearch.html", context)



def project_page_view(request):
    return render(request,"projectpage.html")



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Widget
# from .forms import WidgetForm

# # View to display all widgets for a user
# @login_required
# def widget_list(request):
#     widgets = Widget.objects.filter(user=request.user)
#     return render(request, 'widget_list.html', {'widgets': widgets})

# # View to create a new widget
# @login_required
# def create_widget(request):
#     if request.method == 'POST':
#         form = WidgetForm(request.POST)
#         if form.is_valid():
#             widget = form.save(commit=False)
#             widget.user = request.user  # Set the user as the currently logged-in user
#             widget.save()
#             return redirect('widget_list')
#     else:
#         form = WidgetForm()
#     return render(request, 'create_widget.html', {'form': form})

# # View to edit an existing widget
# @login_required
# def edit_widget(request, pk):
#     widget = Widget.objects.get(pk=pk, user=request.user)
#     if request.method == 'POST':
#         form = WidgetForm(request.POST, instance=widget)
#         if form.is_valid():
#             form.save()
#             return redirect('widget_list')
#     else:
#         form = WidgetForm(instance=widget)
#     return render(request, 'edit_widget.html', {'form': form, 'widget': widget})


def accounts_view(request):
    return render(request,"accounts.html")

def completed_task_view(request):
    return render(request,"activeprojects.html")


def pending_task_view(request):
    return render(request,"pendingtask.html")

def pastdue_task_view(request):
    return render(request,"pastdue.html")

def profile_view(request):
    return render(request,"profile.html")


def dash_view(request):
    return render(request,"dash.html")


from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def profile_tab(request, tab_name):
    # Map tab names to their respective templates
    template_map = {
        "blogs": "profile/tabs/blogs.html",
        "posts": "profile/tabs/posts.html",
        "whitepapers": "profile/tabs/whitepapers.html",
        "experience": "profile/tabs/experience.html",
        "education": "profile/tabs/education.html",
        "skills": "profile/tabs/skills.html",
    }

    # Get the template path or default to "blogs.html"
    template = template_map.get(tab_name, "profile/tabs/blogs.html")

    # Log a warning if the tab_name is invalid
    if tab_name not in template_map:
        logger.warning(f"Invalid tab_name: {tab_name}. Defaulting to blogs.")

    # Add context if needed
    context = {
        "tab_name": tab_name,  # Useful for dynamic content in templates
    }

    return render(request, template, context)



def timeline_view(request):
    return render(request,"timeline.html")
    

def research_view(request):
    return render(request,"research.html")


def email_view(request):
    return render(request,"email.html")




def chatroom_view(request):
    return render(request,"chatroom.html")