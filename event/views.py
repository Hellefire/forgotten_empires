from django.core.exceptions import PermissionDenied
from django.shortcuts import render


def gameevent_list(request):
    if request.user.is_staff:
        return render(request, 'gm_gameevent.html')
    else:
        raise PermissionDenied


def shardevent_list(request):
    if request.user.is_staff:
        return render(request, 'gm_shardevent.html')
    else:
        raise PermissionDenied
