## :pencil: Team Number - 11
## Non-profit Organisation - Key Education Foundation

### Problem Statement:
One-stop portal for teachers and employees for content management, progress tracking and overall analytics

### Our solution:
A website having numerous features seggregated based on user roles

#### Components: (In order of hierarchy)
1. Managers - Can add/remove employees
2. Employees - each employee serves 10-15 schools
3. Headmasters - representative of each school
4. Teachers - working at schools

#### Salient Features: :sparkles: :boom:
1. Data analytics
2. Simplified user experience
3. User oriented paths 
4. Interactive UI

## 🔧 Instructions to run
```
https://github.com/IndiaCFG2/team-11
```

### In the cloned repository
Execute 
```
cd KEF11
```

### Install all the requirements at once
```
pip3 install -r requirements.txt
```

### Create a superuser for login
Create your username and password of your choice
```
python3 manage.py createsuperuser
```

### Now you require to migrate all the database table schemas to the default sql database 
```
python3 manage.py makemigrations
```

### Migrate it
```
python3 manage.py migrate
```

### Now run the server
```
python3 manage.py runserver
```

## Hit the below URL
```http://127.0.0.1:8000/```





##### The code ("Code") in this repository was created solely by the student teams during a coding competition hosted by JPMorgan Chase Bank, N.A. ("JPMC").						JPMC did not create or contribute to the development of the Code.  This Code is provided AS IS and JPMC makes no warranty of any kind, express or implied, as to the Code,						including but not limited to, merchantability, satisfactory quality, non-infringement, title or fitness for a particular purpose or use.