// Código refatorado
import axios from 'axios';
async function cadastrarUsuario(dadosUsuario) {
  try {
    // 1. Simplicidade: URL + Objeto JS direto.
    // O Axios define o método, o header e faz o stringify sozinho.
    const resposta = await axios.post(URL, dadosUsuario);
    // 2. Acesso Direto: Dados em .data (sem segundo await)
    alert(`Sucesso! ID: ${resposta.data.id}`);

  } catch (erro) {
    // 3. Robustez: Captura erros 400/500 automaticamente aqui
    console.error('Falha no cadastro:', erro.message);
    alert('Erro ao cadastrar.');
  }
}
