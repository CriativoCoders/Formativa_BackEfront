import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

const tratarErro = (error) => {
  if (error.response) {
    // O servidor respondeu com um código de status que não é 2xx
    console.error(error.response.data);
  } else if (error.request) {
    // A requisição foi feita, mas não houve resposta
    console.error('Sem resposta do servidor');
  } else {
    // Algo aconteceu ao configurar a requisição
    console.error('Erro ao configurar a requisição');
  }
};

export function buscarDados() {
  return api.get('/dados').catch(tratarErro);
}

export function criarDado(dado) {
  return api.post('/dados', dado).catch(tratarErro);
}

export function atualizarDado(id, dado) {
  return api.put(`/dados/${id}`, dado).catch(tratarErro);
}

export function deletarDado(id) {
  return api.delete(`/dados/${id}`).catch(tratarErro);
}