# Ponto de Venda com Descontos

## O que faz?
Recebe compras, aplica descontos e mostra o resumo do dia.

## Menu
- 1: registrar uma compra.
- 2: consultar o resumo e voltar ao menu.
- 0: mostrar o resumo final e encerrar.

## Como funciona
1. Ao escolher 1 no menu, pede o valor da compra. Digite 0 nesse valor para encerrar também.
2. Se o valor for negativo, pede outro valor.
3. Pede a idade. Se for negativa, pede novamente.
4. Para clientes com 65 anos ou mais, aplica 20% de desconto.
5. Se o valor após esse desconto for maior que R$ 100.00, aplica mais 10%.
6. Guarda cada compra na lista com append: primeiro o valor original e depois o final.
7. Soma os valores durante as compras. A opção 2 mostra o resumo sem encerrar; a opção 0 encerra e mostra o resumo final.
8. Uma opção inválida mostra um aviso e retorna ao menu.

## Como executar
Abra o terminal na pasta nivel_1 e digite:

```bash
python pdv.py
```

Digite somente números. Use ponto nos centavos (exemplo: 50.00) e idade inteira.

## Casos de teste do enunciado
| Caso | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

Para testar cada linha, escolha 1 no menu e informe o valor e a idade. Os 10 casos foram testados. Juntos, resultam em total bruto de R$ 2156.00, descontos de R$ 447.10 e total final de R$ 1708.90.

## Resumo do programa
O programa foi feito em Python, usando condições, laços e uma lista. O menu permite registrar compras, consultar o resumo e encerrar. Opções inválidas geram um aviso. Primeiro, aplica o desconto por idade. Depois, verifica se o valor restante permite o desconto extra. Cada compra é guardada com append, e os totais são somados durante a execução. Ao digitar zero, o programa mostra a quantidade de compras, o total bruto, os descontos e o total final. Também verifica valores e idades negativos. A solução não usa funções definidas com def, try/except ou bibliotecas externas.
