![awd-sec-box](https://github.com/lucas-apd/aws-security-box/blob/main/screenshots/aws_sec_box.png?raw=true)
# aws-security-box
Este projeto usa Python3 e Flask para criar uma aplicação web que faz upload de arquivos para um bucket S3, fazendo uso do recurso ['presigned URL'](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) da aws (criação de URL pré assinada temporária) para compartilhamento do arquivo.

O código define 3600 segundos para expiração da url.

Etapas:
 - Deploy;
 - Acesso;
 - Seleção do arquivo;
 - Upload do arquivo para o bucket;
 - Criação da url;
 - Cópia da url;
 - Compartilhar a url.
 
Atenção: Este projeto foi criado para fins de estudos e testes, então **não está pronto para ambiente produtivo!**

## Deployment

### Docker
 - git clone https://github.com/lucas-apd/aws-security-box.git
 - cd aws-security-box
 - docker build -t aws-sec-box:latest .
 - export S3_BUCKET_NAME=""
 - export AWS_ACCESS_KEY_ID=""
 - export AWS_SECRET_ACCESS_KEY=""
 - export AWS_SESSION_TOKEN=""
 - docker run -d --name aws-sec-box --env S3_BUCKET_NAME=$S3_BUCKET_NAME --env AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --env AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY --env AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN --name aws-sec-box -p 8080:8080 aws-sec-box 

#### Access
 - http://localhost:8080

Inspirações e Referências:

[ShareObjectPreSignedURL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)

[github-fork-ribbon-css](https://github.com/simonwhitaker/github-fork-ribbon-css)
