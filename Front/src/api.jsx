import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
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

// ProfessorGestor
export async function buscarProfessores() {
  try {
    const response = await api.get('/professores/');
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function criarProfessor(professor) {
  try {
    const response = await api.post('/professores/', professor);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function atualizarProfessor(id, professor) {
  try {
    const response = await api.put(`/professores/${id}/`, professor);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function deletarProfessor(id) {
  try {
    const response = await api.delete(`/professores/${id}/`);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

// Disciplina
export async function buscarDisciplinas() {
  try {
    const response = await api.get('/disciplinas/');
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function criarDisciplina(disciplina) {
  try {
    const response = await api.post('/disciplinas/', disciplina);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function atualizarDisciplina(id, disciplina) {
  try {
    const response = await api.put(`/disciplinas/${id}/`, disciplina);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function deletarDisciplina(id) {
  try {
    const response = await api.delete(`/disciplinas/${id}/`);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

// Sala
export async function buscarSalas() {
  try {
    const response = await api.get('/salas/');
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function criarSala(sala) {
  try {
    const response = await api.post('/salas/', sala);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function atualizarSala(id, sala) {
  try {
    const response = await api.put(`/salas/${id}/`, sala);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function deletarSala(id) {
  try {
    const response = await api.delete(`/salas/${id}/`);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

// Ambiente
export async function buscarAmbientes() {
  try {
    const response = await api.get('/ambientes/');
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function criarAmbiente(ambiente) {
  try {
    const response = await api.post('/ambientes/', ambiente);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function atualizarAmbiente(id, ambiente) {
  try {
    const response = await api.put(`/ambientes/${id}/`, ambiente);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}

export async function deletarAmbiente(id) {
  try {
    const response = await api.delete(`/ambientes/${id}/`);
    return response.data;
  } catch (error) {
    tratarErro(error);
  }
}