from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import User, UserProfilePicture, Project, ProgramLang, Message
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

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            # automatically log the user in following account creation
            login(request, user)
            messages.success(
                request,
                f"Account successfully created. Welcome {user.username}!",
            )
            return redirect(reverse("app_user:profile"))
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )


class ProfileView(LoginRequiredMixin, TemplateView):
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
        try:
            p_langs = user.p_language.values()
        except:
            p_langs = None
        context = {
            "user": user,
            "p_langs": p_langs,
            "user_projects": user_projects,
        }
        return render(request, "app_user/user_profile.html", context)


class DeleteProfileView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        user.delete()
        messages.success(request, "Profile successfully deleted!")
        return redirect(reverse("app_home:index"))


class EditProfileView(LoginRequiredMixin, TemplateView):
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
            messages.error(
                request, "Please do not use profanities in your username!"
            )
        elif "duplicate_name" in form.errors.as_text():
            messages.error(
                request, "Username already in use! Please choose another"
            )
        elif not form["p_language"].value():
            messages.error(
                request, "Please select at least one programming language"
            )
        else:
            messages.error(
                request, "Form could not be submitted. Please try again."
            )
        return redirect(reverse("app_user:edit-profile"))


class AddProfilePicView(LoginRequiredMixin, TemplateView):
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
        new_picture = AddProfilePictureForm(
            request.POST, request.FILES, initial={"user": user}
        )
        if new_picture.is_valid():
            new_picture = new_picture.save(commit=False)
            new_picture.user = user
            new_picture.save()
            messages.success(request, "Picture successfully added!")
        return redirect(reverse("app_user:add-profile-pic"))


class DeleteProfilePicView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pic_to_delete = get_object_or_404(UserProfilePicture, pk=kwargs["pk"])
        if request.user == pic_to_delete.user:
            pic_to_delete.delete()
            messages.success(request, "Picture successfully deleted!")
            return redirect(reverse("app_user:add-profile-pic"))
        return redirect("app_home:about")


class Messages(LoginRequiredMixin, TemplateView):
    """
    View of user's received and sent messages
    """

    model = Message
    template_name = "app_user/messages.html"

    def get(self, request):
        received_msgs = Message.objects.filter(user_receiver=request.user)
        # set up pagination for messages (6 per page)
        paginator = Paginator(received_msgs, 6)
        page_number = request.GET.get("page")
        messages = paginator.get_page(page_number)
        p_nums = "p" * messages.paginator.num_pages
        context = {
            "msgs": messages,
            "p_nums": p_nums,
        }
        return render(request, "app_user/messages.html", context)


class SentMessages(LoginRequiredMixin, TemplateView):
    """
    View of user's received and sent messages
    """

    model = Message
    template_name = "app_user/sent_messages.html"

    def get(self, request):
        sent_msgs = Message.objects.filter(user_sender=request.user)
        # set up pagination for messages (6 per page)
        paginator = Paginator(sent_msgs, 6)
        page_number = request.GET.get("page")
        messages = paginator.get_page(page_number)
        p_nums = "p" * messages.paginator.num_pages
        context = {
            "msgs": messages,
            "p_nums": p_nums,
        }
        return render(request, "app_user/sent_msgs.html", context)


class IndividualMsg(LoginRequiredMixin, TemplateView):
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


class AddMessage(LoginRequiredMixin, TemplateView):
    model = Message
    template_name = "app_user:new_message.html"

    def get(self, request, *args, **kwargs):
        form = MessageForm(
            initial={
                "user_sender": request.user,
                "user_receiver": kwargs["pk"],
            }
        )
        context = {
            "sender": request.user,
            "receiver": get_object_or_404(User, pk=kwargs["pk"]),
            "form": form,
        }
        return render(request, "app_user/new_message.html", context)

    def post(self, request, *args, **kwargs):
        new_msg = MessageForm(request.POST)
        if new_msg.is_valid():
            new_msg = new_msg.save("new", commit=False)
            new_msg.user_sender_id = request.POST["sender"]
            new_msg.user_receiver_id = request.POST["receiver"]
            new_msg.save("new")
            messages.success(request, "Message sent!")
        return redirect("app_user:messages")


class EditMessage(LoginRequiredMixin, TemplateView):
    model = Message
    template_name = "app_user/edit_message.html"

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        receiver = get_object_or_404(User, pk=message.user_receiver_id)
        if message.user_sender == request.user:
            context = {
                "msg": message,
                "receiver": receiver,
                "form": MessageForm(instance=message),
            }
            return render(request, "app_user/edit_message.html", context)
        return redirect("app_user:messages")

    def post(self, request, *args, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save("edit")
            messages.success(request, "Message successfully updated.")
        else:
            messages.error(
                request, "Message could not be edited. Please try again."
            )
        return redirect(reverse("app_user:messages"))


class DeleteMessage(LoginRequiredMixin, TemplateView):
    model = Message

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        message.delete()
        messages.success(request, "Message successfully deleted!")
        return redirect(reverse("app_user:messages"))
