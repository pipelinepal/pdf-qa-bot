# PDF Q&A Bot

A small Python tool that answers questions about a PDF using AI.

## What it does
Reads a PDF, takes your question, and answers using only what's written in the document. If the answer isn't in the PDF, it says so.

## How it works
1. Extracts the text from `sample.pdf` using pypdf
2. Sends the text and your question to the Gemini API
3. Gets the answer back as JSON and prints it

## How to run it
1. Install the libraries: `pip install requests pypdf`
2. Get a free API key from Google AI Studio
3. Create a file called `key.txt` and paste your key in it (one line, nothing else)
4. Put a text-based PDF in the folder and name it `sample.pdf`
5. Run `pdfbot.py` and type your question

Your API key stays in `key.txt` and is never written in the code.

## Tools used
Python, JSON, Gemini API, pypdf

## Note
Works with PDFs that contain real text. Scanned PDFs made of images are not supported.
