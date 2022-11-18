import requests

r = requests.get('https://xkcd.com/353/')

# print(help(r))

# html response: if you wanna parse html response you should use html parser
# print(r.text)

# Downloading an image
# https://imgs.xkcd.com/comics/python.png
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)  # We get byte results

# Getting byte contents and storing them as an image file
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

print(60 * '-')

# Checking the status of response

# print(r.status_code)  # 200
'''
Status Code
200: Success
300: Redirect
400: Client Errors - like when you are trying to access a page and you don't have the permission
500: Server Errors - like sometimes that a website crashes and you can't use it
'''
print(r.ok)  # True. True for anything that has a value less than 400
# False for 400 and 500 status codes
print(r.headers)  # Shows the information about the website. It returns headers with response
# For Example:
# 'Server': 'nginx'
# 'Content-Type': 'image/png'

print(60 * '-')
# ==============================================
# httpbin
# We can test http methods like: delete, patch, get, put, post
# We can test Authentication

# # get method and adding some parameters to the url
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
# print(r.url)    # https://httpbin.org/get?page=2&count=25
# # these are get parameters


# # ==============================================
# # post method
# payload = {'username': 'mehdi', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# # print(r.text)
# r_dict = r.json()
# print(r_dict)
# # {'args': {}, 'data': '', 'files': {}, 'form': {'password': 'testing', 'username': 'mehdi'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '31', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-6302400b-0489e23f1be9019166071dc2'}, 'json': None, 'origin': '78.39.245.200', 'url': 'https://httpbin.org/post'}
# # Now We have access to key value pairs
# print(r_dict['form'])   # {'password': 'testing', 'username': 'mehdi'}

# =================================================================================
# Putting right username and password
# r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(r.text)
# print(r)  # <Response [401]>
# # {
# #   "authenticated": true,
# #   "user": "corey"
# # }

# =================================================================================

# Wrong username
# r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('coreyms', 'testing'))
# print(r)
# <Response [401]>  # Unauthorized response code

# => extra <==
# We can use all this for monitoring website if your website didn't respond that means something's worng
# But we need to use a timeout for this

# =================================================================================
# using timeout parameter
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)  # <Response [200]>
'''
we can use this in httpbin.org
Dynamic data 
    Get/delay/{delay} Returns a delayed response(max of 10 seconds)

=> if we set delay value more than timeout value then we will
get an exception which is ReadTimeout
overall it's better to use timeout parameter for your requests
'''

# url = 'https://icanhazip.com'
# method = 'GET'
# response = requests.request(method, url)

# print(response.text)
# 123.321.123.321
# You can use the 'curl' command to get your ip:
# => curl https://icanhazip.com

# ===============================================
'''
Methods
- delete(url, args)             Sends a DELETE request to the specified url
- get(url, params, args)        Sends a GET request to the specified url
- head(url, args)               Sends a HEAD request to the specified url
- patch(url, data, args)        Sends a PATCH request to the specified url
- post(url, data, json, args)   Sends a POST request to the specified url
- put(url, data, args)          Sends a PUT request to the specified url
- request(method, url, args)    Send a request of the specified method to the specified url
'''

# Example
url = 'http://ma-web.ir/maktab64/'
method = 'GET'
get_response = requests.request(method, url, params={'name': 'akbar'})  # = request.get(url, ...)
print(get_response.content)
# result => b'<p>your method is:<p><H1>GET</H1><p>Hello akbar!</p>'

get_response = requests.post(url, data={'name': 'akbar'})
print(get_response.text)
# <p>your method is:<p><H1>POST</H1><p>Hello akbar!</p>
