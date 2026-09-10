exceçoes e erros

falha na bipagem
(registrar quando um produto não puder ser lido, mensagem para tentar de novo ou cadastro manual)
armazenar data, hora e usuario responsavel pela operaçao

produto com dados inconsistentes
(detectar informaçoes invalidas como:
data de vencimento anterior a data de entrada
quantidade negativa ou igual a zero
valor do produto invalido)

falha na integraçao com o PDV
(registrar erros de comunicaçao entre sistema e o caixa	)

divergencia de estoque
(registrar diferenças entre fisico e registrado e o responsavel pela ultima movimentação do item)

falha de comunicaçao com banco de dados
(registrar tentativas de acesso e indisponibilidades)

tentativas de acesso nao autorizado
(gerar alertas de segurança para os administradores)

perda de conexao durante operaçoes
(salvar temporariamente as informaçoes digitadas pelo usuário e permitir restauração automatica )

auditoria e historico de alteraçoes
(registrar todas as alteraçoes realizadas nos produtos 
inclusao, alteraçao, exclusao, ajustes de estoque...
armazenar usuario, data, hora e motivo da alteraçao)