# Data-Source-API-Analyst-Test

## Introduction

This repository demonstrates interaction with the GitHub API for data extraction and processing using Python within a Google Colab environment.

## Project Structure


## Setup Instructions

1. **Open the Google Colab Notebook:**
   - Navigate to `Content/Postman_Collection/GitHub_API_test.ipynb` and open it in Google Colab.

2. **Upload the `Content.zip` File:**
   - Ensure that the `Content` folder is zipped as `Content.zip`.
   - Run **Cell 1** to upload and unzip the folder.

3. **Update Python Path:**
   - Run **Cell 2** to add necessary subdirectories to Python's `sys.path`.

4. **Import Modules:**
   - Run **Cell 3** to import required libraries and custom modules.

5. **Create Necessary Directories:**
   - Run **Cell 4** to ensure `saved_responses` and `cleaned_data` directories exist.

6. **Authenticate with GitHub:**
   - Run **Cell 5** and enter your GitHub Personal Access Token when prompted.

7. **Define Helper Functions:**
   - Run **Cell 6** to define the `save_to_csv` function.

8. **Data Extraction:**
   - Run **Cells 7-17** sequentially to perform data extraction tasks.

9. **Final Checks:**
   - Run **Cell 18** to check the final rate limit status and confirm completion.

## Using the Postman Collection

1. **Import the Collection:**
   - Open Postman.
   - Click **Import** > **File**.
   - Select `Content/Postman_Collection/postman_collection.json`.
   - Click **Import**.

2. **Set Up Environment Variables:**
   - Create a new environment named `GitHub API`.
   - Add a variable `github_token` with your GitHub PAT as its value.

3. **Replace Placeholders:**
   - In each request's **Authorization** header, ensure `{{github_token}}` is used.

4. **Test Requests:**
   - Select the `GitHub API` environment.
   - Execute each request and verify the responses.

## Dependencies

- **Python Packages:**
  - `requests`
  - `json`
  - `os`
  - `time`
  - `getpass`
  - `pandas`
  - `python-dotenv` (if using environment variables)

- **Install dependencies using `pip`:**

  ```python
  !pip install requests pandas python-dotenv
