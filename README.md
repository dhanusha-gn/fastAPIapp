# fastAPIapp

## creating fastAPI  application

# Architecture of fastapi application
-model--tables creation
-router --routes requests to controllers
-controller --controller logic
-service --business logic
-repository --data access layer
-middleware -- request processing pipeline

# database
## non-realtional database
-mongodb
-dynamodb
-redils

# constraints in database
-primary key --eg: student_id
-foreign key --eg: dept_id in student table
-unique --eg:email,phonenumber
-not null --eg:name
-check --eg:salary>0
-default --eg:timestamp:func.now()