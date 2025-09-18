# Python Skill Revival  
A series of exercises with increasing difficulty level to revive Python knowledge.

## Runtime environment  
Starting with this series of exercises I am also starting a GIT repository and a Docker development environment, this way, the 3 software technologies will be used and rehersed at the same time.  

### Docker  
The image is generated with the following command:  
- `docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) --build-arg USR=$(whoami) -t python_dev_image .`  

The 3 x `--build-arg` are passed so that inside the Dockerfile it can have the `userid`, `groupid` and `username` of the user in the host platform to create everything with the same credentials so file permissions are not a problem when sharing volumes and files, that way development cycle gets seamless inside the docker container for "this" project and is not coliding with other projects avoiding virtual envs.

The container is created in the following way:  
```
docker run -it --rm -v $(pwd):/app -p 8000:8000 --name python_dev_container python_dev_image /bin/bash
```  

That way the container:  
- remains open (`-it`), 
- shares the volume/directory of the aplication so each change done is available inside the container,
- Port 8000 is exposed, so web interaction is reflected inside the container for easy test, 
- and the /bin/bash shell is open for tests

## Exercises.md  
The Exercises.md file contains the definition of each exercise.

The levels listed are:
- Level 1: Syntax & Core Concepts Refresh
- Level 2: Data Structures & Algorithms
- Level 3: Object-Oriented Programming (OOP)
- Level 4: Intermediate & Job-Readiness Concepts
- Level 5: Advanced & Real-World Simulation

And there are some tips:
*   **Don't Just Code, Refactor**
*   **Version Control**
*   **Read the Docs**
*   **Virtual Environments**, here replaced by **Docker**.