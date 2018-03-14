# Anonymize DICOM directory

Step 1
Establish a 1-to-1 relation between the spreadsheet patient records and their 
corresponding image file(s).

Step 2
Create a mapping file that relates original patient ID, randomized ID and image file path.
If there are multiple images (e.g., TAG files) associated with that patient, their file
paths must be added as additional columns. Also, any additional attributes you would like 
to add to distinguish different underlying data sources (e.g., MUMC and RWTH) add these
attributes as columns to the mapping file.

Step 3
Make a copy of the original spreadsheet and remove all patient-identifying information,
replacing the patient ID with the randomized ID.

Step 4
Add extra columns based on the extra attribute in the mapping file.

Step 4
Save the mapping file and original spreadsheet in a safe place, e.g., a locker file
created by VeraCrypt.

Step 6
For each random ID in the mapping file, get the file paths and copy these to a single
flat directory while renaming them with the same random ID. 