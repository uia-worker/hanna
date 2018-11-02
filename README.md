# Leksehjelp :smile:

## Oppgave a)
![Oppgave a)](/images/oblig2_a_skisse.jpg)

## Oppgave b)
Bruker den generelle løsningen for en annen ordens homogen differensialligning (usikker hvor mye detaljer trenges her, men tok med også noen eksempler)
![Oppgave b) Ark 1](/images/oblig2_b_skisse01.jpg)

Løser her ligningen med initielle betingelser (innebærer derivasjon)
![Oppgave b) Ark 2](/images/oblig2_b_skisse02.jpg)

Kladd, hvis interesse av detaljert fremgangsmåte for derivasjon (usikker hvor mye detaljer er nødvendig)
![Oppgave b) Kladd derivasjon](/images/oblig2_b_skisse03_kladd.jpg)


## Oppgaver c) og d)

I filen [euler_pendelum_v1](oblig2/euler_pendelum_v1.py) er det gjennomgått de to første stegene i Euler's metoden.
Eulers ligninger for (3) (se oppgaveteksten) er:
```
v(k+1)     = v(k) + h * (-g * theta(k))
theta(k+1) = theta(k) + h * (v(k)/L)

hvor k = 0, 1 ,..., N-1
```
I tillegg er det nevnt at dette gjelder for små utslag og at t(k) = h * k.

De generelle ligninger for Eulers metoden (for en første grads ligning) er:
```
x(n+1) = x(n) + h
y(n+1) = y(n) + h * A(n), hvor A(n) = f(x(n), y(n)), dvs. det er stigningsgraden (en. **slope**)
```

I dette tilfelle har man 2 ligninger og stigningsgradene for de er:
* `(-g * theta(k))` for den første og
* `(v(k)/L) for den andre.

I programmet er disse definert som
```python
slopev_array = []
slopetheta_array = []
```

Det er vanlig å bygge en tabell som inneholder en indeks for hvert steg k, og tilsvarende verdier som definerer diskrete punkter i planet, - t(k), theta(k), v(k), slopev(k), slopetheta(k):

k  | t(k)  | theta(k) | v(k)   | slopev(k)| slopetheta(k)
---| ------|----------|--------|----------|--------------
0  | 0     | 1.571	  | 0	     | -15.412  | 0.0
1	 | 0.125 | 1.571	  | -1.927 | -15.412  | -1.927
2	 | 0.25	 | 1.33	    | -3.854 | -13.047  | -3.854
 | | | | |


I filen [euler_pendelum_v2](oblig2/euler_pendelum_v2.py) er en løkke laget og en plot-funksjon implementert.
Python lister er brukt slik at de er definert tomme og verdiene er lagt inn fortløpende med `appends`.
Innebygde funksjon `range` (https://docs.python.org/3/library/stdtypes.html#range) brukes for å itererer over verdiene i Euler ligningene.


Et eksempel på en numerisk løsningsforslag av det lineære systemet (3):
![oblig2 d) numerisk løsning v2](/images/linear_euler_v2.png)

I filen [euler_pendelum_v3](oblig2/euler_pendelum_v3.py)
```python
v, theta = lin_pendel_euler(v0, theta0, g, L, N, h);
```
er implementert.

Koden kan optimaliseres videre, blant annet listen med tidsverdier burde bli tatt ut av funksjonen `lin_pendel_euler`.

Funksjoner brukes på følgende møte:
```python
# Using the Euler's method to approximate a solution of the linearized
# version of differential equations
v, theta = lin_pendel_euler(v0, theta0, g, L, N, h)

# plott resultatene
plot_results(t, theta)
```

Plottet som er resultat av kommandoen `python3 euler_pendelum_v3`

![oblig2 d) numerisk løsning v3](/images/linear_euler_v3.png)
