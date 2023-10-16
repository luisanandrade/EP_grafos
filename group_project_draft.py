def sim(Tritmo, Tlimiar, Tfiltro, Tfinal, Tgrafo): #as tres variaveis de tempo, o tempo final, e o grafo a ser utilisado
    ct = 0
    A = #Coeficiente de adaptação
    I = #criar uma data de nascensa para cada grafo, e suptrai-la ao ct
    gen = 0
    T = 100 # populacao atual 
    K = T #populacao inicial
    p = new()
    c = cap.new()

    for x in range(T):
        p = popu.addI(p,ind.new(col.new(Tgrafo,w),ct,n))
        n += 1

    for x in p: #inicializa os eventos de avaliação para toda a população
        c = cap.add(event.event(avaliação,ind.ident(x),ct + random(Tlimiar)),c)



    for x in p: #inicializa os eventos de evolução para toda a população
        c = cap.add(event.event(evolução,ind.ident(x),ct + random(Tritmo)),c)



    #inicializa o evento de filtragem para toda a população
    c = cap.add(event.event(seleção, p ,ct + random(Tfiltro)),c) 



    



    while Tfinal >= cT:

        if event.evento(event.next(listaeventos)) == avaliação:

            A = grafo.avaliação(event.object(evento)) #coeficiente de avaliação do grafo do evento
            I = grafo.idade(event.object(evento), cT) #coeficiente de avaliação do grafo do evento


            if random() <= (1-(2/pi)(1+A)**(1+8(1+I)))




            excedule(avaliação, cT + random(Tlimiar))



        elif event.evento(event.next(listaeventos)) == evolução:


            if random() <= (1/(1+e**((K-T)/10)): #mutação
                grafo.---(grafo atual cor diferente)
                if grafo.avaliação(novo) > grafo.avaliação(antigo): #substitui o antigo pelo novo com cor diferente (mutado), se for melhor
                    grafo.delete(antigo)
                    grafo.add(novo) 
                else: #elemina o mutado se ele for pior e mantem o antigo
                    grafo.delete(novo)





                
            else:   #reprodução
                



                
                grafo.---(grafo atual cor diferente, idade 0)
                T += 1

             excedule(evolução, cT + random(Tritmo))  



        else: #seleçaõ
            while grafo.avaliação(grafo.worse(listagrafos)) < 1: #deleta os invalidos
                grafo.delete(grafo.worst(listagrafos))
                T -= 1
            while T > K * (3/2): #deleta os validos até a populacão for de tamanho adequada
                grafo.delete(grafo.worst(listagrafos))
                T -= 1

            excedule(seleção, cT + random(Tfiltro))
        event.delete(event.next(listaeventos))  
        ct = event.date(event.next(listaeventos))
    