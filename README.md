# Upload Data to Firestore
A python code for sending data from source (JSON data in cloud storage) and the write it to firestore database.

## Overiview
This code is for implementation step 1 of project that send the result data from clustering (JSON file) and save it to Firestore Database. This code will be implemented in Cloud Function.

## Running the Program
### In Cloud Function
In cloud function, just download or copy the code to code section and requirement to requirement section and adjust the cloud storage bucket to the bucket that has been provided. Before that you need to set the trigger type to google cloud storage and set other settings as needed, then set the entry point to main and deploy the function. 
