from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_skills, name="my_skills"),
    path("add/", views.add_skill, name="add_skill"),
    path("edit/<int:skill_id>/", views.edit_skill, name="edit_skill"),
    path("delete/<int:skill_id>/", views.delete_skill, name="delete_skill"),
    path("browse/",views.browse_skills,name="browse_skills"),
    path("request/<int:skill_id>/",views.request_swap,name="request_swap"),
    path("requests/",views.requests_list,name="requests_list"),
    path("request/<int:request_id>/accept/",views.accept_request,name="accept_request",),
    path("request/<int:request_id>/reject/",views.reject_request,name="reject_request"),
    path("sent-requests/",views.sent_requests,name="sent_requests"),
]