# ⚙️ EduAgent AI — Engenharia da Solução

> Registro das decisões técnicas e arquiteturais adotadas durante o desenvolvimento do EduAgent AI.

---

## 🎯 Objetivo

Este documento registra as principais decisões de Engenharia de Software e Engenharia de Inteligência Artificial adotadas durante o desenvolvimento do **EduAgent AI**.

A finalidade é documentar não apenas quais tecnologias foram utilizadas, mas principalmente **por que determinadas abordagens foram escolhidas** e como elas contribuem para a evolução do projeto.

O desenvolvimento segue uma estratégia incremental:

```text
Conceito
   │
   ▼
Implementação simples
   │
   ▼
Teste
   │
   ▼
Documentação
   │
   ▼
Evolução
````
A proposta inicial é construir uma aplicação simples e funcional antes de adicionar complexidade.

## 🧱 Arquitetura Modular

Uma das primeiras decisões do projeto foi organizar a aplicação de forma modular.

A estrutura foi criada dentro de:
````
src/
└── eduagent/
````
Com módulos separados por responsabilidade:
````
src/eduagent/
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
````
Motivo da decisão

A separação das responsabilidades evita concentrar toda a lógica da aplicação em um único arquivo.

Em vez de construir uma aplicação na qual app.py seja responsável por todas as operações, cada componente possui uma função específica.

O objetivo é obter:

Maior organização;
Menor acoplamento;
Maior facilidade de manutenção;
Maior facilidade para testes;
Facilidade para substituir componentes;
Evolução incremental da aplicação.

## 🧩 Separação de Responsabilidades

A arquitetura segue como referência o princípio:

Single Responsibility Principle (SRP)

Cada componente deve possuir uma responsabilidade bem definida.

Por exemplo:
````
PDFLoader
    │
    └── Carregar documentos PDF

TextSplitter
    │
    └── Dividir documentos em chunks

Retriever
    │
    └── Recuperar informações relevantes

Prompt Builder
    │
    └── Construir o contexto utilizado pelo modelo

RAG Service
    │
    └── Coordenar o fluxo de recuperação e geração
````
A intenção é evitar que um único componente seja responsável por todas essas operações.

## 🧠 Responsabilidade da camada services

A pasta:
````
src/eduagent/services/

````

Foi criada para funcionar como uma camada de coordenação da aplicação.

Ela pode ser entendida como o "cérebro" responsável por orquestrar determinados fluxos.

Entretanto, uma decisão importante foi tomada:

A pasta services não deve concentrar todas as responsabilidades da aplicação.

As responsabilidades específicas devem continuar delegadas para seus respectivos módulos.

Por exemplo:
````
services/
      │
      ├───────────────┐
      │               │
      ▼               ▼
  loaders/        retrievers/
      │               │
      ▼               ▼
 documentos       informações
````
Dessa forma, os serviços coordenam os componentes, enquanto cada componente especializado executa sua própria responsabilidade.

## ⚙️ Configuração da aplicação

Para centralizar as configurações da aplicação foi criado o módulo:

````
src/eduagent/config/settings.py
````
Foi adotado o:
````
from pydantic_settings import BaseSettings
````
Motivo da decisão

A utilização de BaseSettings permite centralizar configurações e variáveis de ambiente em uma camada específica da aplicação.

Isso evita espalhar configurações diretamente pelo código.

A estrutura segue a ideia:
````
Aplicação
    │
    ▼
config/
    │
    ▼
settings.py
    │
    ▼
Configurações

````
Essa abordagem também facilita a separação entre código e configurações sensíveis.

## 📄 Carregamento de documentos

Para o processamento de arquivos PDF foi adotada uma camada específica de carregamento:

````
src/eduagent/loaders/
````
A responsabilidade desse módulo é receber um arquivo PDF, processá-lo e retornar documentos em um formato que possa ser utilizado pelas etapas seguintes do pipeline.

Foi utilizada a abstração:

````
PyPDFLoader
````

do ecossistema LangChain.

## 🔌 Por que encapsular o PyPDFLoader?

Uma decisão arquitetural importante foi não espalhar chamadas ao PyPDFLoader pela aplicação.

A ideia é criar uma camada própria para o carregamento dos documentos.

Conceitualmente:
````
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
````
Dessa forma, o restante da aplicação depende da nossa abstração PDFLoader, e não diretamente da implementação específica da biblioteca.

Benefício

Caso futuramente seja necessário substituir a biblioteca utilizada para leitura dos PDFs, a alteração ficará concentrada principalmente na camada de loaders.

Isso reduz o acoplamento.

## ✂️ Divisão dos documentos

Após o carregamento dos documentos, será necessário dividir os conteúdos em partes menores.

Para isso foi criada a estrutura:
````
src/eduagent/splitters/
````
A solução planejada utiliza:

````
RecursiveCharacterTextSplitter
````

O objetivo é criar chunks que mantenham o máximo possível de contexto sem gerar partes excessivamente grandes.

O fluxo será:

````
PDF
 │
 ▼
PDF Loader
 │
 ▼
Documents
 │
 ▼
Text Splitter
 │
 ▼
Chunks
````

A implementação dessa etapa será realizada posteriormente.

## 🔢 Embeddings

Após a divisão dos documentos, o conteúdo poderá ser transformado em representações vetoriais.

Essa responsabilidade ficará isolada em:
````
src/eduagent/embeddings/
````

O conceito de embeddings é importante para o funcionamento da busca semântica.

Em vez de depender exclusivamente da correspondência literal de palavras-chave, o conteúdo será representado matematicamente em um espaço vetorial.

Essa etapa ainda será implementada.

## 🗄️ Banco Vetorial

Para a primeira implementação do projeto foi escolhido o FAISS.

A responsabilidade será isolada em:
````
src/eduagent/vectorstore/
````
O banco vetorial será utilizado para armazenar e consultar as representações vetoriais dos documentos.

O fluxo planejado é:
````
Chunks
   │
   ▼
Embeddings
   │
   ▼
FAISS
````
Motivo da escolha

A escolha inicial do FAISS está relacionada à proposta de manter a primeira implementação simples e adequada ao objetivo educacional do projeto.

A intenção é primeiro compreender e implementar corretamente o pipeline RAG antes de introduzir uma infraestrutura mais complexa.

## 🔄 Possibilidade de substituir FAISS

Durante o planejamento foi discutida a possibilidade de utilizar ChromaDB futuramente.

A arquitetura modular facilita essa mudança porque o armazenamento vetorial está isolado em:

````
vectorstore/
````

Assim, a aplicação não precisa conhecer diretamente todos os detalhes internos do banco vetorial.

Conceitualmente:

                    Vector Store
                         │
              ┌──────────┴──────────┐
              │                     │
             FAISS               ChromaDB

A decisão atual é utilizar FAISS na primeira implementação e manter a possibilidade de evolução posteriormente.

## 🔍 Retriever

O Retriever será responsável por receber uma consulta e recuperar os documentos ou chunks mais relevantes para aquela pergunta.

Conceitualmente:

````
Pergunta
   │
   ▼
Retriever
   │
   ▼
Busca no Vector Store
   │
   ▼
Documentos relevantes
````

Essa responsabilidade será isolada em:

````
src/eduagent/retrievers/
````
O Retriever ainda será implementado nas próximas etapas.

## 📝 Prompt Builder

A construção dos prompts será isolada em:
````
src/eduagent/prompts/
````

A responsabilidade será organizar a instrução enviada ao modelo de linguagem juntamente com o contexto recuperado.

O conceito planejado é:
````
Pergunta
   +
Contexto recuperado
   +
Instruções
   │
   ▼
Prompt
````
Essa separação permite modificar a estratégia de prompting sem alterar diretamente outras partes do pipeline.

## 🤖 Modelo de linguagem

O projeto utiliza o ecossistema do Google Gemini como modelo de linguagem.

O modelo será utilizado na etapa de geração das respostas após a recuperação das informações relevantes.

Conceitualmente:
````
Contexto recuperado
        +
     Pergunta
        │
        ▼
     Gemini
        │
        ▼
     Resposta
````
A integração com o modelo será utilizada como parte do pipeline RAG.

## 🔗 RAG

O conceito central da solução é:

Retrieval-Augmented Generation — RAG

O fluxo planejado é:

                    ┌───────────────┐
                    │  Documentos   │
                    └───────┬───────┘
                            │
                            ▼
                       PDF Loader
                            │
                            ▼
                        Splitter
                            │
                            ▼
                        Embeddings
                            │
                            ▼
                      Vector Store
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

O objetivo é permitir que o modelo utilize informações recuperadas da documentação como contexto para gerar respostas.

## 🖥️ Interface Streamlit

O Streamlit foi escolhido para a construção da interface inicial.

A principal motivação é permitir desenvolver rapidamente uma aplicação web utilizando Python, sem introduzir inicialmente uma arquitetura frontend/backend mais complexa.

O fluxo inicial é:
````
👤 Usuário
     │
     ▼
🖥️ Streamlit
     │
     ▼
💬 Interface
````
A interface poderá ser modularizada conforme novos componentes forem adicionados.

## 🧩 Modularização da interface

Também foi tomada a decisão de não concentrar toda a interface em um único componente.

A separação em componentes permite que diferentes partes da interface possuam responsabilidades específicas.

Conceitualmente:
````
ui/
│
├── componente A
├── componente B
└── componente C
````
Essa abordagem facilita a identificação e correção de problemas.

Se um componente apresentar uma falha, a investigação pode ser concentrada naquele componente específico.

## 🧪 Desenvolvimento incremental

O projeto está sendo desenvolvido de forma incremental.

A estratégia adotada é:
````
1. Criar estrutura
        │
        ▼
2. Implementar componente
        │
        ▼
3. Executar e testar
        │
        ▼
4. Documentar
        │
        ▼
5.    Commit
        │
        ▼
6. Próximo componente
````
Essa abordagem evita tentar construir todo o agente de uma única vez.

## 📚 Estratégia de aprendizagem

O projeto também possui uma finalidade educacional.

Por isso, as tecnologias não estão sendo utilizadas apenas como "caixas pretas".

Durante o desenvolvimento busca-se compreender:
````
O papel de cada componente;
A responsabilidade de cada camada;
O fluxo de dados;
O motivo de cada decisão;
O relacionamento entre os componentes;
As limitações da solução;
As possibilidades de evolução.
````
O objetivo é compreender tanto como implementar quanto por que implementar dessa maneira.

## 🔭 Evolução futura

Após a conclusão do agente básico proposto no desafio, foi considerada uma evolução para uma solução de Curso de Espanhol / Escola Online.

A visão futura contempla:

                    🌐 Landing Page
                           │
                           ▼
                    🏫 Site da Escola
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

O n8n poderá ser utilizado posteriormente como camada de automação e integração entre os diferentes canais.

Essa arquitetura representa uma evolução futura e não faz parte do estado atual da aplicação.

## 📌 Estado da solução

Neste momento, o projeto está concentrado na construção da base arquitetural e dos primeiros componentes.
````
Implementado / estruturado
Estrutura modular;
Configuração da aplicação;
Interface inicial com Streamlit;
Organização dos módulos;
Estrutura para loaders;
Estrutura para splitters;
Estrutura para embeddings;
Estrutura para retrievers;
Estrutura para vector store;
Estrutura para prompts;
Estrutura para services;
Estrutura para UI.
Em desenvolvimento
Text Splitter;
Pipeline de ingestão;
Embeddings;
Vector Store;
Retriever;
Prompt Builder;
RAG Service;
Interface de atendimento.
Futuro
Deploy em nuvem;
Plataforma educacional completa;
Landing Page;
Curso de Espanhol;
Integração com WhatsApp;
Integração com Telegram;
Automação com n8n.
````
## 📌 Princípio geral da solução

A Engenharia da Solução do EduAgent AI segue uma ideia central:

Começar simples, separar responsabilidades e evoluir incrementalmente.

A arquitetura deve permitir que novos componentes sejam adicionados sem exigir a reescrita completa da aplicação.

O projeto prioriza:
````
Simplicidade
     +
Modularidade
     +
Baixo acoplamento
     +
Responsabilidade única
     +
Evolução incremental
     +
Documentação
````
