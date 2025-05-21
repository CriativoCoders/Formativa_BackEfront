import estilo from './BarraNavegacao.module.css';

export function BarraNavegacao(){
    return(
        <nav className={estilo.conteiner}>
            <ul>
               <li>Escola</li>
               <li>Missão</li> 
               <li>Visão</li>
               <li>Valores</li>   
            </ul>
        </nav>














    )
}