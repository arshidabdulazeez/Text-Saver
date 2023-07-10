# Text-Saver / Snippet Saver


## Installation

Follow these steps to install the app.

 1. Clone the repository
 2. Run the below Commands for docker build
        cd Text-Saver (Change Directory to docker-compose.yml path)

        docker-compose -f  docker-compose.yml up -d --build

 3. Restore the Database

        docker cp new.sql snippets-saving-postgres:/new.sql
        docker exec -i snippets-saving-postgres psql -U postgres -d snippets < new.sql


##### Admin Credentials

	url      : http://localhost:8000/admin
    username : admin
	password : As@12345
		
##### Login API
API for Login.

	Endpoint : http://localhost:8000/api/login/
	Method : POST


##### Refresh API
API for Refresh.

	Endpoint : http://localhost:8000/api/refresh/
	Method : POST


##### Overview API
API will display the Total number of snippet and list all available snippets with a hyperlink to respective detail APIs.

	Endpoint : http://localhost:8000/api/snippets-overview/
	Method : GET


##### Create API
API to collect the snippet information and save the data to DB.

	Endpoint : http://localhost:8000/api/snippets-create/
	Method : POST
	Data : title,snippets,tag
	Data Example : {
		"title" : "Python",
		"snippets" : "Django Framework",
		"tag" : "Programming"
	}

##### Detail API
API will display the snippet title, content, and timestamp information.

	Endpoint : http://localhost:8000/api/snippets-details/<snippet_id>/
	Method : GET

##### Update API
API to update individual items. Update API should return item detail response.

	Endpoint : http://localhost:8000/api/snippets-update/<snippet_id>/
	Method : PUT
	Data : title,snippets
	Data Example : {
		"title" : "Python",
		"snippets" : "Flask Django Framework"
	}

##### Delete API
API to delete selected Snippets.

	Endpoint : http://localhost:8000/api/snippets-delete/<snippet_id>/
	Method : DELETE

##### Tag list API
API to list tags. It will return the tag id and tag title.

	Endpoint : http://localhost:8000/api/tag-list/
	Method : GET


##### Tag Detail API
API to return snippets linked to the selected tag.

	Endpoint : http://localhost:8000/api/tag-details/<tag_id>/
	Method : GET


## Technical Specifications

	Django version : 4.0.2
	Database used  : PostgreSQL
