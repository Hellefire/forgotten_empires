from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def gm_character_list(request):
    if request.user.is_staff:
        return render(request, 'gm_character.html')
    else:
        raise PermissionDenied

