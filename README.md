# Yit_Django

A django project with register,login and homepage.

# Deployment
download the Yit_Django and un zip it.

open cmd use the command ```cd "path to project"\Yit_Django-main```

it is recommended to create a virtualenv and use it with the command ```python -m venv "name of env"```

use virtualenv with the command
```name of env\Scripts\activate.bat```

move to the site folder using the command ```cd mysite```

pip install the needed models using the command ```pip install .```

migrate the project with the command ```python manage.py migrate```

now that the data base is all set up run the command ```python manage.py runserver```

# About the project

the project support 4 pages:

login page located at http://127.0.0.1:8000/login/

register page located at http://127.0.0.1:8000/register/

home page located at http://127.0.0.1:8000/homepage/

the basic admin page for easy database managment at http://127.0.0.1:8000/admin/

only loged-in users can reach homepage.
