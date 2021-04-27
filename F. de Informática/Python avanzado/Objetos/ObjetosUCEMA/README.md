# Paradigmas de programación

# Introducción a la programación con objetos

## Objetos y mensajes

Somos ornitólogos y ornitólogas que estudiamos el comportamiento de las aves, y Pepita es una golondrina.

```python
from aves import pepita
```

¿Qué sabe hacer pepita? ¿Sabe volar_en_circulos?

```
pepita.volar_en_circulos()
```

¿Sabe cantar_boleros?

```
pepita.cantar_boleros()
# AttributeError: 'Golondrina' object has no attribute 'cantar_boleros'
```

Ups, no :stuck_out_tongue:. ¿Y sabe comer_alpiste?

```
pepita.comer_alpiste()
# TypeError: comer_alpiste() missing 1 required positional argument: 'gramos'
```

Ups, sí, pero tenemos que decirle cuantos gramos de alpiste queremos que coma

```
pepita.comer_alpiste(10)
```

> :light_bulb: Formalización: `pepita` es un objeto, y como todo **objeto**, entiende algunos **mensajes**.
> En particular, nuestra golondrina entiende los mensajes `comer_alpiste` y `volar_en_circulos`,
> pero no entiende `cantar_boleros` (ni casi ninguna otra cosa que se te ocurra :wink:)
> En otras palabras, `pepita` _sabe_ comer alpiste y volar en circulos.
>
> Por otro lado, si le pedimos a un objeto que haga cosas que no sabe hacer, éste se rehusará.

¿Y qué pasa cuando le _enviamos_ estos mensajes? `pepita` no tiene infinita energía para hacer todo lo que le pidamos, sino que sabe cuanta es la `energia` que le queda:

```python
pepita.energia
```

> :dart: Sabiendo esto, ¿te animás a averiguar cómo queda la energia después de hacerla comer alpiste? ¿y después de hacerla volar en círculos?

Como vemos, cada vez que hacemos que pepita coma y vuele, su energia cambia.

> :light_bulb: Formalización: los objetos pueden tener **estado** (en el caso de pepita, su estado es la energía), el cual puede cambiar a lo largo del tiempo.

> :dart: ¿Te animás a averiguar según qué formula?

> :light_bulb: Formalización: cada vez que un objeto recibe un mensaje, _hace_ algo, reaccionando al mismo. Por tanto, decimos que los objetos tienen un cierto _comportamiento_ (por ejemplo, cuando pepita come alpiste, su energia sube en tantas unidades como los gramos ingeridos)

## Ambiente e interfaces

`pepita` no es nuestra única golodrina. También contamos con `anastasia`. ¿Tendrá su misma energia?

```
anastasia.energia
pepita.energia
```

`anastasia` es otro objeto, y como tal, cuenta con su propio estado. Por eso es que si bien las dos tienen `energia`, presentan valores diferentes. ¿Qué cosas sabrá hacer `anastasia`?



```python
anastasia.volar_en_circulos()
anastasia.comer_alpiste(10)
```

Como `anastasia` es otra golondrina, sabe hacer las mismas cosas que `pepita`.

> :light_bulb: Formalización: llamaremos _ambiente_ al contexto en el que el viven los objetos, tienen su estado y pueden entender mensajes. En un mismo ambiente podemos contar con varios objetos, como por ejemplo, pepita y anastasia. En otras palabras es el mundo que los objetos habitan y en que se relacionan. Cada vez que apretamos play en replit, o le damos reset en colab, o cerramos nuestro intérprete de python en nuestra computadora y lo volvemos a iniciar, estamos destruyendo ese mundo y volviendo a empezar.

Pero no sólo contamos con `pepita` y `anastasia`, sino también con `roberta`. ¿Cuánta energía tendrá inicialmente?

```python
roberta.energia
```

:open_mouth: Ohh, ¡tiene mucha energia! Y también sabrá volar en círculos, ¿no?

```python
roberta.volar_en_circulos()
roberta.energia
```

Bien, aunque como vemos perdió sólo una unidad de energía, pese a que anastasia y pepita gastan 10 al hacerlo.
Parece que las tres saben hacer lo mismo, pero roberta lo hace de forma _diferente_.

> :light_bulb: Formalización: no todos los objetos tienen que reaccionar de igual forma a los mismos mensajes. En otras palabras, no todos los objetos tienen por qué comportarse igual.

¿Y qué hay sobre `comer_alpiste`?

```python
roberta.comer_alpiste(10)
```

Ey, ¡no le gusta el alpiste! Pero nos dijeron que sí le gusta comer peces:

```python
roberta.comer_peces(2)
roberta.energia
```

> :light_bulb: Formalización: no todos los objetos tienen qué entender los mismos mensajes. Por ejemplo `roberta` no entiende `comer_alpiste`, pero sí entiende `comer_peces` (que anastasia y pepita no entienden, si no nos creés podés comprobarlo vos :smile:). Al conjunto de mensajes que cada objeto expone lo llamaremos **interfaz**, la cual puede ser (y típicamente será) diferente para cada objeto.

Qué rara es nuestra nueva golondrina, ¿no? ¡Es que no es una Golondrina! ¡Es un dragón! :fire:

```python
roberta.escupir_fuego()
```

Perdón, esperamos no haber quemado nada :see_no_evil:


## Clases y polimorfismo

Momento, ¿y cómo están definidas `pepita`, `anastasia`  y `roberta`? ¿Dónde dice _qué_ saber hacer cada una y _cómo_?

En el paradigma de objetos, los mismos se crean a partir de _moldes_ llamados **clases**, que sirven para dar vida a objetos que se comporten de igual forma. Por ejemplo nuestras golondrinas `pepita` y `anastasia` se crearán de la siguiente forma....

```
pepita = Golondrina(100)
anastasia = Golondrina(200)
```

... partir de una clase llamada `Golondrina` que se verá así:


```python
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
```


> :light_bulb: Formalización: al acto de crear un objeto a partir de una clase se lo denomina _instanciación_, y por tanto a los objetos también se los denomina _instancias_ (de una clase particular). Por ejemplo, `pepita`  es una instancia (de la clase `Golondrina`).
>
> Si bien el término _instancia_ quizás no nos diga mucho, en este contexto significa "ejemplo", dado que cada golondrina como pepita o anastasia son ejemplo concretos (es decir, casos particulares) de la idea más general de una Golondrina.

Como vemos, una clase es nuevo tipo de definición, que se suma a las funciones y procedimientos que ya conocíamos. Se escribe mediante la palabra reservada `class`, seguida de un nombre y `:`. Dentro de ella encontraremos los métodos, que son el código que especifica cómo se comportará un objeto cuando reciba un mensaje.

> :memo: Nota: sí, los métodos se definen usando la misma palabra clave `def` que usabamos para funciones y procedimientos. Sin embargo, no son lo mismo: como podemos ver los métodos siempre están "dentro" de una clase, y además tienen como primer parámetro `self`. Más sobre esto, en breve.

## Un poco de práctica

Ahora les toca a ustedes: 

* Hacer `esta_debil`: si tienen menos de 10 puntos de energia (golondrinas) o 50 (dragones)
* Hacer `esta_feliz`: si tiene más de 500 puntos de eneria (sin importar cuál)
* Hace a `hipo`, entrenador de dragones: sabe aceptar a dragones y luego hacerlos entrenar, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
















