import estilo from './Rodape.module.css';
export function Rodape(){
    return(
        <div className={estilo.container}>
            <footer>
                {/* <p>Menu</p> */}
                <ul className=''>
                    <li>Quem Somos?</li>
                    <li>Desenvolvedor(a)</li>
                    <li>Politicas de Privacidade</li>
                </ul>
            </footer>
        </div>
    )
}