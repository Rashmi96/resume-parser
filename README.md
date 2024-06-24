upload:

curl -X POST -F "files[]
=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/assets/presentation.pdf" http://127.0.0.1:5000/resumeUpload

curl -X POST -F "files[]=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/assets/presentation.pdf" -F "
files[]
=@/Users/rashmiranjanswain/Documents/workspace/resume-ranking/backend/requirements.txt" http://127.0.0.1:5000/resumeUpload

curl -X POST -F "files[]=@/Users/rashmiranjanswain/Documents/myDocuments/Resume.pdf" http://127.0.0.1:5000/resumeUpload

download:

curl -o /Users/rashmiranjanswain/Downloads/presentation.pdf http://127.0.0.1:5000/ReportDownload/presentation.pdf

curl -o /Users/rashmiranjanswain/Downloads/Resume.pdf http://127.0.0.1:5000/ReportDownload/Resume.pdf

delete:

curl -X DELETE http://127.0.0.1:5000/existingFileDelete

predict:

curl --location 'http://127.0.0.1:5000/predict'

curl --location 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data '{
  "context" : "Java Developer 5 year of Experience",
  "category" : "resume",
  "threshold" : 50,
  "noOfMatches" : 3
}'

# Build the Docker image
docker build -t rashmi9678/resume-parser-api:latest .

# Log in to Docker Hub (skip if using another registry)
docker login

# Push the Docker image to the registry
docker push rashmi9678/resume-parser-api:latest 

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

kubectl get services

http://localhost:80/ping

#GCP

project Id: prime-chess-427017-g2

gcloud projects add-iam-policy-binding prime-chess-427017-g2 \
    --member='user:swain96@gmail.com' \
    --role='roles/artifactregistry.writer'

gcloud auth configure-docker

docker buildx create --use

docker buildx build --platform linux/amd64 -t us-central1-docker.pkg.dev/prime-chess-427017-g2/my-docker-repo/resume-parser-api --push .

docker pull us-central1-docker.pkg.dev/prime-chess-427017-g2/my-docker-repo/resume-parser-api 

gcloud run deploy resume-parser-api \
    --image us-central1-docker.pkg.dev/prime-chess-427017-g2/my-docker-repo/resume-parser-api \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
