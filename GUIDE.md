# Setup Guide: PDF Q&A Bot

Follow these steps in order. It takes about 15 minutes.

## 1. Install Python
Download Python from python.org and install it. Tick "Add Python to PATH" during setup.

## 2. Install the libraries
Open a terminal and run:
pip install requests pypdf

## 3. Get a free API key
1. Go to aistudio.google.com and log in with a Google account.
2. Click "Get API key" and create a key.
3. Copy it.

## 4. Save your key
Create a file called key.txt in the same folder as pdfbot.py. Paste your key in it (one line, nothing else). Never share this file.

## 5. Add your PDF
Put a PDF with real, selectable text in the same folder. Scanned PDFs made of images won't work.

## 6. Run it
Run pdfbot.py, type the PDF's file name (for example, myfile.pdf), then ask questions. Type quit to stop.

## Troubleshooting
- FileNotFoundError: the file name doesn't match, check spelling and .pdf
- Status 503: Google's server is busy, wait a minute and try again
- Status 403 or 400: your key is wrong, copy it again from AI Studio
