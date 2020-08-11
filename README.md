This repository is created for learing docker and aws.

## Requirement

- docker
- docker-compose

## Installation

First, clone the repo:

```bash
git clone https://github.com/SambhavChoradia/django-docker.git
```

### Usage

```bash
cd app
```

Build and run :

```
sudo docker-compose build
```

```
sudo docker-compose up db
```

Start mysql and create new user

```
sudo docker-compose exec db mysql -u root -p
```

```
create user 'docker'@'localhost' identified by 'password';
```

```
grant all privileges on docker.* to 'docker'@'localhost';
```

Start django app :

```
sudo docker-compose up api
```

Run migrations

```
sudo docker-compose exec api python manage.py migrate
```
