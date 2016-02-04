
usuarios = [['admin@admin', '123mudar'], ['diego@python', '321naomudar']]

def valida_login(usuario):
    login_informado, senha_informada = usuario
    for login, senha in usuarios:
        if login_informado == login and senha_informada == senha:
            return True
    return False
    
usuario = []
login_informado = input('Digite o seu login: \n')
senha_informada = input('Digite a sua senha: \n')
usuario.append(login_informado)
usuario.append(senha_informada)

if valida_login(usuario):
    print('usuario valido')
else:
    print('usuário invalido')