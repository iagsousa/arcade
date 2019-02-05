#### ![Resultado de imagem para formula de bhaskara](http://alunosonline.uol.com.br/upload/conteudo_legenda/9768480add7616fa1fe2081ce3542378.jpg)

#### Motivação
Não sei se você amava ou odiava o tal do Bhaskara por inventar aquela fórmula das raízes.Agora é hora de implementar aquela conta pra nunca ter mais que fazer na mão.


#### Ação
Dados os valores de A, B e C, calcule as raízes.


#### Entrada e Saída:
Entrada:

- Valores de A, B e C em ponto flutuante, um por linha.

Saída:
- Caso delta seja positivo, a saída deve ser a raiz positiva e raiz negativa, com duas casas decimais.
    - Imprima uma raiz por linha.
- Caso delta seja igual a zero, uma única raiz deve ser considerada, com duas casas decimais.
- Caso delta sela negativo, a saída deve ser "nao ha raiz real"



#### Exemplos

```bash
>>>>>>>> 01 duas raízes
5.4
25.0
-12.0
========
0.44
-5.07
<<<<<<<<

>>>>>>>> 02 duas raízes
3.0
-7.0
4.0
========
1.33
1.00
<<<<<<<<

>>>>>>>> 03 uma raiz
9.0
-12.0
4.0
========
0.67
<<<<<<<<

>>>>>>>> 04 sem raízes
5.0
3.0
5.0
========
nao ha raiz real
<<<<<<<<
```

**Ajuda**

Para calcular a raiz quadrada você deverá importar a biblioteca math em seu projeto e chamar a função sqrt() passando o valor que você deseja encontrar a raiz. Declare uma variável para armazenar o valor de delta, isso tornará o código mais simples.

```c
#include <math.h>
#include <stdio.h>

int main(){
    float value = sqrt(...);
}
```