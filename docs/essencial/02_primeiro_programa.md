---
title: Nosso Primeiro Programa em Python
description: Vamos escrever nosso primeiro programa em Python
---

# Nosso Primeiro Programa em Python

Olá, pessoal!
Aqui iniciamos nossa grande jornada no mundo da programação utilizando a linguagem [Python](https://www.python.org/).
Vamos começar com algo bem básico, mas super empolgante: criar nosso primeiro programa em Python! 🐍

## Criando o Arquivo

Primeiro, crie uma pasta chamada `01_primeiro_programa` e dentro dela, um novo arquivo chamado `01_hello_world.py`.

??? Note
    :man_raising_hand: **Dica de ouro**: todos os arquivos Python devem ter a extensão `.py`.
    Isso é para o que Python saiba que o arquivo contém código para ser executado.


``` shell title="Comandos de terminal"
mkidr 01_primeiro_programa #(1)!
cd 01_primeiro_programa #(2)!
touch 01_hello_world.py #(3)!
```

1.  :woman_raising_hand_tone2: Comando `mkdir`, do inglês **make directory** é usado para criação de pastas.
2.  :woman_raising_hand: Comando `cd`, do inglês **change directory** é usado para movimentação (entrar e sair) de pastas.
3.  :woman_raising_hand: Comando `touch`, do inglês **tocar** é usado para criar arquivos.

## Escrevendo o Código

Beleza, abra o arquivo `01_hello_world.py` e digite o seguinte código:

=== "01_hello_world.py"

    ```python
    print('Seu Nome Aqui')
    ```
=== "Resultado"

    ``` shell
    Seu Nome Aqui #(1)!
    ```

    1. :woman_raising_hand: Resultado esperado durante execução do arquivo.


Bem tranquilo, né? Mas deixa eu explicar rapidinho alguns detalhes importantes:

1. **`print()`**: É a função que usamos para exibir algo na tela.
2. **Parênteses e aspas**: Aqui dentro colocamos o texto que queremos mostrar.
3. **Seu nome**: Troque `'Seu Nome Aqui'` pelo seu próprio nome ou qualquer coisa que você queira exibir!

Por exemplo, no meu caso, ficaria assim:

=== "01_hello_world.py"

    ```python
    print('Gabriel Dornas')
    ```
=== "Resultado"

    ```shell
    Gabriel Dornas #(1)!
    ```

    1. :woman_raising_hand: Resultado esperado durante execução do arquivo.

Isso aí! Você acabou de escrever seu primeiro programa em Python. 🎉

## Executando o Programa

Agora vem a parte divertida: ver o resultado do seu programa no terminal.


=== "Código"

    ```python
    python 01_hello_world.py
    ```
=== "Resultado"

    ```
    Gabriel Dornas
    ```


??? Note

    O terminal é como uma janelinha mágica onde vemos os resultados do que programamos. No caso do nosso exemplo, você verá algo assim:

    ```
    Gabriel Dornas
    ```

    Legal, né? É simples, mas já dá aquele gostinho do que você pode fazer com Python.

    **Ah, e uma dica**: conforme você escreve mais códigos, o terminal pode começar a ocupar muito espaço.
    Sem problema, pois você pode abrir, fechar ou até mesmo redimensiona-lo para o tamanho que quiser.
    Tente descobrir o atalho do seu teclado responsável por abrir e fecha-lo, isso pode te ajudar bastante.
    O meu aqui é ++ctrl+'`'++.

## E Agora?

Pronto, você já deu o primeiro passo no mundo da programação em Python! 🚀
No futuro, você poderá criar programas com interfaces gráficas (o famoso GUI), mas, por enquanto, vamos ficar com o terminal.
É super prático e ótimo para aprender.

Se por acaso você não viu o resultado que mostrei ou encontrou algum erro, não precisa se preocupar!
Use a caixa de comentários abaixo para me contar o que aconteceu.
Não só eu, mas todos que tem acesso a esta aula poderão te ajudar a resolver.

---

Bom, já que falamos da caixa de comentários abaixo, se você não teve nenhum problema, que tal nos contar lá como foi sua primeira experiência com Python? 😃
