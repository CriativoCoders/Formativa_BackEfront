import { Route, Routes } from 'react-router-dom';
import { Login } from '../paginas/Login';
import { Professores } from '../paginas/Professores';
import { Inicial } from '../paginas/Inicial';


export function Rotas(){
    return(
        <Routes>
            <Route path='/' element={<Login/>}/>
            <Route path='/Inicial' element={<Inicial/>}/>
            <Route path='/Professores' element={<Professores/>}/>
            
        </Routes>
    )
}