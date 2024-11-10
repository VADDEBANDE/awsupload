import requests

def upload_file_to_s3(bucket_url, file_path):
    """
    Upload a file to the specified S3 bucket URL.
    
    :param bucket_url: The full URL of the S3 bucket where the file will be uploaded.
    :param file_path: The path to the local file you want to upload.
    """
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file_data:
            # Perform the PUT request
            response = requests.put(bucket_url, data=file_data, headers={"Content-Type": "text/plain"})
        
        # Check the response
        if response.status_code == 200:
            print(f"File uploaded successfully to {bucket_url}")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}, Response: {response.text}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    # Take inputs from the user
    bucket_url = input("Enter the S3 bucket URL (e.g., http://bucket-name.s3.amazonaws.com/object-key): ")
    file_path = input("Enter the local file path to upload (e.g., test.txt): ")

    # Upload the file
    upload_file_to_s3(bucket_url, file_path)
