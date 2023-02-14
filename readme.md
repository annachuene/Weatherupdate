Instructions for running the app:

1. Install the necessary packages using the requirements.txt
   a. Open the terminal and navigate to the root folder of your project.
   b. Run the command “pip install -r requirements.txt" to install the necessary packages.

2. Configure the Database in the settings.py by adding your database configuration.
   a. Open the settings.py file.
   b. Add your database configuration, such as the database name, user name, and password.

3. Run migrations to create the database tables.
   a. Make sure you are in the root folder of your project.
   b. Run the command "python manage.py migrate" to create the database tables.

4. create a .env file in the /weatherapp folder and the following code

   ```bash
   MAPBOX_API_KEY=...
   OPENWEATHERMAP_API_KEY=...

MAPBOX_API_KEY=pk.eyJ1IjoiYWNodWVuZSIsImEiOiJjbGUwNHZlNzYwM2I0M29tdm91NmppZWxmIn0.KNSukP8HhNvCV5qff3cznA
OPENWEATHERMAP_API_KEY=116645c1b7abc82ed584e2c8aa85f752
   ```

   Replace '...' with the actual api keys.

5. Finally, run the server to start the app.
   a. In the same root folder, run the command "python manage.py runserver".
   b. The server should be running on the specified port.
