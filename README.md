# Django_project

A django project with register,login and homepage.

# Deployment
download the Django_project and un zip it.

open cmd use the command ```cd "path to project"\Django_project-main```

use virtualenv with the command
```workproject-env\Scripts\activate.bat```

move to the site folder using the command ```cd mysite```

migrate the project with the command ```python manage.py migrate```

now that the data base is all set up run the command ```python manage.py runserver```

# About the project

the project support 4 pages:

login page located at http://127.0.0.1:8000/login/

register page located at http://127.0.0.1:8000/register/

home page located at http://127.0.0.1:8000/homepage/

the basic admin page for easy database managment at http://127.0.0.1:8000/admin/

only loged-in users can reach homepage.
