import axios from 'axios';
async function buscarComAxios() {
  try {
    // VANTAGEM 1: Apenas uma linha.
    // O Axios já faz o GET, verifica o status e converte o JSON.
    const response = await axios.get('http://127.0.0.1:8000/produtos');
    // VANTAGEM 2: Os dados já estão prontos em .data
    console.log(response.data);

  } catch (erro) {
    // VANTAGEM 3: Cai aqui automaticamente se for erro 404 ou 500.
    console.error('erro:', erro.message);
  }
}

