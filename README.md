# Blood_Finder_Web_Application

## Project Description

From this web app one could contact with the blood donor very easily. The main aim is to provide fast and efficient way to gain attention of potential donors in the need of hour. 

## Python version: 3.9+

## Instructions to run the script

1. Goto the directory where you want to store your project.
2. Clone the git repository to the project directory.
3. Open the terminal and navigate to the project directory from the terminal.
4. Create virtual environment from the terminal by typing ```virtualenv venv``` and activate it by typing `source venv/bin/activate`(for Linux), `venv/Scripts/activate`(for Windows).
    * If you don't have `virtualenv` installed then install it by typing `pip install virtualenv`.
5. Install the project dependencies by typing `pip install -r requirements.txt` on the terminal.
7. Migrate the database by typing `python manage.py makemigrations` and then `python manage.py migrate` on the terminal.
8. Create admin user if you want by typing `python manage.py createsuperuser` and give the required credentials on the terminal.
9. Now, Run the project from your **localhost** by typing `python manage.py runserver`
10. Navigate to the URL [127.0.0.1:8000](127.0.0.1:8000) or [localhost:8000](localhost:8000) from your browser.
11. You can terminate the server anytime by **CTRL+c**.

### URL's I've implemented:
* index/
* register/
* profile/
* update-profile/
* search_blood/
* donerInfo/{pk}/
* login/
* logout/

## Snapshots:

* **index/**
![](./screen/01_home_1.png)
* **index/**
![](./screen/02_home_2.png)
* **login/**
![](./screen/03_login.png)
* **register/**
![](./screen/04_register.png)
* **search_blood/**
![](./screen/05_search_1.png)
* **search_blood/**
![](./screen/06_search_2.png)
* **profile/**
![](./screen/07_profile.png)
* **update-profile/**
![](./screen/08_update_profile.png)
* **donerInfo/1/**
![](./screen/09_doner_details.png)
* **logout/**
![](./screen/10_logout.png)
