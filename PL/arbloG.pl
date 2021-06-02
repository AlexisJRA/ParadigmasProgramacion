padre(candido, javier).
padre(candido, jorge).

padre(macario, alicia).
padre(macario, gloria).

madre(luz, javier).
madre(luz, jorge).

madre(sara, alicia).
madre(sara, gloria).

padre(javier, alexis).
padre(javier, fer).

madre(alicia, alexis).
madre(alicia, fer).

madre(gloria, kevin).
padre(tomas, kevin).
madre(gloria, toni).
padre(tomas, toni).


madre(lupe, maria).
padre(jorge, maria).

mujer(fer).
hombre(alexis).
hombre(kevin).
mujer(maria).

mujer(A):-madre(A, C).
hombre(A):- padre(A, C).

padres(A, B) :- padre(A, C), madre(B, C).
hijo(A, B) :- padre(B, A); madre(B, A), hombre(A).
hija(A, B) :- padre(B, A); madre(B, A), mujer(A).
hermano(A, B) :- padre(C, A), padre(C, B), madre(D, A), madre(D, B), hombre(A).
hermana(A, B) :- padre(C, A), padre(C, B), madre(D, A), madre(D, B), mujer(A).
abuelo(A, B) :- padre(A, C), (padre(C, B); madre(C, B)).
abuela(A, B) :- madre(A, C), (padre(C, B); madre(C, B)).
tio(A, B) :- hermano(A, C), (padre(C, B); madre(C, B)).
tia(A, B) :- hermana(A, C), (padre(C, B); madre(C, B)).
primo(A, B) :- (padre(C, A); madre(C, A)),(padre(D, B); madre(D, B)), (hermano(C, D); hermana(C, D)), hombre(A).
prima(A, B) :- (padre(C, A); madre(C, A)),(padre(D, B); madre(D, B)), (hermano(C, D); hermana(C, D)), mujer(A).
nieto(A, B) :- (padre(B, C); madre(B, C)), hijo(A, C).
nieta(A, B) :- (padre(B, C); madre(B, C)), hija(A, C).









