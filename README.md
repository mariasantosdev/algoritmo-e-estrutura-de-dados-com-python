Nesse README deixarei um breve resumo dos capítulos para consultas futuras. Além dos exercícios escritos propostos em cada capítulo

## Índice

- [Capítulo 1](#Capítulo-1)

## Capítulo 1
### Busca binária:

A busca binária é um algoritmo que recebe como entrada uma lista ordenada de elementos. Se o elemento que você está procurando estiver nessa lista, a busca binária retorna a posição onde ele está localizado. Caso contrário, retorna null.

Com a busca binária, você adivinha o número do meio e sempre elimina metade dos números restantes.

Basicamente, se você tiver um array de 100 itens, a busca binária funciona da seguinte forma:

100 - 50 - 25 - 13 - 7 - 4 - 2 - 1

Seja qual for o número em que você está pensando, você pode adivinhar no máximo sete palpites – porque você elimina muitos números a cada palpite!

Suponha que você esteja procurando uma palavra no dicionário. O dicionário tem 240.000 palavras. Em caso de pior cenário, quantos passos você acha que cada busca levará?

A busca simples poderia levar 240.000 passos se a palavra que você está procurando for a última do livro. Com cada passo da busca binária, você corta o número de palavras pela metade até sobrar apenas uma palavra.

Portanto, a busca binária levará 18 passos – uma grande diferença! Em geral, para qualquer lista de n elementos, a busca binária levará log2 n passos no caso mais extremo, enquanto a busca simples levará n passos.

Para entender exatamente quantos passos você precisa, é basicamente um cálculo de logaritmo.


### big O notation:
    O(log n), também conhecido como tempo de log. Exemplo: pesquisa binária.

    O(n), também conhecido como tempo linear. Exemplo: pesquisa simples.

    O (n * log n). Exemplo: um algoritmo de classificação rápida, como quicksort

    O(n2). Exemplo: um algoritmo de ordenação lento

* A velocidade do algoritmo não é medida em segundos, mas sim no crescimento do número de operações.
* Em vez de segundos, falamos sobre a rapidez com que o tempo de execução de um algoritmo aumenta à medida que o tamanho da entrada aumenta.
* O tempo de execução dos algoritmos é expresso em notação `Big O`.
* O(log n) é mais rápido que O(n) e fica muito mais rápido à medida que a lista de itens que você está pesquisando aumenta.

Exercícios:

  1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?
  log2 128 = 7

  
  1.2 Suppose you double the size of the list. What’s the maximum number of steps now?
  log2 256 = 8.

  Give the run time for each of these scenarios in terms of big O.

  
  1.3 You have a name, and you want to find the person’s phone number in the phone book.

  1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

  1.5 You want to read the numbers of every person in the phone book.

  1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)



