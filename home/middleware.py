# # from django.http import HttpResponseForbidden
# from django.shortcuts import render
# from django.http import HttpResponseForbidden
# from menu.models import Pages

# class GroupAccessMiddleware:
#     """
#     Middleware to restrict access based on user groups and request paths.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         aa = Pages.objects.all()
#         for item in aa:
#             print(item.link_page.url)
#         # Define paths that should be restricted
#         restricted_paths = ['/abc/']
#         allowed_group = 'AccessGroup'  # Define the user group that should have access
        
#         # Check if the current request path is restricted
#         if request.path in restricted_paths:
#             # Check if the user is authenticated and in the allowed group
#             if request.user.is_authenticated:
#                 if not request.user.groups.filter(name=allowed_group).exists():
#                     return render(request, '403.html', status=403)
#             else:
#                 return render(request, '403.html', status=403)

#         return self.get_response(request)



# from django.shortcuts import render
# from menu.models import Pages, AccessPages

# class GroupAccessMiddleware:
#     """
#     Middleware to restrict access based on user groups and request paths.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
        
#         restricted_paths = {}
#         pages = Pages.objects.all()
#         for page in pages:
#             if page.link_page:
#                 url = page.link_page.url
#                 user_groups = request.user.groups.all()
#                 for group in user_groups:
#                   allowed_group = group.name
#                 if url:
#                     restricted_paths[url] = allowed_group
        

#         # Fetch all pages and dynamically add their URLs to restricted paths
#         restricted_paths = [item.link_page.url for item in Pages.objects.all() if item.link_page]
#         print("restricted_paths", restricted_paths)
        
        
#         user_groups = request.user.groups.all()
#         for group in user_groups:
#            allowed_group = group.name
        
#         # Define the user group that should have access
#         # allowed_group = 'Moderators'
        
#         # Check if the current request path is restricted
#         if request.path in restricted_paths:
#             # Check if the user is authenticated and in the allowed group
#             if request.user.is_authenticated:
#                 if not request.user.groups.filter(name=allowed_group).exists():
#                     return render(request, '403.html', status=403)
#             else:
#                 return render(request, '403.html', status=403)

#         return self.get_response(request)




# from django.shortcuts import render
# from menu.models import Pages,AccessPages



# class GroupAccessMiddleware:
#     """
#     Middleware to restrict access based on user groups and request paths.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Initialize restricted_paths dictionary
#         restricted_paths = {}

#         # Fetch all Pages and dynamically create a path-to-groups mapping
#         pages = Pages.objects.all()
#         for page in pages:
#             if page.link_page:
#                 url = page.link_page.url
#                 allowed_groups = AccessPages.objects.all().values_list('group', flat=True)  # Assuming Pages model has a many-to-many field 'allowed_groups'
#                 if url:
#                     restricted_paths[url] = list(['Moderator'])

#         print(restricted_paths)
#         # Check if the current request path is restricted
#         if request.path in restricted_paths:
#             # Check if the user is authenticated
#             if request.user.is_authenticated:
#                 # Get the groups the user belongs to
#                 user_req = request.user.groups.all()
#                 for group in user_req:
#                   print("request.user.groups", group.id)
#                   user_groups = group.name
                 
#                 # Get allowed groups for the current path
#                 allowed_groups = restricted_paths.get(request.path, [])

#                 # Check if the user is in any of the allowed groups for the current path
#                 if not any(group in user_groups for group in allowed_groups):
#                     return render(request, '403.html', status=403)
#             else:
#                 return render(request, '403.html', status=403)

#         return self.get_response(request)







from django.shortcuts import render
from menu.models import Pages, AccessPages, Privileges

class GroupAccessMiddleware:
    """
    Middleware to restrict access based on user groups and request paths.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Initialize restricted_paths dictionary
        restricted_paths = {}

        # Fetch all Privileges and dynamically create a path-to-groups mapping
        privileges = Privileges.objects.all()
        for privilege in privileges:
            for access_page in privilege.page_access.all():
                for page in access_page.pages.all():
                    url = page.link_page.url if page.link_page else '#'
                    allowed_groups = access_page.group.name
                    if url and allowed_groups:
                        restricted_paths[url] = restricted_paths.get(url, []) + [allowed_groups]

        print("Restricted Paths:", restricted_paths)
        
        # Print user groups for debugging
        if request.user.is_authenticated:
            user_req = request.user.groups.all()
            user_groups = [group.name for group in user_req]  # List of user group names
            print("Request User Groups (IDs and Names):")
            for group in user_req:
                print(f"ID: {group.id}, Name: {group.name}")
        else:
            user_groups = []

        # Check if the current request path is restricted
        if request.path in restricted_paths:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Get allowed groups for the current path
                allowed_groups = restricted_paths.get(request.path, [])

                # Check if the user is in any of the allowed groups for the current path
                if not any(group in user_groups for group in allowed_groups):
                    return render(request, '403.html', status=403)
            else:
                return render(request, '403.html', status=403)

        return self.get_response(request)
