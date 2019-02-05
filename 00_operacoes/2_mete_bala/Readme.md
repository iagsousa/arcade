
![sniperdog](https://user-images.githubusercontent.com/4747652/52280317-691f1f00-293a-11e9-93d0-c8861b282a11.jpg)

### Motivação

Um atirador de elite estava atirando a 400 metros de distância em em um papel milimetrado.
Para calcular a imprecisão da arma, ele dava dois tiros e media a distância entre eles.
Como ele não tinha régua, ele pegou os pontos no plano cartesiano e a fórmula
da distância entre os pontos para poder calcular a distância.

### Ação

Dada a fórmula da distância entre dois pontos e os valores x e y de cada ponto,
imprima a distância entre os pontos com duas casas decimais.

### Entrada e Saída:

Entrada:

* Coordenada X e coordenada Y do primeiro ponto.
* Coordenada X e coordenada Y do segundo ponto.

Saída:

* A distância entre os pontos com duas casas decimais.


### Exemplos

```
>>>>>>>>
3
7
1
4
========
3.61
<<<<<<<<

>>>>>>>>
1
8.2
-4
12
========
6.28
<<<<<<<<

>>>>>>>>
3
1
3
5
========
4.00
<<<<<<<<

```

### Ajuda

Fórmula da distância entre dois pontos:
![equação que calcula a distância entre dois pontos](http://s5.static.brasilescola.uol.com.br/img/2016/10/formula-da-distancia-entre-dois-pontos.jpg)
Lembre-se que distância é uma grandeza sempre positiva.

Como imprimir duas casas decimais em Python e C:

```py
# imprimindo com duas casas decimais em python 3
print ("%.2f" % valor)
```
```c
// imprimindo com duas casas decimais em c 
printf("%.2f", valor);
```


Para calcular a raiz quadrada você deverá importar a biblioteca math.h em seu projeto e chamar a função sqrt() passando o valor que você deseja encontrar a raiz.

Para elevar ao quadrado você pode usar a função pow(x,2) que retorna x², ou fazer x * x. A função pow() também pertence à math.h.