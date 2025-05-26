import estilo from './BarraNavegacao.module.css';
import { Link } from 'react-router-dom';

export function BarraNavegacao(){
    return(
        <nav className={estilo.conteiner}>
            <ul>
               <li>Escola</li>
               <li><Link to="/Login">Login</Link></li>
               <li>Missão</li> 
               <li>Visão</li>
               <li>Valores</li>   
            </ul>
        </nav>

    )
}