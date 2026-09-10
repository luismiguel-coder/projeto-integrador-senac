**ENTREGA: RNF – MANUTENIBILIDADE**

- **Projeto:** Sistema de Gestão de Perdas – Supermercado

- **Documento:** Especificação de Requisitos Não Funcionais (RNF)

- **Equipe Responsável:** Grupo 1 (Documentação e Suporte)

- **Líder de Área:** Emilli

- **Data de Emissão:** \[Preencher Data\]

**1. INTRODUÇÃO E OBJETIVO**

**Pergunta para Alaíde:**

*Pensando no dono do mercado, por que é importante ter um manual que
ensine a usar o sistema e um plano para quando algo der erro? Como isso
ajuda a não perder dinheiro?*

**Sua Resposta (Escreva aqui):**

**Ter um manual que ensine todos a usarem o sistema corretamente
evitando erros por desconhecimento, já o plano garante que se algo
falhar o trabalho não pare e as operações continue, assim não há
interrupção no controle do estoque e de perdas evitando prejuízo e
mantendo controle eficiente para proteger o lucro do marcado.**

**2. DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)**

*Alaíde, preencha as explicações simples na tabela abaixo baseada no que
o sistema deve fazer:*

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 52%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th><strong>Processo e Suporte</strong></th>
<th style="text-align: left;"><p><em>Se o "bipado" de produtos estragar
ou a internet cair, o que o sistema deve deixar o funcionário fazer para
o trabalho não parar?</em></p>
<p><strong>Sua resposta:</strong></p>
<p><strong>O funcionário cadastre e registre os produtos e perdas de
forma manual informando o motivo da digitação manual com justificativa
obrigatória, toda vez que alguém registrar uma perda, o sistema deve
gravar quem fez, qual o produto foi, quantidade motivo da perda além de
data, hora e IP de forma que não possa ser alterado
depois</strong></p></th>
<th><blockquote>
<p>Opção de <strong>cadastro manual</strong> com justificativa
obrigatória.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Monitoramento Logs</strong></td>
<td><p><em>Para o dono do mercado ter certeza de que ninguém está
mentindo sobre os produtos, que informações o sistema deve gravar toda
vez que alguém registrar uma perda?</em></p>
<blockquote>
<p><strong>Sua resposta:</strong></p>
</blockquote>
<p><strong>Registro imutável ID do usuário, Data, Hora e
IP.</strong></p></td>
<td><blockquote>
<p>Registro imutável de: <strong>ID do usuário, Data, Hora e
IP</strong>.</p>
</blockquote></td>
</tr>
<tr>
<td><strong>Documentação Técnica</strong></td>
<td><p><em>Como o manual deve ser feito para que, daqui a um ano, outro
técnico consiga consertar o sistema rápido?</em></p>
<p><strong>Sua resposta:</strong></p>
<p><strong>O manual deve ser claro organizado e completo, com
explicações simples passo a passo, diagramas e informações sobre como o
sistema funciona, onde ficam os arquivos e como é o banco de
dados.</strong></p></td>
<td><blockquote>
<p>Documentação organizada detalhando a estrutura do <strong>banco de
dados</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

**3. MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)**

*Alaíde, como essas tarefas ajudam a cumprir as ordens do projeto?*

- **RN-09 (Segurança e Confiabilidade):** O registro de quem fez a
  operação (Logs) garante que as informações não sejam apagadas para
  esconder erros.

- **RN-10 (Investigação de Divergências):** Se houver uma **diferença
  maior que 5%** no estoque, os registros ajudam o gerente a descobrir
  quem foi o último a mexer no produto.

**4. INTEGRAÇÃO E SEGURANÇA**

**Pergunta para Alaíde:** *Quem você acha que deve ter o poder de ver
esses relatórios de erros e quem mexeu no estoque? (O Gerente ou
qualquer funcionário?)*

**Sua Resposta (Escreva aqui):**

**Apenas o gerente e o dono de mercado**

*(Nota Técnica: O acesso deve ser restrito conforme o perfil, protegendo
dados sensíveis de custos)*

**5. VALIDAÇÃO DO LÍDER GERAL E LÍDER DE ÁREA**

- **1ª Revisão Técnica realizada por:** Luis Miguel (Líder Geral)

- **Parecer:** ( ) Aprovado \| ( ) Necessita Ajustes

- **2ª Revisão de Liderança realizada por:** Emilli (Líder de Área)

- **Parecer:** ( ) Aprovado \| ( ) Necessita Ajustes
