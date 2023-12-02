import csv
import random


def guardar(nombre,lista) :
 
    
    with open('C:/Users/Ricardo/Desktop/'+nombre+'.csv', 'w',  newline='') as biblio:
            escri=csv.writer(biblio, delimiter=';')
            escri.writerows(lista)
            
def leer(nombre):
   
    a=[]
    with open('C:/Users/Ricardo/Desktop/'+nombre+'.csv', "r") as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            a.append(row)
    return a
def generar_nombre(a,nombres_generados):
    nombres_hombres = ["Juan", "Pedro", "Carlos", "Luis", "Miguel", "José", "Andrés", "Fernando", "Santiago", "Daniel", "Alejandro", "Héctor", "Ricardo", "Javier", "Pablo", "Gabriel", "Raúl", "Emilio", "Gonzalo", "Hugo"]
    nombres_mujeres = ["María", "Ana", "Laura", "Sofía", "Isabella", "Valentina", "Camila", "Lucía", "Daniela", "Paula", "Fernanda", "Carolina", "Gabriela", "Mariana", "Andrea", "Valeria", "Natalia", "Emma", "Victoria", "Luisa"]
    if a=="hombre":
        
        if len(nombres_generados) == len(nombres_hombres):
            return None  
        
        nombre = random.choice(nombres_hombres)  
        
        
        while nombre in nombres_generados:
            nombre = random.choice(nombres_hombres)  
        
         
        
        return nombre
    elif a=="mujer":
        if len(nombres_generados) == len(nombres_mujeres):
            return None  
    
        nombre = random.choice(nombres_mujeres)  
    
    
        while nombre in nombres_generados:
            nombre = random.choice(nombres_mujeres)  
    
        
    
        return nombre
def muchosnombres(a,gen):
    b=[]
    for i in range(0,a):
        c=generar_nombre(gen,b)
        b.append(c)
    return b
def eliminar(b,nombre):
    a=leer(nombre)
    z=[]
    l=0
    k=0
    for i in a:
       
    
        for c in i:
            j=""
            k=0
            for d in c:
                
                if d==";":
                    a[l][k]=j
                    j=""
                    k=k+1
                else:
                    j=j+d
            if k>0:
                a[l][k].append(j)
                
            else :
                a[l]=[j]       
        l=l+1             
    guardar(nobre,a)                  
                
