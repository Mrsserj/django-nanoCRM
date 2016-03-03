from django.contrib.auth.decorators import user_passes_test

def any_permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms))