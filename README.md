## Como rodar:
Nessa versão da aplicação para rodar basta colocar todos arquivos dentro de uma mesma pasta
e abrir o arquivo index.html utilizando algum navegador(firefox, chrome). A ideia é utilizar o NW.js para rodar a aplicação
, contudo, para fins de testes acredito que assim fique mais facil

## Salvamento e Parser:
Nessa versão não se encontra o parser para JSON da plataforma, quando fui testar em outro computador  que não fosse o meu reparei que tinha bloqueios de acesso a arquivos locais, por isso estou modificando certas coisas. Contudo já é possivel salvar os arquivos contendoos dados sobre os nós. Para salvar basta utilizar o botão "save" e para carregar os dados é necessario ( por enquanto,até entender o problema) copiar os dados salvos no arquivo txt e coloca-los no prompt de texto!


##Comandos dos nós
#Esses comandos serão entendidos no momentos de passar os scripts para o formato JSON aceito pela plataforma

## Funcionamento do nó de script
Aqui vão alguns comando em relação a criação de scripts:
@voice:      -> Corresponde ao "Falar"
@wait:       -> Corresponde ao "Espera"
@listen:     -> Corresponde ao "Escutar"
;            -> Passa para o próximo bloco dentro do script

## Funcionamento do nó de Diálogo
Basta adicionar os textos em relação a inputs do lado esquerdo e outputs do direito

;            -> Passa para ou o próximo "input" ou "output"
