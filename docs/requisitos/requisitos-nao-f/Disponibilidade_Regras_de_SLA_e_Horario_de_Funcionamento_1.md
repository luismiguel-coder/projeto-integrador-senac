**ESTRUTURA PADRÃO DO**

**DOCUMENTO DE ENTREGA**

- **Projeto:** Sistema de Gestão de Perdas – Supermercado

- **Documento:** Disponibilidade, Regras de SLA e Horário de
  Funcionamento

- **Equipe Responsável:** Grupo \[1\]

- **Líder de Área:** \[Emilli\]

- **Data de Emissão:** \[23/08/2026\]

1.  **INTRODUÇÃO E OBJETIVO**

*Este documento define os requisitos de disponibilidade, horário de
funcionamento e regras de SLA do Sistema de Gestão de Perdas. O objetivo
é garantir que o sistema permaneça disponível durante o período de
operação do supermercado, reduzindo impactos nas atividades e evitando
perdas causadas por indisponibilidade.*

2.  **DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)**

**Métrica/Indicador de Requisito (RNF) Descrição do Funcionamento**

> **Sucesso**
>
> O sistema deverá permanecer disponível continuamente,

Disponibilidade de 24

> **Disponibilidade do** permitindo o registro e

horas por dia, 7 dias por

**Sistema** acompanhamento das perdas

> semana. durante o funcionamento do supermercado.

<table style="width:98%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: right;"><p>100% de
disponibilidade</p>
<blockquote>
<p>O sistema deverá garantir durante o horário de</p>
</blockquote>
<p><strong>Disponibilidade no</strong> prioridade de funcionamento
funcionamento do cliente,</p>
<p><strong>Horário do Cliente</strong> durante todo o horário de</p>
<p>exceto em situações</p></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: right;"></td>
<td style="text-align: right;">operação do supermercado.
emergenciais.</td>
</tr>
<tr>
<td style="text-align: right;"><strong>Manutenção
Programada</strong></td>
<td style="text-align: right;"><p>Atualizações e manutenções</p>
<p>que possam afetar o 100% das manutenções funcionamento ou programadas
realizadas desempenho deverão ser fora do horário de realizadas fora do
horário de funcionamento. funcionamento do cliente.</p></td>
</tr>
<tr>
<td style="text-align: right;"><strong>Manutenção
Emergencial</strong></td>
<td style="text-align: right;"><p>Em caso de falha grave ou</p>
<p>Início da intervenção em situação que comprometa a até 15 minutos
após a estabilidade e segurança do identificação de uma falha sistema, a
manutenção deverá</p>
<p>crítica. ser iniciada imediatamente.</p></td>
</tr>
<tr>
<td style="text-align: right;"><strong>Comunicação de
Indisponibilidade</strong></td>
<td style="text-align: right;">Sempre que possível, o cliente
Comunicação realizada deverá ser informado com no mínimo 24 horas de
previamente sobre antecedência para manutenções programadas e
manutenções seus possíveis impactos. programadas.</td>
</tr>
<tr>
<td style="text-align: right;"><strong>Continuidade do
Serviço</strong></td>
<td style="text-align: right;">O sistema deverá priorizar a estabilidade
e a continuidade Interrupções não da operação, principalmente planejadas
devem ser durante o horário de tratadas imediatamente funcionamento do
após sua identificação. supermercado.</td>
</tr>
</tbody>
</table>

3.  **MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)**

> • **RN-05:** \[Notificações via Dashboard, E-mail e WhatsApp para
> anomalias.\] – Relaciona-se ao requisito de comunicação de
> indisponibilidades e intervenções, permitindo que informações
> importantes sobre anomalias e possíveis impactos sejam comunicadas aos
> responsáveis.
