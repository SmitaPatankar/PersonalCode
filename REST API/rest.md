# REST
- resources
- unique uri
- simple interface
- representation of resource
- stateless

# path parameters vs query parameters
```
https://xx/v1/boards/1234?name=xx&surname=xx
path parameter - v1, 1234 - identify resource/resources
query parameter - name, surname - sort/filter resources
```

# status codes
https://www.restapitutorial.com/httpstatuscodes.html

# headers
https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

# upload file
curl -F "data=@/home/smita/xyz.txt" url

# download file
curl -O url