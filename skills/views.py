from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from .forms import SkillForm

@login_required
def add_skill(request):

    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user
            skill.save()

            return redirect("home")

    else:
        form = SkillForm()

    return render(request, "skills/add_skill.html", {"form": form})

from .models import Skill, SwapRequest

@login_required
def my_skills(request):
    skills = Skill.objects.filter(owner=request.user)

    return render(request, "skills/my_skills.html", {
        "skills": skills
    })

@login_required
def edit_skill(request, skill_id):

    skill = get_object_or_404(
        Skill,
        id=skill_id,
        owner=request.user
    )

    if request.method == "POST":

        form = SkillForm(request.POST, instance=skill)

        if form.is_valid():

            form.save()

            return redirect("my_skills")

    else:

        form = SkillForm(instance=skill)

    return render(
        request,
        "skills/edit_skill.html",
        {"form": form}
    )
@login_required
def delete_skill(request, skill_id):

    skill = get_object_or_404(
        Skill,
        id=skill_id,
        owner=request.user
    )

    if request.method == "POST":

        skill.delete()

        return redirect("my_skills")

    return render(
        request,
        "skills/delete_skill.html",
        {"skill": skill}
    )
@login_required
def browse_skills(request):

    query = request.GET.get("q")

    skills = Skill.objects.exclude(owner=request.user)

    if query:
        skills = skills.filter(
            name__icontains=query
        )

    return render(
        request,
        "skills/browse_skills.html",
        {
            "skills": skills
        }
    )
@login_required
def request_swap(request, skill_id):
    skill = get_object_or_404(
    Skill,
    id=skill_id
)
    SwapRequest.objects.create(
    sender=request.user,
    receiver=skill.owner,
    skill=skill,
)
    return redirect("browse_skills")
@login_required
def requests_list(request):

    requests = SwapRequest.objects.filter(
        receiver=request.user
    )

    return render(
        request,
        "skills/requests.html",
        {
            "requests": requests
        }
    )
@login_required
def accept_request(request, request_id):

    swap_request = get_object_or_404(
        SwapRequest,
        id=request_id,
        receiver=request.user,
    )

    swap_request.status = "Accepted"

    swap_request.save()

    return redirect("requests_list")
@login_required
def reject_request(request, request_id):

    swap_request = get_object_or_404(
        SwapRequest,
        id=request_id,
        receiver=request.user,
    )

    swap_request.status = "Rejected"

    swap_request.save()

    return redirect("requests_list")
@login_required
def sent_requests(request):

    requests = SwapRequest.objects.filter(
        sender=request.user
    )

    return render(
        request,
        "skills/sent_requests.html",
        {
            "requests": requests
        }
    )

# Create your views here.
