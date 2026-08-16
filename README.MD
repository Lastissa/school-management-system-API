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
    - Admin a managemnt user and then subsequent management usr can be onboarded by that management

## TEST
Test are available in [TEST_FOLDER](TEST_FOLDER)


## CURRENT DONE - Will be moed to internal soon
### Admin onboarding
A endpoint for an admin member to get onboard as we will not be using a normal interface
```json GET

/sy/_admin/email/password/sy_secret

```
Email must be a valid email and sy_secret only wil be granted by the sy team

### Disable Api
used middleware