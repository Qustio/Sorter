# Sorter
This programs can help you to sort files. You can control everything with a `config.json` file.
## Configuration
```json
{
    "#Path": "D:/",
    "#Scanning directories": [
        "D:/",
        "D:/Downloads"
    ],
    "Images": [
        "png",
        "jpg",
        "JPG"
    ],
    "Music": [
        "mp3"
    ],
    "Images/Icons": [
        "ico"
    ]
}
```
JSON dictionary where 
>```#Path``` - directory for a new folders 

>```#Scanning directories```  - folders to be scanned

Then there is a folder name witch contain files with the required extension.
>
For example, folder ```Music``` will contain .mp3 files and so on. If there is do folder, program will automatically create new folder.
