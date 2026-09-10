# Integracao de Dispositivo de Bipagem no Sistema de Gestao de Perdas

## Tipos de Leitores de Codigos de Barras

| Tipo | Conexao | Ideal Para |
|------|---------|------------|
| **Lineares (1D)** | USB / Bluetooth | Codigos EAN-13, Code 128, Code 39 |
| **Area (2D)** | USB / Bluetooth / Wi-Fi | QR Code, Data Matrix, notas fiscais |
| **Caneta (Wand)** | Cabo direto | Leitura simples e manual |
| **Bluetooth Movel** | Sem fio | Docas de recebimento e armazem |

## Conexao com o Sistema

### Emulacao de Teclado (HID)
O leitor funciona como um teclado USB. Ao ler o codigo, ele digita os caracteres na tela. E a forma mais simples, nao precisa de driver especial.

### Comunicacao via Serial / USB (COM)
O leitor abre uma porta COM virtual. O sistema le os dados direto da porta, dando mais controle e evitando leituras duplicadas.

### API / SDK do Fabricante
O fabricante oferece bibliotecas proprias para integrar com o software. Permite funcionalidades avancadas como leitura multipla e validacao em tempo real.

## Codigos de Barras Utilizados no Varejo Brasileiro

- **EAN-13** — Padrao mais usado em supermercados. Tem 13 digitos.
- **EAN-8** — Versao menor do EAN-13. Para produtos de embalagem pequena.
- **Code 128** — Aceita letras e numeros. Usado em notas fiscais e etiquetas.
- **GS1-128** — Versao do Code 128 com dados de lote, validade e peso.
- **QR Code** — Codigo bidimensional. Usado em NFe e promocoes.

## O que e o EAN-13?

E o codigo de barras mais comum no varejo. Tem **13 digitos**: os primeiros identificam o pais (789 para o Brasil), os proximos sao o codigo do fabricante e do produto, e o ultimo e um digito de verificacao. Esta presente em praticamente todos os produtos de supermercado.

## O que e a GS1?

E a organizacao global que cria e administra os padroes de codigos de barras no mundo. No Brasil, a **GS1 Brasil** emite os codigos para fabricantes e garante que os codigos funcionem em todo o varejo e logistica.

## O que e o EAN-8?

E a versao compacta do EAN-13. Tem apenas **8 digitos** e e usado em produtos pequenos onde o EAN-13 nao cabe na embalagem, como balas e canetas.

## O que e o Code 128?

E um codigo que aceita **letras e numeros**. E o padrao exigido pela Receita Federal nas notas fiscais eletronicas (NFe). Tambem e usado em etiquetas logisticas e controle de estoque.

## O que e o QR Code?

E um codigo bidimensional (2D) que guarda muita informacao em pouco espaco. Pode conter URLs, textos e dados fiscais. No Brasil, e obrigatorio nas notas fiscais eletronicas e tambem e usado em pagamentos e promocoes.

## Compatibilidade com o Sistema

- **Navegadores** — Funciona via emulacao de teclado no Chrome, Edge e Firefox.
- **Multiplataforma** — Deve rodar em Windows, Android e iOS.
- **Velocidade** — Resposta rapida.
- **Resistencia** — Suporta poeira, quedas e variacao de temperatura.
- **Alcance wireless** — Minimo de 10 metros para operacao sem fio.

## Como Funciona na Pratica?

O bipador se conecta ao computador via **USB ou Bluetooth**. Ele funciona como um teclado — quando le o codigo de barras, envia os caracteres direto para o navegador.

**Fluxo simples:**

1. O operador abre a tela de **recebimento** no navegador.
2. Aponta o bipador para o codigo de barras e apota o gatilho.
3. O codigo e enviado direto para o **backend FastAPI via API REST**.
4. O FastAPI consulta o banco e retorna os dados do produto.
5. O produto aparece na tela para o operador conferir e confirmar.

**Exemplo de rota no FastAPI:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    codigo: str
    nome: str
    quantidade: int
    validade: str
    fornecedor: str

@app.get("/api/produto/{codigo}")
def buscar_produto(codigo: str):
    # consulta no banco de dados
    produto = buscar_no_banco(codigo)
    return produto
```

O frontend faz um `fetch` para `http://localhost:8000/api/produto/7891234567890` e o FastAPI devolve o JSON com os dados do produto.

Nao precisa instalar nada no computador. O navegador ja reconhece o bipador como teclado.

## Boas Praticas

- Usar leitores com certificacao **GS1**.
- Manter o firmware atualizado.
- Testar a leitura periodicamente.
- Configurar o leitor para apertar **Enter** apos a leitura.
- Ter um dispositivo de backup na area de operacao.

---

## Fontes de Informacao

1. **GS1 Brasil** — [https://www.gs1br.org](https://www.gs1br.org)

2. **ABRAS** — [https://www.abras.com.br](https://www.abras.com.br)

3. **IBM Documentation** — [https://www.ibm.com/docs](https://www.ibm.com/docs)

4. **MDN Web Docs** — [https://developer.mozilla.org](https://developer.mozilla.org)

5. **SENAI** — [https://www.senai.br](https://www.senai.br)

6. **Receita Federal** — [https://www.nfe.fazenda.gov.br](https://www.nfe.fazenda.gov.br)
