# board-api
## Show Questions List

- URL: `/api/questions`

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

- URL: `/api/questions`

- Method: `POST` 

- URL params: `Unrequired`

- Request Header: `Authorization: Bearer Token {access token}`

- Sample Call: <br>
  ```
  curl -XPOST\
  -H "Content-Type: application/json"\
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyNTM1Nzk0LCJqdGkiOiI5MWI4MTk1NTI3Yzk0ZmU5ODlkNDliMjdlNGQ4MjMyYyIsInVzZXJfaWQiOjJ9.X86zWl88r3YHNlAkGuuMGNdm3iDIu-zZKMawp63EkQI"\
  -d '{"title":"title1", "content":"content1"}'\
  0.0.0.0:8000/api/questions 
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

- URL: `/api/questions/<:id>`

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

- URL: `/api/questions/<:id>`

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

## Delete Question Detail

- URL: `/api/questions/<:id>`

- Method: `DELETE` 

- URL params: <br>
  Required: `id=[integer]`

- Request Header: <br>
`Authorization: Bearer Token {access token}`<br>

- Sample Call: <br>
  ```
  curl -XPOST\
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyNTM1Nzk0LCJqdGkiOiI5MWI4MTk1NTI3Yzk0ZmU5ODlkNDliMjdlNGQ4MjMyYyIsInVzZXJfaWQiOjJ9.X86zWl88r3YHNlAkGuuMGNdm3iDIu-zZKMawp63EkQI"\
  0.0.0.0:8000/api/questions/7
  ```

- Success Response
    
  - Code: `204 NO CONTENT` <br> 
  content:

- Error Response:<br>
  - Code: `401 UNAUTORIZED` <br>
    Content: `{"detail":"Authentication credentials were not provided."}` <br>

  - Code: `403 FORBIDDEN` <br>
    Content: `{"detail":"You do not have permission to perform this action."}`

  - Code: `404 NOT FOUND` <br>
    Content: `{"detail":"Not found."}`