import estilo from './Cabecalho.module.css';
export function Cabecalho(){
    return(
        <header className={estilo.conteiner}>
            <h1>Gerenciamento Escola SENAI</h1>
        </header>
    )
}