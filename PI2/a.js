import axios from 'axios';
const novoProduto = { nome: 'Teclado Gamer', preco: 150 };
async function inserirProdutosComAxios() {
  try {
    // O Axios faz tudo sozinho:
    // Define POST, Content-Type e transforma em JSON    
    const response = await axios.post('http://127.0.0.1:8000/produtos', novoProduto);
    alert('Sucesso: ' + response.data.id);
  } catch (erro) {
    // 4. Captura erros 400/500 automaticamente
    console.error('Erro na API:', erro.response.status);
  }
}

