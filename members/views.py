from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Members


# Create your views here.
def index(request):
    #latest_question_list = Members.objects.order_by('-date_created')[:5]
    #output = ', '.join([q.first_name for q in latest_question_list])
    #return HttpResponse(output)

    list_of_members = Members.objects.order_by('-date_created')[:5]
    context = {'list_of_members': list_of_members}
    return render(request, 'members/index.html', context)
