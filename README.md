# Shopping list app (Dockercompose Version)

Project of a simple shopping list website using **Python Flask** backend and a **PostgreSQL** database.
(use of dockercompose, docker networks, persistent volumes)

## Project Structure
We must be in the `App_Container/Docker_compose/` directory.

## Prerequisites
- Docker/Docker compose installed 

## Execution guide

Follow these steps to deploy the application:
(command lines to type are with a tabulation)

### 1. Create and run the whole project 
    docker compose up --build -d

### 2. Access the Application
Open your web browser and navigate to:
    http://localhost:5000

To test data persistence : 
1. add items to the list 
2. Destroy the conatiners and the network
    docker compose down
3. Re-create the app
    docker compose up -d
4. refresh the page, items should be there

clean up : 
    docker compose down