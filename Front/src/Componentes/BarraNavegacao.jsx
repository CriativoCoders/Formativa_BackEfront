import estilo from './BarraNavegacao.module.css';
import { Link } from 'react-router-dom';

export function BarraNavegacao(){
    return(
        <nav className={estilo.conteiner}>
            <ul>
               <li><Link to="/">Escola</Link></li>
               <li><Link to="/">Missão</Link></li> 
               <li>Visão</li>
               <li>Valores</li>   
            </ul>
        </nav>

    )
}

