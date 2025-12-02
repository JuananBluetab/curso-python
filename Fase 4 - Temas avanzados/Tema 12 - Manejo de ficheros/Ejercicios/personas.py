personas = []
campos = ['id','nombre','apellido','nacimiento']
with open('personas.txt','r', encoding = 'utf8') as txtfile:
    for i, linea in enumerate(txtfile):
        personas.append({})
        if linea.endswith("\n"):
            linea_corregida = linea[:-1]
        else:
            linea_corregida = linea
        for j, campo in enumerate(linea_corregida.split(";")):
            personas[i][campos[j]]=campo
        print(personas[i])