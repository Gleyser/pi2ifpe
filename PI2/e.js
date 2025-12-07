async function cadastrarUsuario(dadosUsuario) {
  try {
    // 1. Verbosidade: Configuração manual excessiva
    const resposta = await fetch('https://api.sistema.com/usuarios', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // OBRIGATÓRIO no Fetch
      },
      body: JSON.stringify(dadosUsuario)   // OBRIGATÓRIO converter p/ texto
    });
    
    if (!resposta.ok) {
      throw new Error(`Erro na API: ${resposta.status}`);
    }
    
    const resultado = await resposta.json();
    
    alert(`Sucesso! ID: ${resultado.id}`);

  } catch (erro) {
    console.error('Falha no cadastro:', erro);
    alert('Erro ao cadastrar.');
  }
}