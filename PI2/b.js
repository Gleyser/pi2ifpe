const novoProduto = { nome: 'Teclado Gamer', preco: 150 };
async function inserirProdutosComFetch() {
  try {
    const response = await fetch('http://127.0.0.1:8000/produtos', {
      method: 'POST',
      // 1. Tivemos que definir o cabeçalho manualmente
      headers: {
        'Content-Type': 'application/json'
      },
      // 2. Tivemos que transformar o objeto em texto manualmente
      body: JSON.stringify(novoProduto)
    });
    // 3. Tivemos que verificar erro HTTP manualmente
    if (!response.ok) throw new Error('Erro ao cadastrar');
    const dados = await response.json();
    alert('Sucesso: ' + dados.id);
  } catch (erro) {
    console.error(erro);
  }
}
