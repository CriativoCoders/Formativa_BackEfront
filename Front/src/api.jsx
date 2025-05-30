import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

// Adicione cabeçalhos de autenticação se necessário
// api.defaults.headers.common['Authorization'] = `Bearer ${token}`;

const tratarErro = (error) => {
  if (error.response) {
    // O servidor respondeu com um código de status que não é 2xx
    console.error(error.response.data);
    throw error.response.data;
  } else if (error.request) {
    // A requisição foi feita, mas não houve resposta
    console.error('Sem resposta do servidor');
    throw new Error('Sem resposta do servidor');
  } else {
    // Algo aconteceu ao configurar a requisição
    console.error('Erro ao configurar a requisição');
    throw new Error('Erro ao configurar a requisição');
  }
};

export async function buscarDados() {
  try {
    const response = await api.get('/dados');
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function criarDado(dado) {
  try {
    const response = await api.post('/dados', dado);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function atualizarDado(id, dado) {
  try {
    const response = await api.put(`/dados/${id}`, dado);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function deletarDado(id) {
  try {
    const response = await api.delete(`/dados/${id}`);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}