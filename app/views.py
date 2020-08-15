from django.shortcuts import render
import string, random

# Create your views here.
def home(request):
	return render(request, 'app/index.html')

def password(request):
	chars = list(string.ascii_lowercase)
	req = {}
	if request.GET.get('ucase'):
		req['ucase'] = True
		chars.extend(list(string.ascii_uppercase))

	if request.GET.get('schar'):
		req['schar'] = True
		chars.extend(list(string.punctuation))

	if request.GET.get('num'):
		req['num'] = True
		chars.extend(list(string.digits))

	length = int(request.GET.get('length', 12))
	req['length'] = length

	generated_password = ''
	for x in range(length):
		generated_password += random.choice(chars)

	return render(request, 'app/index.html', {'req':req, 'password':generated_password})