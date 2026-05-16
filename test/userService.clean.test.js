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
});
