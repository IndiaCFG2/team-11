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
cd IPR_Website
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

Now go to login and enter the created username and password. Once logged in, create the team by filling in the required details and then skit and presentations data can easily be loaded using the forms in the UI. 


