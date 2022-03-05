# flaskProject
A synthesis of a couple projects I've done in the past, but now in Python. A REST API with authorization and KDC authentication.

The app is going to allow users to add Pokemon(because why not?) to their account, modify them, and remove them. Admin will have permission to manage users' Pokemon. Everything 
will be secured with a KDC. The app and KDC will be run from seperate Docker containers.

### **TODO:** 
- Create an API for Pokemon management
- Add front-end support for the API
- Create an API for Users, Roles
- Make sure that it works with DB relations
- Create separate views for user and admin permissions
- Add KDC support
- Containerize the whole thing
