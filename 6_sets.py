#Sets: Es un conjuneto, es decir una coleccion de elementos unicos y desordenados

my_sets=set()
my_other_set={}

print(type(my_sets))
print(type(my_other_set))

var1={"Hola", "Jose", 34}
print(type(var1))

var1.add("Que tal")
print(var1)

#Añadir
var1.add("Hola")
print(var1)

#Eliminar
var1.remove("Hola")
print(var1)

#Busqueda de elemento en el set(Conjunto)

print("Jose" in var1)

#Transformacion de set a lista

var3=list(var1)
print(var3)

#Union
my_other_set={"Kotlin","Swift","Python"}
my_other_languages={"php","Css"}

var_unio=my_other_set.union(my_other_languages).union({"JavaScript", "C#","C++"})

print(var_unio)

#Diferencia

my__other_set_languages={"JavaScript", "C#"}

print(var_unio.difference(my__other_set_languages))