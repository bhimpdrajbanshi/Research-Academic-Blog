# from django.http import HttpResponseForbidden
from django.shortcuts import render
 
# class GroupAccessMiddleware:
#     """
#     Middleware to restrict access based on user groups and request paths.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Define paths that should be restricted
#         restricted_paths = ['/abc/']
#         allowed_groups = ['AccessGroup']  # Define the user group that should have access
        
#         # Check if the current request path is restricted
#         if request.path in restricted_paths:
#             # Check if the user is authenticated and in the allowed group
#             if request.user.is_authenticated:
#                 user_groups = request.user.groups.values_list('name', flat=True)
#                 if any(group in allowed_groups for group in user_groups):
#                     return self.get_response(request)
#                 else:
#                     return HttpResponseForbidden("You do not have access to this page.")
#             else:
#                 return render(request, 'login.html')  # Redirect to login if user is not authenticated

#         return self.get_response(request)





from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse

class GroupAccessMiddleware:
    """
    Middleware to restrict access based on user groups and request paths.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define paths that should be restricted
        restricted_paths = ['/abc/']
        allowed_group = 'AccessGroup'  # Define the user group that should have access
        
        # Check if the current request path is restricted
        if request.path in restricted_paths:
            # Check if the user is authenticated and in the allowed group
            if request.user.is_authenticated:
                if not request.user.groups.filter(name=allowed_group).exists():
                    return render(request, '403.html', status=403)
            else:
                return render(request, '403.html', status=403)

        return self.get_response(request)
