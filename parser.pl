utterance(X):- sentence(X, []).

sentence(Start, End):- introduction(Start, Rest), nounphrase(Rest, Rest2), verbphrase(Rest2, Rest3), punctuation(Rest3, End).
sentence(Start, End):- introduction(Start, Rest), verbphrase(Rest, Rest2), nounphrase(Rest2, Rest3), punctuation(Rest3, End).
sentence(Start, End):- nounphrase(Start, Rest), verbphrase(Rest, Rest2), punctuation(Rest2, End).
sentence(Start, End):- prepositionalphrase(Start, Rest), nounphrase(Rest, Rest2), verbphrase(Rest2, Rest3), punctuation(Rest3, End).
sentence(Start, End):-

nounphrase(Start, End):- modifier(Start, Rest), np_part(Rest, Rest2), prepositionalphrase(Rest2, End).

modifier([Art | End], End):- article(Art).
modifier([Det | End], End):- determiner(Det).
modifier([Det, Adj, Noun | End], End):- determiner(Det).

np_part([Pro | End]):- pronoun(Pro).
np_part([Noun | End]):- noun(Noun).

np_part([Art, Noun | End]):- article(Art), noun(Noun).
np_part([Det, Adj, Noun | End]):- determiner(Det), adjective(Adj), noun(Noun).

verbbody([Verb| End], End):- verb(Verb).

verbphrase([Verb| End], End):- verb(Verb).
verbphrase([Verb| Rest], End):- verb(Verb), nounphrase(Rest, End).
verbphrase([Verb, Prep | Rest], End):- verb(Verb), preposition(Prep), nounphrase(Rest, End).
verbphrase([Verb| Rest], End):- verbphrase(Rest, [Con, Rest2]), conjunction(Con), verbphrase(Rest2, End).


prepositionalphrase([Prep, N | End]):- preposition(Prep), np_part(N).

introduction([Intro, Comma | End], End):- introductory(Intro), comma(Comma).
introduction([Intro | End], End):- introductory(Intro).

quoted([Q | Rest], End):- quote(Q), sentence(Rest, Q2), quote(Q2).

punctuation(P | End):- punctuationmark(P).

introductory(so).
introductory(nope).
introductory(hey)

conjunction(and).
conjunction(that).

determiner(that).
determiner(your).

adverb(here).
adverb(out).
adverb(then).
adverb(back).
adverb(in).
adverb(just).

adjective(same).
adjective(little).
adjective(frayed).

article(a).
article(the).

noun(rope).
noun(piece).
noun(bar).
noun(drink).
noun(bartender).
noun(kind).
noun(knot).
noun(wall).
noun(bit).

pronoun(we).
pronoun(you).
pronoun(he).
pronoun(himself).
pronoun(which).

verb(walks).
verb(says).
verb(orders).
verb(serve).
verb(ties).
verb(rubs).
verb(was).
verb(responds).

preposition(of).
preposition(into).
preposition(against).
preposition(to).

postposition(ago).

verb(arent).
something(dont).
something(im).

quote('"')
comma(',')
punctuationmark('.')
punctuationmark('?')
