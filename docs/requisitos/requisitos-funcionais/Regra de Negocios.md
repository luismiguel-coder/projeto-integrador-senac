📄 DOCUMENTAÇÃO DE REGRAS DE NEGÓCIO 
# 📋 Documento de Regras de Negócio (RN) – Sistema Dedicado de Registro de Perdas

## 1. Segurança e Controle de Acesso (Perfil de Usuário)

* **RN01 – Restrição de Visibilidade Financeira:** O perfil Repositor/Operador não possui permissão para visualizar relatórios, painéis (*dashboards*) ou campos que contenham valores monetários de faturamento, custo ou total acumulado de perdas do supermercado.
* **RN02 – Duplo Fator de Validação:** Todo lançamento de perda exige a identificação de duas figuras distintas:
  * **Operador:** Identificado pelo ID de login ativo que realizou a coleta dos dados físicos.
  * **Validador:** Obrigatório autenticar via senha para homologar e salvar o registro no banco de dados.
* **RN03 – Fluxo de Homologação Final:** O registro de perda não entra diretamente no balanço final do sistema. Ele permanece em estado pendente e só será integrado oficialmente após a aprovação manual de um Gerente ou Analista.

---

## 2. Identificação e Entrada de Dados da Ocorrência

* **RN04 – Registro de Volumetria Exata:** O sistema deve exigir o preenchimento da Quantidade acompanhado de sua respectiva Unidade de Medida (ex: Unidade, Kg, Litro). O campo aceita valores decimais para produtos pesados (ex: `4.35 Kg`).
* **RN05 – Preço da Perda:** É obrigatório o preenchimento manual do valor unitário ou total do item afetado para fins de cálculo do prejuízo daquela ocorrência específica.
* **RN06 – Rastreabilidade de Lote:** É opcional o preenchimento manual dos campos Lote e Data de Validade, garantindo dados consolidados para cruzamento com a indústria em casos de sinistro ou ressarcimento.

---

## 3. Motivos de Descarte e Destinação Final

* **RN07 – Tabela Padronizada de Motivos:** É estritamente proibido o uso de campos de texto livre ou a opção "Outros" para justificar a perda. O operador deve selecionar obrigatoriamente uma das seguintes opções homologadas:
  * `AVARIA_FISICA`: Embalagem danificada, produto rasgado, amassado ou quebrado por cliente ou repositor.
  * `QUEBRA_CADEIA_FRIO`: Produtos congelados ou resfriados expostos fora da temperatura permitida.
  * `PRODUTO_VENCIDO`: Item que atingiu a data de validade na área de vendas.
  * `FURTO_CONSTATADO`: Embalagens encontradas vazias na loja.
* **RN08 – Destinação Final Física:** O sistema deve indicar o destino físico do item descartado selecionando uma das seguintes categorias:
  * Lixo Comum
  * Lixo Orgânico / Compostagem
  * Descarte Químico (Produtos de limpeza/higiene)
  * Devolução para Troca (Fornecedor)

---

## 4. Evidências e Inteligência Artificial

* **RN09 – Evidência Fotográfica Obrigatória:** O sistema bloqueia a finalização do registro caso não seja anexada pelo menos uma foto nítida do estado atual do produto a ser descartado.
  * *Exceção:* Caso o motivo selecionado em **RN07** seja `FURTO_CONSTATADO`, a obrigatoriedade da foto é dispensada automaticamente.
* **RN10 – Guia de Descarte por IA:** Após a seleção do produto e do motivo, o sistema exibirá na tela uma instrução automatizada via Inteligência Artificial local orientando o operador sobre as normas de segurança e práticas corretas para manusear e descartar aquele tipo de resíduo.

---

## 5. Inteligência Analítica e Relatórios (Mês Vigente vs. Anterior)

* **RN11 – Regra de Análise Comparativa Temporal:** A tela de fechamento e os relatórios gerenciais devem se comportar de forma dinâmica baseando-se no histórico existente:
  * **Cenário A (Com Histórico):** Se houver dados consolidados no banco de dados referentes ao mês imediatamente anterior, o sistema deve exibir os indicadores atuais comparados lados a lado com os do período passado (calculando a variação percentual de perdas por motivo, produto e valor).
  * **Cenário B (Sem Histórico / Primeiro Mês de Uso):** Se não houver nenhum registro no mês anterior, o sistema deve ocultar automaticamente as colunas ou gráficos de comparação e operar exibindo exclusivamente as métricas e acumulados do mês vigente.


