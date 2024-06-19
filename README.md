# Django Auth Project Template

JWT Tokens will act as the permissions or authentication everytime we acesss a website. 
So, everytime we send a request to the backend it needs to know who we are and what permission we have, so we along with the request we send a token which can be decoded and understood to represent a certain set of permissions

Credentials are given to frontend, it passes them to backend and grants them token based on credentials. 

Access Token: request
Refresh Token: to refresh the access token
