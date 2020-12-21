import os
import sys
sys.path.append('../../')
from app.wsgi import *
from core.erp.models import Type, Employee

# Listar

#query = Type.objects.all()
#print(query)

#Insercion

#t = Type()
#t.name = 'Hola'
#t.save()

#Edicion
#try:
 #t = Type.objects.get(id=2)
 #print(t.name)
 #t.delete()
#except Exception as e :
    #print(e)
#Eliminacion
#t.delete()
#Filtro
#obj = Type.objects.filter(name__icontains='pre') #Contengan la palabra Pre
#obj = Type.objects.filter(name__istartswith='p') #---->Comiencen con la letra p
#obj = Type.objects.filter(name__iendswith='a') # ----> Terminen con la letra
#obj = Type.objects.filter(name__in=['Hola', 'Viba']).count() # ---->Mostrar valores exactos y count contar los valores
Employee.objects.filter(type_id=1)
for i in  Type.objects.filter(name__iendswith='a'):
    print(i.name)
