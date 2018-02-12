import json
from django.core import serializers
from django.http import HttpResponse
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
