from django.shortcuts import redirect
def auth_middleware(get_response):

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl= request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')

        reponse=get_response(request)
        return reponse
    
    return middleware
