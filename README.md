# teammanagementsystem
Team management system (supports below):
listing team members, 
adding a new team member, 
editing an existing team member 
and deleting a team member


Installations:
1. Please install django_mysql module using pip install django-mysql command.
2. This project used MySQL database. Please create the database manaully using CREATE DATABASE command with the name as teammanagementsystem
3. Run migrations using python manage.py migrate on terminal after CD-ing to the project folder.

Command to run server:
python manage.py runserver

Curl commands:
Listing: curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/teammembers/members/

Adding: curl -d "first_name=dummy&last_name=tummy&phone_number=9821143210&email=dummy@example.com&role=regular" -X POST http://127.0.0.1:8000/teammembers/addmember/

Editing: curl -d "first_name=dummy_edited&last_name=tummy_edited&phone_number=9821143210&email=dummy@example.com&role=admin&id=5" -X POST http://127.0.0.1:8000/teammembers/editmember/

Deleting: curl -d "id=12" -X POST http://127.0.0.1:8000/teammembers/deletemember/



SQLs: Below is the SQL generated using sqlmigrate command
"""
BEGIN;
--
-- Create model Member
--
CREATE TABLE `teammembers_member` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(200) NOT NULL, `last_name` varchar(200) NOT NULL, `phone_number` varchar(20) NOT NULL, `email` varchar(254) NOT NULL, `role` enum('admin','regular') NOT NULL);
COMMIT;
"""

Note: Database is not included in the repo.