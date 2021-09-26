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
  curl -XGET "0.0.0.0:8000/api/questions 
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

- Sample Call: <br>
  ```
  ```

- Success Response
    
  - Code: `201` <br> 
  content:  `{"id":6,"user":"test","title":"title1","content":"content1","created_at":"2021-09-24T16:24:07.688698Z","updated_at":"2021-09-24T16:24:07.701209Z"}`

- Error Response:

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
  curl -XPOST\
  -H "Content-Type: application/json"\
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyNTM1Nzk0LCJqdGkiOiI5MWI4MTk1NTI3Yzk0ZmU5ODlkNDliMjdlNGQ4MjMyYyIsInVzZXJfaWQiOjJ9.X86zWl88r3YHNlAkGuuMGNdm3iDIu-zZKMawp63EkQI"\
  -d '{"title":"title1", "content":"content1"}'\
  0.0.0.0:8000/api/questions 
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

- Sample Call: <br>
  ```
  curl -XPOST\
  -H "Content-Type: application/json"\
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyNTM1Nzk0LCJqdGkiOiI5MWI4MTk1NTI3Yzk0ZmU5ODlkNDliMjdlNGQ4MjMyYyIsInVzZXJfaWQiOjJ9.X86zWl88r3YHNlAkGuuMGNdm3iDIu-zZKMawp63EkQI"\
  -d '{"title":"newtitle", "content":"content1"}'\
  0.0.0.0:8000/api/questions 
  ```

- Success Response
    
  - Code: `200` <br> 
  content:  `{"id":7,"user":"test","title":"newtitle","content":"content","created_at":"2021-09-25T03:03:05.305107Z","updated_at":"2021-09-25T03:03:12.880046Z"}`

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
  curl -xpost\
  -h "authorization: bearer eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyj0b2tlbl90exblijoiywnjzxnziiwizxhwijoxnjmyntm1nzk0lcjqdgkioii5mwi4mtk1nti3yzk0zmu5odlkndlimjdlngq4mjmyyyisinvzzxjfawqiojj9.x86zwl88r3yhnlakguumgndm3idiu-zzkmawp63ekqi"\
  0.0.0.0:8000/api/questions/7
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

- sample call: <br>
  ```
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

## show comments on question
## search comments
## like
## unlike
