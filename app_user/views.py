from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib import messages
from .models import User, UserProfilePicture, Project, ProgrammingLanguage, Message
from .forms import (
    UserRegistrationForm,
    UserEditForm,
    AddProfilePictureForm,
    MessageForm,
)


class RegisterView(TemplateView):
    """
    View for a new user to register on the site.
    """

    model = User
    template_name = "app_user/register.html"

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            # automatically log the user in following account creation
            login(request, user)
            return redirect(reverse("app_user:profile"))
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
    """
    View for user to view their own profile.
    """

    model = User
    template_name = "app_user/user_profile.html"

    def get(self, request):
        user = request.user
        try:
            user_projects = Project.objects.filter(user=user)
        except:
            user_projects = None
        context = {
            "user": user,
            "user_projects": user_projects,
        }
        return render(request, "app_user/user_profile.html", context)


def delete_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user.delete()
    messages.success(request, "Profile successfully deleted!")
    return redirect(reverse("app_home:index"))


class EditProfileView(TemplateView):
    """
    View to edit the logged in user's profile
    """

    model = User
    template_name = "app_user/user_profile_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        context = {"form": UserEditForm(instance=user)}

        return render(request, "app_user/user_profile_edit.html", context)

    def post(self, request, *args, **kwargs):
        # get the current user (or return a 404)
        user = get_object_or_404(User, pk=request.user.pk)
        # add data to the form and save it
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated!")
            # redirect to main profile page
            return redirect(reverse("app_user:profile"))
        elif "profanity" in form.errors.as_text():
            messages.error(request, "Please do not use profanities in your username!")
        elif "duplicate_name" in form.errors.as_text():
            messages.error(request, "Username already in use! Please choose another")
        elif not form["p_language"].value():
            messages.error(request, "Please select at least one programming language")
        else:
            messages.error(request, "Form could not be submitted. Please try again.")
        return redirect(reverse("app_user:edit-profile"))


class EditProfilePicView(TemplateView):
    """
    View to add or delete a profile picture
    """

    model = User
    template_name = "app_user/profile_pic_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        # get all the pictures for the selected user
        pic_query_set = user.profile_pic.values()
        form = AddProfilePictureForm()
        context = {
            "user": user,
            "pictures": pic_query_set,
            "form": form,
        }

        return render(request, "app_user/profile_pic_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        # as there are two post methods (add and delete), they have a hidden input field
        # called "method" added to distinguish them

        # the add route
        if request.POST.get("method") == "add":
            new_picture = AddProfilePictureForm(
                request.POST, request.FILES, initial={"user": user}
            )
            if new_picture.is_valid():
                new_picture = new_picture.save(commit=False)
                new_picture.user = user
                new_picture.save()
            return redirect(reverse("app_user:edit-profile-pic"))

        # the delete route
        elif request.POST.get("method") == "delete":
            # retrieve the id from the post request in the template
            pic_id = int(request.POST["pic_id"])
            picture = get_object_or_404(UserProfilePicture, pk=pic_id)
            picture.delete()
        return redirect(reverse("app_user:edit-profile-pic"))


class Messages(TemplateView):
    """
    View of user's received and sent messages
    """

    model = Message
    template_name = "app_user/messages.html"

    def get(self, request):
        received_msgs = Message.objects.filter(user_receiver=request.user)
        sent_msgs = Message.objects.filter(user_sender=request.user)
        context = {
            "received_msgs": received_msgs,
            "sent_msgs": sent_msgs,
        }
        return render(request, "app_user/messages.html", context)


class IndividualMsg(TemplateView):
    """
    View of a specific selected message
    """

    model = Message
    template_name = "app_user/messages.html"

    def get(self, request, *args, **kwargs):
        message_pk = kwargs["pk"]
        message = Message.objects.get(pk=message_pk)
        if message.user_sender == request.user:
            msg_type = "sent"
        else:
            msg_type = "received"
        context = {
            "msg": message,
            "msg_type": msg_type,
        }
        return render(request, "app_user/individual_msg.html", context)


class AddMessage(TemplateView):
    model = Message
    template_name = "app_user:new_message.html"

    def get(self, request, *args, **kwargs):
        form = MessageForm(
            initial={"user_sender": request.user, "user_receiver": kwargs["pk"]}
        )
        context = {
            "sender": request.user,
            "receiver": get_object_or_404(User, pk=kwargs["pk"]),
            "form": form,
        }
        return render(request, "app_user/new_message.html", context)
