# 🗺️ EduAgent AI — Roadmap

> Planejamento da evolução do EduAgent AI durante o desenvolvimento do projeto.

---

## 🎯 Objetivo do Roadmap

O desenvolvimento do EduAgent AI será realizado de forma incremental.

A estratégia é implementar primeiro uma base simples e funcional e, posteriormente, adicionar os componentes necessários para completar o pipeline RAG.

O desenvolvimento segue o princípio:

```text
Planejar
   │
   ▼
Implementar
   │
   ▼
Testar
   │
   ▼
Documentar
   │
   ▼
Commit
   │
   ▼
Evoluir
````
📍 Estado atual

O projeto já possui uma estrutura modular inicial e uma interface básica utilizando Streamlit.

✅ Concluído
Estrutura inicial do projeto;
Ambiente virtual Python;
Configuração das dependências;
Configuração centralizada;
Estrutura modular em src/eduagent;
Estrutura inicial da interface;
Interface inicial utilizando Streamlit;
Separação inicial das responsabilidades;
Organização da documentação;
Versionamento com Git;
Repositório no GitHub.
🧱 Etapa 1 — Fundação do projeto
Objetivo

Criar uma base organizada para o desenvolvimento do agente.

Status

✅ Concluída

Atividades
Criar o projeto Python;
Criar ambiente virtual;
Configurar dependências;
Criar app.py;
Criar estrutura src/eduagent;
Criar módulos da aplicação;
Configurar Git;
Criar repositório no GitHub.
⚙️ Etapa 2 — Configuração
Objetivo

Centralizar as configurações da aplicação.

Status

✅ Concluída

Componentes
src/eduagent/config/
└── settings.py

Foi utilizada a abordagem baseada em:

from pydantic_settings import BaseSettings
🖥️ Etapa 3 — Interface
Objetivo

Criar a primeira interface de interação com o usuário.

Status

✅ Inicialmente concluída

Tecnologia
Streamlit

A interface será evoluída conforme o agente receber novos componentes.

📄 Etapa 4 — Document Loader
Objetivo

Criar o componente responsável pelo carregamento dos documentos PDF.

Status

🚧 Próxima etapa

Responsabilidade
PDF
 │
 ▼
PDF Loader
 │
 ▼
Document

O componente deverá receber um arquivo PDF e retornar uma lista de objetos Document.

A implementação será encapsulada na camada:

src/eduagent/loaders/

A utilização do PyPDFLoader ficará concentrada nessa camada para reduzir o acoplamento com a biblioteca.

✂️ Etapa 5 — Text Splitter
Objetivo

Dividir os documentos carregados em partes menores.

Status

⏳ Planejada

Tecnologia planejada
RecursiveCharacterTextSplitter

Fluxo:

Document
   │
   ▼
Text Splitter
   │
   ▼
Chunks

Essa etapa será implementada na camada:

src/eduagent/splitters/
🔢 Etapa 6 — Embeddings
Objetivo

Transformar os chunks em representações vetoriais.

Status

⏳ Planejada

Fluxo:

Chunks
   │
   ▼
Embeddings
   │
   ▼
Vetores

A implementação ficará isolada em:

src/eduagent/embeddings/
🗄️ Etapa 7 — Vector Store
Objetivo

Armazenar as representações vetoriais e permitir buscas por similaridade.

Status

⏳ Planejada

Primeira tecnologia
FAISS

Fluxo:

Embeddings
    │
    ▼
FAISS

A responsabilidade ficará isolada em:

src/eduagent/vectorstore/
Evolução futura

Uma possível evolução será avaliar a utilização do ChromaDB.

A arquitetura foi organizada para permitir essa mudança sem que o restante da aplicação precise conhecer os detalhes internos do banco vetorial.

🔍 Etapa 8 — Retriever
Objetivo

Recuperar os documentos ou chunks mais relevantes para uma pergunta.

Status

⏳ Planejada

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

A responsabilidade ficará em:

src/eduagent/retrievers/
📝 Etapa 9 — Prompt Builder
Objetivo

Construir o prompt utilizado pelo modelo de linguagem utilizando:

Pergunta do usuário;
Contexto recuperado;
Instruções para o modelo.
Status

⏳ Planejada

Fluxo:

Pergunta
     +
Contexto
     +
Instruções
     │
     ▼
Prompt

A responsabilidade ficará em:

src/eduagent/prompts/
🤖 Etapa 10 — RAG Service
Objetivo

Orquestrar o fluxo principal de recuperação e geração.

Status

⏳ Planejada

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
Gemini
   │
   ▼
Resposta

O serviço deverá coordenar os componentes sem assumir responsabilidades que pertencem às demais camadas.

A implementação ficará em:

src/eduagent/services/
💬 Etapa 11 — Chat
Objetivo

Integrar o pipeline RAG à interface do usuário.

Status

⏳ Planejada

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
🧪 Etapa 12 — Testes e validação
Objetivo

Validar o funcionamento dos componentes individualmente e do pipeline completo.

Status

⏳ Planejada

Serão considerados testes para:

Carregamento de PDFs;
Divisão dos documentos;
Geração de embeddings;
Armazenamento vetorial;
Recuperação;
Construção dos prompts;
Geração das respostas;
Interface.
📚 Etapa 13 — Documentação
Objetivo

Manter a documentação atualizada durante o desenvolvimento.

Status

🚧 Em andamento

Documentos principais:

docs/
├── aprendizados.md
├── arquitetura.md
├── diario-desenvolvimento.md
├── engenharia-da-solucao.md
├── roadmap.md
├── sprints.md
└── vision.md

Também está prevista a criação de:

docs/rag-pipeline.md

A documentação será atualizada incrementalmente, e não somente ao final do projeto.

☁️ Etapa 14 — Deploy
Objetivo

Disponibilizar a aplicação em ambiente de nuvem.

Status

⏳ Planejada

A tecnologia considerada para essa etapa é:

Oracle Cloud Infrastructure (OCI)

O deploy será realizado após a validação da aplicação localmente.

🚀 Evolução pós-desafio

Após a conclusão do projeto proposto pela formação da Alura, existe a possibilidade de utilizar a base construída para uma solução educacional mais ampla.

Uma das ideias discutidas é uma Escola Online de Espanhol.

Visão futura:

                    🌐 Landing Page
                           │
                           ▼
                    🏫 Escola Online
                           │
                           ▼
                       🤖 Agente IA
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
           Site        WhatsApp       Telegram
                           │
                           ▼
                          n8n

Essa etapa é uma visão futura e não faz parte do escopo inicial do desafio.

📊 Visão geral
┌─────────────────────────────────────────────┐
│              EDUAGENT AI                    │
├─────────────────────────────────────────────┤
│                                             │
│  Fundação                    ✅              │
│  Configuração               ✅              │
│  Interface                  ✅              │
│  Document Loader             🚧              │
│  Text Splitter               ⏳              │
│  Embeddings                  ⏳              │
│  Vector Store                ⏳              │
│  Retriever                   ⏳              │
│  Prompt Builder              ⏳              │
│  RAG Service                 ⏳              │
│  Chat                        ⏳              │
│  Testes                      ⏳              │
│  Deploy                      ⏳              │
│                                             │
└─────────────────────────────────────────────┘
🔄 Estratégia de evolução

Cada etapa deverá seguir o seguinte ciclo:

┌──────────────┐
│    Código    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Teste     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Documentação │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Commit    │
└──────┬───────┘
       │
       ▼
   Próxima etapa

Esse ciclo será utilizado para acompanhar a evolução do projeto de forma organizada.

🎯 Meta do projeto

A primeira meta é concluir uma aplicação RAG funcional capaz de:

📄 Receber documentos
       │
       ▼
📚 Processar documentos
       │
       ▼
🔢 Gerar representações vetoriais
       │
       ▼
🗄️ Armazenar documentos
       │
       ▼
🔍 Recuperar informações relevantes
       │
       ▼
🤖 Utilizar o Gemini
       │
       ▼
💬 Responder ao usuário

A solução deverá ser simples, funcional, modular e documentada antes de avançar para funcionalidades mais complexas.


## ⚠️ Uma correção importante no nosso processo

Neste documento, estou usando:

- `✅` = realmente concluído;
- `🚧` = próxima etapa/em implementação;
- `⏳` = planejado.

Isso vai nos ajudar a não cometer um erro comum em documentação de projetos: **confundir estrutura de pastas criada com funcionalidade implementada**.

### Depois de salvar

Teremos três documentos principais revisados:

```text
docs/
├── vision.md                    ✅
├── engenharia-da-solucao.md     ✅
└── arquitetura.md               ✅

