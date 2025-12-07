async function cadastrarUsuario(dadosUsuario) {
  try {
    const resposta = await fetch(URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' 
      },
      body: JSON.stringify(dadosUsuario)
    });
   
    if (!resposta.ok) {
      throw new Error(`Erro na API: ${resposta.status}`);
    }    
    const resultado = await resposta.json();    
    alert(`Sucesso! ID: ${resultado.id}`);

  } catch (erro) {
    console.error('Falha no cadastro:', erro);    
  }
}
