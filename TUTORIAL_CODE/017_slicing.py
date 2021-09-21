# why last item is omitted
'''
It’s easy to see the length of a slice or range when only the stop position is given: range(3) and my_list[:3] both produce three items.
It’s easy to compute the length of a slice or range when start and stop are given: just subtract stop - start.
It’s easy to split a sequence in two parts at any index x, without overlapping: simply get my_list[:x] and my_list[x:]. For example:
'''

l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # split at 2
# [10, 20]
print(l[2:])
# [30, 40, 50, 60]
print(l[:3])  # split at 3
# [10, 20, 30]
print(l[3:])
# [40, 50, 60]

s = 'bicycle'
print(s[::3])
# 'bye'
print(s[::-1])
# 'elcycib'
print(s[::-2])
# 'eccb'

# seq[start:stop:step], Python calls seq.__getitem__(slice(start, stop, step))

invoice = """
... 0.....6.................................40........52...55........
... 1909  Pimoroni PiBrella                     $17.50    3    $52.50
... 1489  6mm Tactile Switch x20                 $4.95    2     $9.90
... 1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
... 1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

'''
        $17. 09  Pimoroni PiBrella             
         $4. 89  6mm Tactile Switch x20        
        $28. 10  Panavise Jr. - PV-201         
        $34. 01  PiTFT Mini Kit 320x240        
'''
