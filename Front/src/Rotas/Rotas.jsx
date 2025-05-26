import { Route, Routes } from 'react-router-dom';
import { Login } from '../paginas/Login';
import { Inicial } from '../Paginas/Inicial';


export function Rotas(){
    return(
        <Routes>
            <Route path='/' element={<Inicial/>}/>
            <Route path='/Login' element={<Login/>}/>
            
        </Routes>
    )
}