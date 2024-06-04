### Gerenciamento de Memória como uma Biblioteca

Imagine que a memória do seu computador é como uma biblioteca, mas com espaço limitado nas estantes (a RAM). Os livros representam os dados e programas que você está usando.

Quando você precisa de um livro (dados ou programa) que não está na estante, você pede ao bibliotecário (sistema operacional) para buscá-lo do depósito (o armazenamento secundário, como o disco rígido). Esse processo de trazer o livro para a estante se chama PG-IN.

Se a estante já está cheia e você quer colocar um novo livro lá, o bibliotecário precisa tirar um livro menos usado da estante e guardá-lo no depósito. Esse processo de mover o livro da estante para o depósito se chama PG-OUT.

Além disso, as cores dos livros que estão na estante representam os processos do programa que está sendo executado. O vermelho indica o programa que está consumindo mais memória, enquanto o verde indica o programa que está consumindo menos memória. Essas cores são atualizadas conforme a última execução do programa (livro). Se o usuário precisa de um livro que está no depósito, o programa menos usado será removido pelo bibliotecário.

Dessa forma, a biblioteca pode sempre ter os livros mais relevantes e usados à mão, mesmo que o espaço nas estantes seja limitado.

Na simulação visual fornecida pelo código, você pode observar o funcionamento desse processo, com a estante representando a memória RAM, o depósito representando o armazenamento secundário, o Bibliotecário representando o sistema operacional e os Alunos representando o usuário.
