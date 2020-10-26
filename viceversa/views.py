from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    len_of_original_word = len(user_text.split())
    return render(request, 'reverse.html', {'user_text': user_text,
                                            'reversed_text': reversed_text,
                                            'count_of_word': len_of_original_word})