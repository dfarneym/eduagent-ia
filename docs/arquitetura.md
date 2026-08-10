# 🏗️ EduAgent AI — Arquitetura

> Documentação da arquitetura atual e da evolução planejada do EduAgent AI.

---

## 📌 Objetivo da arquitetura

A arquitetura do EduAgent AI foi organizada para separar as responsabilidades da aplicação em módulos independentes.

O objetivo é evitar que a lógica fique concentrada em um único arquivo e permitir que cada componente seja desenvolvido, testado e evoluído de forma independente.

A estrutura utiliza:

```text
src/eduagent/
````
🟢 Arquitetura Atual — Implementada

A arquitetura abaixo representa o estado atual da estrutura do projeto.

                         👤 Usuário
                              │
                              ▼
                          📄 app.py
                              │
                              ▼
                    🖥️ Interface Streamlit
                              │
                              ▼
                  🧩 Componentes da Interface
                              │
                              ▼
                       ⚙️ Configuração
                       settings.py
                              │
                              ▼
                     📦 Núcleo da Aplicação
                       src/eduagent
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
        📄 Loaders        ✂️ Splitters      🔢 Embeddings
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
       🔍 Retrievers      📝 Prompts       🗄️ Vector Store
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
                              ▼
                        ⚙️ Services
Observação

A existência dos módulos na estrutura do projeto não significa que todos os componentes acima já estejam implementados funcionalmente.

Neste momento, parte deles representa a estrutura arquitetural preparada para receber as próximas implementações.

📂 Estrutura modular atual

A estrutura principal do projeto é:

eduagent-ia/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── docs/
│
└── src/
    │
    └── eduagent/
        │
        ├── __init__.py
        │
        ├── config/
        │   ├── __init__.py
        │   └── settings.py
        │
        ├── embeddings/
        │   └── __init__.py
        │
        ├── loaders/
        │   └── __init__.py
        │
        ├── prompts/
        │   └── __init__.py
        │
        ├── retrievers/
        │   └── __init__.py
        │
        ├── services/
        │   └── __init__.py
        │
        ├── splitters/
        │   └── __init__.py
        │
        ├── ui/
        │   └── __init__.py
        │
        ├── utils/
        │   └── __init__.py
        │
        └── vectorstore/
            └── __init__.py

Essa estrutura representa a separação inicial das responsabilidades do sistema.

🧩 Responsabilidades dos módulos
config

Centraliza as configurações da aplicação.

Principal arquivo:

config/settings.py

Responsabilidade:

⚙️ Configurações
     │
     ▼
Variáveis de ambiente
     │
     ▼
Configuração da aplicação
loaders

Responsável pelo carregamento dos documentos.

A primeira fonte considerada é o formato PDF.

Fluxo:

📄 PDF
 │
 ▼
PDF Loader
 │
 ▼
Document

O carregamento utiliza a abstração PyPDFLoader.

splitters

Responsável pela divisão dos documentos em partes menores.

O componente planejado é:

RecursiveCharacterTextSplitter

Fluxo:

Document
   │
   ▼
Text Splitter
   │
   ▼
Chunks
embeddings

Responsável pela transformação dos textos em representações vetoriais.

Fluxo planejado:

Chunks
   │
   ▼
Embeddings
   │
   ▼
Vetores
vectorstore

Responsável pelo armazenamento e consulta das representações vetoriais.

A primeira implementação planejada utiliza:

FAISS

Fluxo:

Vetores
   │
   ▼
FAISS

A arquitetura também permite uma futura substituição por outra tecnologia, como ChromaDB.

retrievers

Responsável pela recuperação dos conteúdos relevantes para uma consulta.

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
prompts

Responsável pela construção dos prompts utilizados pelo modelo de linguagem.

Fluxo:

Pergunta
     +
Contexto recuperado
     +
Instruções
     │
     ▼
   Prompt
services

Responsável pela coordenação dos fluxos da aplicação.

A pasta services funciona como uma camada de orquestração.

Entretanto, a arquitetura evita concentrar nela todas as responsabilidades.

A ideia é:

                  ⚙️ Services
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Loaders      Retriever     Prompt
          │            │            │
          ▼            ▼            ▼
      Documentos    Contexto     Instruções

Dessa maneira, cada componente permanece responsável por sua própria função.

ui

Responsável pelos componentes da interface.

A interface utiliza inicialmente:

Streamlit

O objetivo é evitar que toda a lógica visual fique concentrada em app.py.

utils

Reservado para funções auxiliares que não pertençam diretamente a uma responsabilidade específica dos demais módulos.

🔄 Arquitetura do Pipeline RAG

A arquitetura completa do agente será construída progressivamente.

O fluxo planejado é:

                       📄 Documentos
                             │
                             ▼
                      📥 PDF Loader
                             │
                             ▼
                       📑 Documents
                             │
                             ▼
                       ✂️ Splitter
                             │
                             ▼
                         🧩 Chunks
                             │
                             ▼
                       🔢 Embeddings
                             │
                             ▼
                     🗄️ Vector Store
                             │
                             ▼
                        🔍 Retriever
                             │
                             ▼
                       📚 Contexto
                             │
                  ┌──────────┴──────────┐
                  │                     │
                  ▼                     ▼
           ❓ Pergunta             📝 Prompt
                  │                     │
                  └──────────┬──────────┘
                             │
                             ▼
                       🤖 Google Gemini
                             │
                             ▼
                       💬 Resposta

Esse diagrama representa a arquitetura planejada do pipeline RAG, e não significa que todos os componentes já estejam implementados.

🔍 Fluxo de recuperação

A etapa de recuperação deverá seguir o fluxo:

👤 Usuário
    │
    ▼
❓ Pergunta
    │
    ▼
🔢 Representação vetorial
    │
    ▼
🔍 Retriever
    │
    ▼
🗄️ Vector Store
    │
    ▼
📚 Trechos relevantes

Esses trechos serão posteriormente utilizados como contexto para a geração da resposta.

🤖 Fluxo de geração

Depois da recuperação:

📚 Contexto recuperado
          +
❓ Pergunta
          │
          ▼
     📝 Prompt
          │
          ▼
   🤖 Google Gemini
          │
          ▼
      💬 Resposta

O objetivo é gerar uma resposta baseada no contexto recuperado dos documentos.

🔌 Baixo acoplamento

Um dos princípios arquiteturais do projeto é reduzir o acoplamento entre os componentes.

Por exemplo, a aplicação não deve depender diretamente da implementação interna do carregador de PDF.

Em vez disso:

Aplicação
    │
    ▼
PDFLoader
    │
    ▼
PyPDFLoader

Da mesma forma, a aplicação deve interagir com a camada de armazenamento vetorial por meio de uma responsabilidade bem definida:

Retriever
    │
    ▼
Vector Store
    │
    ├── FAISS
    │
    └── ChromaDB

Isso permite que a tecnologia utilizada seja substituída com menor impacto no restante da aplicação.

🔁 Evolução da arquitetura

A arquitetura será construída em etapas.

Etapa atual
Estrutura modular
       │
       ▼
Configuração
       │
       ▼
Interface
Próxima evolução
PDF
 │
 ▼
Loader
 │
 ▼
Splitter
 │
 ▼
Chunks
Evolução seguinte
Chunks
 │
 ▼
Embeddings
 │
 ▼
FAISS
Pipeline RAG
Pergunta
 │
 ▼
Retriever
 │
 ▼
Contexto
 │
 ▼
Prompt
 │
 ▼
Gemini
 │
 ▼
Resposta
🧭 Princípio arquitetural

A arquitetura do EduAgent AI segue o seguinte princípio:

                    RESPONSABILIDADE
                           │
                           ▼
                    MÓDULO ESPECÍFICO
                           │
                           ▼
                    SERVIÇO DE ORQUESTRAÇÃO
                           │
                           ▼
                         FLUXO

Ou seja:

Cada componente executa uma responsabilidade específica, enquanto os serviços coordenam o fluxo entre esses componentes.

📌 Estado da arquitetura
✅ Estrutura criada
config
embeddings
loaders
prompts
retrievers
services
splitters
ui
utils
vectorstore
✅ Componentes estruturais
app.py
settings.py
Ambiente virtual;
Dependências do projeto;
Interface inicial com Streamlit.
🚧 Próximas implementações
PDF Loader;
Text Splitter;
Pipeline de ingestão;
Embeddings;
FAISS;
Retriever;
Prompt Builder;
RAG Service;
Interface de chat.
🎯 Objetivo arquitetural

A arquitetura não pretende começar como uma solução excessivamente complexa.

O objetivo é construir uma base:

Simples
   +
Modular
   +
Testável
   +
Documentada
   +
Evolutiva

A complexidade deverá ser adicionada somente quando existir uma necessidade real no projeto.

Isso permite que o EduAgent AI evolua de uma aplicação educacional simples para uma solução de agente de IA mais completa sem exigir uma reestruturação total da aplicação.


## ⚠️ Uma observação importante

Neste arquivo eu fiz uma distinção que será importante para o restante do projeto:

**`Estrutura criada` ≠ `funcionalidade implementada`.**

Por exemplo, você já possui:

```text
vectorstore/
splitters/
embeddings/
retrievers/

mas isso não significa que FAISS, splitter, embeddings e retriever já estejam funcionando no pipeline.

Isso deixa sua documentação tecnicamente honesta e, ao mesmo tempo, mostra que você já planejou a arquitetura.