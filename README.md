# Startup Idea Generator

## Visão Geral

Este projeto é uma aplicação web que permite aos usuários gerar ideias para startups. Utilizando tecnologias modernas como React no frontend e FastAPI no backend, a aplicação se conecta a um serviço de inteligência artificial para gerar ideias com base em prompts fornecidos pelos usuários.

## Estrutura do Projeto
/Frontend
    /public
        index.html
    /src
        /components
            Chat.js
        /pages
            Home.js
        /styles
            styles.css
/Backend
    /app
        /services
            ai_service.py


### Frontend

- **public/index.html**: O arquivo HTML principal que carrega a aplicação React.
- **src/components/Chat.js**: Componente responsável pela interação do usuário, onde o usuário pode inserir um prompt e receber uma ideia gerada.
- **src/pages/Home.js**: Página principal que renderiza o componente `Chat`.
- **src/styles/styles.css**: Arquivo CSS que contém os estilos da aplicação.

### Backend

- **app/services/ai_service.py**: Serviço que se conecta à API de inteligência artificial para gerar ideias com base no prompt fornecido.

## Como Funciona

### Frontend

1. **Interface do Usuário**: O usuário acessa a aplicação e vê um campo de entrada onde pode digitar um prompt.
2. **Geração de Ideias**: Quando o usuário envia o prompt, a aplicação faz uma requisição ao backend para gerar uma ideia.
3. **Exibição da Ideia**: A ideia gerada é exibida na tela, formatada para melhor legibilidade.

### Backend

1. **Recepção do Prompt**: O backend recebe o prompt enviado pelo frontend.
2. **Geração da Ideia**: Utiliza a API de inteligência artificial para gerar uma ideia com base no prompt.
3. **Retorno da Ideia**: A ideia gerada é enviada de volta ao frontend para ser exibida ao usuário.

## Tecnologias Utilizadas

- **Frontend**: 
  - **React**: Biblioteca JavaScript para construir interfaces de usuário.
  - **Axios**: Biblioteca para fazer requisições HTTP.
  
- **Backend**: 
  - **FastAPI**: Framework para construir APIs com Python.
  - **Google Generative AI**: API utilizada para gerar ideias.

## Como Executar o Projeto

### Pré-requisitos

- Node.js e npm instalados para o frontend.
- Python e pip instalados para o backend.

### Passos para o Frontend

1. Navegue até o diretório `Frontend`.
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```

### Passos para o Backend

1. Navegue até o diretório `Backend`.
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## Contribuição

Se você deseja contribuir para este projeto, siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para mais informações, entre em contato com hudsono256@gmail.com.

---

Essa documentação deve ajudar qualquer pessoa, mesmo aquelas com pouco conhecimento técnico, a entender como o projeto funciona e como executá-lo. Se precisar de mais informações ou ajustes, é só avisar!
            
