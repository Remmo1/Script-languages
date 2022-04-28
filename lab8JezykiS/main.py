from Controlled_text import Controlled_text
from First_name import First_name

c1 = Controlled_text('text1')
print(c1.get_text())
c1.set_text('dasdsadasdadwadewfwefwfesfswf')
print(c1.get_text())
c1.set_text('text1')

c2 = Controlled_text('text2')

print(c1.__lt__(c2))
print(c2.__lt__(c1))

print(c1.__gt__(c2))
print(c2.__gt__(c1))

names = First_name.open_file(First_name.FILEPATH)
f1 = First_name(names, 'maRiA')
f2 = First_name(names, 'tOmASz')

print(f1.get_text())
print(f2.get_text())
