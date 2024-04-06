def make_weighted_average_graph(data, param): #data - štruktura dict dní dictor rokov dictor parametrov, param - žiadaný parameter
    number_of_years = 3 # počet dostupných rokov v databáze
    days = {}
    last_day_coeficient = 2 #Dôležitosť posledného roku, v pomere k prvému roku (ten má hodnotu 1, zvyšok sa preškáluje rovnomerne)
    rate_increment = (last_day_coeficient - 1) / (number_of_years - 1)
    division_coeficent = number_of_years + rate_increment * ((number_of_years - 1) * (number_of_years / 2))
    for day in data:
        current_coeficient = 1
        day_sum = 0
        for year in data[day]:
            day_sum += data[day][year][param] * current_coeficient
            current_coeficient += rate_increment
        days[day] = day_sum / division_coeficent
    return days #Vracia dict dní k váženým priemerom daného parametra


#Testik pre srandu

banan = {"1.1":{1900:{"Vlhkosť":5, "Teplo":23}, 1901:{"Vlhkosť":12, "Teplo":21}, 1902:{"Vlhkosť":3, "Teplo":33}}, 
         "2.1.":{1900:{"Vlhkosť":6, "Teplo":21}, 1901:{"Vlhkosť":3, "Teplo":11}, 1902:{"Vlhkosť":9, "Teplo":27}}}

print(make_weighted_average_graph(banan, "Vlhkosť"))

