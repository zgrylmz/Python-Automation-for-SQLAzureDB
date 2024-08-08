import os
import pyodbc
import base64

# Establish a connection to the database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlAzureDBURL.database.windows.net;DATABASE=firstsqldb;UID=account;PWD=password')
cursor = conn.cursor()

# Directory containing your photos
photos_directory = 'C://Users//Neu//Desktop//Test-daten'

# Default width and height values
default_width = 192
default_height = 108

# Iterate through the files in the directory
for filename in os.listdir(photos_directory):
    # Check if the file is a photo (adjust file extension as needed)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Remove the file extension from the filename
        title = os.path.splitext(filename)[0]
        # Read the photo file
        photo_path = os.path.join(photos_directory, filename)
        with open(photo_path, 'rb') as photo_file:
            photo_data = photo_file.read()
        # Encode the photo data to Base64
        encoded_photo = base64.b64encode(photo_data).decode('utf-8')
        # thumbnail= base64.b64encode(photo_data).decode('utf-8')
        # Insert the filename (without extension), default width, default height,
        # and encoded photo data into the database
        cursor.execute("INSERT INTO dbo.testTableForAutomationn (Title, Width, Height, Encoded_data) VALUES (?, ?, ?, ?)", (title, default_width, default_height,encoded_photo))
        

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()