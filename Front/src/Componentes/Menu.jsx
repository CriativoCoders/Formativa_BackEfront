import { Link } from "react-router-dom";
import estilo from './Menu.module.css';
import gestores from '../assets/Gestor.png';
import professor from '../assets/Professor.png';
import Disciplina from '../assets/Disciplinas.png';
import Ambiente from '../assets/Ambiente.png';
// colcar as imagens no asse


export function Menu() {
    return (
        <div className={estilo.Maincontainer}>
            <table>
                <tbody>
                    <tr>
                        <td className={estilo.item}>
                            <Link to='/Professores'>
                            <img src={professor} alt="Img professor"></img>
                            <p>Professores</p>
                            </Link>
                        </td>
                        <td className={estilo.item}>
                            <Link to='/gestor'>
                            <img src={gestores} alt="Img gestor"></img>                                
                            <p>Gestores</p>
                            </Link>
                        </td>
                        <td className={estilo.item}>
                            <Link to='/Disciplinas'>
                            <img src={Disciplina} alt="Img Disciplina"></img>   
                            <p>Disciplinas</p>
                            </Link>
                        </td>
                        <td className={estilo.item}>
                            <Link to='/Ambientes'>
                            <img src={Ambiente} alt="Img Ambiente"></img>    
                            <p>Ambientes</p>
                            </Link>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    )
}