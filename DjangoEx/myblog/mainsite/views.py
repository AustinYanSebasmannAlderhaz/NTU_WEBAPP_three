from django.shortcuts import get_object_or_404, render
from .models import Character, Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'mainsite/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mainsite/post.html', {'post': post})


def character_list(request):
    characters = list(Character.objects.prefetch_related('images'))
    for character in characters:
        images = list(character.images.all())
        character.cover_image = images[0] if images else None
    return render(request, 'mainsite/character_list.html', {'characters': characters})


def character_detail(request, pk):
    character = get_object_or_404(Character.objects.prefetch_related('images'), pk=pk)
    images = list(character.images.all())
    return render(
        request,
        'mainsite/character_detail.html',
        {
            'character': character,
            'images': images,
        },
    )
