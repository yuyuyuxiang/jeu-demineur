import random
import time

def afficher(T):
	for i in range(n):
		for j in range(m):
			print(T[i][j], end=" ")
		print("\n", end="")
	print("\n", end="")

def int_jeu(n,m,difficulte):
	T = []
	for i in range(n):
		T.append([])
		for j in range(m):
			T[i].append(0)
	p = n*m
	if difficulte == 1:
		p = p*20//100
	elif difficulte == 2:
		p = p*40//100
	elif difficulte == 3:
		p = p*60//100
	for k in range(p):
		i1 = random.randint(0, n-1)
		j1 = random.randint(0, m-1)
		T[i1][j1] = 2
	return T

def quantite_de_mines(T,n,m):
	b = 0
	for i in range (n):
		for j in range (m):
			if T[i][j] == 2:
				b += 1
	return b

def nb_mine(i,j,T):
	Dx = [-1, -1, -1, 0, 0, 1, 1, 1]
	Dy = [-1, 0, 1, -1, 1, -1, 0, 1]
	mi = 0
	for a in range(8):
		x = i + Dx[a]
		y = j + Dy[a]
		if (0 <= x) and (x <= n-1) and (0 <= y) and (y <= m-1):
			if T[x][y] == 2: mi += 1
	return mi

def mines_autour(n,m,T):
	M = []
	for i in range(n):
		M.append([])
		for j in range(m):
			mi = nb_mine(i,j,T)
			M[i].append(mi)
	return M

def poser_drapeau(T,i,j):
	if T[i][j] == 0:
		T[i][j] = 3
	elif T[i][j] == 2:
		T[i][j] = 4
	return T[i][j]

def lever_drapeau(T,i,j):
	if T[i][j] == 3:
		T[i][j] = 0
	elif T[i][j] == 4:
		T[i][j] = 2
	return T[i][j]

def existence(i,j,n,m):
	if (0 <= i) and (i <= n-1) and (0 <= j) and (j <= m-1):
		return True
	else:
		return False

def pouvoir_creuser(T,i,j):
	ex = existence(i,j,n,m)
	if (ex == True) and ((T[i][j] == 0) or (T[i][j] == 2)):
		return True
	else:
		return False

"""
#fonction creuser sans recursivite
def creuser(T,M,i,j,N):
	if pouvoir_creuser(T,i,j) == True:
		if T[i][j] == 0:
			T[i][j] = 1
			return (True, M[i][j], N + 1)
		else:
			return (False, M[i][j], N + 1)
	else:
		return (False, M[i][j], N)
"""

def creuser_recu(T,M,i,j):
	if pouvoir_creuser(T,i,j) == True:
		if T[i][j] == 0:
			T[i][j] = 1
			c = True
		else:
			c = False
	else:
		c = False
	if (0 <= i) and (i <= n-1) and (0 <= j) and (j <= m-1) and (c == True) and (M[i][j] == 0):
		Dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		Dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for a in range(8):
			x = i + Dx[a]
			y = j + Dy[a]
			if (0 <= x) and (x <= n-1) and (0 <= y) and (y <= m-1):
				creuser_recu(T,M,x,y)
	return (c, M[i][j])

def cases_decouvertes(L,n,m):
	N = 0
	for i in range(n):
		for j in range(m):
			if (L[i][j] != "d") and (L[i][j] != "*") and (L[i][j] != "?"):
				N += 1
	return N

def plateau_de_jeu(n,m,T,M):
	L = []
	for i in range(n):
		L.append([])
		for j in range(m):
			L[i].append("-")
	for i in range(n):
		for j in range(m):
			if (T[i][j] == 3) or (T[i][j] == 4):
				L[i][j] = "d"
			elif (T[i][j] == 0) or (T[i][j] == 2):
				L[i][j] = "?"
			elif T[i][j] == 1:
				L[i][j] = M[i][j]
	return L

def exemplaire(n,m):
	Z = []
	a = 0
	b = 0
	for i in range(n):
		Z.append([])
		for j in range(m):
			Z[i].append("?")
	for i in range(1,n):
		Z[i][0] = a
		a += 1
	for j in range(1,m):
		Z[0][j] = b
		b += 1
	Z[0][0] = " "
	afficher(Z)

#le jeu
n = 10
m = 10
N = 0
print("Bienvenue au jeu du demineur !!!")
difficulte = int(input("Veuillez choisir le niveau de difficulte que vous preferez (1/2/3): "))
debut = time.time()
T = int_jeu(n, m, difficulte)
b = quantite_de_mines(T,n,m)
#afficher(T)
M = mines_autour(n,m,T)
#afficher(M)
L = plateau_de_jeu(n,m,T,M)
afficher(L)
print("Voici un exemple du reperage des numeros de lignes et de colonnes:")
exemplaire(n,m)
print("Veuillez noter que vous ne pouvez pas creuser une case deja creusee, une case contenant un drapeau ou une case inexistante !")
print("d = drapeau, * = mine, un chiffre = le nombre de mines dans le voisinage immediat")
jeu = True
#n*m-b == le numero de cases necessaires a creuser pour gagner le jeu
while jeu == True and N < n*m-b:
	print("\n", end="")
	print("Quelle case est-ce que vous voulez choisir ?")
	i = int(input("-Numero de la ligne de case: "))
	j = int(input("-Numero de la colonne de case: "))
	verifier = existence(i,j,n,m)
	if verifier == False: 
		print("Vous ne pouvez pas choisir une case inexistante")
		jeu = True
	else:
		print("\n", end="")
		print("Qu est-ce que vous voulez faire ?")
		print("1, Creuser la case choisie")
		print("2, Poser un drapeau")
		print("3, Lever le drapeau")
		choix=int(input("Veuillez choisir une option (1/2/3): "))
		print("\n", end="")
		if choix == 1:
			c, M[i][j] = creuser_recu(T, M, i, j)
			if c == True:
				L = plateau_de_jeu(n,m,T,M)
				N = cases_decouvertes(L, n, m)
				afficher(L)
				print("Les cases decouvertes: ", N)
				jeu = True
			elif (T[i][j] == 3) or (T[i][j] == 4) or (T[i][j] == 1) :
				print("Vous ne pouvez pas creuser cette case")
				jeu = True
			elif c == False: 
				jeu = False
		elif choix == 2:
			poser_drapeau(T, i, j)
			L = plateau_de_jeu(n,m,T,M)
			afficher(L)
			jeu = True
		elif choix == 3:
			lever_drapeau(T, i, j)
			L = plateau_de_jeu(n,m,T,M)
			afficher(L)
			jeu = True
print("\n", end="")
if N == n*m-b:
	for f in range(n):
		for g in range(m):
			if L[f][g] == "?": L[f][g] = "*"
	afficher(L)
	print("Vous avez gagne. Bravo !!!")
	print("Les cases decouvertes: ", N)
	fin = time.time()
	print("--------------------")
	duree = float(fin - debut)
	print("Le temps consacre a ce jeu en minute: ", duree/60)
	print("--------------------")
	print("Votre score est ", int(N + duree))
else:
	L[i][j] = "*"
	afficher(L)
	print("Vous avez perdu. Merci d avoir joue a ce jeu !!!")
	print("Les cases decouvertes: ", N)
	fin = time.time()
	print("--------------------")
	duree = float(fin - debut)
	print("Le temps consacre a ce jeu en minute: ", duree/60)
	print("--------------------")
	print("Votre score est ", int(N + duree))


