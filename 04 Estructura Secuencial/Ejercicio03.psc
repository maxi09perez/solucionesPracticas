Algoritmo sin_titulo
	Escribir "Ingrese la cantidad de partidos ganados del equipo"
	Leer partidosGanados
	
	Escribir "Ingrese la cantidad de partidos empatados del equipo"
	Leer partidosEmpatados
	
	Escribir "Ingrese la cantidad de partidos perdidos del equipo"
	Leer partidosPerdidos
	
	puntosEquipo = (partidosGanados * 3) + partidosEmpatados
	
	Escribir "El equipo tiene ",puntosEquipo," puntos hasta el momento, luego de jugar ",partidosGanados+partidosEmpatados+partidosPerdidos," partidos."
FinAlgoritmo
