import axios from 'axios';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useNavigate } from 'react-router-dom'; // importar :npm i react-router-dom
import { error } from 'zod/v4/locales/ar.js';
const schemaLogin = z.object({
    usernname: z.string()
        .min(1, 'Informe seu usuario')
        .max(25, 'Informe até 25 caracteres'),
    password: z.string()
        .min(15, 'Informe no maximo 15 caracteres')
})

export function Login(){
    const navigate = useNavigate();

    const{
        register, // Registra para mim e valide
        handleSubmit, // no momento em que eu fizer o envio do formulario
        formState: { errors } // e aguarde os erros em "erros"
    } = userForm({ // usuando das bibliotecas do hookform
        resolver: zodResolver(schemaLogin) // fazendo a resolução com schema acima.
    })

    async function obterDAdos(data) {
        console.log(`dados: ${data}`)

        try{
            const response = await axios.post('http://127.0.0.1:8000/api/token/', {
                usernname: data.usernname,
                password: data.password
            });
            const { acess, refresh, user } = response.data;

            localStorage.getItem('access_token', acess);
            localStorage.setItem('refresh_token', refresh);
            localStorage.setItem('tipo', user.tipo);
            localStorage.setItem('user_id', user.id);
            localStorage.setItem('username', username);

            console.log('login realizado')
            navigate('/inicial');
        }catch(erros){
            console.error('Erro no login', erro);
            alert("credenciais inválidas")
        }
    }

    return(
        <div className={estilos.loginForm}>
            <form>
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
    )

}