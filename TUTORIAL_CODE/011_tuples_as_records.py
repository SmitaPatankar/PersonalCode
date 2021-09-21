lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)  # %s treats elements in tuple separately
# BRA/CE342567
# ESP/XDA205856
# USA/31195855

for country, _ in traveler_ids:  # for loop also unpacks tuples
    print(country)
# USA
# BRA
# ESP

