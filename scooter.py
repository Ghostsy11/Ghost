q1 = int(input("Verzerkeringkosten?"))
q2 = int(input(" km per maand?"))

def maandkosten(verzekering_per_maand  , km_per_maand):
    liter_per_kilometer = benzine_kosten_per_liter =  1.54
    maandkosten = ((km_per_maand * liter_per_kilometer)* benzine_kosten_per_liter) + verzekering_per_maand
    bereken_maandkosten = maandkosten
    print("je betaalt : ", bereken_maandkosten , "€")

maandkosten(q1 , q2)