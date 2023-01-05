# Main development repo for Koala Klub - Tree House

***
***

## Prerequisites
* [Docker & Docker Compose](https://docs.docker.com/desktop/) (<span style="color:orange">Local Development with Docker</span> only)
* [Github CLI](https://cli.github.com/) (<span style="color:orange">GitHub CLI installed on your machine)

***
***

## Repository
Clone or pull from the develop branch before you begin coding.
```
#cloning
git clone --branch develop git@github.com:HBARDEV/Koala-Klub-Treehouse.git

#pulling
git pull origin develop
```

***
***

## Celery Logs
Celery logs are kept away from GitHub. Therefore, we need to create the necessary directories.
```
cd backend
cd logs && echo This is our celery log > celery.log
cd ../..
```

***
***


## Environment variable and secrets
1. Create a .env file from .env.template
    ```
    #Unix and MacOS
    cp .env.template .env

    #windows
    copy .env.template .env
    ```

2. Update your new .env file. Work your way down the .env file and add secrets where necessary. Any questions in regards to secrets should be directed towards bobby@didcoding.com

***
***

## Fire up Docker:

>Note: You will need to make sure Docker is running on your machine!

Use the following command to build the docker images:
```
docker-compose -f compose/docker-compose.yml up -d --build
```
***
***


### Finished
You should now be up and running!

* Your database instances are accessible at [http://localhost:5050](http://localhost:5050)
* The web app is running on  http://localhost:8000

>Note: You can connect to the database in [http://localhost:5050](PGAdmin). All you need is the IP addresses (192.168.9.2) and database name (nft_alpha_dev).

***
***


### On first push to server

Open a fresh ubuntu terminal and use the following commands to create SSL certificates. Pay close attention to the domains, email and staging variables.
```
chmod +x init-letsencrypt.sh
sudo ./init-letsencrypt.sh
```

***
***

### Push code changes to stage (Staging)
Open a fresh terminal and use the following commands to 
```
git add -A
git commit -m "my message"
git push -u origin develop
gh pr create --head develop --base stage
***Type a title
***Type a body (optional)
***Press enter on 'Submit'
gh pr merge <pr number>
***Press enter on 'Click create merge commit'
***Type 'N'
***Press enter on 'Submit'
```

Your code has now been deployed to **Your stage domain**
***
***

### Push code changes to main (Production)
Open a fresh terminal and use the following commands to 
```
gh pr create --head stage --base main
***Type a title
***Type a body (optional)
***Press enter on 'Submit'
gh pr merge <pr number>
***Press enter on 'Click create merge commit'
***Type 'N'
***Press enter on 'Submit'
```

Your code has now been deployed to **Your prod domain**

***
***
