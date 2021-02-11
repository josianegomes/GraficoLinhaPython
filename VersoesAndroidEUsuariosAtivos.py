import matplotlib.pyplot


porcentagem = ["1.36%",  "3.08%", "3.48%", "4.26%", "5.17%", "5.77%", "9.89%", "21.29%", "44.47%"]
versao = ["4.4 Kitkat", "7.1 Nougat", "5.1 Lollipop", "7.0 Nougat", "8.0 oreo", "6.0 Marshmallow", "8.1 oreo", "9.0 Pie", "10.0 10"]
matplotlib.pyplot.plot(versao, porcentagem)
matplotlib.pyplot.xlabel('Versões do Android')
matplotlib.pyplot.ylabel('Porcentagem de usuários ativos 01/2021')
matplotlib.pyplot.show()
