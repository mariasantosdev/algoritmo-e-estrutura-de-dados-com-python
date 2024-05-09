Nesse README deixarei um breve resumo dos capítulos para consultas futuras

## Índice

- [Capítulo 1](#Capítulo-1)

## Capítulo 1
Busca binária:

A busca binária é um algoritmo que recebe como entrada uma lista ordenada de elementos. Se o elemento que você está procurando estiver nessa lista, a busca binária retorna a posição onde ele está localizado. Caso contrário, retorna null.

Com a busca binária, você adivinha o número do meio e sempre elimina metade dos números restantes.

Basicamente, se você tiver um array de 100 itens, a busca binária funciona da seguinte forma:

100 - 50 - 25 - 13 - 7 - 4 - 2 - 1

Seja qual for o número em que você está pensando, você pode adivinhar no máximo sete palpites – porque você elimina muitos números a cada palpite!

Suponha que você esteja procurando uma palavra no dicionário. O dicionário tem 240.000 palavras. Em caso de pior cenário, quantos passos você acha que cada busca levará?

A busca simples poderia levar 240.000 passos se a palavra que você está procurando for a última do livro. Com cada passo da busca binária, você corta o número de palavras pela metade até sobrar apenas uma palavra.

Portanto, a busca binária levará 18 passos – uma grande diferença! Em geral, para qualquer lista de n elementos, a busca binária levará log2 n passos no caso mais extremo, enquanto a busca simples levará n passos.

Para entender exatamente quantos passos você precisa, é basicamente um cálculo de logaritmo.
