# A SCHOOL MANAGEMENT SYSTEM API
I designed this api for a quick mvp status for authentication, authorization tesing
- roles:
    - ADMIN
    - Management
    - Teachers
    - Non teaching staff
    - Student
    - Parents

- phase:
    - Admin add a managemnt user and then subsequent management usr can be onboarded by that management

## TEST
Test are available in [TEST_FOLDER](TEST_FOLDER)


## CURRENT DONE - Will be moed to internal soon
### Admin onboarding
A endpoint for an admin member to get onboard as we will not be using a normal interface
```json-GET

(domain is private)

```
Email must be a valid email and sy_secret only wil be granted by the sy team

### Disable Api
used middleware to stand as guard for every incoming request checking the status of the api before allowing it access

### ADDED RATE LIMITING TO THE ADMIN CREATE ACCOUNT ENDPOINT
TO avoid abuse, it caps at 60 seconds

### HAD ISSUES WITH THE MODELS USER_KEY BEIGN NULL
mean of auth cannot be null, so i used a placeholder - A random generated role key based on role type

### CREATE AN ENDPOINT FOR LOGIN
I implemented jwt for auth but i did not make it truly of database as i update the last login manually on every token pair obtained
This mean a little bit slower cycle. No rate limiting needed, the serializer already guard against attackers


### TOKEN REFRESH VIEW
An endpoint for collecting a new token access using the refresh key
I stil need  to find a way to nullify the former access key associated with that refresh key to avoid stolen identities

### Onboarding of Application from interested student 
Interested student sign up with email -> accoutn get created but deactivated -> they walk down to school / management send user_key -> then they can log in with user key

## NEXT TODO
### MANAGEMENT ONBOARDING BY THE SY TEAM
Onboarding the management team by any sy member



## Current Endpoints And Their Purpose
-------------------------------------------------------------------------------
### domain/api/account/
For accessing common data between all user type
#### domain/api/account/login/              -   POST    -user_key, password
#### domain/api/account/refresh_token/      -   POST    -refresh
#### domain/api/account/verify_token/       -   POST    -token
-------------------------------------------------------------------------------
### domain/api/onboarding/
Used by any new user account creation (currently support only interestee)
### domain/api/onboarding/student/          -   POST    -email, password