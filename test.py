import re
p = re.compile(r"((A)\,(B))|((B)\,(A))|(([A|B]),(\([A-Za-z]*\)))|((\([A-Za-z]*\)),([A|B]))|(([A|B]),([0-9]*))")
print(p.match("A,B"))