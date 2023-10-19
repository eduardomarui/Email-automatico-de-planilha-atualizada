# Envio Automático de Planilha Atualizada via E-mail

Desenvolvi um script em Python que permite enviar automaticamente uma planilha do Google Sheets via e-mail todos os dias ao meio-dia. O processo é realizado em etapas claras e concisas, garantindo eficiência e precisão.

## Bibliotecas Utilizadas

Utilizei as bibliotecas `smtplib` para o envio de e-mails, `pandas` para manipulação de dados, `gspread` e `oauth2client` para acessar o Google Sheets e `schedule` para automatizar o envio dos e-mails.

## Passos que Segui

1. **Instalação das Bibliotecas:** Executei o comando `pip install gspread oauth2client pandas schedule` para instalar todas as bibliotecas necessárias.
   
2. **Configuração do E-mail:** Substituí as credenciais de e-mail no script com meu próprio e-mail e senha para permitir o envio automatizado.

3. **Acesso ao Google Sheets:** Acessei o [Console do Google Cloud](https://console.cloud.google.com/), ativei a API do Google Sheets e criei as credenciais de serviço. Coloquei o arquivo JSON das credenciais na mesma pasta do script e compartilhei minha planilha do Google Sheets com o e-mail fornecido nas credenciais.

4. **Execução do Script:** Ao executar o script, ele acessa a planilha do Google Sheets, a converte em um arquivo CSV e a envia para o e-mail especificado todos os dias ao meio-dia.

## Conclusão

Com esses passos, consegui automatizar eficientemente o processo de enviar uma planilha atualizada via e-mail diariamente, economizando tempo e garantindo que os dados mais recentes sejam compartilhados de maneira oportuna e precisa.
