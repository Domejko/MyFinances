from django.shortcuts import redirect, render
from django.contrib import messages
from functools import wraps

from django.urls import reverse

from backend.models import TeamPermissions


def team_permission_required(redirect_url=None, permission=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.logged_in_as_team:
                team_perms = TeamPermissions.objects.filter(user=request.user, team=request.user.logged_in_as_team)
                team_permissions_list = [perm.permissions for perm in team_perms]

                if permission in team_permissions_list:
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "You don't have permission to do that.")
                    return redirect(reverse(redirect_url))
            elif request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return redirect(reverse(redirect_url))

        return _wrapped_view

    return decorator
