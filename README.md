# aws-security-box
Atenção: Este projeto foi criado para fins de estudos e testes, então **não está pronto para ambiente produtivo!**

## Deployment

### Docker
 - git clone https://github.com/lucas-apd/aws-security-box.git
 - docker build -t aws-sec-box:latest .
 - export S3_BUCKET_NAME=""
 - export AWS_ACCESS_KEY_ID=""
 - export AWS_SECRET_ACCESS_KEY=""
 - export AWS_SESSION_TOKEN=""
 - docker run -d --name aws-sec-box --env S3_BUCKET_NAME=$S3_BUCKET_NAME --env AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --env AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY --env AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN --name aws-sec-box -p 8080:8080 aws-sec-box 

#### Access
 - http://localhost:8080
