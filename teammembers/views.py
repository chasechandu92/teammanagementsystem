from django.db.utils import DataError
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from teammembers.models import Member


# Below view/endpoint returns a json array of all team members
def members(request):
	members_list = Member.objects.values()
	return JsonResponse({'results': list(members_list)})


# Below view/endpoint accepts data form and saves the data into Member table;
# returns a json array of the newly added team member along with the ID
@csrf_exempt
def add_member(request):
	try:
		mem = Member(first_name = request.POST.get('first_name')
			, last_name = request.POST.get('last_name')
			, phone_number = request.POST.get('phone_number')
			, email = request.POST.get('email')
			, role = request.POST.get('role')
			)
		mem.save()
		member = Member.objects.filter(id=mem.id).values()
		return JsonResponse({'results': list(member)})
	except DataError:
		return HttpResponseBadRequest('Data Error occured; Please check the data you have entered is per standards.\n')


# Below view/endpoint accepts data form and edits the data in the Member table using id column;
# returns a json array of the newly modified team member along with the ID
@csrf_exempt
def edit_member(request):
	if request.POST.get('id'):
		mem = Member.objects.filter(id=request.POST.get('id'))
		data_dict = {}
		for key in request.POST.keys():
			if key != 'id':
				data_dict[key] = request.POST.get(key)
		mem.update(**data_dict)
		member = mem.values()
		return JsonResponse({'results': list(member)})
	else:
		return HttpResponseNotFound('Please specify member id\n')


# Below view/endpoint accepts data form and deletes the data in the Member table using id column
@csrf_exempt
def delete_member(request):
	mem = Member.objects.filter(id=request.POST.get('id'))
	if mem:
		mem.delete()
		return HttpResponse('Team member with unique id - %s has been deleted successfully\n' % request.POST.get('id'))
	else:
		return HttpResponseNotFound('Entered unique id is not present in the database\n')
