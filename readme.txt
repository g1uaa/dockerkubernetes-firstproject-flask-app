

1. this project is using following course


2. course link:

3. How to configure your project for dockers using:

-  Use Python 3.9 installation installed under c:\sw_install\python
-  Create virtual env using following link: https://docs.python.org/3/tutorial/venv.html 
-  can find dependencies (pkgs or modules like maven central repo) under python package index url at:
	https://pypi.org/search/?q=flask
	
	cmds used are:
	- create virtual env
	C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>%PYTHON% -m venv tutorial-venv39
	- check version of python inside virtual env to match the currently running python version (python 3.9.1 in our case)
	C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>dir tutorial-venv\Scripts\python.exe --version
	- activate the virtual env
	C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>tutorial-venv39\Scripts\activate.bat
	- install flask for webapp dependency
	(tutorial-venv39) C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>pip3 install flask
	- list all pkgs + libs inside your virtual env as
	pip list or pip freeze
	- write your libs to a file so can check into git with your project as
	(tutorial-venv39) C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>pip freeze > requirements.txt
	- run your module or program inside virtual env
	(tutorial-venv39) C:\training\udemy\free_dockers_kubernetes_pranjalSrivastava\dockers_ch02>python app.py 
 	

4. Run when your module 'app.py' as a script from cmd line (in the newly created virtual envt) as:
        python app.py, then

	- goto browser as: http://localhost:5001/

5. Build your docker image as below:
	- create a docker file
	- goto docker hub and get a version of 'python docker base image' to base your image (your dockerfile) off
		link: https://hub.docker.com/_/python   
		i chose buster as per instructor but newer version
	- build your docker image (based on your dockerfile that has build instructions as):
	docker build -t <tagname> <my dockerfile location> as:
	docker build -t flaskapp .
	- inspect your docker image in your local registry as:
	docker images
