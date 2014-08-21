Dropbox-Service:
===============

Implementation of Dropbox Service. Where a file is digitally signed before syncing and will be verified when retrived.


Steps:
======

The File to be read and is assumed to be present in E:\working-draft.txt location and named as working-draft.txt
The File will be uploaded to dropbox and saved as magnum-opus.txt
The File is being digitally signed and then verified when download
The signed file is being uploaded to dropbox and then the signatures are verified.
The Dropbox-Service is implemented in Python
Tested with Text, jpg and Pdf file formats
