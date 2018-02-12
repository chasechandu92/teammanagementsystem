import json
from django.core import serializers
from django.db.utils import DataError
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from teammembers.models import Member

# Below method translates list of query-able objects to json object
def get_json(list_of_objects):
	serialized_data = serializers.serialize('python', list_of_objects)

	for item in serialized_data:
		item['fields']['id'] = item['pk']

	serialized_data_with_id = [item['fields'] for item in serialized_data]
	json_array = json.dumps(serialized_data_with_id)
	return json_array

# Below view/endpoint returns a json array of all team members
def members(request):
	members_list = Member.objects.all()
	json_array = get_json(members_list)
	return HttpResponse(json_array)

@csrf_exempt
def add_member(request):
	try:
		m = Member(first_name = request.POST.get('first_name')
			, last_name = request.POST.get('last_name')
			, phone_number = request.POST.get('phone_number')
			, email = request.POST.get('email')
			, role = request.POST.get('role')
			)
		m.save()
		output = get_json(Member.objects.filter(id=m.id))
		return HttpResponse(output)
	except DataError:
		return HttpResponseBadRequest('Data Error occured; Please check the data you have entered is per standards.\n')
