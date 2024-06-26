Nesse README deixarei um breve resumo dos capítulos para consultas futuras. Além dos exercícios propostos em cada capítulo

## Índice

- [Capítulo 1](#Capítulo-1)
- [Capítulo 2](#Capítulo-2)

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
  Since the phone directory is organized alphabetically, employing a binary search algorithm becomes feasible, resulting in a time complexity of O(log₂(n)).

  1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)
  In this case, a simple search is sufficient because we need to look at all individuals O(n)

  1.5 You want to read the numbers of every person in the phone book.
  In this case, a simple search is sufficient because we need to look at all individuals O(n)

  1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)
  Even though you only need to read 1/20 of the names in the phone book, the growth rate of the number of operations is still linear. This means that even though you're reading only a fraction     of the names, the relationship between the number of names read and the time taken remains proportional. In simpler terms, for every name you read, one operation is performed. Thus, whether      it's f(x)=x20f(x)=20x​ or f(x)=xf(x)=x, the number of operations increases linearly with the number of names read. Consequently, the time complexity for this search remains O(n).


## Capítulo 2

#### Arrays e listas encadeadas

Arrays armazenam elementos de forma contígua na memória, permitindo acesso aleatório eficiente, enquanto as listas encadeadas conectam os elementos através de ponteiros, facilitando inserções e remoções.

Os arrays são eficientes para operações de leitura, oferecendo acesso direto aos elementos por índice. No entanto, eles enfrentam desafios em inserções, especialmente no meio da estrutura, onde pode ser necessário realocar elementos e mover dados, resultando em complexidade e lentidão em casos de grande volume de dados.

Por outro lado, as listas encadeadas são mais eficientes em operações de inserção e remoção, principalmente no meio da lista, pois exigem apenas ajustes nos ponteiros, sem a necessidade de mover grandes conjuntos de dados. No entanto, seu acesso aos elementos é sequencial, o que pode ser menos eficiente em cenários que exigem acesso aleatório.

Em resumo, a escolha entre arrays e listas encadeadas depende das necessidades específicas da aplicação, incluindo o tipo de operações realizadas e as restrições de memória. Arrays são adequados para acesso aleatório e operações de leitura eficientes(dependendo de onde ocorrem), enquanto listas encadeadas são mais vantajosas em cenários com inserções e remoções frequentes(ou quando é necessário a leitura em sequencia)

#### Selection Sort

Passo inicial: Considere o array inteiro como a sublista não ordenada.

Encontrar o menor elemento: Encontre o menor elemento na sublista não ordenada.

Troca de posição: Troque esse menor elemento com o primeiro elemento da sublista não ordenada.

Mover limites: Mova o limite entre a sublista ordenada e a não ordenada uma posição à direita.

Repetir: Repita os passos 2 a 4 até que toda a sublista não ordenada esteja vazia.

Vamos considerar o array [29, 10, 14, 37, 13] e ordená-lo em ordem crescente:

    Array inicial: [29, 10, 14, 37, 13]
    Encontrar o menor elemento na sublista não ordenada [29, 10, 14, 37, 13] é 10. Trocar 10 com 29: [10, 29, 14, 37, 13]
    Encontrar o menor elemento na sublista não ordenada [29, 14, 37, 13] é 13. Trocar 13 com 29: [10, 13, 14, 37, 29]
    Encontrar o menor elemento na sublista não ordenada [14, 37, 29] é 14. Trocar 14 com 14 (nenhuma mudança necessária): [10, 13, 14, 37, 29]
    Encontrar o menor elemento na sublista não ordenada [37, 29] é 29. Trocar 29 com 37: [10, 13, 14, 29, 37]

O array agora está ordenado: [10, 13, 14, 29, 37].

A complexidade de tempo do Selection Sort é O(n2)O(n2), onde nn é o número de elementos no array. Isso ocorre porque, em cada iteração, o algoritmo percorre a sublista não ordenada para encontrar o menor elemento, e o número de elementos a serem verificados diminui linearmente com cada iteração.

Exercícios:

 2.2 Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders off the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it.
 Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)

For this scenario, a linked list would likely be the better choice to implement the order queue.

Here's why:

  Insertions and Deletions: Linked lists excel at insertions and deletions, particularly at the beginning or end of the list. In this case, servers are adding orders to the back of the queue and chefs are taking orders off the front of the queue. Both of these operations involve adding/removing elements at the ends of the list, which is efficient with a linked list.
  
  Dynamic Size: Linked lists can grow or shrink dynamically, which is useful in this scenario where the number of orders can vary. Arrays, on the other hand, have a fixed size (in most programming languages), so if the array fills up, you'd need to allocate a new, larger array and copy elements over, which can be inefficient.
  
  No Random Access Needed: The nature of this scenario doesn't require random access to elements in the list. Servers add orders sequentially to the end of the queue, and chefs take orders sequentially from the front. Arrays are better suited for scenarios where you need to access elements randomly by index, which isn't the case here.

Therefore, a linked list is a more suitable choice for implementing the order queue in this scenario.


  2.3 Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list?
  
  Given that binary search requires random access to elements, implementing the list of usernames as an array would be more suitable than using a linked list.

Here's why:
   Random Access: Arrays provide constant-time access to elements by index, which is essential for binary search. This allows for instant access to the middle element of the array, which is crucial for the efficiency of binary search.

   Efficient Searching: Binary search relies on dividing the search space in half with each iteration. This is most effectively done with arrays, where accessing the middle element can be done in constant time. In contrast, linked lists would require traversing from the beginning of the list to reach the middle element, which would not be as efficient.

   Memory Efficiency: Arrays typically use contiguous memory allocation, which can lead to better memory locality and cache efficiency compared to linked lists. This can result in faster search times, especially for large datasets.
Therefore, for the scenario described, implementing the list of usernames as an array would be the better choice, as it provides efficient random access required for binary search.


  2.4 People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?
  Insertion Time Complexity: In an array, inserting an element at a specific position (other than the end) requires shifting all the subsequent elements to make room for the new element. This operation has a time complexity of O(n), where n is the number of elements in the array. When adding new users frequently, this shifting process becomes inefficient, especially as the array grows larger.

  Memory Reallocation: As the array fills up with new users, it may reach its capacity. When this happens, the array needs to be resized to accommodate more elements. Resizing typically involves allocating a new, larger array, and copying all existing elements into it. This operation can be costly, especially if it needs to be done frequently.

  Disruption of Sorted Order: If the array is sorted to facilitate binary search, inserting a new user requires maintaining the sorted order of the array. This often involves finding the correct position for the new user, which can be time-consuming, especially in large arrays. Additionally, after insertion, the array may need to be re-sorted to maintain the order, which adds further overhead.

  Impact on Binary Search Efficiency: Binary search assumes that the array is sorted. If frequent insertions disrupt the sorted order of the array, it may require resorting or additional overhead to ensure the array remains sorted. This can impact the efficiency of binary search operations, as the search algorithm relies on the sorted nature of the array to work effectively.

  Overall, while using an array for storing users allows for efficient random access, frequent insertions can lead to performance issues, especially when combined with binary search operations. In scenarios where frequent inserts are expected, a data structure that supports efficient insertions, such as a balanced binary search tree or a dynamic array, may be more suitable.

  2.5 In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with A. The second slot points to a linked list containing all the usernames starting with B, and so on.
  
  Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the linked list for slot 1, and add Adit B at the end. Now, suppose you want to search for Zakhir H. You go to slot 26, which points to a linked list of all the Z names. Then you search through that list to find Zakhir H. Compare this hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You don’t have to give big O run times, just whether the data structure would be faster or slower.
  This hybrid data structure offers advantages over both arrays and linked lists in certain scenarios:

Insertion:
        Faster than arrays: Inserting into the linked list associated with the appropriate slot is faster than shifting elements in an array when inserting in the middle.
        Slower than linked lists: While insertion at the end of a linked list is fast, finding the correct slot in the array requires additional computation compared to simply appending to the end of a linked list.

Searching:
        Faster than arrays: Searching within the linked list associated with the appropriate slot is generally faster than searching through an unsorted array.
        Comparable to linked lists: Once you reach the correct slot in the array, searching within the linked list for a specific element is comparable to searching in a regular linked list. However, if the linked lists within each slot are long, searching could potentially take longer than in a single, well-balanced linked list.

Overall, this hybrid data structure is generally faster than arrays for both insertion and searching, and comparable to linked lists for searching, depending on the distribution of elements among the slots and the lengths of the linked lists.
 


