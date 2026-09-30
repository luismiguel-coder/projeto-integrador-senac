# Especificação de Requisitos Não Funcionais (RNF) e Infraestrutura 

**Projeto:** Sistema de Registro e Gestão de Perdas – Supermercado  
**Documento:** Especificação Técnica de Infraestrutura, Arquitetura Python e Interface Mobile/PWA  
**Responsável:** Luis Miguel  
**Data de Atualização:** 29/09/2026  

---

### 1. Introdução e Objetivo
Este documento especifica a infraestrutura tecnológica e a arquitetura de software para o **Sistema de Registro de Perdas para Supermercado**. O sistema opera de forma autônoma e independente (sem integração direta com ERP/PDV), focado no registro operacional em loja através de **dispositivos móveis (celulares/tablets)** e na gestão backend desenvolvida em **Python**. 

A infraestrutura garante a captura de evidências fotográficas via câmera do celular no próprio corredor, compressão de imagens, resiliência off-line e auditoria completa dos lançamentos.

---

### 2. Tabela Detalhada de Requisitos Não Funcionais (RNF)

| Requisito (RNF) | Descrição do Funcionamento Técnico | Métrica / Indicador de Sucesso |
| :--- | :--- | :--- |
| **Interface Mobile & Usabilidade (PWA)** | Interface Web Responsiva (*Mobile-First*) otimizada para uso em celulares e leitores de código de barras. Permite captura direta de foto da avaria pela câmera do celular. | Design touch-friendly, formulário fluido no celular e integração nativa com a câmera do dispositivo sem necessidade de instalação de app de loja. |
| **Backend em Python** | API de alta performance desenvolvida em **Python (FastAPI)** para regra de negócio, autenticação e geração de relatórios. | Tempo de resposta de endpoints de lançamento em menos de 500ms; exportação de relatórios em PDF (`ReportLab`) e Excel (`Pandas`) em < 2s. |
| **Capacidade de Armazenamento & Mídia** | Dimensionamento para banco de dados relacional e repositório de arquivos de evidência fotográfica. | Suporte para upload de fotos (até 5MB em JPG/PNG) enviadas pelo celular, com compressão automática via Python (`Pillow`) e retenção por 90 dias. |
| **Escalabilidade e Multi-loja** | Arquitetura parametrizada para suportar o crescimento do volume de dados, novas filiais e setores. | Capacidade de adicionar novos supermercados, depósitos ou setores (Hortifruti, Açougue, Padaria) via painel administrativo, sem novo deploy de código. |
| **Resiliência e Conectividade Off-line** | Mecanismo de salvamento temporário no navegador do celular (PWA/LocalData) para zonas de sombra nos corredores do mercado. | Salvar lançamentos e fotos localmente no celular durante quedas de sinal e realizar a sincronização automática com o backend em até 2 segundos após reconectar. |
| **Recuperação de Desastres (DR) e Backup** | Plano de backup automático e redundância para evitar perda de dados financeiros e logs de auditoria. | Execução de backups diários automatizados do banco de dados (às 03:00h) com tempo máximo de restauração (RTO) de 4 horas. |
| **Segurança e Rastreabilidade (Auditoria)** | Restrição de acesso, tráfego criptografado (HTTPS/TLS), senhas com hash seguro e log imutável de todas as ações. | Registro automático de IP, modelo de dispositivo móvel, usuário, data/hora e tipo de alteração no Relatório de Auditoria. |

---

### 3. Arquitetura do Ambiente Tecnológico Recomendado

1. **Frontend / Cliente (Mobile & Desktop):**
   * **Tecnologia:** Progressive Web App (PWA) / HTML5 / CSS3  / JavaScript.
   * **Recursos:** Acesso à câmera nativa do celular para foto de evidência, leitor de código de barras web e interface adaptada para telas sensíveis ao toque.

2. **Backend / Servidor de Aplicação (Python):**
   * **Linguagem & Framework:** Python 3.10+ utilizando **FastAPI** .
   * **Processamento de Imagens:** Biblioteca `Pillow` para redimensionar e comprimir as fotos enviadas pelos celulares antes de salvar no disco.
   * **Relatórios e Exportações:** Bibliotecas `Pandas` / `openpyxl` para exportação em Excel (`.xlsx` e `.csv`) e `ReportLab` para relatórios consolidados em `PDF`.

3. **Banco de Dados Relacional:**
   * **Tecnologia:** PostgreSQL ou MySQL.
   * **Recursos:** Suporte a transações ACID, campos de auditoria e índices otimizados para consultas temporais (mês atual vs. mês anterior).

4. **Hospedagem e Servidor:**
   * Servidor ...  sob protocolo HTTPS com certificado SSL/TLS.
   * Bucket/Diretório seguro para arquivos de mídia com política de expiração automática de 90 dias.