from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib import messages
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserRegistrationForm, UserEditForm, AddProfilePictureForm


class RegisterView(TemplateView):
    model = User
    template_name = "app_user/register.html"

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            # automatically log the user in following account creation
            login(request, user)
            return redirect(reverse("app_user:success"))
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )

    def get(self, request, *args, **kwargs):
        # if the user is logged in, registration page is not available
        if request.user.is_authenticated:
            return redirect("/")

        registration_form = UserRegistrationForm
        # show user signup page
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )


class ProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user.delete()
    messages.success(request, "Profile successfully deleted!")
    return redirect(reverse("app_home:index"))


class EditProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        context = {"form": UserEditForm(instance=user)}

        return render(request, "app_user/user_profile_edit.html", context)

    def post(self, request):
        # get the current user (or return a 404)
        user = get_object_or_404(User, pk=request.user.pk)
        # add data to the form and save it
        form = UserEditForm(request.POST, instance=user)
        form.save()
        # redirect to main profile page
        return redirect(reverse("app_user:profile"))


class EditProfilePicView(TemplateView):
    model = User
    template_name = "app_user/profile_pic_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        pic_query_set = user.profile_pic.values()
        # picture_ids = []
        form = AddProfilePictureForm()
        # for picture in pic_query_set:
        #     breakpoint()
        # #     pictures.append(picture.id)
        context = {
            "user": user,
            "picture_q_set": pic_query_set,
            "form": form,
        }

        return render(request, "app_user/profile_pic_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        if request.POST.get("method") == "add":
            new_picture = AddProfilePictureForm(
                request.POST, request.FILES, initial={"user": user}
            )
            if new_picture.is_valid():
                new_picture = new_picture.save(commit=False)
                new_picture.user = user
                new_picture.save()
            return redirect(reverse("app_user:edit-profile-pic"))

        # elif request.POST.get("method") == "delete":
        #     pic_url = request.POST["pic_url"]
        # elif request.POST.get("method") == "delete":
        #     print("delete")
        #     user = get_object_or_404(User, pk=request.user.pk)
        #     pic_url = request.POST["pic_url"]
        #     for num in range(len(user.profile_pic.values())):
        #         if user.profile_pic.values()[num]["profile_picture"].url == pic_url:
        #             id_pic_to_delete = user.profile_pic.values()[num]["id"]
        #     picture = get_object_or_404(UserProfilePicture, pk=id_pic_to_delete)
        #     picture.delete()
        # return redirect(reverse("app_user:edit-profile-pic"))


# class DeleteProfilePicView(TemplateView):
#     model = UserProfilePicture
#     template_name = "app_user/profile_pic_edit.html"

#     def post(self, request, *args, **kwargs):
#         breakpoint()
#         pic_id = kwargs["id"]
#         picture = get_object_or_404(UserProfilePicture, pk=pic_id)
#         picture.delete()
#         messages.success(request, "Profile picture successfully deleted!")
#         return redirect(reverse("app_user:edit-profile-pic"))


def delete_profile_pic(request, *args, **kwargs):
    pic_pk = kwargs.pk
    pic = get_object_or_404(UserProfilePicture, pk=pic_pk)
    pic.delete()
    messages.success(request, "Profile picture successfully deleted!")
    return redirect(reverse("app_user:profile"))
