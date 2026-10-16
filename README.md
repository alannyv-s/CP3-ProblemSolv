# CP3- Simulador de Vendas e Lucro de uma Panificadora

## Explicação do problema
- uma panificadora deseja melhorar o seu planejamento financeiro, com o principal objetivo de descobrir a quantidade de pães produzidos diariamente e qual o retorno lucrativo disso.
- Para isso, precisaremos descobrir o faturamento, os custos e o lucro, e projetar o crescimento das vendas.
- Por isso, desenvolvemos um um programa em Python que simule tudo isso, basta o usuario informar:
  - o preço unitário do pão
  - custo unitário da produção
  - qtd média de pães vendidos diariamente
  - despesas fixas e variáveis
  -qtd dos dias que deseja simular
  - 

## Formulas utilizadas
### Função Polinomial- para o cálculo do lucro
  As funções polinomiais servem para modelar, prever e resolver problemas do dia a dia, da economia e das ciências. Elas transformam relações complexas da vida real em fórmulas matemáticas simples de calcular.

*L(q)=(p-c). q-F*
-L= custo mensal
-q= quantidade vendida
-p= preço unitário do pão
-c= custo de produção
-F= despesas fixas diárias

### Função exponencial- projeção de crescimento de vendas
  A função exponencial serve para modelar situações onde o crescimento ou o decaimento acontece de forma extremamente rápida, proporcional ao valor atual.
*Q(t)= Q0(1 +r)^^t*
- Q= Quantidade projetada de vendas
- Q0= quantidade inicial
- r= taxa mensal de crescimento
- t= numero de meses

## Fontes
https://www.todamateria.com.br/funcao-polinomial/
https://www.todamateria.com.br/funcao-exponencial/