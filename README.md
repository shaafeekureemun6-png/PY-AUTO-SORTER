AutoSorter

A small Python script that sorts downloaded lecture files into module folders, based on the website each file was downloaded from.


How it works

When a browser downloads a file on Windows, it attaches a hidden NTFS alternate data stream called Zone.Identifier (the "Mark of the Web").

AutoSorter:

Loops over the files in a source folder.
Reads each file's Zone.Identifier stream.
Extracts the course ID from ReferrerUrl 
Looks the ID up in a dictionary to find the module name.
Moves the file into a folder for that module, without overwriting existing files.

Files with no source information, or from a course that isn't in the dictionary, are left untouched.

Requirements
Windows (the files must be on an NTFS drive)
Python 3.8 or newer


No external packages are needed.

Setup
Clone or download this repository.
Open AutoSorter.py and edit the settings at the top:
python
SOURCE = Path.home() / "Desktop" / "test_downloads"
DEST = Path.home() / "Desktop" / "test_university"
DRY_RUN = True

COURSE_IDS = {
    "12345": "Module Name One",
    "67890": "Module Name Two",
}
To find a course ID, open the course page on your Moodle site and copy the number after id= in the address bar.
Usage

Always start with a dry run on a test folder of copied files:

powershell
python AutoSorter.py

With DRY_RUN = True it only prints what it would do:

WOULD MOVE: Lecture 2.pdf -> ...\Module Name One\Lecture 2.pdf
SKIP: photo.jpeg

When the output looks right, set DRY_RUN = False and run it again to move the files.

Tip: make Chrome record the source page

If you open a PDF in Chrome's built-in viewer and then save it, Chrome may not record the course page. In chrome://settings/content/pdfDocuments, choose Download PDFs so the source page is saved with the file.

To check what a file recorded:

powershell
Get-Content "file.pdf" -Stream Zone.Identifier
Limitations
Windows and NTFS only.
Files saved through a browser extension, copied from a USB drive, or received from chat apps usually have no source information and are skipped.
The referrer depends on the page you clicked the file from; links from pages other than the course page may not match.
Course IDs must be added to the dictionary by hand.
It only runs when you run it.
