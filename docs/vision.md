# 🎓 EduAgent AI — Visão do Projeto

> Agente de Inteligência Artificial para consulta inteligente à documentação de instituições de ensino.

---

## 🎯 Visão

O **EduAgent AI** é um projeto desenvolvido como parte da minha jornada de aprendizagem em **Engenharia de Inteligência Artificial**, com foco na construção de agentes capazes de consultar documentos institucionais e fornecer respostas em linguagem natural.

A proposta é desenvolver uma aplicação que permita que estudantes, colaboradores ou usuários de uma instituição de ensino encontrem informações presentes em documentos sem precisar realizar manualmente a leitura de arquivos extensos.

A solução utiliza como base o conceito de **RAG — Retrieval-Augmented Generation (Geração Aumentada por Recuperação)**.

---

## 🧩 Problema

Instituições de ensino possuem diversos documentos que concentram informações importantes, como:

- Regulamentos;
- Políticas institucionais;
- Perguntas frequentes;
- Informações sobre cursos;
- Regras para certificação;
- Programas de bolsas;
- Orientações para utilização da plataforma;
- Outros documentos administrativos e acadêmicos.

Quando essas informações estão distribuídas em vários arquivos, localizar uma informação específica pode exigir tempo e leitura manual.

O problema que o EduAgent AI busca solucionar é:

> **Como permitir que um usuário consulte documentos institucionais utilizando linguagem natural e receba uma resposta objetiva baseada no conteúdo desses documentos?**

---

## 💡 Solução proposta

O EduAgent AI propõe uma aplicação de Inteligência Artificial capaz de:

1. Receber documentos institucionais;
2. Processar e preparar o conteúdo desses documentos;
3. Dividir os documentos em partes menores;
4. Transformar os conteúdos em representações vetoriais;
5. Armazenar essas representações em um banco vetorial;
6. Recuperar os trechos mais relevantes para uma pergunta;
7. Utilizar esses trechos como contexto para um modelo de linguagem;
8. Gerar uma resposta baseada na documentação disponibilizada.

O fluxo conceitual da solução é:

```text
📄 Documentos
      │
      ▼
📚 Processamento
      │
      ▼
✂️ Divisão em chunks
      │
      ▼
🔢 Embeddings
      │
      ▼
🗄️ Banco Vetorial
      │
      ▼
🔍 Recuperação
      │
      ▼
📝 Contexto
      │
      ▼
🤖 Modelo de Linguagem
      │
      ▼
💬 Resposta

🤖 Conceito de RAG

O projeto utiliza o conceito de Retrieval-Augmented Generation (RAG).

A ideia é combinar duas etapas:

1. Retrieval — Recuperação

O sistema recebe uma pergunta e realiza uma busca para encontrar os trechos dos documentos mais relevantes para aquela pergunta.

O componente responsável por essa etapa será o Retriever.

2. Generation — Geração

Os trechos recuperados são utilizados como contexto para o modelo de linguagem.

O modelo então gera uma resposta baseada nas informações recuperadas.

De forma simplificada:

Pergunta do usuário
        │
        ▼
Busca por informações relevantes
        │
        ▼
Contexto recuperado
        │
        ▼
Prompt + Contexto
        │
        ▼
Modelo de linguagem
        │
        ▼
Resposta
🏫 Contexto educacional

O projeto foi inicialmente concebido para atender ao desafio proposto pela formação da Alura, utilizando uma instituição de ensino como contexto para aplicação do agente.

Como documentação de referência para o projeto, foram definidos exemplos de documentos que poderiam ser utilizados pelo agente:

Regulamento do estudante;
Política de reembolso de matrículas;
Perguntas frequentes sobre cursos e certificados;
Guia de uso da plataforma;
Programa de bolsas e afiliados.

Esses documentos representam um cenário no qual o usuário poderia consultar informações institucionais utilizando perguntas em linguagem natural.

🖥️ Interface

A aplicação utiliza Streamlit como tecnologia para construção da interface.

O Streamlit foi escolhido por permitir desenvolver rapidamente uma interface para aplicações de Inteligência Artificial utilizando Python, mantendo o foco principal do projeto no funcionamento do agente.

A interface atual representa a primeira camada de interação da aplicação:

👤 Usuário
    │
    ▼
🖥️ Streamlit
    │
    ▼
💬 Interface da aplicação

A interface será evoluída conforme os componentes do agente forem implementados.

🧱 Arquitetura modular

O projeto utiliza uma estrutura modular organizada dentro de:

src/eduagent/

A proposta é separar as responsabilidades da aplicação em diferentes módulos.

Estrutura atual:

src/
└── eduagent/
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

Essa organização busca evitar que toda a lógica da aplicação fique concentrada em um único arquivo ou componente.

Cada módulo deverá possuir uma responsabilidade específica.

🧠 Responsabilidade dos principais módulos
config/

Responsável pelas configurações da aplicação.

Atualmente contém a configuração centralizada utilizando pydantic-settings.

loaders/

Responsável pelo carregamento dos documentos.

Para documentos PDF, o projeto utiliza o PyPDFLoader, disponibilizado pelo ecossistema LangChain.

A responsabilidade do loader é receber um arquivo e transformá-lo em objetos Document.

splitters/

Responsável pela divisão dos documentos em partes menores, chamadas de chunks.

Será utilizado o RecursiveCharacterTextSplitter.

embeddings/

Responsável pela geração das representações vetoriais dos textos.

Essa etapa será implementada posteriormente.

vectorstore/

Responsável pelo armazenamento das representações vetoriais.

A implementação inicial planejada utiliza FAISS.

retrievers/

Responsável pela recuperação dos conteúdos mais relevantes para uma determinada pergunta.

Essa camada será desenvolvida posteriormente.

prompts/

Responsável pela construção e organização dos prompts utilizados pelo agente.

services/

Responsável por orquestrar partes do fluxo da aplicação.

A pasta services não deverá concentrar todas as responsabilidades. A intenção é utilizá-la como camada de coordenação entre os componentes especializados.

ui/

Responsável pelos componentes relacionados à interface da aplicação.

A separação da interface em componentes permite reduzir o acoplamento e facilita a manutenção.

🔐 Princípios adotados

Durante o desenvolvimento, alguns princípios de Engenharia de Software estão sendo utilizados como referência.

Single Responsibility Principle — SRP

Cada componente deve possuir uma responsabilidade específica.

Por exemplo:

PDFLoader
    │
    └── Responsável por carregar PDFs

TextSplitter
    │
    └── Responsável por dividir documentos

Retriever
    │
    └── Responsável por recuperar informações
Baixo acoplamento

A aplicação busca reduzir a dependência direta entre os componentes.

Por exemplo, o restante da aplicação não precisa conhecer os detalhes internos utilizados pelo PDFLoader para carregar um PDF.

Isso facilita futuras substituições de bibliotecas ou tecnologias.

Separação de responsabilidades

A aplicação não deve concentrar todas as tarefas em app.py ou em um único serviço.

O objetivo é distribuir as responsabilidades entre módulos especializados.

🛠️ Tecnologias

As principais tecnologias utilizadas ou planejadas para o projeto são:

Tecnologia	Finalidade
Python	Linguagem principal
LangChain	Construção do pipeline do agente
Google Gemini	Modelo de linguagem
PyPDF	Processamento de PDFs
PyPDFLoader	Carregamento de PDFs
FAISS	Banco vetorial
Streamlit	Interface da aplicação
Pydantic Settings	Gerenciamento de configurações
Git	Controle de versão
GitHub	Hospedagem do código
📈 Estado atual

O projeto encontra-se em desenvolvimento.

Até o momento foram estabelecidas:

Estrutura modular da aplicação;
Configuração centralizada;
Interface inicial utilizando Streamlit;
Organização dos módulos responsáveis pelas diferentes etapas do agente;
Definição da arquitetura inicial;
Definição da estratégia de processamento de documentos;
Implementação/estruturação do carregamento de documentos PDF;
Planejamento do pipeline RAG.

Os componentes de splitter, embeddings, banco vetorial, retriever e geração de respostas ainda serão desenvolvidos nas próximas etapas.

🚀 Evolução planejada

Após a implementação do agente básico para o desafio da Alura, o projeto poderá evoluir para uma solução educacional mais ampla.

Uma das possibilidades estudadas é transformar o EduAgent AI em uma solução para uma Escola Online de Espanhol, incluindo:

🌐 Landing Page
      │
      ▼
🏫 Site da Escola
      │
      ▼
🤖 Atendimento com IA
      │
      ├── Site
      ├── WhatsApp
      └── Telegram

Essa evolução poderá utilizar ferramentas de automação, como n8n, para integração dos canais de atendimento.

Essa etapa representa uma visão futura do projeto e não faz parte da implementação atual do desafio.

☁️ Deploy

Uma das etapas finais do desafio é disponibilizar a aplicação na nuvem.

A tecnologia inicialmente considerada para essa etapa é a Oracle Cloud Infrastructure (OCI), utilizando uma instância de Compute.

O deploy será realizado somente após o funcionamento e validação da aplicação no ambiente local.

🎓 Objetivo de aprendizagem

Mais do que desenvolver uma aplicação funcional, o projeto tem como objetivo consolidar conhecimentos relacionados a:

Desenvolvimento de aplicações Python;
Arquitetura modular;
Engenharia de Software;
LangChain;
RAG;
Engenharia de Prompts;
Embeddings;
Bancos vetoriais;
Agentes de Inteligência Artificial;
Streamlit;
Deploy em nuvem;
Organização e documentação de projetos;
Controle de versão com Git e GitHub.
📌 Visão de longo prazo

O EduAgent AI está sendo desenvolvido inicialmente como um projeto educacional para aplicação prática dos conceitos estudados durante a formação.

A visão de longo prazo é utilizar a base construída para experimentar arquiteturas mais robustas de agentes de IA aplicados à educação, mantendo como princípios:

Simplicidade
    +
Modularidade
    +
Baixo acoplamento
    +
Documentação
    +
Evolução incremental

A primeira meta é construir uma solução simples, funcional e bem documentada.

A evolução para uma plataforma educacional completa será realizada posteriormente, após a conclusão e entrega do desafio inicial.

