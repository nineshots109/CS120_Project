## Running the Application

To run the application locally, follow these steps:

Before all of this, do 'pip install -r requirements.txt'
Then... 
1. Clone the repository to your local machine:

$ git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
$ cd REPO_NAME


2. Initialize a virtual environment:
- Windows:
  ```
  $ python3 -m venv venv
  $ venv\Scripts\activate.bat
  ```
- Unix/MacOS:
  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```

3. Install the dependencies:
$ pip install -r requirements.txt


4. Install other necessary dependencies:
- Sass:
  ```
  $ gem install sass
  ```
- Redis:
  - Mac:
    ```
    $ brew install redis
    ```
  - Linux:
    ```
    $ sudo apt-get install redis-server
    ```

5. Create the database:
$ python manage.py recreate_db

6. Run the app:
$ source env/bin/activate
$ honcho start -e config.env -f Local


7. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to view the application.

These instructions will set up and run the Flask application locally on your machine, allowing you to access it through your web browser.
