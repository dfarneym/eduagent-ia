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