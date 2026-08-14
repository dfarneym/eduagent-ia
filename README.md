# 🎓 EduAgent AI

> Agente educacional inteligente baseado em **RAG (Retrieval-Augmented Generation)** e agentes de IA, capaz de responder perguntas com base no conteúdo de documentos fornecidos pelo usuário.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![Docker](https://img.shields.io/badge/Docker-enabled-blue)

---

## 📌 Sobre o projeto

O **EduAgent AI** é um projeto desenvolvido durante a **Formação de Agentes de IA da Alura**, com foco na construção de um agente capaz de consultar documentos e responder perguntas em linguagem natural.

A aplicação utiliza uma arquitetura baseada em **RAG**, combinando recuperação semântica de documentos com um agente ReAct para gerar respostas fundamentadas no conteúdo recuperado.

Na versão atual, o sistema trabalha com **documentos PDF** enviados pelo usuário e apresenta as fontes utilizadas na resposta.

O projeto está sendo desenvolvido de forma incremental, com foco em:

- arquitetura modular;
- RAG;
- agentes de IA;
- histórico conversacional;
- rastreabilidade das fontes;
- execução local e via Docker;
- futura publicação em nuvem.

---

## 🎯 Objetivo

Criar um assistente educacional capaz de:

- receber documentos;
- processar seu conteúdo;
- criar uma representação vetorial;
- recuperar informações relevantes;
- responder perguntas em linguagem natural;
- manter contexto entre perguntas;
- informar as fontes consultadas;
- evitar respostas baseadas em conhecimento externo ao documento.

---

## ✨ Funcionalidades atuais

- [x] Interface web com Streamlit
- [x] Upload de arquivos PDF
- [x] Validação do tamanho do arquivo
- [x] Processamento do PDF
- [x] Chunking do conteúdo
- [x] Geração de embeddings
- [x] Indexação vetorial com FAISS
- [x] Busca semântica
- [x] Ferramenta `search_documents`
- [x] Agente ReAct com LangGraph
- [x] Integração com Groq
- [x] Modelo `qwen/qwen3.6-27b`
- [x] Histórico conversacional
- [x] Perguntas consecutivas sem limpar a conversa
- [x] Respostas baseadas no conteúdo recuperado
- [x] Recusa quando a informação não está disponível no documento
- [x] Exibição das fontes consultadas
- [x] Limite de caracteres por pergunta
- [x] Limite de histórico enviado ao agente
- [x] Execução via Docker

---

## 🧪 Teste rápido

A aplicação foi projetada para permitir testes por meio do upload de um PDF.

### Fluxo

1. Abra a aplicação.
2. Envie um arquivo PDF.
3. Clique em **Indexar documento**.
4. Faça perguntas sobre o conteúdo.
5. Consulte as fontes apresentadas abaixo das respostas.

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

## 🧠 Arquitetura atual

```text
                           👤 Usuário
                               │
                               ▼
                    ┌────────────────────┐
                    │     Streamlit      │
                    │   Interface Web    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    AgentService    │
                    │     ReAct Agent    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │  search_documents  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     RAGService     │
                    │                    │
                    │  Embeddings        │
                    │  FAISS             │
                    │  Retriever         │
                    └─────────┬──────────┘
                              │
                              ▼
                         📄 Documento
                              │
                              ▼
                         🤖 Groq / Qwen
```

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

## 📁 Estrutura do projeto

```text
eduagent-ia/
│
├── docs/                      # Documentação técnica complementar
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
```

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

🔄 **Próxima etapa**

A versão funcional será publicada para disponibilizar uma demonstração online.

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
- [ ] Criar documentos de demonstração
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

## 📚 Documentação técnica

A documentação complementar do projeto será organizada no diretório:

```text
docs/
```

A documentação poderá incluir:

- arquitetura;
- fluxo RAG;
- decisões técnicas;
- processamento de documentos;
- execução com Docker;
- deploy;
- evolução do projeto.

O README permanece como ponto de entrada principal, enquanto o diretório `docs/` concentra explicações técnicas mais detalhadas.

---

## 🎓 Challenge Alura

Este projeto faz parte do **Challenge da Formação de Agentes de IA da Alura**.

### Requisitos do challenge

- [x] Repositório público no GitHub
- [ ] Deploy do agente na Oracle Cloud Infrastructure
- [ ] Imagem ou vídeo da aplicação executando em nuvem no README

### Situação atual

O projeto já possui uma versão funcional executada localmente e em Docker.

A próxima etapa é publicar essa versão e adicionar as evidências de execução em nuvem ao README.

---

## 👨‍💻 Autor

**Daniel Farney**

Engenheiro de IA Jr. | Dados | Python | IA Generativa

GitHub: https://github.com/dfarneym