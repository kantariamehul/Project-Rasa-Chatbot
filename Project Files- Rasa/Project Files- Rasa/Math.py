import requests

def Math_is_fun():

	url = "https://random-math-problem.p.rapidapi.com/random-problem"

	querystring = {"type":"text"}

	headers = {
		"X-RapidAPI-Host": "random-math-problem.p.rapidapi.com",
		"X-RapidAPI-Key": "694de9ccf2msh9d39ce5d36d984cp1c7ae4jsn3176a528dd6d"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	response_text=response.text

	print(response_text)

	return response_text

Math_is_fun()