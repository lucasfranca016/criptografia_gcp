# Criptografia com Cloud KMS e Cloud DLP

Códigos simples que utilizam as API's do Cloud KMS e Cloud DLP para criptografar dados sensíveis de um CSV.

# **Códigos baseados nos seguintes artigos da documentação GCP**

[Artigo sobre API do DLP](https://cloud.google.com/dlp/docs/libraries?hl=pt-br#using_the_client_library )
[Artigo sobre API do KMS](https://cloud.google.com/kms/docs/encrypt-decrypt?hl=pt_br#kms-encrypt-symmetric-python)

# **Instruções de uso**
  
O código principal é o "verify.py". Para usá-lo basta mudar o arquivo de leitura de "teste.csv" para o csv que deseja fazer a inspeção/criptografia de dados sensíveis. Outros parâmetros que devem ser mudados são os tipos de dados sensíveis que o DLP deve identificar, o projeto a ser utilizado e o json de credenciais.
  
Precimos das bibliotecas do KMS e DLP, para isso:

pip3 install --upgrade "google-cloud-kms"
pip3 install google-cloud-dlp
  
Para definir o caminho para a o json de credenciais:
  
"export GOOGLE_APPLICATION_CREDENTIALS="/caminho/para/json/credenciais.json"
