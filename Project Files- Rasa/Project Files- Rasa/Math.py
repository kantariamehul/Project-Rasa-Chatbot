import requests

def Math_is_fun():

	url = "https://random-math-problem.p.rapidapi.com/random-problem"

	querystring = {"type":"text"}

	headers = {
		"X-RapidAPI-Host": "random-math-problem.p.rapidapi.com",
		"X-RapidAPI-Key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	response_text=response.text

	print(response_text)

	return response_text

Math_is_fun()
