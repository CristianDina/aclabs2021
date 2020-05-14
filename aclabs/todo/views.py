import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo


@csrf_exempt
def todo_list(request):
    supported_actions = {
        'POST': create_todo,
        'GET': retrieve_all_todos
    }
    if request.method not in supported_actions:
        return HttpResponse(status=405, content="METHOD NOT ALLOWED.")
    return supported_actions[request.method](request)


def create_todo(request):
    new_todo = Todo()
    new_todo.text = json.loads(request.body).get("text")
    new_todo.save()
    return HttpResponse(content=json.dumps({"todo_id": new_todo.pk}), status=201)


def retrieve_all_todos(request):
    return HttpResponse(content=json.dumps({"todos": {t.pk: t.text for t in Todo.objects.all()}}), status=200)


@csrf_exempt
def todo_interaction(request, todo_id):
    supported_actions = {
        'GET': retrieve_todo,
        'DELETE':  delete_todo,
        'PUT': update_todo
    }

    if request.method not in supported_actions:
        return HttpResponse(status=405, content="METHOD NOT ALLOWED.")
    return supported_actions[request.method](request, todo_id)


def retrieve_todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except ObjectDoesNotExist:
        return HttpResponse(status=404, content="NOT FOUND")

    return HttpResponse(content=json.dumps({
        "id": todo.pk,
        "text": todo.text,
        "priority": todo.priority,
        "completed": todo.completed
    }), status=200)


def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except ObjectDoesNotExist:
        return HttpResponse(status=404, content="NOT FOUND")
    todo.delete()
    return HttpResponse(status=200)


def update_todo(request, todo_id):
    return HttpResponse(status=501, content="METHOD NOT IMPLEMENTED")
