start:-
    write('RESPONDE A LAS SIGUIENTES PREGUNTAS'),
    nl,
    nl,
    sera(Animal),
    nl,
    nl,
    write('*********************************'),
    nl,
    write('Creo que el animal es '),
    write(Animal),
    nl,
    write('*********************************'),
    nl,
    nl,

    borrar.

sera(cocodrilo) :- cocodrilo, !.
sera(nutria) :- nutria, !.
sera(tiburon) :- tiburon, !.
sera(ballena) :- ballena, !.
sera(delfin) :- delfin, !.
sera(jirafa) :- jirafa, !.
sera(conejo) :- conejo, !.
sera(hombre) :- hombre, !.
sera(oso) :- oso, !.
sera(tigre) :- tigre, !.
sera(leon) :- leon, !.
sera(aguila) :- aguila, !.
sera(pato) :- pato, !.
sera(gallina) :- gallina, !.
sera(avestruz) :- avestruz, !.
sera(pinguino) :- pinguino, !.
sera(carpa) :- carpa, !.
sera(pez_espada) :- pez_espada.


/*Acuatico*/
/*Agua dulce*/
cocodrilo :- acuatico,
    agua_dulce,
    verificar(es_carnivoro).

nutria :- acuatico,
    agua_dulce.

/*Agua Salada*/
tiburon :- acuatico,
    verificar(es_carnivoro).

ballena :- acuatico,
    verificar(es_el_animal_mas_grande_del_mundo).

delfin :- acuatico.

/*Terrestres*/
jirafa :- terrestre,
    herbivoro,
    verificar(tiene_cuello_largo).

conejo :- terrestre,
    herbivoro.

hombre :- terrestre,
    omnivoro,
    verificar(razona).

oso :- terrestre,
    omnivoro.

tigre :- terrestre,
    verificar(tiene_rayas).

leon :- terrestre.

/*Aves*/
aguila :- ave,
    voladora,
    verificar(es_ave_rapaz).

pato :- ave,
    voladora.

gallina :- ave,
    verificar(es_domestico).

avestruz :- ave,
    verificar(corre_veloz).

pinguino :- ave.

/*Peces*/
carpa :- verificar(vive_rio).
pez_espada.


acuatico :- verificar(vive_en_agua).
agua_dulce :- verificar(vive_en_agua_dulce).
terrestre :- verificar(es_terrestre).
herbivoro :- verificar(es_herbivoro).
omnivoro :- verificar(es_omnivoro).
ave :- verificar(tiene_alas).
voladora :- verificar(vuela).


verificar(S) :-
    (cumple(S)
    ->
    true;
    (no_cumple(S)
     ->
     fail;
     preguntar(S))).

preguntar(Pregunta) :-
    write('Tiene el animal la siguiente caracteristica: '),
    write(Pregunta),
    write('? (s/n) '),
    read(Respuesta),
    nl,

    ( (Respuesta == s)
      ->
       assert(cumple(Pregunta));
       assert(no_cumple(Pregunta)), fail).

:- dynamic cumple/1,no_cumple/1,sera/1,verificar/1.

borrar :- retract(cumple(_)),fail.
borrar :- retract(no_cumple(_)),fail.
borrar.
