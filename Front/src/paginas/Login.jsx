import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import estilos from './Login.module.css';
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from '@hookform/resolvers/zod';
import { Cabecalho2 } from '../Componentes/Cabecalho';
 
const schemaLogin = z.object({
    username: z.string()
        .min(1, 'Informe um nome')
        .max(25, 'Informe no máximo 25 caracteres'),
    password: z.string()
        .min(1, 'Informe uma senha')
        .max(50,'Informe no máximo 15 caracteres')
});
 
export function Login() {
    const navigate = useNavigate();
 
    const {
        register,
        handleSubmit,
        formState: { errors }
    } = useForm({
        resolver: zodResolver(schemaLogin)
    });
 async function obterDadosFormulario(data) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/login/', {
      username: data.username,
      password: data.password
    });

    const { access, refresh } = response.data;

    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);

    // Verificar se os tokens foram armazenados com sucesso
    const accessToken = localStorage.getItem('access_token');
    const refreshToken = localStorage.getItem('refresh_token');

    if (accessToken && refreshToken) {
      console.log('Login bem-sucedido! Bem Vindo!');
      navigate('/inicial');
    } else {
      throw new Error('Erro ao armazenar tokens');
    }
  } catch (error) {
    console.error('Erro de autenticação', error);
    alert("Dados Inválidos, por favor verifique suas credenciais");
  }
}
 
    return (
        <div className={estilos.conteiner}>
            <Cabecalho2 />
            <form onSubmit={handleSubmit(obterDadosFormulario)} className={estilos.loginForm}>
                <h2 className={estilos.titulo}>Login</h2>
 
                <label className={estilos.label}>Usuário:</label>
                <input
                    {...register('username')}
                    placeholder='username'
                    className={estilos.inputField}
                />
                {errors.username && <p className={estilos.error}>{errors.username.message}</p>}
 
                <label>Senha: </label>
                <input
                    {...register('password')}
                    placeholder='Senha'
                    type="password"
                    className={estilos.inputField}
                />
                {errors.password && <p className={estilos.error}>{errors.password.message}</p>}
 
                <button type="submit" className={estilos.submitButton}>Entrar</button>
            </form>
        </div>
    );
}