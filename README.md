# Leksehjelp :smile:

![Oppgave a)](/images/oblig2_a_skisse.jpg)

Optimalisering av koden fra euler_pendelum_v1.py
Dette mønsteret gjentar seg, så kan settes i en løkke ...
```python
# Lets do one more step
k = 2

# Values at the next step (k=2)
t2 = t1 + h
theta2 = theta1 + h*slopetheta_array[1]
v2 = v1 + h*slopev_array[1]

# Third point, values put in the lists
t.append(t2)
theta.append(theta2)
v.append(v2)
slopev_array.append(round(-g*theta[2], 2))
slopetheta_array.append(round(v[2]/L, 2))

# Here is all of the values after the second step
print(str(k) + "\t" +
        str(t[2]) + "\t" +
        str(theta[2]) + "\t" +
        str(v[2]) + "\t" +
        str(slopev_array[2]) + "\t" +
        str(slopetheta_array[2])
)
```
