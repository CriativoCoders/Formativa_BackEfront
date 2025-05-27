import { Route, Routes } from 'react-router-dom';
import { Login } from '../paginas/Login';
import { Professores } from '../paginas/Professores';
import { Inicial } from '../paginas/Inicial';


export function Rotas(){
    return(
        <Routes>
            <Route path='/' element={<Inicial/>}/>
            <Route path='/Login' element={<Login/>}/>
             <Route path='/Professores' element={<Professores/>}/>
            
        </Routes>
    )
}