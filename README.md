# Proxy Reverse and Load Balance

Developed for help to create containerized projects using Docker with Nginx features.

## Installation
1. Install Docker and Docker Compose.
2. Clone this repository or fork this repository:
```bash
git clone https://github.com/heytorvas/template-nginx-docker.git
```
3. Change directory to repository:
```bash
cd template-nginx-docker
```

## Environment
1. Build the containers:
```bash
docker-compose build &
```

## Reverse Proxy
1. Up the containers:
```bash
docker-compose up nginx_rp &
```
2. Run project:
```bash
http://localhost/server1
http://localhost/server2
http://localhost/server3
```

## Load Balance
1. Up the containers:
```bash
docker-compose up nginx_lb &
```
2. Run project:
```bash
http://localhost
```
