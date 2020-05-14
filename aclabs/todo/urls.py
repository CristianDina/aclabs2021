""" URL Conf file for todo app."""

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    path('todos', views.todo_list, name="todo-list"),
    path('todos/<int:todo_id>', views.todo_interaction, name="todo-interaction"),

    # GraphQL routes
    path('graphqlapi/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
]
