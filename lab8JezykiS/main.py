from Controlled_text import Controlled_text

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
