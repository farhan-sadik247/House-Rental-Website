# House-Rental-Website
# Overview
This house rental website is built using the Django framework which is a popular Python-based web development framework, along with Bootstrap for the front-end designing. It features a range of functionalities for house rentals, including user authentication, property listings, booking management, available dates, and comprehensive search capabilities.

On the backend, this project was built with python based Django framework along with some other libraries like Pillow(Image processing, Image Format Conversion, Image Filter), Requests(HTTP Requests which allow sending get, put, and delete requests to websites), etc. For the database, I use a relational database SQLite. On the front-end, I use typical HTML, along with the Bootstrap CSS framework for quick styling.

# Technologies Used

1. Programming Language: Python
2. Framework: Django
3. Database: SQL
4. HTML
5. Bootstrap CSS

# Project Features
The following are some of the main features of this house rental website project:
1. User Registration and Authentication: Users can create an account and log in to
add their properties to the website.
2. Property Creation: Registered users can add or list their rental houses or properties
on the website. Each registered user can add multiple properties through their
accounts.
3. Property Search: Users can explore and search through a diverse range of properties
available on the website. The homepage will display different properties randomly to
ensure fairness.
4. Property Information: Users or non-user accounts can view the properties present
on the homepage where they can scheme through property information like bedroom
number, locations, available date, owner phone number, etc.
5. Favorite List: Registered users can create a list of their favorite properties for easy
reference during their search.
6. User Profile management: Registered users can update their profile information
anytime they want.
7. Property Management: Property owners can add, update, or delete properties when
sold. Each property includes availability, property features, and rental details.



# Screenshots
![Home Page](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/4e067565-c4d1-4807-b1f8-95da1ea36359)
![Registration](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/2b2c2a0a-e217-4ea5-a8e8-20339f7dcac5)
![Login](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/4322c1ec-3a34-4918-bcc3-0e0e9de2e477)
![Add Property page](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/67d9a11c-a8ba-4f88-9ae2-d011fb3ded12)
![manage property 1](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/460035a7-eebc-4b8a-96f2-e629583d6c9f)
![manage property 2](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/f451a666-fb45-4590-af2c-1b839f5f0546)
![search 1](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/9a122662-8785-4204-bd24-78c264f93e7b)
![search 2](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/278e26b6-9b22-4d12-a560-42b772b30e7a)
![Property page](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/bfb2ae1c-f87b-483e-be7a-7bb2e620c138)
![Cart](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/9732b3ef-b4f0-431c-b7d3-3ff1f7a025c4)

# ER/EER and Schema Diagram
![CSE370 project ER](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/3d7d437e-8c5d-4fb9-b7a4-09bb64b930e5)
![ER schema diagram](https://github.com/farhan-sadik247/House-Rental-Website/assets/135944786/c456ddde-9e3c-4dee-ba6d-898d17743899)


## Commands to run the Project



```bash
python -m venv env
env/scripts/activate
pip install -r requirements.txt
python manage.py runserver

For SuperUser:
python manage.py createsuperuser  
```
    
