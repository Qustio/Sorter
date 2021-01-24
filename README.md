# Sorter
This programs can help you to sort files. It is controlled by `config.json` and `settings.json` files.
## Configuration file
```json
{
    "Images": [
        "png",
        "jpg",
        "JPG"
    ],
    "Music": [
        "mp3"
    ],
    "Text": [
    	"txt"
    ]
}
```
This file contains folder names into which the files with certain extentions are sorted. For example, folder ```Music``` will contain .mp3 files and so on. If folder doesn`t exist, it will be created automatically.
## Settings file
```json
{
    "Path": "D:/Desktop/Sorted files",
    "Scanning directories": [
        "D:/Desktop"
    ]
}
```
JSON dictionary where 
>```#Path``` - directory for a new (sorted) folders 

>```#Scanning directories```  - folders to be scanned
