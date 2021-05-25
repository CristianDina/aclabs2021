import datetime

import graphene
from graphene_django.types import DjangoObjectType

from todo.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class EditTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        text = graphene.String()
        priority = graphene.String()
        dueDate = graphene.String()
        completed = graphene.Boolean()

    todo = graphene.Field(TodoType)

    def mutate(self, info, id, text=None, priority=None, dueDate=None, completed=False):
        todo = Todo.objects.get(pk=id)
        if text is not None:
            todo.text = text
        if priority:
            todo.priority = priority
        if dueDate:
            todo.due_date = datetime.datetime.fromisoformat(dueDate)
        if completed:
            todo.completed = completed
        todo.save()
        return EditTodoMutation(todo=todo)


class AddTodoInput(graphene.InputObjectType):
    # all fields are optional
    text = graphene.String()
    priority = graphene.String()
    dueDate = graphene.String()
    completed = graphene.Boolean()


class AddTodoMutation(graphene.Mutation):
    class Arguments:
        todo = AddTodoInput(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, todo):
        # Added all fields here
        due_date = None
        completed = False
        if todo.dueDate:
            due_date = datetime.datetime.fromisoformat(todo.dueDate)
        if todo.completed is True:
            completed = True
        new_todo = Todo.objects.create(
            text=todo.text,
            priority=todo.priority or "LOW",
            due_date=due_date,
            completed=completed
        )
        return AddTodoMutation(todo=new_todo)


class DeleteTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    id = graphene.Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        todo = Todo.objects.filter(pk=kwargs.get("id")).first()
        count, _ = todo.delete()
        deleted = True if count == 1 else False
        return DeleteTodoMutation(ok=deleted)


class Mutation(graphene.ObjectType):
    edit_todo = EditTodoMutation.Field()
    add_todo = AddTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    todo = graphene.Field(
        TodoType,
        id=graphene.Int(),
        text=graphene.String()
    )

    def resolve_all_todos(self, info, **kwargs):
        return Todo.objects.all()

    def resolve_todo(self, info, **kwargs):
        _id = kwargs.get("id")
        _text = kwargs.get("text")

        if _id:
            return Todo.objects.get(id=_id)
        if _text:
            return Todo.objects.get(text=_text)
        return None


schema = graphene.Schema(query=Query, mutation=Mutation)
