upload:

curl -X POST -F "files[]=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/assets/presentation.pdf" http://127.0.0.1:5000/resumeUpload

curl -X POST -F "files[]=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/assets/presentation.pdf" -F "files[]=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/backend/requirements.txt" http://127.0.0.1:5000/resumeUpload


download:

curl -o /Users/rashmiranjanswain/Downloads/presentation.pdf http://127.0.0.1:5000/resumeDownload/presentation.pdf

delete:

curl -X DELETE http://127.0.0.1:5000/existingFileDelete