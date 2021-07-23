from fcards.serializers import CardSerializer, CategorySerializer
from fcards.models import Category, Flashcard
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from fcards.forms import SignUpForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




@login_required(login_url='/accounts/login/')
def index(request):
    return HttpResponse('Hi there')


def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        profiles = Category.objects.all()
        serializer = CategorySerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CategorySerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryDetail(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlashcardList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        projects =Flashcard.objects.all()
        serializer = CardSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

