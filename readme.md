## API USAGE
1. POST Request rotates Nth page only
2. GET Request rotates upto Nth page

### A. With POST request - Roate Nth page only
1. POST request API endpoint: http://127.0.0.1:5000/pdf/
2. JSON data is required to be sent in the request body with following format:

```
{
    "file_path" : "FILE_PATH/FILE_NAME.pdf",
    "rot_ang" : ROTATION_ANGLE,
    "page_num" : PAGE_NUMBER,
}
```

3. API returns a JSON response with the following format:

```
{
    "Success": "File rotated successfully",
    "Rotated_File_path": "FILE_PATH/FILE_NAME_rotated.pdf"
}
```

### B. With GET request - Roate upto Nth page
1. GET request API endpoint: http://127.0.0.1:5000/pdf/
2. JSON data is required to be sent in the request body with following format:

```
{
    "file_path" : "FILE_PATH/FILE_NAME.pdf",
    "rot_ang" : ROTATION_ANGLE,
    "page_num" : PAGE_NUMBER,
}
```

3. API returns a JSON response with the following format:

```
{
    "Success": "File rotated successfully",
    "Rotated_File_path": "FILE_PATH/FILE_NAME_rotated.pdf"
}
```