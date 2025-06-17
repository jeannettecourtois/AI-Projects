/*Question 1 */

/* Fonction longueur */
longueur([], 0).
longueur([_|T], N):-
    longueur(T, N1), 
    N is N1 + 1.

nBienPlace([], [], 0).
nBienPlace([T1|R1], [T1|R2], BP) :- 
    nBienPlace(R1, R2, BP1), 
    BP is BP1 + 1.
nBienPlace([T1|R1], [T2|R2], BP):-
    T1 \= T2, 
    nBienPlace(R1, R2, BP).

 
gagne(X, Y):-
    nBienPlace(X, Y, N), 
    longueur(X, N).

/*Question 2*/

%element(_, []).Attention, si tu rajoutes ça, ça ne marche pas. Ce n'est pas partie des conditions
element(X, [X|_]).
element(X, [_|R]):-
    element(X, R).

%mais cela n'enlève pas uniquement la première occurrence 
enleve(_, [], []).
enleve(E, [T1|R1], L2):-
    E \= T1,
    enleve(E, R1, L2Res), 
    L2 = [T1|L2Res].
enleve(E, [E|R1], L2):-
       enleve(E, R1, L2).

enleve1(_, [], []).

enleve1(E, [E|R], R) :- !.  % On enlève la première occurrence et STOP grâce au cut (!)

/*Exclamation point ! denotes Cut in Prolog, a special goal that always succeeds, and blocks backtracking for all branches above it that may have alternatives.*/

enleve1(E, [X|R], [X|R2]) :-
    enleve1(E, R, R2).

enleveBP([], [], [], []).
enleveBP([T1|R1], [T1|R2], Code1Bis, Code2Bis):- 
    enleveBP(R1, R2, Code1Bis, Code2Bis).

enleveBP([T1|R1], [T2|R2], Code1Bis, Code2Bis):-
    T1 \= T2,  
    enleveBP(R1, R2, Res1, Res2), 
    Code1Bis = [T1|Res1], 
    Code2Bis = [T2|Res2].

%code auxiliaire


/*nMalPlacesAux([], [], 0).
nMalPlacesAux([T1|R1], [T2|R2], MP):-
    T1 \= T2, 
    nMalPlacesAux(R1, R2, MP1), 
    MP is MP1 + 1. */

nMalPlacesAux([], _, 0).

nMalPlacesAux([X|R], C2, MP) :-
    element(X, C2),                 % si X ∈ C2
    enleve1(X, C2, C2Rest),         % on enlève 1 occurrence de X
    nMalPlacesAux(R, C2Rest, MP1),
    MP is MP1 + 1.

nMalPlacesAux([X|R], C2, MP) :-
    \+ element(X, C2),              % si X ∉ C2
    nMalPlacesAux(R, C2, MP).


nMalPlaces(Code1, Code2, MP):-
    enleveBP(Code1, Code2, C1Bis, C2Bis),
    nMalPlacesAux(C1Bis, C2Bis, MP).
    

codeur(_, 0, []).                      % Cas de base : 0 élément → liste vide

codeur(M, N, [C|R]) :-                % Cas récursif
    N > 0,
    MPlus1 is M + 1,
    random(1, MPlus1, C),             
    N1 is N - 1,
    codeur(M, N1, R).

% Question 4 

boucle_jeu(_, 0) :-
    writeln("Perdu ! Plus d'essais.").

boucle_jeu(Code, N) :-
    N > 0,
    format("Il reste ~w coup(s).~n", [N]),
    write("Donner un code : "), 
    read(Proposition),
    nBienPlace(Code, Proposition, BP),
    nMalPlaces(Code, Proposition, MP),
    format("BP: ~w / MP: ~w~n", [BP, MP]),
    ( BP =:= 4 ->
        writeln("Gagné !!!")
    ;
        N1 is N - 1,
        boucle_jeu(Code, N1)
    ).
jouons(M, N, Max) :-
    codeur(M, N, CodeSecret),
    boucle_jeu(CodeSecret, Max).