"""
URL configuration for projectX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import landing_page, register_view, login_view, dashboard, logout_view,career_form_view,course_view,course_grid_view,course_content_page_view,work_listing_view,work_search_view,project_page_view,accounts_view,completed_task_view,pastdue_task_view,pending_task_view,profile_view,dash_view,profile_tab,timeline_view,research_view,email_view,chatroom_view


urlpatterns = [
    path('', landing_page, name='landing'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('career-form/', career_form_view, name='career_form'),
    path('course/', course_view, name='course'),
    path('coursegrid/', course_grid_view, name='course_grid'),
    path('coursecontent/', course_content_page_view, name='course_content'),
    path('worklisting/', work_listing_view, name='work'),
    path('workseacrh/', work_search_view, name='worksearch'),
    path('projectpage/', project_page_view, name='projectpage'),
    # path('widgetlist/', widget_list, name='widgetlist'),
    path('accounts/', accounts_view, name='accounts'),
    path('activeprojects/', completed_task_view, name='activeprojects'),
    path('pendingtask/', pending_task_view, name='pendingtask'),
    path('pastduetask/', pastdue_task_view, name='pastduetask'),
    path('profileview/', profile_view, name='profileview'),
    path('dash/', dash_view, name='dash'),
    path('profile/tab/<str:tab_name>/', profile_tab, name='profile_tab'),
    path('timeline/', timeline_view, name='timeline'),
    path('research/', research_view, name='research'),
    path('email/', email_view, name='email'),
    path('chatroom/', chatroom_view, name='chatroom'),





   

    

]

