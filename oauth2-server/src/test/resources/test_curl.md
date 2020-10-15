```shell
curl -u admin:admin123456 -d "grant_type=authorization_code&scope=all&client_id=admin&redirect_uri=http://www.baidu.com&code=o4X1Yp" http://localhost:9401/oauth/token
```

{"access_token":"86ac023e-318e-45de-8320-9ff4ae740672","token_type":"bearer","expires_in":3599,"scope":"all"}

```shell
curl -H "Authorization: Bearer 86ac023e-318e-45de-8320-9ff4ae740672" http://localhost:9401/user/getCurrentUser
```

{"username":"macro","password":"$2a$10$kdMBhC6tEMkJGzMABKypbu3S2twgXw2Ft6w2waXjyz5Mb1nv0dbxe","authorities":[{"authority":"admin"}],"enabled":true,"credentialsNonExpired":true,"accountNonLocked":true,"accountNonExpired":true}
