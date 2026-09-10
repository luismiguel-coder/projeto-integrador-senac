📄 DOCUMENTAÇÃO DE REGRAS DE NEGÓCIO E STAKEHOLDERS

👥 Stakeholders Envolvidos

O sistema atende a oito perfis principais.

Proprietário/Gestor é o decisor estratégico responsável por aprovar
políticas e analisar relatórios financeiros.

Administrador do Sistema cuida do cadastro de produtos, usuários e
configurações do sistema.

Operador de Estoque realiza os registros diários de movimentação,
conferência de validade e identificação de produtos danificados.

Controle de Qualidade fiscaliza perdas, autoriza descartes e audita os
processos de validade.

Fornecedor realiza as entregas e emite notas fiscais.

O Cliente Final é impactado pelo recebimento de produtos em bom estado e
dentro do prazo de validade.

Auditor/Contador valida a rastreabilidade e a conformidade dos
relatórios financeiros.

TI/Segurança da Informação garante os backups, a integridade do banco de
dados e o controle de acesso simultâneo.

🏗️ Regras de Negócio

RN-01 (Controle de Estoque Inteligente): O estoque nunca pode ficar
negativo. Todo produto exige a definição de quantidade mínima e máxima,
com atualização do saldo em tempo real e suporte a múltiplos locais.

RN-02 (Classificação de Movimentações): Toda movimentação deve ser
obrigatoriamente classificada como Entrada, Saída ou Ajuste, alterando o
saldo imediatamente e gerando histórico auditável.

RN-03 (Informações Obrigatórias):Todo registro deve conter data, hora,
ID do usuário, tipo de movimentação, ID do produto, quantidade,
validade, lote, justificativa e condição do item.

RN-04 (Custo Médio Automático): O sistema calcula automaticamente o
custo médio ponderado do produto a cada nova entrada, atualizando os
relatórios de valorização do estoque.

RN-05 (Alertas Automáticos): Disparo de notificações via Dashboard,
E-mail e WhatsApp para estoque baixo, produtos sem movimentação,
validade próxima, vencidos, itens danificados e diferenças na contagem.

RN-06 (Controle de Acesso por Perfil): O Administrador tem acesso total
e autoriza descartes, enquanto o Operador tem acesso restrito às
movimentações do dia a dia, sem visualizar custos operacionais.

RN-07 (Multiestoque e Transferências): Controle de saldos independentes
por loja ou depósito, permitindo a movimentação rastreável entre
unidades.

RN-08 (Relatórios Gerenciais): Emissão automática de relatórios de
posição de estoque, movimentações, produtos mais e menos vendidos, giro
de estoque, valorização e histórico de descartes.

RN-09 (Segurança e Confiabilidade): Realização de backups automáticos
diários, validações obrigatórias no backend, controle de concorrência
para evitar acessos simultâneos no mesmo produto e histórico imutável de
alterações.

RN-10 (Validade, Produtos Danificados e Diferenças de Estoque):
Aplicação da regra FEFO (vender primeiro o que vence antes), bloqueio
automático de vencidos, registro obrigatorio de produtos danificados
para ajuste de saldo e investigação imediata caso haja diferença maior
que 5% entre a contagem física e o sistema.
