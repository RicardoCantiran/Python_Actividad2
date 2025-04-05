def imprimir(ronda, n_ronda):
  
    if(n_ronda <5):
        print(f'Ronda numero: {n_ronda}')
    else:
        print(f'Ronda final')
    print(f"{'Jugador':<15} {'Kills':<8} {'Asists':<10} {'Muertes':<9} {'MVPs':<7} {'Puntos':<6}")
    print('-'*65)
    for item in ronda:
        print(f"{item[0]:<15} {item[1]['kills']:<8} {item[1]['assists']:<10} {item[1]['deaths']:<9} {item[1]['mvps']:<7} {item[1]['pts']:<6}")
    print('-'*65)


def ejercicio10(rondas):
    n_ronda = 1
    resul_final = {
        'Shadow': { 'kills': 0 , 'assists': 0, 'deaths': 0, 'pts': 0, 'mvps': 0},
        'Blaze': { 'kills': 0 , 'assists': 0, 'deaths': 0, 'pts': 0, 'mvps': 0},
        'Viper': { 'kills': 0 , 'assists': 0, 'deaths': 0, 'pts': 0, 'mvps': 0},
        'Frost': { 'kills': 0 , 'assists': 0, 'deaths': 0, 'pts': 0, 'mvps': 0},
        'Reaper': { 'kills': 0 , 'assists': 0, 'deaths': 0, 'pts': 0, 'mvps': 0}
    }

    for nRonda in rondas:

      
        n_ronda = n_ronda +1
        puntajes = {}
        for jugador, infoRonda in nRonda.items():
            #Calcular puntos del jugador
            #Actualizar sus datos 
            #Ordenar la tabla antes de imprimir 
            puntos = infoRonda['kills'] * 3 + infoRonda['assists'] - (1 if infoRonda['deaths'] else 0) 
            resul_final[jugador]['pts'] += puntos
            resul_final[jugador]['kills'] += infoRonda['kills']
            resul_final[jugador]['assists'] += infoRonda['assists']
            resul_final[jugador]['deaths'] += 1 if infoRonda['deaths'] else 0
            puntajes [jugador] = {'pts': puntos,'kills': infoRonda['kills'], 'assists': infoRonda['assists'], 'deaths' : infoRonda['deaths'],'mvps': 'no'} 
            
        ordenados = sorted(puntajes.items(), key = lambda x : x [1]['pts'], reverse=True )
        resul_final[ordenados[0][0]]['mvps'] += 1
        ordenados[0][1]['mvps'] = 'si'
        imprimir(ordenados,n_ronda)
    imprimir(sorted(resul_final.items(), key = lambda x : x [1]['pts'], reverse=True), n_ronda)
    
 










