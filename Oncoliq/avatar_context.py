from .views import getAvatar

def avatar_context_processor(request):
    avatar = getAvatar(request)
    return {'avatar':avatar}