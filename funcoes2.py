def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

loginUsuario('Admin')      # Bem-vindo, Administrador
loginUsuario('admin')      # Bem-vindo, Administrador
loginUsuario('User')       # Bem-vindo, Usuário
loginUsuario('usuário')    # Bem-vindo, Usuário
loginUsuario('ADMIN')      # Bem-vindo, Administrador
