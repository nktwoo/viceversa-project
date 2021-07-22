from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	word_list = user_text.split()
	number_of_words = len(word_list)
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'numberofwords':number_of_words})