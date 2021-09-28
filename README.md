# board-api

<br>

# Questions
## Show Questions List

- URL: `/api/board/questions`
- Method:  `GET` 
- URL params: `Unrequired`
- Request Header: `Unrequired`
- Sample Call: <br>
  ``` 
  curl --location --request GET '0.0.0.0:8000/api/board/questions?title=t' 
  ```
- Success Response
  - code: `200` <br> 
  content:  `[{"id":1,"user":"김순태","title":"title","content":"content","created_at":"2021-09-24T15:26:10.290574Z","updated_at":"2021-09-24T15:38:08.058355Z"}, ..."`

<br>
<br>

## Search Questions

- URL: `/api/board/questions`
- Method:  `GET` 
- URL params: <br>
  Required: `title=[string]` or `content=[string]`
- Request Header: `Unrequired`
- Sample Call: <br>
  ``` 
  curl --location --request GET '0.0.0.0:8000/api/board/questions
  ```
- Success Response
  - code: `200` <br> 
  content:  `[{"id":1,"user":"김순태","title":"title1","content":"content1","created_at":"2021-09-24T15:26:10.290574Z","updated_at":"2021-09-24T15:38:08.058355Z"}, {...}`

<br>
<br>

## Create Question

- URL: `/api/board/questions`
- Method: `POST` 
- URL params: `Unrequired`
- Request Header: `Authorization: Bearer Token {access token}`
- Request Data: `{"title" : "title1", "content" : "content1}`
- Sample Call: <br>
  ```
  curl --location --request POST '0.0.0.0:8000/api/board/questions' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc' \
  --header 'Content-Type: application/json' \
  --data-raw '{"title" : "title1", "content":"content1"}'
  ```
- Success Response
  - Code: `201` <br> 
  content:  `{"id":13,"user":"김순태","title":"title1","content":"content1","created_at":"2021-09-28T03:03:55.569888Z","updated_at":"2021-09-28T03:03:55.569936Z"}`
- Error Response:
  - Code: `400 Bad Request` <br>
  content: `{"content":["This field is required."]}`
  - Code: `401 Aunauthorized` <br>
    Content: `{"detail":"Authentication credentials were not provided."}`
  
<br>
<br>

## Show Question Detail

- URL: `/api/board/questions/<:id>`
- Method: `GET` 
- URL params: <br>
  Required: `id=[integer]`
- Request Header: <br>
`Authorization: Bearer Token {access token}`<br>
`Content-Type: application/json`
- Sample Call: <br>
  ```
  curl --location --request GET '0.0.0.0:8000/api/board/questions/16' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc'
  ```
- Success Response   
  - Code: `200` <br> 
  content:  `{"id":1,"user":"김순태","title":"title1","content":"content1","created_at":"2021-09-24T15:26:10.290574Z","updated_at":"2021-09-24T15:38:08.058355Z"}`
- Error Response:<br>
  - Code: `401 UNAUTORIZED` <br>
    Content: `{"detail":"Authentication credentials were not provided."}`
  - Code: `404 NOT FOUND` <br>
    Content: `{"detail":"Not found."}`

<br>
<br>

## Modify Question Detail

- URL: `/api/board/questions/<:id>`
- Method: `PATCH` 
- URL params: <br>
  Required: `id=[integer]`
- Request Header: <br>
`Authorization: Bearer Token {access token}`<br>
`Content-Type: application/json`
- Reqest Data: <br>
`{"title" : "newtitle"}` or <br>
`{"content" : "newcontent"}` or <br>
`{"title":"newtitle", "content":"newcontent"}`
- Sample Call: <br>
  ```
  curl --location --request PATCH '0.0.0.0:8000/api/board/questions/16' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc' \
  --header 'Content-Type: application/json' \
  --data-raw '{"title" : "title"}'
  ```
- Success Response    
  - Code: `200` <br> 
  content:  `{"id":16,"user":"김순태","title":"title","content":"content","created_at":"2021-09-28T03:11:18.082282Z","updated_at":"2021-09-28T03:14:20.819224Z"}`
- Error Response:<br>
  - Code: `401 UNAUTORIZED` <br>
    Content: `{"detail":"Authentication credentials were not provided."}` <br>
  - Code: `403 FORBIDDEN` <br>
    Content: `{"detail":"You do not have permission to perform this action."}`
  - Code: `404 NOT FOUND` <br>
    Content: `{"detail":"Not found."}`

<br>
<br>

## delete question detail

- url: `/api/board/comments`
- method: `delete` 
- url params: <br>
  required: `id=[integer]`
- request header: <br>
`authorization: bearer token {access token}`<br>
- sample call: <br>
  ```
  curl --location --request DELETE '0.0.0.0:8000/api/board/questions/15' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc'
  ```
- success response  
  - code: `204 no content` <br> 
  content:
- error response:<br>
  - code: `401 unautorized` <br>
    content: `{"detail":"authentication credentials were not provided."}` <br>
  - code: `403 forbidden` <br>
    content: `{"detail":"you do not have permission to perform this action."}`
  - code: `404 not found` <br>
    content: `{"detail":"not found."}`

<br>
<br>

# Comments
## create comment
- url: `/api/board/comments`
- method: `post` 
- url params: <br>
  unrequired: 
- request header: <br>
`authorization: bearer token {access token}`<br>
`Content-Type: application/json`
- Reqest Data: <br>
`{"question" : 1, "content" : "comment content}` 
- sample call: <br>
  ```
  curl --location --request POST '0.0.0.0:8000/api/board/comments' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc' \
  --header 'Content-Type: application/json' \
  --data-raw '{"question" : 16, "content" : "asdf"}'
  ```
- success response
  - code: `201 created` <br>
  content: `{"id":27,"user":"김순태","question":16,"content":"asdf","created_at":"2021-09-28T03:23:30.447388Z","updated_at":"2021-09-28T03:23:30.447430Z"}`
- error response:<br>
  - code: `401 unautorized` <br>
    content: `{"detail":"authentication credentials were not provided."}` <br>
  - code: `403 forbidden` <br>
    content: `{"detail":"you do not have permission to perform this action."}`
  - code: `404 not found` <br>
    content: `{"detail":"not found."}`

<br>
<br>

## show comments on question

- url: `/api/board/questions/16/comments`
- method: `get` 
- url params: <br>
  unrequired: 
- request header: <br>
`authorization: bearer token {access token}`<br>
- Reqest Data: <br>
  unrequired:
- sample call: <br>
  ```
  curl --location --request GET '0.0.0.0:8000/api/board/questions/16/comments' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc'
  ```
- success response
  - code: `201 created` <br>
  content: `[{"id":26,"user":"김순태","question":16,"content":"adsf","created_at":"2021-09-28T03:22:59.120207Z","updated_at":"2021-09-28T03:22:59.120249Z"},{"id":27,"user":"김순태","question":16,"content":"asdf","created_at":"2021-09-28T03:23:30.447388Z","updated_at":"2021-09-28T03:23:30.447430Z"}, ...]`
- error response:<br>
  - code: `401 unautorized` <br>
    content: `{"detail":"authentication credentials were not provided."}` <br>
  - code: `403 forbidden` <br>
    content: `{"detail":"you do not have permission to perform this action."}`
  - code: `404 not found` <br>
    content: `{"detail":"not found."}`


# like/unlike

## create like
- url: `/api/board/like/question`
- method: `post` 
- url params: <br>
  unrequired: 
- request header: <br>
`authorization: bearer token {access token}`<br>
`Content-Type: application/json`
- Reqest Data: <br>
`{"question" : "1"}` 
- sample call: <br>
  ```
  curl --location --request POST '0.0.0.0:8000/api/board/like/question' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc' \
  --data-raw '{"question" : "1"}'
  ```
- success response
  - code: `201 created` <br>
  content: `{"id":153,"question":1,"user":"김순태"}`
- error response:<br>
  - code: `400 bad request` <br>
    content: `["You are already liked to this question"]` <br>

<br>
<br>

## delete like

- url: `/api/board/unlike/question/1`
- method: `delete` 
- url params: <br>
  unrequired: 
- request header: <br>
`authorization: bearer token {access token}`<br>
- Reqest Data: <br>
  unrequired:
- sample call: <br>
  ```
  curl --location --request DELETE '0.0.0.0:8000/api/board/unlike/questions/1' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODMzOTA0LCJqdGkiOiI3M2MzZTY4OGQ1ODg0NmMzYmVlOWYxM2Q1YTEwMDg5YSIsInVzZXJfaWQiOjF9.d0zwT-h4U3QHRrJ1TsO7XSV_ISmtnTkaK9xmhy1qnyc'
  ```
- success response
  - code: `204 no content` <br>
  content: `{}`
- error response:<br>
  - code: `400 bad request` <br>
    content: `{"detail":"You are not liked to this question"}` <br>

<br>
<br>