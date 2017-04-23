utterance(X):- sentence(X, []).

sentence(Start, End):- introduction(Start, Rest), nounphrase(Rest, Rest2), verbphrase(Rest2, Rest3), punctuation(Rest3, End).
sentence(Start, End):- introduction(Start, Rest), verbphrase(Rest, Rest2), nounphrase(Rest2, Rest3), punctuation(Rest3, End).
sentence(Start, End):- nounphrase(Start, Rest), verbphrase(Rest, Rest2), punctuation(Rest2, End).
sentence(Start, End):- prepositionalphrase(Start, Rest), nounphrase(Rest, Rest2), verbphrase(Rest2, Rest3), punctuation(Rest3, End).

nounphrase(Start, End):- modifier(Start, Rest), nounbody(Rest, End).
nounphrase(Start, End):- modifier(Start, Rest), nounbody(Rest, Rest2), prepositionalphrase(Rest2, End).
nounphrase([Pronoun | End], End):- pronoun(Pronoun).

modifier([Art | End], End):- article(Art).
modifier([Det | End], End):- determiner(Det).

nounbody([Noun | End], End):- noun(Noun).
nounbody([Adj, Noun | End], End):- adjective(Adj), noun(Noun).

verbphrase(Start, End):- fullverbphrase(Start, End).
verbphrase(Start, End):- multiverbphrase(Start, End).
verbphrase([Verb, Comma | Rest], End):- verb(Verb), commamark(Comma),  quoted(Rest, End).

fullverbphrase(Start, End):- verbbody(Start, End).
fullverbphrase([Neg | Rest], End):- negation(Neg), verbbody(Rest, End).
fullverbphrase(Start, End):- verbbody(Start, Rest), adverbword(Rest, End).
fullverbphrase(Start, End):- adverbword(Start, Rest), verbbody(Rest, End).
fullverbphrase([Neg | Rest], End):- negation(Neg), verbbody(Rest, Rest2), adverbword(Rest2, End).

adverbword([Adv | End], End):- adverb(Adv).

verbbody([Verb| End], End):- verb(Verb).
verbbody([Verb| Rest], End):- verb(Verb), nounphrase(Rest, End).
verbbody([Verb, Prep | Rest], End):- verb(Verb), preposition(Prep), nounphrase(Rest, End).
verbbody([Verb, Adv, Prep | Rest], End):- verb(Verb), adverb(Adv), preposition(Prep), nounphrase(Rest, End).
verbbody([Verb, Pro, Prep | Rest], End):- verb(Verb), pronoun(Pro), preposition(Prep), nounphrase(Rest, End).

multiverbphrase(Start, End):- fullverbphrase(Start, Rest), conjunctionjoin(Rest, Rest2), fullverbphrase(Rest2, End).
multiverbphrase(Start, End):- fullverbphrase(Start, Rest), comma(Rest, Rest2), fullverbphrase(Rest2, Rest3), comma(Rest3, Rest4), conjunctionjoin(Rest4, Rest5), fullverbphrase(Rest5, End).

conjunctionjoin([Con | End], End):- conjunction(Con).

prepositionalphrase([Prep, N | End], End):- preposition(Prep), noun(N).
prepositionalphrase([Prep, Det, N | End], End):- preposition(Prep), determiner(Det), noun(N).
prepositionalphrase([Prep, N | End], End):- preposition(Prep), pronoun(N).

introduction([Intro, Comma | End], End):- introductory(Intro), commamark(Comma).
introduction([Intro | End], End):- introductory(Intro).

quoted(Start, End):- quote(Start, Rest), sentence(Rest, Rest2), quote(Rest2, End).

quote([Q | End], End):- quotationmark(Q).

comma([C | End], End):- commamark(C).

punctuation([P | End], End):- punctuationmark(P).
punctuation(End, End).

introductory(so).
introductory(nope).
introductory(hey).

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
pronoun(i).

verb(walks).
verb(says).
verb(orders).
verb(serve).
verb(ties).
verb(rubs).
verb(was).
verb(responds).
verb(are).
verb(am).

preposition(of).
preposition(into).
preposition(against).
preposition(to).

negation(dont).

quotationmark('"').
commamark(',').
punctuationmark('.').
punctuationmark('?').
