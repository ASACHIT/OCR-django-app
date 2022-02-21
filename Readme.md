
# Text Extractor/ OCR in Django


A django webapp for scanning texts from images, simply you have to upload image and it will provide you with texts found



## Home page

![App Screenshot](https://cdn.discordapp.com/attachments/884460118715019274/945247468747124736/unknown.png)

## Result page

![App Screenshot](https://cdn.discordapp.com/attachments/884460118715019274/945247765259247616/unknown.png)

## Nepali Language
![App Screenshot](https://media.discordapp.net/attachments/884460118715019274/945248254428323850/unknown.png)

## Hindi Language
![App Screenshot](https://media.discordapp.net/attachments/884460118715019274/945248807912882206/unknown.png)

Currently i have included commonly used language list only, feature request for another langauges are welcomed ;)
- English
- Nepali
- Hindi

## Installation

```bash
  git clone https://github.com/ASACHIT/OCR-django-app.git
  cd OCR-django-app
  pip install -r requirements
  python manage.py runserver 
  # open localhost:8000  url in browser 
```
Note: You have to install [tesseract module](https://github.com/UB-Mannheim/tesseract/wiki) too
## Frameworks/lib used
- Tailwindcss
- django
- pytesseract

## Things i learnt after creating this project

- Taking image input from user 
- Processing input image without saving it anywhere and uploading it directly to user
- scanning text from image (backend)
- and other many more


## Features
- Quickly Upload image and get scanned text 
- Image is Not saved, it is directly processed in memory and directly sent to you
- Friendly and Clean UI

## Contributing

Contributions are always welcome!


