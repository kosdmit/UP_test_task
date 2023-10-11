## What is this
This is a custom django template tag and django models for rendering your menu tree

## Getting Started

If you want use this in your project do next steps:
- copy models from models.py, apply migrations
- copy code from admin.py
- register custom tag from templatetags package
- add menu.html and menu_items.html to your templates
- add menu items using django admin panel
- use tag 'draw menu' in your templates

Below is instruction on setting up this project locally.
To get a local copy up and running it for testing follow these simple steps.

### Prerequisites
_Let's check if we are ready._

* This project uses Python 3.11. Check your python version:
  ```sh
  python --version
  ```
  *work on earlier versions is not guaranteed*

### Installation

_Let`s start._

1. Clone the repo
   ```sh
   git clone https://github.com/kosdmit/UP_test_task.git
   ```
2. Create and activate a virtual environment
   ```sh
   cd yourrepository
   virtualenv venv
   source venv\Scripts\activate
   ```
   If you are on Unix or MacOS, run this for activate virtual environment:  
   ```sh
   source  venv/bin/activate
   ```

3. Install required Python packages
   ```sh
   pip install -r requirements.txt
   ```
   
4. Create and apply migrations
   ```sh
   python mange.py makemigrations
   python manage.py migrate
   ```
   
5. That`s it! Run the Django server and test it!
   ```sh
   python manage.py runserver
   ```


## Thank you for attention!