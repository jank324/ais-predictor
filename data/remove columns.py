import pandas
data = pandas.read_csv("PY11 rotterdam_hamburg - times to UNIX time.csv")
data =data.drop(['bla','blubb'], axis = 1)
#bla und blubb müsst ihr in der csv umändern, so hab ich meinen ersten und zweiten eintrag genannt(vor TripID)
# axis=1 bedeutet, es handelt sich hierbei um spalten und nicht zeilen
#man kann zeilen löschen, indem man anstelle 'bla' und 'blub' nur die Zeilennummer schreibt, ohne axis=1

data.to_csv("PY11 rotterdam_hamburg - times to UNIX time.csv" ,index=None)
#wenn ihr doch lieber noch den index behalten wollt, dann lässt index=None weg, aber wenn wir das nicht schreiben, fügt er jedes mal ein Index an