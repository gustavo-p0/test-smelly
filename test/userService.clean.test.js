const { UserService } = require('../src/userService');

describe('UserService', () => {
  let userService;

  beforeEach(() => {
    userService = new UserService();
    userService._clearDB();
  });

  describe('createUser', () => {
    test('deve retornar um usuário com id definido ao criar com dados válidos', () => {
      const nome = 'Alice';
      const email = 'alice@email.com';
      const idade = 28;

      const usuario = userService.createUser(nome, email, idade);

      expect(usuario.id).toBeDefined();
      expect(usuario.nome).toBe(nome);
      expect(usuario.status).toBe('ativo');
    });
  });

  describe('getUserById', () => {
    test('deve retornar o usuário correto pelo id', () => {
      const criado = userService.createUser('Bob', 'bob@email.com', 30);

      const encontrado = userService.getUserById(criado.id);

      expect(encontrado.nome).toBe('Bob');
    });

    test('deve retornar null para id inexistente', () => {
      const resultado = userService.getUserById('id-que-nao-existe');
      expect(resultado).toBeNull();
    });
  });

  describe('deactivateUser', () => {
    test('deve desativar usuário comum e retornar true', () => {
      const usuario = userService.createUser('Comum', 'comum@email.com', 30);

      const resultado = userService.deactivateUser(usuario.id);

      expect(resultado).toBe(true);
      expect(userService.getUserById(usuario.id).status).toBe('inativo');
    });

    test('deve recusar desativação de admin e retornar false', () => {
      const admin = userService.createUser('Admin', 'admin@email.com', 40, true);

      const resultado = userService.deactivateUser(admin.id);

      expect(resultado).toBe(false);
      expect(userService.getUserById(admin.id).status).toBe('ativo');
    });

    test('deve retornar false para id inexistente', () => {
      const resultado = userService.deactivateUser('id-inexistente');
      expect(resultado).toBe(false);
    });
  });
});
