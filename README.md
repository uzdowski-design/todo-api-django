# TASK MANAGER - REST API

## Procject Overview
This project provides and API service for a **TASK MANAGER** application.  
Created using *Django* and *Django REST framework*.  
API was set up according to *RESTful* convention.  
Data is stored in *SQLite3* database.

### Project Setup

It is advised to create a new virtual enviroment for new applications to keep them hermetic. 

Install *virtualenv*:
```
pip install virtualenv
```  
<br />

Create new virtual enviroment in new **env-name** directory using *virtualenv* package.
```
virtualenv <env-name>
```  
<br />

Ativate new virtual env with one of those commands.
```
. /<env-name>/bin/activate

or

source ./<env-name>/bin/activate
```  
<br/>

All dependencies can be installed from *requirements.txt* file.

```
pip install -r api/requirements.txt
```  
<br />
  

### API Routes

This is made with RESTful conventions and has two routes registered.
#### Lists Route
```
/lists
```  

#### Tasks Route
```
/tasks
```  
<br />

#### Allowed Methods
* GET
* POST
* PUT
* PATCH
* DELETE
* OPTIONS

All methots are set up with default RESTful API conventions.  

#### Calls Examples

Get all lists:
```
GET method to /lists/
```  
<br />

Update a list by **id**
```
PATCH method to /lists/id/
```
</br>

Delete a list by **id**
```
DELETE method to /lists/id/
```
</br>

***Note:*** *There is a relation between Tasks and Lists. Upon detelion of a list all tasks assossiated with that list will also be deleted.*
