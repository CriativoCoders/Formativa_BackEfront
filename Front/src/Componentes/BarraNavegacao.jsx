import estilo from './BarraNavegacao.module.css';
import { Link } from 'react-router-dom';

export const BarraNavegacao = () => {
    return(
        <nav className={estilo.conteiner}>
            <ul>
               <li><Link to="">Escola</Link></li>
               <li><Link to="">Missão</Link></li> 
               <li><Link to="">Visão</Link></li>
               <li><Link to="">Valores</Link></li>   
            </ul>
        </nav>

    )
}

