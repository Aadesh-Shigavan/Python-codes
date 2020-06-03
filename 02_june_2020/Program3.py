progLang = ['c', 'Reactjs', 'C++', 'Python', 'Java', 'Android', 'JS', 'GoLang']

del progLang[4]     #['c', 'Reactjs', 'C++', 'Python', 'Android', 'JS', 'GoLang']
print(progLang)

del progLang[-3]    #['c', 'Reactjs', 'C++', 'Python', 'JS', 'GoLang']
print(progLang)

del progLang[:2]    #[C++', 'Python',  'JS', 'GoLang']
print(progLang)

del progLang       #Error - "progLang" not define
print(progLang)