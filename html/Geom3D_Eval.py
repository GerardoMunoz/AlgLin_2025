#Todo:
    #* funciones para calificar panos y tectas y llamarlas
    #* completar el elnsolucionario y actualizar los valores para calificar


import json
rtas_ctas={
  'puntos_xyz':{
       '0d_l1_xy':[2,1,0],
       '0d_l1_yz':[0,1,-2],
       '0d_l1_l2':[1,1,--1]
  },

  'planos_abcd':{
      '2d_l1_l2':[0,0,1,0]
  },

  'rectas_abc;defgh':{
      '1d_l1':[[0,1,0,1],[1,0,-1,2]],
      '1d_l2':[[1,-1,1,-1],[1,0,-1,2]]
  }
}



notas={}


def punto_en_plano(P: list, plano_data: dict, tolerancia=1e-9) -> bool:
    """Revisa si un punto P=[x,y,z] está en un plano definido por un diccionario de datos."""
    x_p, y_p, z_p = P
    a = plano_data.get('a', 0)
    b = plano_data.get('b', 0)
    c = plano_data.get('c', 0)
    d = plano_data.get('d', 0)
    resultado = a * x_p + b * y_p + c * z_p - d
    return 1 if abs(resultado) < tolerancia else 0


def punto_igual(xyz,est):
   # print(xyz,[est['x'],est['y'],est['z']])
    if xyz==[est['x'],est['y'],est['z']]:
        return 1
    else:
        return 0

def plano_igual(abcd,est):
   # print(xyz,[est['x'],est['y'],est['z']])
    if est['b']*abcd[0]==abcd[1]*est['a'] and est['d']*abcd[2]==est['c']*abcd[3]:
        return 1
    else:
        return 0

        

def recta_2puntos(abcd,est):
    nota=0
    abcd[0]*est



with open("answ_all.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    #print(file.read())
    
    for code,vals in data.items():
       if code not in notas:
           notas[code]={}
       for datos in vals:
           print(code,len(datos['rta']))
           #print(datos)
           for fig in datos['rta']:
               #print(fig)
                    if fig['tipo']=='Punto':
                       pest=fig['data']['pos']
                       for nombre, coord in rtas_ctas[ 'puntos_xyz'].items():
                         nota=punto_igual(coord,pest)
                         if nombre not in notas[code]:
                             notas[code][nombre]=[]
                         notas[code][nombre].append(nota)
                    elif fig['tipo']=='Plano':
                       pest=fig['data']
                       for nombre, coord in rtas_ctas[ 'planos_abcd'].items():
                         nota=plano_igual(coord,pest)
                         if nombre not in notas[code]:
                             notas[code][nombre]=[]
                         notas[code][nombre].append(nota)
                    # elif fig['tipo']=='Linea':
                    #    pest=fig['data']['pos']
                    #    for nombre, coord in rtas_ctas[ 'puntos_xyz'].items():
                    #      nota=punto_igual(coord,pest)
                    #      if nombre not in notas[code]:
                    #          notas[code][nombre]=[]
                    #      notas[code][nombre].append(nota)
           
print(notas)
