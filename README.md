# API para TCC
	Criação de uma api para recurar despesas de faturas de cartão em PDF.

## Instalar as dependências do Python
É necessário a instalação das depencias do projeto com o comando abaixo.
```Shell
	pip install -r requirements.txt
```

## Rodando o projeto com Python
Para rodar o projeto utilizando o Python localmente. Execute o comando para dar o start na aplicação conforme abaixo.
```Shell
	python -u ./app/main.py
```

## Rodando com o docker-compose
Para rodar a aplicação sem precisar instalar as dependencias e sem o python. Será necessário utilizar o docker para criar um container. Para subir o container é só executar o comando abaixo na raiz do projeto.
```Shell
	docker-compose up
```