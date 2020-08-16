from django.shortcuts import render
import string, random

# Create your views here.
def home(request):
	return render(request, 'app/index.html')

def password(request):
	req = {
		'ucase_len' : request.GET.get('ucase_len'),
		'schar_len' : request.GET.get('schar_len'),
		'num_len'   : request.GET.get('num_len'),
		'pass_len'  : request.GET.get('pass_len'),
	}
	char_len = {
		'pass_len'  : 0,
		'ucase_len' : 0,
		'num_len'   : 0,
		'schar_len' : 0,
	}
	generated_password = ''
	chars = list(string.printable.strip())
	while char_len['pass_len'] < int(req['pass_len']):
		r_chars = random.choice(chars)
		# lowecase
		if (r_chars.islower()):
			char_len['pass_len']+=1
			generated_password += r_chars
			continue
		# uppercase
		if (r_chars.isupper() and ( int(req['ucase_len']) == -1
		or char_len['ucase_len'] < int(req['ucase_len'])) ):
			char_len['pass_len']+=1
			char_len['ucase_len']+=1
			generated_password += r_chars
			continue
		# num
		if (r_chars.isnumeric() and ( int(req['num_len']) == -1
		or char_len['num_len'] < int(req['num_len'])) ):
			char_len['pass_len']+=1
			char_len['num_len']+=1
			generated_password += r_chars
			continue
		# symbols
		if (r_chars.isalnum() == False and (int(req['schar_len']) == -1
		or char_len['schar_len'] < int(req['schar_len'])) ):
			char_len['pass_len']+=1
			char_len['schar_len']+=1
			generated_password += r_chars
			continue

	return render(request, 'app/index.html', {'req':req, 'password':generated_password})