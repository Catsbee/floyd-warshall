##############################################################################################
##############################PROGRAMME DE FLOYD-WARSHAL######################################
##################################L3 GR B - EQUIPE 8##########################################
##############################################################################################


#############################INITIALISATION DES STRUCTURE#####################################

##Mise en tableau des information du fichier txt##
def lecture_graphe(nom_graphe):
    file = open(nom_graphe, "r")
    graphe = []
    graphe.append(int(file.readline()[0:-1]))#nombre de sommet
    graphe.append(int(file.readline()[0:-1]))#nombre d'arc
    ligne = ''
    
    #Mise en tableau des valeurs de graphe du texte#
    for i in range (0,graphe[1]):
        ligne = file.readline()[0:-1]
        graphe.append(ligne.split())
        
    file.close()
    return graphe


###Initialise le tableau de distanceen valeur neutre (i) et diagonale (0)##
def init_distance(gr):
    dis = []
    for i in range(0,gr[0]):
        po=[]
        for j in range(0,gr[0]):
            if i == j:
                po.append('0')
            else:
                po.append('i')
        dis.append(po)
    return dis


##Remplis le tableau des distances avec les valeurs du graphe##
def fill_distance(dis, gr):
    for i in range(0,gr[1]):
        dis[int(gr[2+i][0])][int(gr[2+i][1])]= gr[2+i][2]
    return dis


##Initialise le tableau des chemin avec N)##
def init_chemins(gr):
    che = []
    for i in range(0,gr[0]):
        po=[]
        for j in range(0,gr[0]):
            if i == j:
                str(po.append(i))
            else:
                po.append("N")
        che.append(po)
    return che


##Remplis le tableau des chemins par la valeurs du chemins##
def fill_chemin(che, gr):
    for i in range(0,gr[1]):
        che[int(gr[2+i][0])][int(gr[2+i][1])]= gr[2+i][0]
    return che
 

##Matrice d'adjacence##
def matrice_adjacence(che, gr):
    mat = init_chemins(gr)
    for i in range(0, len(che)):
        for j in range(0, len(che)):
            if(che[i][j]!='N'):
                mat[i][j]=1
            else:
                mat[i][j]=0
    return mat


################################FONCTION D'AFFICHAGE##########################################

##Fonction pour afficher les tableau##       
def affichage(tab):
    print("\t", end='')
    for i in range (len(tab)):
        print(i,"\t",end='')
    print("\n")
    i=0
    for row in tab:
        print(i,"\t",end='')
        for element in row:
            print(element, "\t", end='')
        i+=1
        print("\n")
        
        
##AffiChage des matrices chemin et adjacente que l'on retrouve a chaque itération de F-W##
def affichage_floyd(che, gr, dis,nb):
    adj = matrice_adjacence(che, gr)
    print("\n\n-----------------------------------------------\n\nPour l'itération "+str(nb))
    print("\nCeci est la matrice des chemins\n")
    affichage(che)
    print("\nCeci est la matrice des distances\n")
    affichage(dis)
    print("\nCeci est la matrice d'adjacence\n")
    affichage(adj)


##Affichage des matrices de distance et chemin choisit par l'utilisateur##
def affichage_initial(dis, che):
    print("-----------------------------------------------")
    print("\nGraphe choisit\n")
    print("Ceci est la matrice de valeur du graphe que vous avez choisi\n")
    affichage(dis)
    print("\nCeci est la matrice de chemin du graphe que vous avez choisi\n")
    affichage(che)



##Fonction pour afficher les chemin existant
def aff_chemin(che, s, d):
    path = []
    path.append(d)
    if(che[s][d] == 'N'):#On test si le chemin existe ou non
        print("Ce chemin n'existe pas")
    else:
        while int(che[s][d]) != s:
            path.append(int(che[s][d]))
            d = int(che[s][d])
        print(s)
        for i in range(1,len(path)+1):
            print(path[len(path)-i])


##############################Algorihtmes fonctionnels########################################

##Floyd-Warshall##
def floyd_warshall(gr, dis, che):
    #Affichage du graphe de départ
    affichage_initial(dis, che)
    
    #Algorythme de floyd warshall
    for k in range(0,graphe[0]):
        for i in range(0,graphe[0]):
            for j in range(0,graphe[0]):
                if(distance[i][k] !='i' and distance[k][j] !='i'):
                    if(distance[i][j] =='i'):
                        distance[i][j] = str(int(distance[i][k]) + int(distance[k][j]))
                        chemin[i][j] = chemin[k][j]
                    elif(int(distance[i][k]) + int(distance[k][j])) < int(distance[i][j]):
                        distance[i][j] = str(int(distance[i][k]) + int(distance[k][j]))
                        chemin[i][j] = chemin[k][j]
        
        #Affichage des matrice chemin et adjacente pour chaque itération
        affichage_floyd(che, gr, dis,k+1)


##Saisie sécurisé pour les chemin##
def saisie_securise_chemin(che):
    etat = input("Donnez moi un état : \n >")
    while int(etat) < 0 or int(etat) > len(che)-1 :
                print("Votre choix n'est pas valable, veuillez choisir un etat entre 0 et ",+len(che)-1)
                print(" > ")
                etat = input()
    return(etat)


##Test d'un circuit absorbant##
def test_floyd(gr, dis):
    for i in range(0,gr[0]):
        if(int(dis[i][i]) < 0):
            return 0#circuit absorbant
    return 1#circuit okay


##Fonction pour choisir le chemin si pas de circuit absorbant##
def menu_chemin(gr, dis, che):
    print("-----------------------------------------------")
    print("Floyd - Warshall")
    if (test_floyd(gr, dis) == 1):
        rep = True
        #Affichage des chemins
        choix_chemins = 'o'
        while(choix_chemins == 'o'):
            s = saisie_securise_chemin(che)
            d = saisie_securise_chemin(che)
            aff_chemin(che, int(s), int(d))
            choix_chemins = input("Voulez-vous choisir un autre chemin ? o/n >")
    else:
        rep = False
        print("Il y a un circuit absorbant")


##################Main#####################
#choix du graphe
nom = input("Quel est le numéro de l'automate ? Tapez 'quitter' pour sortir du programme : \n >")
while (nom != "n") :

    #test du choix d'un graphe
    while int(nom) < 1 or int(nom) >13 :
        print("Cet automate n'existe pas entrez une valeur entre 1 et 13")
        nom = input()
        
    test = ("L3-B8-graphe"+nom+".txt")
    
    #lecture du graphe
    graphe = lecture_graphe(test)
    
    #mise en structure du graphe
    distance = init_distance(graphe)
    distance = fill_distance(distance, graphe)
    chemin = init_chemins(graphe)
    chemin = fill_chemin(chemin, graphe)
    
    #Floyd-Warshall
    floyd_warshall(graphe, distance, chemin)
    
    #Existance d'un circuit absorbant ?
    menu_chemin(graphe, distance, chemin)

    #boucler ou s'arreter
    print("-----------------------------------------------")
    nom = input("Quel est le numéro de l'automate ? Tapez 'n' pour sortir du programme : \n >")
    
    
print("\nFin de Floyd Warshall, ceci était le projet de théorie des graphe de L3.\nIl vous a été présenté par le groupe B8\n\n\n")