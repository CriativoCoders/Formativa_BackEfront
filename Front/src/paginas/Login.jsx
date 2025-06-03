import axios from 'axios';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useNavigate } from 'react-router-dom';
import estilos from './Login.module.css';

const schemaLogin = z.object({
  username: z.string()
    .min(1, 'Informe seu usuário')
    .max(25, 'Informe até 25 caracteres'),
  password: z.string()
    .min(8, 'Informe no mínimo 8 caracteres')
    .max(15, 'Informe no máximo 15 caracteres'),
})

export function Login(){
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(schemaLogin)
  })

// tratamento de erro 
async function obterDados(data) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/token/', {
      username: data.username,
      password: data.password
    });
    const { access, refresh, user } = response.data;

    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    localStorage.setItem('tipo', user.tipo);
    localStorage.setItem('user_id', user.id);
    localStorage.setItem('username', user.username);
    
    console.log('Login realizado')
    navigate('/inicial');
  } catch (erro) {
    if (erro.response) {
      // Erro de autenticação
      if (erro.response.status === 401) {
        alert("Credenciais inválidas");
      } else {
        alert("Erro ao realizar login");
      }
    } else if (erro.request) {
      // Erro de rede
      alert("Erro de conexão");
    } else {
      // Erro desconhecido
      alert("Erro desconhecido");
    }
  }
}
  
  return (
    <div className={estilos.BarraNavegacao}>
        <div className={estilos.main}>
          <div className={estilos.loginForm}>
            <form onSubmit={handleSubmit(obterDados)}>
              <h2 className={estilos.titulo}>Login</h2>
              <label>Nome</label>
              <input
                {...register('username')}
                placeholder='username'
                />
              {errors.username && <p>{errors.username.message}</p>}

              <label>Senha</label>
              <input 
                {...register('password')}
                placeholder='senha'
                type='password'
                />
              {errors.password && <p>{errors.password.message}</p>}
              <button type='submit'>Entrar</button>
            </form>
          </div>
        </div>
        <div className={estilos.Rodape}>
        </div>
    </div>
  )
}

// Criar endpoint para conectar com back end 
