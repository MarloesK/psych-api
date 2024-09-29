export TAG=psych/psych-api

# lambda works with --target dir in Docker which poetry doesn't handle well
# so we export to requirements.txt and install with pip in the build
poetry export --without-hashes --format=requirements.txt > requirements.txt

docker build --platform linux/amd64 -t $TAG .

# test locally at port 9000
docker run --platform linux/amd64 -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
    --entrypoint /aws-lambda/aws-lambda-rie \
    --read-only \
    $TAG \
     /usr/local/bin/python -m awslambdaric src.app.handler
