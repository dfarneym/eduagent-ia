# 🚀 EduAgent AI — Sprints

> Registro das etapas de desenvolvimento do EduAgent AI.

---

# 📌 Como as Sprints são organizadas

Cada Sprint representa uma etapa do desenvolvimento.

Ao final de cada etapa, buscamos registrar:

```text
Sprint X

├── Código
├── Testes
├── Documentação
└── Commit
````
O objetivo é manter um histórico claro da evolução do projeto.

🟢 Sprint 1 — Fundação do projeto
🎯 Objetivo

Criar a estrutura inicial do EduAgent AI e preparar o ambiente de desenvolvimento.

💻 Código

Foram criados:

app.py
requirements.txt
src/eduagent/

Também foram criados os módulos iniciais:

config/
embeddings/
loaders/
prompts/
retrievers/
services/
splitters/
ui/
utils/
vectorstore/
⚙️ Ambiente

Foi criado um ambiente virtual Python:

.venv/

O ambiente passou a utilizar uma instalação isolada das dependências do projeto.

📦 Dependências

Foram instaladas as principais dependências necessárias para o desenvolvimento do projeto, incluindo:

LangChain;
Google Gemini;
FAISS;
Streamlit;
Pydantic;
Pydantic Settings;
PyPDF;
Python Dotenv.
🧪 Testado

O ambiente virtual foi ativado e as dependências foram verificadas.

Também foi identificado e solucionado um problema relacionado à política de execução de scripts do PowerShell durante a ativação do ambiente virtual.

📚 Documentação

Foi iniciada a documentação do projeto dentro de:

docs/
🗂️ Git

O projeto foi conectado ao repositório remoto:

eduagent-ia

Também foi realizado o primeiro conjunto de commits.

Durante o processo ocorreu um conflito de histórico entre o repositório local e o remoto.

O problema foi solucionado realizando a integração do histórico remoto antes do push.

Posteriormente o push foi realizado com sucesso.

✅ Status
├── ✅ Código
├── ✅ Testado
├── 🚧 Documentação
└── ✅ Commit realizado
🟢 Sprint 2 — Configuração da aplicação
🎯 Objetivo

Centralizar as configurações da aplicação e evitar que informações de configuração fiquem espalhadas pelo código.

💻 Código

Foi criada a estrutura:

src/eduagent/config/
└── settings.py

Foi utilizada a biblioteca:

from pydantic_settings import BaseSettings
🎯 Responsabilidade

O módulo settings.py será responsável por centralizar as configurações utilizadas pela aplicação.

A ideia é separar:

Código da aplicação
        +
Configurações
🧪 Testado

A configuração foi incorporada à estrutura modular do projeto.

📚 Documentação

A decisão foi registrada em:

docs/engenharia-da-solucao.md

e na visão arquitetural do projeto.

🗂️ Git

As alterações foram versionadas no GitHub.

✅ Status
├── ✅ Código
├── ✅ Testado
├── ✅ Documentação atualizada
└── ✅ Commit realizado
🟢 Sprint 3 — Interface inicial
🎯 Objetivo

Criar uma primeira interface funcional utilizando Streamlit.

💻 Código

O arquivo principal da aplicação:

app.py

foi utilizado como ponto de entrada da aplicação.

A interface inicial foi construída utilizando:

Streamlit
🧪 Problema encontrado

Durante a execução ocorreu o erro:

ModuleNotFoundError: No module named 'eduagent'

O problema estava relacionado à forma como o projeto estava sendo executado e à resolução do pacote localizado dentro de:

src/
🔧 Solução adotada

Neste momento, optou-se por não realizar o empacotamento formal da aplicação.

A aplicação passou a executar corretamente utilizando a estrutura adotada no app.py.

Essa decisão foi mantida como uma solução simples para o estágio atual do projeto.

🧠 Aprendizado

O problema mostrou a importância de compreender:

Estrutura de pacotes Python;
Importações;
Diretório de execução;
Organização src/;
Empacotamento de aplicações Python.
📚 Documentação

O ocorrido foi considerado durante a definição da arquitetura modular.

🗂️ Git

As alterações foram versionadas.

✅ Status
├── ✅ Código
├── ✅ Testado
├── ✅ Documentação atualizada
└── ✅ Commit realizado
🟢 Sprint 4 — Arquitetura modular
🎯 Objetivo

Separar as responsabilidades da aplicação em módulos especializados.

💻 Código

Foi criada a estrutura:

src/eduagent/
│
├── config/
├── embeddings/
├── loaders/
├── prompts/
├── retrievers/
├── services/
├── splitters/
├── ui/
├── utils/
└── vectorstore/
🧠 Decisão arquitetural

A decisão foi evitar que toda a lógica da aplicação ficasse concentrada em app.py.

Cada pasta foi criada para representar uma responsabilidade específica.

⚙️ Services

A pasta:

services/

foi definida como uma camada de coordenação.

Entretanto, decidiu-se que ela não deverá concentrar todas as responsabilidades.

Os componentes especializados deverão executar suas próprias funções.

🖥️ Interface

Também foi definida a separação dos componentes da interface.

A intenção é reduzir o acoplamento e facilitar a manutenção.

📚 Documentação

Foram criados e atualizados:

docs/vision.md
docs/engenharia-da-solucao.md
docs/arquitetura.md
docs/roadmap.md
🗂️ Git

A estrutura foi versionada no GitHub.

✅ Status
├── ✅ Código
├── ✅ Testado
├── ✅ Documentação atualizada
└── ✅ Commit realizado
🟡 Sprint 5 — Document Loader
🎯 Objetivo

Criar o primeiro componente responsável pelo processamento dos documentos utilizados pelo agente.

A responsabilidade será:

PDF
 │
 ▼
PDF Loader
 │
 ▼
List[Document]
🧠 Decisão arquitetural

O carregamento será encapsulado dentro da camada:

src/eduagent/loaders/

A aplicação não deverá depender diretamente dos detalhes internos do PyPDFLoader.

A ideia é:

Aplicação
    │
    ▼
PDFLoader
    │
    ▼
PyPDFLoader
    │
    ▼
Document

Isso reduz o acoplamento e facilita uma futura substituição da biblioteca.

💻 Código

🚧 A implementação será realizada nesta Sprint.

🧪 Testes

⏳ Ainda não realizados.

📚 Documentação

A decisão arquitetural já foi registrada em:

docs/engenharia-da-solucao.md
docs/arquitetura.md
🗂️ Git

O commit será realizado após a implementação e validação.

🔄 Status
├── 🚧 Código
├── ⏳ Testado
├── ✅ Documentação inicial
└── ⏳ Commit
⏳ Sprint 6 — Text Splitter
🎯 Objetivo

Dividir os documentos em partes menores chamadas de chunks.

Fluxo
Document
   │
   ▼
Text Splitter
   │
   ▼
Chunks
Tecnologia planejada
RecursiveCharacterTextSplitter
Estrutura
src/eduagent/splitters/
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 7 — Pipeline de ingestão
🎯 Objetivo

Criar o fluxo responsável por receber os documentos e prepará-los para o armazenamento vetorial.

Fluxo planejado:

PDF
 │
 ▼
Loader
 │
 ▼
Documents
 │
 ▼
Splitter
 │
 ▼
Chunks
 │
 ▼
Embeddings
Componente planejado
src/eduagent/services/
└── ingest_service.py

O ingest_service.py deverá funcionar como um serviço de orquestração da ingestão, utilizando os componentes especializados.

Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 8 — Embeddings
🎯 Objetivo

Transformar os chunks em representações vetoriais.

Chunks
   │
   ▼
Embeddings
   │
   ▼
Vetores
Estrutura
src/eduagent/embeddings/
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 9 — Vector Store
🎯 Objetivo

Armazenar os embeddings e permitir consultas por similaridade.

Tecnologia inicial
FAISS
Estrutura
src/eduagent/vectorstore/
Evolução futura

A arquitetura deverá permitir avaliar uma futura substituição do FAISS pelo ChromaDB.

Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 10 — Retriever
🎯 Objetivo

Recuperar os chunks mais relevantes para uma pergunta.

Fluxo:

Pergunta
   │
   ▼
Retriever
   │
   ▼
Vector Store
   │
   ▼
Documentos relevantes
Estrutura
src/eduagent/retrievers/
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 11 — Prompt Builder
🎯 Objetivo

Construir o prompt que será enviado ao modelo de linguagem.

Fluxo:

Pergunta
     +
Contexto
     +
Instruções
     │
     ▼
Prompt
Estrutura
src/eduagent/prompts/
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 12 — RAG Service
🎯 Objetivo

Orquestrar o fluxo principal do agente.

Fluxo:

Pergunta
   │
   ▼
Retriever
   │
   ▼
Contexto
   │
   ▼
Prompt Builder
   │
   ▼
Google Gemini
   │
   ▼
Resposta
Estrutura
src/eduagent/services/
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 13 — Chat
🎯 Objetivo

Integrar o RAG Service à interface Streamlit.

Fluxo:

👤 Usuário
    │
    ▼
💬 Chat
    │
    ▼
⚙️ RAG Service
    │
    ▼
🤖 Gemini
    │
    ▼
💬 Resposta
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 14 — Testes
🎯 Objetivo

Validar os componentes individualmente e o funcionamento integrado do agente.

Serão avaliados:

Document Loader;
Text Splitter;
Ingest Service;
Embeddings;
Vector Store;
Retriever;
Prompt Builder;
RAG Service;
Interface.
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
⏳ Sprint 15 — Deploy
🎯 Objetivo

Disponibilizar a aplicação em ambiente de nuvem.

A tecnologia considerada é:

Oracle Cloud Infrastructure
Status
├── ⏳ Código
├── ⏳ Testado
├── ⏳ Documentação
└── ⏳ Commit
📊 Visão geral das Sprints
Sprint 1   Fundação                  ✅
Sprint 2   Configuração              ✅
Sprint 3   Interface                 ✅
Sprint 4   Arquitetura modular       ✅
Sprint 5   Document Loader           🚧
Sprint 6   Text Splitter              ⏳
Sprint 7   Ingest Service             ⏳
Sprint 8   Embeddings                 ⏳
Sprint 9   Vector Store               ⏳
Sprint 10  Retriever                  ⏳
Sprint 11  Prompt Builder             ⏳
Sprint 12  RAG Service                ⏳
Sprint 13  Chat                       ⏳
Sprint 14  Testes                     ⏳
Sprint 15  Deploy                     ⏳
🎯 Critério de conclusão

Uma Sprint será considerada concluída quando suas principais atividades tiverem sido realizadas:

Sprint X

├── ✅ Código implementado
├── ✅ Testes realizados
├── ✅ Documentação atualizada
└── ✅ Commit realizado

Caso alguma dessas etapas ainda não tenha sido concluída, a Sprint permanecerá marcada como em desenvolvimento.

🚀 Próxima Sprint

A próxima etapa prática do desenvolvimento será:

Sprint 5 — Document Loader

Objetivo:

Implementar um componente responsável exclusivamente por receber, ler arquivos PDF e retornar uma lista de objetos Document.

A implementação deverá manter o baixo acoplamento e a separação de responsabilidades definidos na arquitetura do projeto.


### Um ponto importante

Agora estamos chegando na parte em que **documentação e código voltam a se encontrar**.

O próximo passo não é criar outro documento imediatamente. Depois de salvar o `sprints.md`, vamos revisar a documentação que já criamos e então partir para a **Sprint 5 — Document Loader**.

A sequência será:

```text
DOCUMENTAÇÃO
     │
     ├── vision.md                 ✅
     ├── engenharia-da-solucao.md  ✅
     ├── arquitetura.md            ✅
     ├── roadmap.md                ✅
     └── sprints.md                ← agora
     
     ▼
CÓDIGO
     │
     ▼
Sprint 5
Document Loader
     │
     ▼
Teste
     │
     ▼
Atualizar documentação
     │
     ▼
Commit
