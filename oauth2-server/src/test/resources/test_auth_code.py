```
Usage: python test_authorization_code.py xxx_auth_code
```
import requests, sys

authorization_code = sys.argv[1]

d = {'grant_type':'authorization_code','scope':'all','client_id':'admin','redirect_uri':'http://www.baidu.com','code':authorization_code}
r = requests.post('http://localhost:9401/oauth/token', auth=('admin', 'admin123456'), data=d)
result = r.json()
if 'access_token' not in result:
	print(result)
	sys.exit()

# use access_token getCurrentUser
access_token = result['access_token']
print("access_token: " + access_token)
headers = {"Authorization": "Bearer " + access_token}
result = requests.get("http://localhost:9401/user/getCurrentUser", headers=headers).json()
print(result)

