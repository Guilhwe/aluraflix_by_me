from django.http import JsonResponse

def videos(request):
    if request.method == 'GET':
        video = {
            'id':'1',
            'titulo':'O que faz uma desenvolvedora front-end?',
            'url':'https://www.youtube.com/watch?v=ZY3-MFxVdEw',
            'decription':'O que é Front-end? Trabalhando na área os termos HTML, CSS e JavaScript fazem parte da rotina das desenvolvedoras e desenvolvedores. Mas o que eles fazem, afinal? Descubra com a Vanessa!'
        }   
        return JsonResponse(video)
