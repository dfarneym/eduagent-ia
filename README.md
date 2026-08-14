# 🎓 EduAgent AI
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![Docker](https://img.shields.io/badge/Docker-enabled-blue)

---

O **EduAgent AI** é um agente de inteligência artificial capaz de responder
perguntas em linguagem natural com base no conteúdo de documentos fornecidos
pelo usuário.

A aplicação utiliza uma arquitetura RAG para carregar, processar, indexar e
recuperar informações relevantes dos documentos antes de gerar uma resposta.



## 🎯 Objetivo

O projeto foi desenvolvido como parte do desafio da Formação de Agentes de IA
da Alura.

A solução permite consultar documentos educacionais e obter respostas baseadas
no conteúdo disponível, evitando que o agente responda utilizando informações
que não estejam presentes no documento consultado.

## ✨ Funcionalidades

- 📄 Upload de documentos PDF
- 📚 Documentos de demonstração incluídos no projeto
- 🔍 Recuperação de informações utilizando RAG
- 🧠 Busca semântica
- 💬 Interface conversacional com Streamlit
- 📑 Indicação das fontes consultadas
- 💡 Sugestões de perguntas relacionadas ao documento
- 📦 Validação do tamanho do arquivo
- 📄 Validação da quantidade de páginas
- 🐳 Execução através de Docker

## 📏 Limites atuais

Para manter o processamento adequado da aplicação:

- **Tamanho máximo:** 10 MB por arquivo
- **Quantidade máxima:** 50 páginas por documento

A interface informa ao usuário o tamanho e a quantidade de páginas do arquivo
antes da indexação.

## 📚 Documentos de demonstração

O projeto disponibiliza documentos educacionais de demonstração para que a
aplicação possa ser testada imediatamente, sem necessidade de preparar ou
enviar um documento próprio.

Os documentos estão disponíveis em:

`data/demo/`

Incluem:

1. Manual do Aluno
2. Matrícula e Acesso
3. Bolsas e Benefícios
4. Avaliações e Recuperação
5. Certificados
6. Calendário Acadêmico
7. Financeiro e Pagamentos
8. Suporte e FAQ

Na interface, selecione **Documentos de demonstração** e escolha um dos documentos disponíveis.

## 🧠 Arquitetura 
                   👤 Usuário
                         │
                         ▼
                ┌─────────────────┐
                │    Streamlit    │
                │   Interface UI  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Documento PDF │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   PDF Loader    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Chunking     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Embeddings   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │      FAISS      │
                │ Vector Store    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Retriever    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Agente / LLM  │
                └────────┬────────┘
                         │
                         ▼
                💬 Resposta + fonte
---

## 🧪 Teste rápido

A aplicação oferece duas formas de teste:

- selecionar um dos documentos de demonstração disponíveis na interface;
- enviar um PDF próprio pelo botão de upload.

Para uma avaliação rápida, recomenda-se utilizar primeiro um dos documentos
de demonstração.

### 📚 Teste com documento de demonstração

1. Abra a aplicação.
2. Expanda **Documentos de demonstração**.
3. Selecione um documento.
4. Aguarde a indexação.
5. Utilize uma das perguntas sugeridas.
6. Faça perguntas adicionais sobre o conteúdo.
7. Consulte as fontes apresentadas nas respostas.

### Exemplos de perguntas

Use perguntas relacionadas ao conteúdo do documento, por exemplo:

```text
Qual é o objetivo deste documento?

Qual componente é responsável por isso?

E o que ele deve retornar?

Explique esse componente com mais detalhes.

Resuma o documento.
```

### Teste de conhecimento externo

Também é possível testar a regra de contenção do agente:

```text
Qual é a capital do Brasil?
```

Quando essa informação não estiver presente no documento, o agente deve informar que ela não foi encontrada nos documentos disponíveis.

### Teste de contexto

Faça uma sequência como:

```text
Qual é o objetivo deste documento?
```

Depois:

```text
Qual componente é responsável por isso?
```

E:

```text
Explique esse componente com mais detalhes.
```

A segunda e a terceira pergunta devem utilizar o contexto da conversa anterior, mas continuar consultando o documento por meio do RAG.

---

## 🔎 Fluxo de processamento

1. O usuário envia um PDF pela interface.
2. O arquivo é salvo temporariamente para processamento.
3. O loader extrai o conteúdo.
4. O conteúdo é dividido em trechos.
5. São gerados embeddings.
6. Os embeddings são indexados no FAISS.
7. O usuário faz uma pergunta.
8. O agente utiliza `search_documents`.
9. O RAG recupera os trechos mais relevantes.
10. O modelo gera a resposta usando o contexto recuperado.
11. As fontes consultadas são apresentadas na interface.

---

## 🛠️ Tecnologias utilizadas

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.13 |
| Interface | Streamlit |
| Agentes | LangGraph |
| Orquestração | LangChain |
| LLM | Groq + Qwen |
| Embeddings | Sentence Transformers |
| Busca vetorial | FAISS |
| Leitura de PDF | PyPDF |
| Configuração | Pydantic Settings |
| Variáveis de ambiente | python-dotenv |
| Containerização | Docker |
| Versionamento | Git / GitHub |

---

## 📄 Formatos de documentos

### Suporte atual

- [x] PDF

### Evolução planejada

- [ ] Word (`.docx`)
- [ ] Excel (`.xlsx`)
- [ ] PowerPoint (`.pptx`)
- [ ] Markdown (`.md`)
- [ ] CSV
- [ ] JSON
- [ ] HTML

> O suporte aos demais formatos faz parte da evolução planejada para atender integralmente ao escopo proposto pelo challenge.

---
````
## 📁 Estrutura do projeto

eduagent-ia/
│
├── data/
│   └── demo/                  # Documentos PDF para demonstração
│       ├── 01_manual_do_aluno.pdf
│       ├── 02_matricula_e_acesso.pdf
│       ├── 03_bolsas_e_beneficios.pdf
│       ├── 04_avaliacoes_e_recuperacao.pdf
│       ├── 05_certificados.pdf
│       ├── 06_calendario_academico.pdf
│       ├── 07_financeiro_e_pagamentos.pdf
│       └── 08_suporte_e_faq.pdf
│
├── src/
│   └── eduagent/
│       ├── config/            # Configurações
│       ├── loaders/           # Leitura de documentos
│       ├── services/          # Regras de negócio
│       ├── tools/             # Ferramentas do agente
│       └── ui/                # Interface Streamlit
│
├── app.py                     # Ponto de entrada
├── Dockerfile                 # Configuração da imagem Docker
├── requirements.txt           # Dependências
├── README.md                  # Documentação principal
└── .gitignore
````
---

## ⚙️ Pré-requisitos

Para executar localmente:

- Python 3.13+
- Git
- chave de API da Groq

Para execução com Docker:

- Docker Desktop ou Docker Engine

---

## 🚀 Execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/dfarneym/eduagent-ia.git
cd eduagent-ia
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
MODEL_NAME=qwen/qwen3.6-27b
```

> O arquivo `.env` não deve ser versionado no Git.

### 6. Executar a aplicação

```bash
python -m streamlit run app.py
```

Acesse:

```text
http://localhost:8501
```

---

## 🐳 Execução com Docker

### Construir a imagem

```bash
docker build -t eduagent-ai .
```

### Executar

```bash
docker run --name eduagent \
  -p 8501:8501 \
  --env-file .env \
  eduagent-ai
```

Acesse:

```text
http://localhost:8501
```

---

## 🔐 Limites atuais

Para evitar processamento excessivo, a aplicação possui limites configuráveis:

```text
Tamanho máximo do arquivo: 10 MB
Máximo de caracteres por pergunta: 2.000
Máximo de mensagens consideradas no histórico: 10
```

Esses valores ficam centralizados nas configurações da aplicação e podem ser ajustados conforme a evolução do projeto.

---

## ☁️ Deploy

### Streamlit Community Cloud

✅ **Publicado**

🔗 Aplicação online: `URL`

A aplicação está disponível para testes online.

### Oracle Cloud Infrastructure (OCI)

⏳ **Planejado**

O deploy final será realizado na Oracle Cloud Infrastructure, atendendo ao requisito de utilização de pelo menos um serviço OCI no challenge.

Após a publicação, esta seção será atualizada com:

- URL da aplicação;
- serviço OCI utilizado;
- instruções de execução;
- evidência da aplicação rodando em nuvem.

---

## 📸 Demonstração

> Esta seção será atualizada após a publicação online.

### Aplicação em execução

_Adicionar aqui uma captura de tela da aplicação rodando na nuvem._

### Link da aplicação

_Adicionar aqui a URL pública após o deploy._

---

## 🛣️ Roadmap

### Concluído

- [x] Estrutura inicial do projeto
- [x] Arquitetura modular
- [x] Interface Streamlit
- [x] PDF Loader
- [x] Chunking
- [x] Embeddings
- [x] FAISS
- [x] RAG
- [x] Agente ReAct
- [x] Histórico conversacional
- [x] Fontes consultadas
- [x] Limites de entrada
- [x] Docker
- [x] Execução do sistema dentro do container

### Próximas etapas

- [ ] Publicação no Streamlit Community Cloud
- [ ] Suporte a múltiplos PDFs
- [ ] Suporte a Word
- [ ] Suporte a Excel
- [ ] Suporte a PowerPoint
- [ ] Suporte a Markdown
- [ ] Suporte a CSV
- [ ] Suporte a JSON
- [ ] Suporte a HTML
- [ ] Melhorar memória/contexto
- [ ] Melhorar apresentação das fontes
- [ ] Melhorar tratamento de erros
- [ ] Criar testes automatizados
- [ ] Reduzir o tamanho da imagem Docker
- [ ] Deploy na OCI
- [ ] Documentação final
- [ ] Evidência da execução em nuvem

---

## 🎓 Challenge Alura

Este projeto faz parte do **Challenge da Formação de Agentes de IA da Alura**.

### Requisitos do challenge

- [x] Repositório público no GitHub
- [ ] Deploy do agente na Oracle Cloud Infrastructure
- [ ] Imagem ou vídeo da aplicação executando em nuvem no README


## 👨‍💻 Autor

**Daniel Farney**

Estudante de  IA | Dados | Python |

GitHub: https://github.com/dfarneym